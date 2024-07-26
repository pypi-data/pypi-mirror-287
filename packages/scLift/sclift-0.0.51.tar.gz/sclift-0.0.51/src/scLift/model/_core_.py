# -*- coding: UTF-8 -*-

import os.path
import time
from typing import Optional, Tuple, Literal

import numpy as np
import pandas as pd
import scvi
import scanpy as sc

from anndata import AnnData
from pandas import DataFrame
from scipy import stats
import snapatac2 as snap

from ykenan_file import StaticMethod
from ykenan_log import Logger

from ._algorithm_ import (
    RandomWalk,
    adata_group,
    adata_map_df,
    semi_mutual_knn_weight,
    euclidean_distances,
    adjustment_tf_idf,
    z_score_normalize,
    mean_symmetric_scale,
    sigmoid,
    umap_data,
    tsne_data
)

from ._preprocessing_ import filter_data

from scLift.plot import (
    scatter_atac,
    scatter_trait,
    communities_graph,
    violin_trait,
    box_trait,
    bar_trait,
    barcode_trait,
    heatmap_annotation,
    kde,
    pie_trait
)

from scLift.data import save_h5ad
from scLift.util import to_sparse, number, path, to_dense, get_index, matrix_data

file_method = StaticMethod("scLift_model_core")
log = Logger("scLift_model_core")


def overlap(regions: DataFrame, variants: DataFrame) -> DataFrame:
    """
    Relate the peak region and variant site
    :param regions: peaks information
    :param variants: variants information
    :return: The variant maps data in the peak region
    """
    log.info("start overlap variant information")

    regions_columns: list = list(regions.columns)

    if "chr" not in regions_columns or "start" not in regions_columns or "end" not in regions_columns:
        log.error(f"The peaks information {regions_columns} in data `adata` must include three columns: `chr`, `start` and `end`. (It is recommended to use the `read_sc_atac` method.)")
        raise ValueError(f"The peaks information {regions_columns} in data `adata` must include three columns: `chr`, `start` and `end`. (It is recommended to use the `read_sc_atac` method.)")

    columns = ['variant_id', 'index', 'chr', 'position', 'rsId', 'chr_a', 'start', 'end']

    if regions.shape[0] == 0 or variants.shape[0] == 0:
        log.warn("Data is empty.")
        return pd.DataFrame(columns=columns)

    regions = regions.rename_axis("index")
    regions = regions.reset_index()
    # sort
    regions_sort = regions.sort_values(["chr", "start", "end"])[["index", "chr", "start", "end"]]
    variants_sort = variants.sort_values(["chr", "position"])[["variant_id", "chr", "position", "rsId"]]

    # Intersect and Sort
    chr_keys: list = list(set(regions_sort["chr"]).intersection(set(variants_sort["chr"])))
    chr_keys.sort()

    variants_chr_type: dict = {}
    variants_position_list: dict = {}

    # Cyclic region chromatin
    for chr_key in chr_keys:
        # variant chr information
        sort_chr_regions_chr = variants_sort[variants_sort["chr"] == chr_key]
        variants_chr_type.update({chr_key: sort_chr_regions_chr})
        variants_position_list.update({chr_key: list(sort_chr_regions_chr["position"])})

    variants_overlap_info_list: list = []

    log.info("Start adding variants to each region")

    for index, chr_a, start, end in zip(regions_sort["index"], regions_sort["chr"], regions_sort["start"], regions_sort["end"]):

        # judge chr
        if chr_a in chr_keys:
            # get chr variant
            variants_chr_type_position_list = variants_position_list[chr_a]
            # judge start and end position
            if start <= variants_chr_type_position_list[-1] and end >= variants_chr_type_position_list[0]:
                # get index
                start_index = get_index(start, variants_chr_type_position_list)
                end_index = get_index(end, variants_chr_type_position_list)

                # Determine whether it is equal, Equality means there is no overlap
                if start_index != end_index:
                    start_index = start_index if isinstance(start_index, number) else start_index[1]
                    end_index = end_index + 1 if isinstance(end_index, number) else end_index[1]

                    if start_index > end_index:
                        log.error("The end index in the region is greater than the start index.")
                        raise IndexError("The end index in the region is greater than the start index.")

                    variants_chr_type_chr_a = variants_chr_type[chr_a]
                    # get data
                    variants_overlap_info: DataFrame = variants_chr_type_chr_a[start_index:end_index].copy()
                    variants_overlap_info["index"] = index
                    variants_overlap_info["chr_a"] = chr_a
                    variants_overlap_info["start"] = start
                    variants_overlap_info["end"] = end
                    variants_overlap_info_list.append(variants_overlap_info)

    log.info("end overlap variant information")
    # merge result
    if len(variants_overlap_info_list) > 0:
        overlap_data: DataFrame = pd.concat(variants_overlap_info_list, axis=0)
    else:
        log.info("Overlap is empty.")
        return pd.DataFrame(columns=columns)

    return overlap_data


def overlap_sum(regions: AnnData, variants: dict, trait_info: DataFrame) -> AnnData:
    """
    Overlap regional data and mutation data and sum the PP values of all mutations in a region as the values for that region
    :param regions: peaks data
    :param variants: variants data
    :param trait_info: traits information
    :return: overlap data
    """

    # Unique feature set
    label_all = list(regions.var.index)
    # Peak number
    label_all_size: int = len(label_all)

    # trait information
    trait_names: list = list(trait_info["id"])

    matrix = np.zeros((label_all_size, len(trait_names)))

    for trait_name in trait_names:
        variant: AnnData = variants[trait_name]
        index: int = trait_names.index(trait_name)
        log.info(f"Start {index + 1} trait/disease {trait_name}")

        # handle overlap data
        overlap_info: DataFrame = overlap(regions.var, variant.obs)

        if overlap_info.shape[0] == 0:
            continue

        overlap_info.rename({"index": "label"}, axis="columns", inplace=True)
        overlap_info.reset_index(inplace=True)
        overlap_info["region_id"] = overlap_info["chr"].astype(str) + ":" + overlap_info["start"].astype(str) + "-" + overlap_info["end"].astype(str)

        # get region
        region_info = overlap_info.groupby("region_id", as_index=False)["label"].first()
        region_info.index = region_info["label"].astype(str)
        label: list = list(region_info["label"])

        # Mutation information with repetitive features
        label_size: int = len(label)
        # Define a matrix
        log.info("Sum each region")

        for j in range(label_size):

            # Determine whether the features after overlap exist, In other words, whether there is overlap in this feature
            if label[j] in label_all:
                # get the index of label
                label_index = label_all.index(label[j])
                overlap_info_region = overlap_info[overlap_info["label"] == label[j]]
                # sum value
                overlap_variant = variant[list(overlap_info_region["variant_id_index"]), :]
                matrix[label_index, index] = overlap_variant.X.sum(axis=0)

    overlap_adata = AnnData(to_sparse(matrix), var=trait_info, obs=regions.var)
    overlap_adata.uns["trait_info"] = trait_info
    return overlap_adata


def group_heatmap(
    adata: AnnData,
    layer: str = None,
    dir_name: str = "heatmap",
    clusters: str = "clusters",
    row_cluster: bool = True,
    col_cluster: bool = True,
    row_index: list = None,
    col_index: list = None,
    is_sort: bool = True,
    width: float = 8.0,
    height: float = 4.0,
    axis: Literal[0, 1] = 0,
    plot_output: str = None,
    show: bool = True
) -> None:
    # The relationship between cluster and trait
    adata_cluster: AnnData = adata_group(adata, clusters, layer=layer, axis=axis)

    if row_index is not None:
        adata_cluster = adata_cluster[row_index, :].copy()
        is_sort = False

    if col_index is not None:
        adata_cluster = adata_cluster[:, col_index].copy()
        is_sort = False

    new_path: path = os.path.join(plot_output, dir_name) if plot_output is not None else None
    # create path
    if plot_output is not None:
        file_method.makedirs(new_path)

    # plot
    try:
        heatmap_annotation(
            adata_cluster.T,
            row_name="labels",
            col_name=clusters,
            width=width,
            height=height,
            label="Mean TRS",
            row_legend=True,
            row_cluster=row_cluster,
            col_cluster=col_cluster,
            is_sort=is_sort,
            row_show_names=True,
            col_show_names=True,
            x_name="Cell type",
            y_name="Trait",
            show=show,
            output=os.path.join(new_path, f"{layer}_trait_mean.pdf") if new_path is not None else None
        )
    except Exception as e:
        log.warn(f"Changing clustering parameters {e.args}")
        heatmap_annotation(
            adata_cluster.T,
            row_name="labels",
            col_name=clusters,
            width=width,
            height=height,
            label="Mean TRS",
            cluster_method="median",
            cluster_metric="euclidean",
            row_legend=True,
            row_cluster=row_cluster,
            col_cluster=col_cluster,
            is_sort=is_sort,
            row_show_names=True,
            col_show_names=True,
            x_name="Cell type",
            y_name="Trait",
            show=show,
            output=os.path.join(new_path, f"{layer}_trait_mean.pdf") if new_path is not None else None
        )

    try:
        heatmap_annotation(
            adata_cluster.T,
            layer="matrix_sum",
            row_name="labels",
            col_name=clusters,
            width=width,
            height=height,
            label="Sum TRS",
            row_legend=True,
            row_cluster=row_cluster,
            col_cluster=col_cluster,
            is_sort=is_sort,
            row_show_names=True,
            col_show_names=True,
            x_name="Cell type",
            y_name="Trait",
            show=show,
            output=os.path.join(new_path, f"{layer}_trait_sum.pdf") if new_path is not None else None
        )
    except Exception as e:
        log.warn(f"Changing clustering parameters {e.args}")
        heatmap_annotation(
            adata_cluster.T,
            layer="matrix_sum",
            row_name="labels",
            col_name=clusters,
            width=width,
            height=height,
            label="Sum TRS",
            cluster_method="median",
            cluster_metric="euclidean",
            row_legend=True,
            row_cluster=row_cluster,
            col_cluster=col_cluster,
            is_sort=is_sort,
            row_show_names=True,
            col_show_names=True,
            x_name="Cell type",
            y_name="Trait",
            show=show,
            output=os.path.join(new_path, f"{layer}_trait_sum.pdf") if new_path is not None else None
        )

    try:
        heatmap_annotation(
            adata_cluster.T,
            layer="matrix_max",
            row_name="labels",
            col_name=clusters,
            width=width,
            height=height,
            label="Max TRS",
            row_legend=True,
            row_cluster=row_cluster,
            col_cluster=col_cluster,
            is_sort=is_sort,
            row_show_names=True,
            col_show_names=True,
            x_name="Cell type",
            y_name="Trait",
            show=show,
            output=os.path.join(new_path, f"{layer}_trait_max.pdf") if new_path is not None else None
        )
    except Exception as e:
        log.warn(f"Changing clustering parameters {e.args}")
        heatmap_annotation(
            adata_cluster.T,
            layer="matrix_max",
            row_name="labels",
            col_name=clusters,
            cluster_method="median",
            cluster_metric="euclidean",
            width=width,
            height=height,
            label="Max TRS",
            row_legend=True,
            row_cluster=row_cluster,
            col_cluster=col_cluster,
            is_sort=is_sort,
            row_show_names=True,
            col_show_names=True,
            x_name="Cell type",
            y_name="Trait",
            show=show,
            output=os.path.join(new_path, f"{layer}_trait_max.pdf") if new_path is not None else None
        )

    try:
        heatmap_annotation(
            adata_cluster.T,
            layer="matrix_min",
            row_name="labels",
            col_name=clusters,
            width=width,
            height=height,
            label="Min TRS",
            row_legend=True,
            row_cluster=row_cluster,
            col_cluster=col_cluster,
            is_sort=is_sort,
            row_show_names=True,
            col_show_names=True,
            x_name="Cell type",
            y_name="Trait",
            show=show,
            output=os.path.join(new_path, f"{layer}_trait_min.pdf") if new_path is not None else None
        )
    except Exception as e:
        log.warn(f"Changing clustering parameters {e.args}")
        heatmap_annotation(
            adata_cluster.T,
            layer="matrix_min",
            row_name="labels",
            col_name=clusters,
            width=width,
            height=height,
            label="Min TRS",
            cluster_method="median",
            cluster_metric="euclidean",
            row_legend=True,
            row_cluster=row_cluster,
            col_cluster=col_cluster,
            is_sort=is_sort,
            row_show_names=True,
            col_show_names=True,
            x_name="Cell type",
            y_name="Trait",
            show=show,
            output=os.path.join(new_path, f"{layer}_trait_min.pdf") if new_path is not None else None
        )


def map_df_plot(
    adata: AnnData,
    layer: str = None,
    trait_cluster_map: dict = None,
    clusters: str = "clusters",
    feature_name: str = "feature",
    width: float = 16,
    y_name: str = "value",
    column: str = "value",
    show: bool = True,
    plot_output: path = None
) -> None:
    # create path
    new_path: path = os.path.join(plot_output, f"{layer}" if layer is not None else feature_name) if plot_output is not None else None
    # create path
    if plot_output is not None:
        file_method.makedirs(new_path)

    # create data
    adata_df: DataFrame = adata_map_df(adata, column=column, layer=layer)

    # pie plot
    if trait_cluster_map is not None:
        pie_trait(
            adata_df,
            trait_cluster_map=trait_cluster_map,
            clusters=clusters,
            title=feature_name,
            show=show,
            output=new_path if plot_output is not None else None
        )

    # box plot
    box_trait(
        adata_df,
        y_name=y_name,
        value=column,
        clusters=clusters,
        width=width,
        title=feature_name,
        show=show,
        output=new_path if plot_output is not None else None
    )

    # rank plot
    barcode_trait(
        adata_df,
        sort_column=column,
        clusters=clusters,
        title=feature_name,
        show=show,
        output=new_path if plot_output is not None else None
    )

    # violin plot
    violin_trait(
        adata_df,
        y_name=y_name,
        value=column,
        width=width,
        clusters=clusters,
        title=feature_name,
        show=show,
        output=new_path if plot_output is not None else None
    )


def complete_ratio(
    adata: AnnData,
    layer: str = None,
    column: str = "value",
    clusters: str = "clusters"
) -> DataFrame:
    # create data
    adata_df: DataFrame = adata_map_df(adata, column=column, layer=layer)
    clusters_group = adata_df.groupby(["id", clusters], as_index=False).size()
    value_group = adata_df.groupby(["id", clusters, "value"], as_index=False).size()
    new_value_group = value_group.merge(clusters_group, on=["id", clusters], how="left")

    # Completion
    id_list = list(set(new_value_group["id"]))
    clusters_list = list(set(new_value_group[clusters]))
    value_list = [1.0, 0.0]
    total_size = len(id_list) * len(clusters_list) * len(value_list)

    if total_size != new_value_group.shape[0]:
        new_value_group_index = new_value_group["id"].astype(str) + "_" + new_value_group[clusters].astype(str) + "_" + new_value_group["value"].astype(int).astype(str)
        new_value_group.index = new_value_group_index
        new_value_group_index = list(new_value_group_index)

        trait_df: DataFrame = pd.DataFrame(columns=new_value_group.columns)

        # [id clusters  value  size_x  size_y]
        for _id_ in id_list:
            for _clusters_ in clusters_list:
                for _value_ in value_list:

                    # At this point, it means that the enrichment effect is 1, while the non enrichment effect is 0, so it does not exist during grouping and needs to be added here
                    if (_id_ + "_" + _clusters_ + "_" + str(int(_value_))) not in new_value_group_index:
                        exit_value = 0 if int(_value_) == 1 else 1
                        exit_index = _id_ + "_" + _clusters_ + "_" + str(exit_value)
                        exit_data = new_value_group[new_value_group.index == exit_index]
                        exit_data.loc[exit_index, "value"] = _value_
                        exit_data.loc[exit_index, "size_x"] = 0
                        exit_data.index = [_id_ + "_" + _clusters_ + "_" + str(int(_value_))]
                        trait_df = pd.concat((trait_df, exit_data), axis=0)

        new_value_group = pd.concat((trait_df, new_value_group), axis=0)

    new_value_group["rate"] = new_value_group["size_x"] / new_value_group["size_y"]

    return new_value_group


def rate_bar_plot(
    adata: AnnData,
    layer: str = None,
    trait_name: str = "All",
    dir_name: str = "feature",
    column: str = "value",
    clusters: str = "clusters",
    color: Tuple = ("#2e6fb7", "#f7f7f7"),
    legend: Tuple = ("Enrichment", "Conservative"),
    x_name: str = "Cell type",
    y_name: str = "Enrichment ratio",
    text_color: str = "#000205",
    width: float = 4,
    height: float = 4,
    bottom: float = 0,
    title: str = None,
    text_left_move: float = 0.15,
    plot_output: path = None,
    show: bool = True
) -> None:

    if dir_name is not None:
        # create path
        new_path = os.path.join(plot_output, f"{dir_name}_{layer}") if plot_output is not None else None
        # create path
        if plot_output is not None:
            file_method.makedirs(new_path)
    else:
        plot_output = None
        new_path = None

    # create data
    new_value_group = complete_ratio(adata=adata, layer=layer, column=column, clusters=clusters)

    bar_trait(
        trait_df=new_value_group,
        value="rate",
        clusters=clusters,
        title=title,
        x_name=x_name,
        y_name=y_name,
        trait_name=trait_name,
        color=color,
        legend=legend,
        text_color=text_color,
        width=width,
        height=height,
        bottom=bottom,
        text_left_move=text_left_move,
        output=new_path if plot_output is not None else None,
        show=show
    )


def calculate_init_score(
    data: matrix_data,
    overlap_data: matrix_data
) -> matrix_data:
    """
    Calculate the initial trait or disease-related cell score
    :param data: Convert the `counts` matrix to the `fragments` matrix using the `scvi.data.reads_to_fragments`
    :param overlap_data: Peaks-traits/diseases data
    :return: Initial TRS
    """
    # Processing data
    matrix = to_dense(data, is_array=True)

    # Summation information
    log.info("Calculate summation information")
    row_col_multiply = np.array(matrix.sum(axis=1)).flatten()[:, np.newaxis] * np.array(matrix.sum(axis=0)).flatten()

    all_sum = matrix.sum()

    # init_score
    log.info("Calculate initial trait-cell score")
    overlap_matrix = to_dense(overlap_data)
    global_scale_data = (row_col_multiply / all_sum) @ overlap_matrix
    global_scale_data[global_scale_data == 0] = np.abs(global_scale_data[global_scale_data != 0]).min() / 2
    init_score: matrix_data = (matrix @ overlap_matrix) / global_scale_data

    return init_score


def calculate_init_score_weight(
    adata: AnnData,
    da_peaks_adata: AnnData,
    overlap_adata: AnnData
) -> AnnData:
    """
    Calculate the initial trait or disease-related cell score with weight
    :param adata: scATAC-seq data
    :param da_peaks_adata: Differential peak data
    :param overlap_adata: Peaks-traits/diseases data
    :return: Initial TRS with weight
    """
    if "trait_info" not in list(overlap_adata.uns.keys()):
        log.error("The description of trait `trait_info` is not in `overlap_data.uns.keys()`")
        raise ValueError("The description of trait `trait_info` is not in `overlap_data.uns.keys()`")

    # Processing data
    fragments = to_dense(adata.layers["fragments"])
    overlap_matrix = to_dense(overlap_adata.X)
    weight_bf = to_dense(da_peaks_adata.X)

    # handler
    weight_bf_tf_idf = to_dense(adjustment_tf_idf(weight_bf))
    weight_bf_normalize = z_score_normalize(weight_bf_tf_idf)
    da_peaks_adata.layers["bf_normalize"] = to_sparse(weight_bf_normalize)

    log.info("Start calculate leiden cluster init_score")
    cluster_weight: matrix_data = weight_bf_normalize @ overlap_matrix
    cluster_weight = mean_symmetric_scale(cluster_weight, axis=0)
    da_peaks_adata.obsm["cluster_weight"] = to_sparse(cluster_weight)

    log.info("Start set weight")
    anno_info = adata.obs
    cell_type_weight = np.zeros((adata.shape[0], cluster_weight.shape[1]))

    for cluster in da_peaks_adata.obs_names:
        cell_type_weight[anno_info["clusters"] == cluster, :] = to_dense(da_peaks_adata[cluster, :].obsm["cluster_weight"], is_array=True).flatten()

    cell_type_weight = sigmoid(cell_type_weight)

    # calculate
    init_score = calculate_init_score(fragments, overlap_matrix)
    log.info("Calculate initial trait-cell score with cell weight")
    init_score_weight = np.multiply(init_score, cell_type_weight)

    init_score_weight_adata = AnnData(to_sparse(init_score_weight), obs=adata.obs, var=overlap_adata.uns["trait_info"])
    init_score_weight_adata.layers["init_score"] = to_sparse(init_score)
    init_score_weight_adata.layers["cell_type_weight"] = to_sparse(cell_type_weight)

    return init_score_weight_adata


def trait_related_cell_score(
    adata: AnnData,
    init_status: AnnData,
    latent_name: str = "latent",
    k: int = 30,
    or_k: int = 3,
    weight: float = 0.01,
    epsilon: float = 1e-05,
    gamma: float = 0.01,
    p: int = 2,
    min_seed_cell_rate: float = 0.01,
    max_seed_cell_rate: float = 0.05,
    is_ablation: bool = False
) -> Tuple[AnnData, RandomWalk]:
    """
    Calculate the trait or disease-related cell score with weight
    :param adata: scATAC-seq data;
    :param init_status: Initial TRS data;
    :param latent_name: Indicate the matrix used to construct the network.
        If the samples are integrated, use the "latent_harmony" with batch processing. Otherwise, for a single sample, use the "latent";
    :param k: When building an mKNN network, the number of nodes connected by each node (and);
    :param or_k: When building an mKNN network, the number of nodes connected by each node (or);
    :param weight: The weight of interactions or operations;
    :param epsilon: conditions for stopping in random walk;
    :param gamma: reset weight for random walk;
    :param p: Distance used for loss {1: Manhattan distance, 2: Euclidean distance};
    :param min_seed_cell_rate: The minimum percentage of seed cells in all cells;
    :param max_seed_cell_rate: The maximum percentage of seed cells in all cells;
    :param is_ablation: True represents obtaining the results of the ablation experiment;
    :return: 1. Cell similarity data. 2. Random walk data
    """
    # data
    latent = adata.obsm[latent_name]
    cell_anno = adata.obs

    # euclidean distances
    ed_data = euclidean_distances(latent)
    ed_scale_data = mean_symmetric_scale(ed_data, axis=1)

    log.info("Start affinity matrix")
    distances = to_dense(ed_scale_data, is_array=True)
    affinity_data = stats.gamma.pdf(distances, a=1, scale=1)
    cell_affinity = mean_symmetric_scale(affinity_data, axis=1)

    # Define KNN network
    cell_mutual_knn_weight, cell_mutual_knn = semi_mutual_knn_weight(cell_affinity, neighbors=k, or_neighbors=or_k, weight=weight)

    # cell-cell graph
    cc_data: AnnData = AnnData(to_sparse(cell_mutual_knn_weight), var=cell_anno, obs=cell_anno)
    cc_data.layers["cell_affinity"] = to_sparse(cell_affinity)
    cc_data.layers["cell_mutual_knn"] = to_sparse(cell_mutual_knn)

    # random walk
    random_walk: RandomWalk = RandomWalk(
        cc_adata=cc_data,
        init_status=init_status,
        epsilon=epsilon,
        gamma=gamma,
        p=p,
        min_seed_cell_rate=min_seed_cell_rate,
        max_seed_cell_rate=max_seed_cell_rate
    )
    random_walk.run_core()
    random_walk.run_enrichment()

    if is_ablation:
        random_walk.run_random()
        random_walk.run_core_nw()
        random_walk.run_none()
        random_walk.run_none_nw()
        random_walk.run_enrichment_nw()
        random_walk.run_en_none()
        random_walk.run_en_none_nw()

    return cc_data, random_walk


def poisson_vi(
    adata: AnnData,
    max_epochs: int = 500,
    resolution: float = 0.6,
    batch: Optional[str] = None,
    model_dir: Optional[path] = None
) -> [AnnData, str]:
    """
    PoissonVI processing of the data results in the current sample representation and peak difference data after Leiden clustering
    :param adata: processing data
    :param max_epochs: The maximum number of epochs for PoissonVI training
    :param resolution: Resolution of the Leiden Cluster
    :param batch: The name of the column in `adata.obs` that differentiates among experiments/batches.
    :param model_dir: The folder name saved by the training module
    :return: Differential peak of clustering types
    """
    log.info("Start PoissonVI")

    if resolution <= 0:
        log.error("The parameter `resolution` must be greater than zero.")
        raise ValueError("The parameter `resolution` must be greater than zero.")

    # PoissonVI, Binarization
    scvi.data.reads_to_fragments(adata)

    def __train__():
        # PoissonVI
        scvi.external.POISSONVI.setup_anndata(adata, layer="fragments")
        _model_ = scvi.external.POISSONVI(adata)
        _model_.train(max_epochs=max_epochs)
        return _model_

    if model_dir is not None:
        if os.path.exists(os.path.join(model_dir, "model.pt")):
            log.info(f"Due to the existence of file `model.pt`, it is loaded by default.")
            try:
                model = scvi.external.POISSONVI.load(model_dir, adata=adata)
            except FileExistsError as fee:
                log.error(f"File `model.pt` failed to load, you can execute `Poisson VI` again by deleting file `model.pt` ({model_dir}/model.pt).\n {fee}")
                raise ValueError(f"File `model.pt` failed to load, you can execute `Poisson VI` again by deleting file `model.pt` ({model_dir}/model.pt).")
        else:
            file_method.makedirs(model_dir)
            model = __train__()
            model.save(model_dir, overwrite=True)
    else:
        model = __train__()

    latent_name: str = "latent"
    # latent space
    latent = model.get_latent_representation()
    adata.obsm[latent_name] = latent

    if batch is not None:
        if batch not in adata.obs.columns:
            log.error(f"The `batch`({batch}) parameter must be in `adata.obs.columns`({adata.obs.columns}).")
            raise ValueError(f"The `batch`({batch}) parameter must be in `adata.obs.columns`({adata.obs.columns}).")

        log.info(f"Perform batch removal operation on `adata` using harmony.")
        latent_name += "_harmony"
        snap.pp.harmony(adata, batch=batch, use_rep="latent", key_added=latent_name, inplace=True)

    if "clusters" in adata.obs.columns:
        log.warn("Due to the original inclusion of the `clusters` column, the original `cluster` column name has been changed to `clusters_x`.")
        adata.obs["clusters_x"] = adata.obs["clusters"]

    # compute the k-nearest-neighbor graph that is used in both clustering and umap algorithms
    sc.pp.neighbors(adata, use_rep=latent_name)
    # cluster the space (we use a lower resolution to get fewer clusters than the default)
    sc.tl.leiden(adata, key_added="clusters", resolution=resolution)
    adata.obs["clusters"] = adata.obs["clusters"].astype(str)

    # umap
    try:
        data_umap = umap_data(adata.obsm[latent_name])
        adata.obsm["umap"] = data_umap
        adata.obs["latent_umap1"] = data_umap[:, 0]
        adata.obs["latent_umap2"] = data_umap[:, 1]
    except Exception as e:
        log.warn(f"UMAP error, your system does not support it, but it does not affect the process. Continue with execution: {e}")

    # tsne
    try:
        data_tsne = tsne_data(adata.obsm[latent_name])
        adata.obsm["tsne"] = data_tsne
        adata.obs["latent_tsne1"] = data_tsne[:, 0]
        adata.obs["latent_tsne2"] = data_tsne[:, 1]
    except Exception as e:
        log.warn(f"TSNE error, your system does not support it, but it does not affect the process. Continue with execution: {e}")

    clusters_list = list(set(adata.obs["clusters"]))
    clusters_list.sort()

    # differential peak
    da_peaks_all: dict = {}

    for cluster in clusters_list:
        log.info(f"Start difference peak: {cluster}/({', '.join(clusters_list)})")
        clusters_all = clusters_list.copy()
        clusters_all.remove(cluster)
        # differential peak
        da_peaks = model.differential_accessibility(adata, groupby="clusters", group1=cluster, two_sided=False)
        da_peaks_all.update({cluster: da_peaks[["bayes_factor", "emp_prob1", "group1"]]})

    adata.uns["da_peaks"] = da_peaks_all

    adata.uns["info"] = {
        "model_dir": model_dir,
        "cluster_size": len(clusters_list)
    }
    peaks_info = adata.var.copy()
    peaks_info["index"] = peaks_info.index
    peaks_info.rename_axis("peak_index", inplace=True)

    matrix_bf = np.zeros((len(clusters_list), adata.shape[1]))
    matrix_ep1 = np.zeros((len(clusters_list), adata.shape[1]))

    for i in range(len(clusters_list)):
        cluster_info = da_peaks_all[clusters_list[i]]
        cluster_info["index"] = cluster_info.index
        cluster_info.rename_axis("cluster_index", inplace=True)
        cluster_info = pd.merge(left=peaks_info, right=cluster_info, left_on="index", right_on="index", how="left")
        matrix_bf[i, :] = cluster_info["bayes_factor"]
        matrix_ep1[i, :] = cluster_info["emp_prob1"]
        time.sleep(1)

    log.info("End PoissonVI")

    obs = pd.DataFrame(clusters_list, columns=["id"])
    obs.index = obs["id"].astype(str)
    da_peaks_adata = AnnData(to_sparse(matrix_bf), obs=obs, var=adata.var)
    da_peaks_adata.layers["emp_prob1"] = matrix_ep1
    return da_peaks_adata, latent_name


def trs_plot(
    trs: AnnData,
    plot_output: str,
    clusters: str = "clusters",
    plot_columns: Tuple[str, str] = ("UMAP1", "UMAP2"),
    trait_cluster_map: dict = None,
    width: float = 8
) -> None:
    # Data distribution
    kde(trs, layer="run_core_trs_source", axis=0, title="Distribution of TRS (source)", output=os.path.join(plot_output, "trs_source_kde"))
    kde(trs, layer="run_core_trs", axis=0, title="Distribution of TRS (scale)", output=os.path.join(plot_output, "trs_scale_kde"))

    trs_layers: list = list(trs.layers)

    # plot
    file_method.makedirs(os.path.join(plot_output, "kde"))
    file_method.makedirs(os.path.join(plot_output, "trait_cell"))
    scatter_trait(trs, output=os.path.join(plot_output, "trait_cell"), title="", columns=plot_columns)
    scatter_trait(trs, output=os.path.join(plot_output, "trait_cell"), title="", layers=trs_layers, columns=plot_columns)

    group_heatmap(adata=trs, dir_name="heatmap", clusters=clusters, plot_output=plot_output)
    map_df_plot(adata=trs, feature_name="init_score_weight", trait_cluster_map=trait_cluster_map, clusters=clusters, y_name="Cell score", column="value", width=width, plot_output=plot_output)
    kde(adata=trs, axis=0, title="Initialization score with weights", output=os.path.join(plot_output, "kde", f"init_score_weight_kde"))

    # Display of Heat Map and Violin Map
    for layer in trs_layers:
        group_heatmap(adata=trs, layer=layer, dir_name="heatmap", clusters=clusters, plot_output=plot_output)
        map_df_plot(adata=trs, layer=layer, feature_name="", trait_cluster_map=trait_cluster_map, clusters=clusters, y_name="Cell score", column="value", width=width, plot_output=plot_output)
        kde(adata=trs, axis=0, layer=layer, title=layer, output=os.path.join(plot_output, "kde", f"{layer}_kde"))

        if layer.startswith("run_en"):
            rate_bar_plot(adata=trs, dir_name="enrichment", clusters=clusters, layer=layer, width=width, column="value", plot_output=plot_output)


def init_score_plot(
    init_score: AnnData,
    plot_output: str,
    clusters: str = "clusters",
    plot_columns: Tuple[str, str] = ("UMAP1", "UMAP2"),
    trait_cluster_map: dict = None,
    width: float = 8
) -> None:
    # plot
    file_method.makedirs(os.path.join(plot_output, "trait_cell"))
    layers: list = list(init_score.layers)

    scatter_trait(init_score, output=os.path.join(plot_output, "trait_cell"), title="", columns=plot_columns)
    scatter_trait(init_score, output=os.path.join(plot_output, "trait_cell"), title="", layers=layers, columns=plot_columns)

    kde(init_score, axis=0, title="Initialization score with weights", output=os.path.join(plot_output, f"init_score_weight_kde"))
    group_heatmap(adata=init_score, dir_name="heatmap", clusters=clusters, plot_output=plot_output)
    map_df_plot(adata=init_score, trait_cluster_map=trait_cluster_map, feature_name="cell", clusters=clusters, y_name="Initial score", column="value", width=width, plot_output=plot_output)

    # Display of Heat Map and Violin Map
    for layer in layers:
        kde(init_score, axis=0, layer=layer, title=layer, output=os.path.join(plot_output, f"{layer}_kde"))
        group_heatmap(adata=init_score, layer=layer, dir_name="heatmap", clusters=clusters, plot_output=plot_output)
        map_df_plot(adata=init_score, layer=layer, trait_cluster_map=trait_cluster_map, feature_name="cell", clusters=clusters, y_name="Initial score", column="value", width=width, plot_output=plot_output)


def cell_cell_plot(
    cc_data: AnnData,
    plot_output: str,
    clusters: str = "clusters",
    is_graph: bool = False
) -> None:
    # heatmap
    heatmap_annotation(
        cc_data,
        layer="cell_affinity",
        col_name=clusters,
        row_name=clusters,
        row_legend=True,
        row_anno_label=True,
        col_anno_label=True,
        output=os.path.join(plot_output, "cc_heatmap.png")
    )
    heatmap_annotation(
        cc_data,
        col_name=clusters,
        row_name=clusters,
        row_legend=True,
        row_anno_label=True,
        col_anno_label=True,
        output=os.path.join(plot_output, "cc_heatmap_mknn_weight.png")
    )
    heatmap_annotation(
        cc_data,
        layer="cell_mutual_knn",
        col_name=clusters,
        row_name=clusters,
        row_legend=True,
        row_anno_label=True,
        col_anno_label=True,
        output=os.path.join(plot_output, "cc_heatmap_mknn.png")
    )

    if is_graph:
        # Cell-cell network
        communities_graph(adata=cc_data, clusters=clusters, labels=cc_data.obs[clusters], output=os.path.join(plot_output, "cc_weight_graph"))
        communities_graph(adata=cc_data, layer="cell_mutual_knn", clusters=clusters, labels=cc_data.obs[clusters], output=os.path.join(plot_output, "cc_graph"))


def data_plot(
    init_score: AnnData,
    cc_data: AnnData,
    trs: AnnData,
    plot_output: str,
    clusters: str = "clusters",
    plot_columns: Tuple[str, str] = ("UMAP1", "UMAP2"),
    trait_cluster_map: dict = None,
    is_graph: bool = False,
    width: float = 8
) -> None:
    # scatter
    scatter_atac(trs, clusters=clusters, output=os.path.join(plot_output, "scATAC_cluster.pdf"), columns=plot_columns)

    kde(init_score, axis=0, title="Initial score with weight (scale)", output=os.path.join(plot_output, "init_score_weight_scale_kde"))

    trs_plot(
        trs=trs,
        plot_output=plot_output,
        clusters=clusters,
        plot_columns=plot_columns,
        trait_cluster_map=trait_cluster_map,
        width=width
    )

    cell_cell_plot(
        cc_data=cc_data,
        plot_output=plot_output,
        clusters=clusters,
        is_graph=is_graph
    )


def core(
    adata: AnnData,
    variants: dict,
    trait_info: DataFrame,
    cell_rate: Optional[float] = None,
    peak_rate: Optional[float] = None,
    max_epochs: int = 500,
    resolution: float = 0.6,
    batch: Optional[str] = None,
    k: int = 30,
    or_k: int = 3,
    weight: float = 0.01,
    epsilon: float = 1e-05,
    gamma: float = 0.01,
    p: int = 2,
    min_seed_cell_rate: float = 0.01,
    max_seed_cell_rate: float = 0.05,
    is_ablation: bool = False,
    model_dir: Optional[path] = None,
    clusters: str = "cell_type",
    plot_columns: Tuple[str, str] = ("UMAP1", "UMAP2"),
    trait_cluster_map: Optional[dict] = None,
    is_graph: bool = False,
    width: float = 8,
    plot_output: Optional[path] = None,
    save_path: Optional[path] = None
) -> Tuple[AnnData, AnnData, AnnData, AnnData, AnnData, RandomWalk]:
    """
    The core algorithm of scLift includes the flow of all algorithms, as well as drawing and saving data.
    In the entire algorithm, the samples are in the row position, and the traits or diseases are in the column position,
       while ensuring that there is no interaction between the traits or diseases, ensuring the stability of the results;
    :param adata: scATAC-seq data;
    :param variants: variant data;
    :param trait_info: variant annotation file information;
    :param cell_rate: Removing the percentage of cell count in total cell count only takes effect when the min_cells parameter is None;
    :param peak_rate: Removing the percentage of peak count in total peak count only takes effect when the min_peaks parameter is None;
    :param k: When building an mKNN network, the number of nodes connected by each node (and operation);
    :param or_k: When building an mKNN network, the number of nodes connected by each node (or operation);
    :param weight: The weight of interactions or operations;
    :param epsilon: conditions for stopping in random walk;
    :param gamma: reset weight for random walk;
    :param p: Distance used for loss {1: Manhattan distance, 2: Euclidean distance};
    :param min_seed_cell_rate: The minimum percentage of seed cells in all cells;
    :param max_seed_cell_rate: The maximum percentage of seed cells in all cells;
    :param max_epochs: The maximum number of epochs for PoissonVI training;
    :param is_ablation: True represents obtaining the results of the ablation experiment;
    :param resolution: Resolution of the Leiden Cluster;
    :param model_dir: The folder name saved by the training module;
    :param batch: The name of the column in `adata.obs` that differentiates among experiments/batches.
    :param clusters: Labels of clusters in the graph;
    :param plot_columns: Draw a scatter plot to display the coordinates of those two columns;
    :param trait_cluster_map: The exact enrichment relationship between known traits and cell types;
        For example:
        trait_cluster_map: dict = {
            'hct': 'Ery',
            'hgb': 'Ery',
            'hlr': 'Ery',
            'irf': 'Ery',
            'lymph': 'Lymph',
            'mch': 'Ery',
            'mchc': 'Ery',
            'mcv': 'Ery',
            'mono': 'Mono',
            'mrv': 'Ery',
            'mscv': 'Ery',
            'rbc': 'Ery',
            'rdw_cv': 'Ery',
            'ret': 'Ery'
        }
    :param is_graph: Defaults to false, indicating that the network graph will not be constructed Because when there are many samples, the construction of this graph will be very slow;
    :param width: Draw a bar chart, the width of the violin chart;
    :param plot_output: Save path for drawing; Only when parameter `plot_output` is set, parameters `clusters`, `plot_columns`, `trait_cluster_map`, `is_graph` and `width` will take effect;
    :param save_path:
    :return: All data types are AnnData:
        1. `overlap_adata`, (obs: peaks, var: traits/diseases) Peaks-traits/diseases data obtained by overlaying variant data with peaks.
        2. `da_peaks`, (obs: clusters (Leiden), var: peaks) Differential peak data of cell clustering, used for weight correction of cells.
        3. `init_score`, (obs: cells, var: traits/diseases) This is the initial TRS data.
        4. `trs`, (obs: cells, var: traits/diseases) This is the final TRS data.
        5. `cc_data`, (obs: cells, var: cells) Cell similarity data.
        6. `random_walk` RandomWalk class.
    """

    if adata.shape[0] == 0:
        log.error("The scATAC-seq data is empty.")
        raise ValueError("The scATAC-seq data is empty.")

    if len(variants.keys()) == 0:
        log.error("The number of mutations is empty.")
        raise ValueError("The number of mutations is empty.")

    if len(variants.keys()) != trait_info.shape[0]:
        log.error("The parameters `variants` and `trait_info` are inconsistent. These two parameters can be obtained using method `read_variants`.")
        raise ValueError("The parameters `variants` and `trait_info` are inconsistent. These two parameters can be obtained using method `read_variants`.")

    if batch is not None and batch not in adata.obs.columns:
        log.error(f"The `batch`({batch}) parameter must be in `adata.obs.columns`({adata.obs.columns}).")
        raise ValueError(f"The `batch`({batch}) parameter must be in `adata.obs.columns`({adata.obs.columns}).")

    peak_columns: list = list(adata.var.columns)

    if "chr" not in peak_columns or "start" not in peak_columns or "end" not in peak_columns:
        log.error(f"The peaks information {peak_columns} in data `adata` must include three columns: `chr`, `start` and `end`. (It is recommended to use the `read_sc_atac` method.)")
        raise ValueError(f"The peaks information {peak_columns} in data `adata` must include three columns: `chr`, `start` and `end`. (It is recommended to use the `read_sc_atac` method.)")

    if cell_rate is not None:

        if cell_rate <= 0 or cell_rate >= 1:
            log.error("The parameter of `cell_rate` should be between 0 and 1.")
            raise ValueError("The parameter of `cell_rate` should be between 0 and 1.")

    if peak_rate is not None:

        if peak_rate <= 0 or peak_rate >= 1:
            log.error("The parameter of `peak_rate` should be between 0 and 1.")
            raise ValueError("The parameter of `peak_rate` should be between 0 and 1.")

    if resolution <= 0:
        log.error("The parameter `resolution` must be greater than zero.")
        raise ValueError("The parameter `resolution` must be greater than zero.")

    if k <= 0:
        log.error("The `k` parameter must be a natural number greater than 0.")
        raise ValueError("The `k` parameter must be a natural number greater than 0.")

    if or_k <= 0:
        log.error("The `or_k` parameter must be a natural number greater than 0.")
        raise ValueError("The `or_k` parameter must be a natural number greater than 0.")

    if k < or_k:
        log.warn("The parameter value of `or_k` is greater than the parameter value of `k`, which is highly likely to result in poor performance.")

    if weight < 0 or weight > 1:
        log.error("The parameter of `weight` should be between 0 and 1.")
        raise ValueError("The parameter of `weight` should be between 0 and 1.")

    if gamma < 0 or gamma > 1:
        log.error("The parameter of `gamma` should be between 0 and 1.")
        raise ValueError("The parameter of `gamma` should be between 0 and 1.")

    if min_seed_cell_rate < 0 or min_seed_cell_rate > 1:
        log.error("The parameter of `min_seed_cell_rate` should be between 0 and 1.")
        raise ValueError("The parameter of `min_seed_cell_rate` should be between 0 and 1.")

    if max_seed_cell_rate < 0 or max_seed_cell_rate > 1:
        log.error("The parameter of `max_seed_cell_rate` should be between 0 and 1.")
        raise ValueError("The parameter of `max_seed_cell_rate` should be between 0 and 1.")

    if epsilon > 0.1:
        log.warn(f"Excessive value of parameter `epsilon`=({epsilon}) can lead to incorrect iteration and poor enrichment effect.")
    elif epsilon < 0:
        epsilon = 0
        log.warn("The parameter value of `epsilon` is less than 0, which is equivalent to the effect of zero. Therefore, setting the value of epsilon will be set to zero.")

    if p <= 0:
        log.error("The `p` parameter must be a natural number greater than 0.")
        raise ValueError("The `p` parameter must be a natural number greater than 0.")
    elif p > 3:
        log.warn("Suggested value for `p` is 1 or 2.")

    if plot_output is not None:

        if clusters not in adata.obs.columns:
            log.warn(f"The value of `clusters`: {clusters} is not included in the column name {adata.obs.columns} in the cell annotation, so it is changed to the column name of the subsequent `Leiden` clustering results.")
            clusters = "clusters"
            log.warn(f"Define parameter `clusters` as \"clusters\"")

        if clusters == "clusters" and clusters in adata.obs.columns:
            log.warn("The `clusters` column name is the result column name of subsequent leiden clustering, so it is changed to \"cluster_x\".")
            clusters = "clusters_x"

        if len(plot_columns) != 2:
            log.error("The parameter `plot_columns` must contain two values.")
            raise ValueError("The parameter `plot_columns` must contain two values.")

        if plot_columns[0] not in adata.obs.columns or plot_columns[1] not in adata.obs.columns:
            log.warn(f"A value in `plot_columns` ({plot_columns}) is not in the corresponding column (adata.obs.columns) ({adata.obs.columns}).")
            plot_columns = ("latent_umap1", "latent_umap2")
            log.warn(f"Define parameter `plot_columns` as (\"latent_umap1\", \"latent_umap2\")")

        if width <= 0:
            log.error("The value of the `width` parameter must be greater than 0.")
            raise ValueError("The value of the `width` parameter must be greater than 0.")

    filter_data(adata, cell_rate=cell_rate, peak_rate=peak_rate)
    # PoissonVI
    da_peaks, latent_name = poisson_vi(adata, max_epochs=max_epochs, resolution=resolution, batch=batch, model_dir=model_dir)

    # overlap
    overlap_adata: AnnData = overlap_sum(adata, variants, trait_info)

    # intermediate score data, integration data
    init_score: AnnData = calculate_init_score_weight(
        adata=adata,
        da_peaks_adata=da_peaks,
        overlap_adata=overlap_adata
    )

    # KNN network and random walk
    cc_data, random_walk = trait_related_cell_score(
        adata=adata,
        init_status=init_score,
        latent_name=latent_name,
        k=k,
        or_k=or_k,
        weight=weight,
        epsilon=epsilon,
        gamma=gamma,
        p=p,
        min_seed_cell_rate=min_seed_cell_rate,
        max_seed_cell_rate=max_seed_cell_rate,
        is_ablation=is_ablation
    )
    trs = random_walk.trs_data

    if save_path is not None:
        save_path = str(save_path)
        file_method.makedirs(save_path)

        # save result
        save_h5ad(trs, f"{save_path}/trs.h5ad")

        # save
        save_h5ad(adata, f"{save_path}/sc_atac_filter.h5ad")
        save_h5ad(da_peaks, f"{save_path}/da_peaks.h5ad")

        save_h5ad(overlap_adata, f"{save_path}/atac_overlap.h5ad")
        save_h5ad(init_score, f"{save_path}/init_score.h5ad")

        save_h5ad(cc_data, f"{save_path}/cc_data.h5ad")

    if plot_output is not None:
        plot_output = str(plot_output)
        file_method.makedirs(plot_output)

        data_plot(
            init_score=init_score,
            trs=trs,
            cc_data=cc_data,
            plot_output=plot_output,
            clusters=clusters,
            plot_columns=plot_columns,
            trait_cluster_map=trait_cluster_map,
            is_graph=is_graph,
            width=width
        )

    return overlap_adata, da_peaks, init_score, trs, cc_data, random_walk
