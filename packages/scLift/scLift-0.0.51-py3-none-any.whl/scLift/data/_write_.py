# -*- coding: UTF-8 -*-

import os.path
from pathlib import Path
from typing import Optional, Union

import h5py
import numpy as np
import pandas as pd
from pandas import DataFrame
from anndata import AnnData
import scipy.io as scio
from scipy.sparse import vstack
import snapatac2 as snap
from snapatac2.genome import Genome

from ykenan_log import Logger
from ykenan_file import StaticMethod

from ._read_ import read_sc_atac, read_h5ad
from scLift.util import path, collection, to_sparse, to_dense, check_adata_get

file_method = StaticMethod()
log = Logger("scLift_data_write")


def save_h5ad(data: AnnData, file: path) -> AnnData:
    """
    Write AnnData data
    :param data: data
    :param file: save file
    :return: AnnData data
    """
    log.info("Saving data to {}".format(file))
    return data.write_h5ad(Path(file), compression='gzip')


def save_h5(data: dict, save_file: path, group_name: str = "matrix"):
    h5_dict = dict(data)

    file = h5py.File(f"{str(save_file)}", 'w')
    grp = file.create_group(group_name)

    for key, value in h5_dict.items():
        grp.create_dataset(key, data=value)

    file.close()


def to_meta(adata: AnnData, dir_path: path, feature_name: str = "peaks.bed"):
    dir_path = str(dir_path)
    file_method.makedirs(dir_path)

    #  Convert dense matrices to sparse matrices
    sparse_matrix = to_sparse(adata.X)
    # write mtx file
    log.info(f"Write mtx file")
    scio.mmwrite(os.path.join(dir_path, 'matrix.mtx'), sparse_matrix.T)

    # Cell annotation
    log.info(f"Write cell annotation")
    cell_info: DataFrame = adata.obs
    cell_info["barcodes"] = adata.obs.index.to_list()
    cell_info.to_csv(os.path.join(dir_path, "annotation.txt"), index=False, sep="\t", lineterminator="\n", encoding="utf-8")

    # barcodes
    log.info(f"Write barcodes")
    barcodes = pd.DataFrame(adata.obs.index.to_list(), columns=["index"])
    barcodes.to_csv(os.path.join(dir_path, "barcodes.tsv"), index=False, header=False, sep="\t", lineterminator="\n", encoding="utf-8")

    # feature
    log.info(f"Write feature")
    feature_info: DataFrame = adata.var
    if feature_name.split(".")[0] == "peaks":
        feature = pd.DataFrame(feature_info.index.to_list(), columns=["index"])
        new_feature = feature["index"].astype(str).str.split("[:-]", expand=True)
        new_feature.to_csv(os.path.join(dir_path, feature_name), index=False, header=False, sep="\t", lineterminator="\n", encoding="utf-8")
    else:
        feature = pd.DataFrame(feature_info.index.to_list(), columns=["index"])
        feature.to_csv(os.path.join(dir_path, feature_name), index=False, header=False, sep="\t", lineterminator="\n", encoding="utf-8")


def to_fragments(
    adata: AnnData,
    fragments: str,
    layer: str = None,
    record_count: int = 100000
) -> None:
    output_path = os.path.dirname(fragments)
    file_method.makedirs(output_path)

    data = check_adata_get(adata=adata, layer=layer).T

    # get group information
    data_obs: DataFrame = data.obs.copy()
    data_var: DataFrame = data.var.copy()

    if "chr" not in data_obs.columns or "start" not in data_obs.columns or "end" not in data_obs.columns:
        log.error("`chr` or `start`or  `end` not in obs column")
        raise ValueError("`chr` or `start` or `end` not in obs column")

    if "barcodes" not in data_var.columns:
        log.error(f"`barcodes` not in obs column")
        raise ValueError(f"`barcodes` not in obs column")

    log.info("Sort chr start")
    data_obs.sort_values(["chr", "start"], inplace=True)
    data = data[data_obs.index, :]
    matrix = to_dense(data.X, is_array=True)

    row_size, col_size = data.shape
    row_range, col_range = range(row_size), range(col_size)
    all_number: int = row_size * col_size
    log.info(f"Get size {row_size, col_size} ==> {all_number}")

    # Convert to dictionary
    barcodes_dict: dict = dict(zip(list(col_range), data_var.index))
    peaks_dict: dict = dict(zip(list(row_range), zip(data_obs["chr"], data_obs["start"], data_obs["end"])))

    count = 0

    log.info("Sort write info")
    with open(fragments, mode="w", encoding="utf-8", newline="\n") as f:
        for value in np.nditer(matrix):

            if count >= record_count and count % record_count == 0:
                log.info(f"Processed {count} lines, completed {round(count / all_number, 4) * 100} %")

            # index
            row_index = count // col_size
            col_index = count % col_size
            # info
            peaks = peaks_dict[row_index]
            barcodes = barcodes_dict[col_index]
            f.write(f"{peaks[0]}\t{peaks[1]}\t{peaks[2]}\t{barcodes}\t{value}\n")
            count += 1


def merge_sc_atac(
    files: dict,
    gene_anno: Genome,
    merge_key: str = "merge_sc_atac",
    min_num_fragments: int = 200,
    sorted_by_barcode: bool = False,
    bin_size: int = 500,
    min_tsse: int = 5,
    max_iter_harmony: int = 20,
    is_selected: bool = False,
    need_features: Optional[Union[int | float]] = None,
    output_path: Optional[path] = None
) -> AnnData:
    """
    Integrate multiple scATAC-seq data through snapATAC2 (https://kzhang.org/SnapATAC2/tutorials/integration.html)
    Note: Please do not move the generated files during this processing
    :param files: {file_key: file path of scATAC-seq data, ...} scATAC-seq data information that needs to be integrated
    :param gene_anno: Reference genome, commonly known as `snap.genome.hg38` and `snap.genome.hg19`
    :param merge_key: Finally form the file name of H5AD
    :param min_num_fragments: Number of unique fragments threshold used to filter cells
    :param sorted_by_barcode: Is the input fragments file sorted
    :param bin_size: The size of consecutive genomic regions used to record the counts.
    :param min_tsse: Minimum TSS enrichment score required for a cell to pass filtering.
    :param max_iter_harmony: The maximum number of iterations in the `harmony` algorithm.
    :param is_selected:
    :param need_features: If `need_features` <=1, it represents the retention of `need_features`% of the overall features. Otherwise, it is considered an integer and `need_features` features are filtered.
    :param output_path: Path to generate file
    :return: Integrated scATAC-seq data
    """
    log.info("Start integrating scATAC-seq data.")

    def get_feature_count(raw_count: int) -> int:
        return int(raw_count * need_features) if need_features <= 1 else int(need_features)

    # Obtain sample information
    filenames: list = list(files.keys())

    if len(filenames) <= 1:
        log.error("At least two samples are required.")
        raise ValueError("At least two samples are required.")

    # file path
    file_list: list = list(files.values())

    # The situation where features have been filtered
    features: Optional[str] = None

    # Sample data container
    adatas: list = []

    if str(file_list[0]).endswith(".h5ad"):
        log.warn("Suggest using fragments files to integrate scATA seq data. (If the process of adding tile matrices, selecting features, and identifying doubles has been completed through snapATAC2, this message can be ignored.)")
        adata_list: list = [(name, adata) for name, adata in zip(filenames, file_list)]

        # Add data
        for file in file_list:
            adatas.append(read_sc_atac(file))

    else:
        output_filenames: list = [os.path.join(output_path, key + ".h5ad") for key in list(files.keys())]

        # import the fragment files
        adatas = snap.pp.import_data(
            file_list,
            file=output_filenames if output_path is not None else None,
            chrom_sizes=gene_anno,
            min_num_fragments=min_num_fragments,
            sorted_by_barcode=sorted_by_barcode
        )

        # the standard procedures to add tile matrices, select features, and identify doublets
        snap.metrics.tsse(adatas, gene_anno)

        log.info(f"Filter cells through TSSE ({min_tsse})")
        snap.pp.filter_cells(adatas, min_tsse=min_tsse)

        log.info("Add tile matrix.")
        snap.pp.add_tile_matrix(adatas, bin_size=bin_size)

        if need_features is not None:
            feature_count: int = get_feature_count(adatas[0].shape[1])
            log.info("Select {} features".format(feature_count))
            snap.pp.select_features(adatas, n_features=feature_count)
            features = "selected"

        log.info("Identify doublets.")
        snap.pp.scrublet(adatas, features=features)
        log.info("Filter doublets.")
        snap.pp.filter_doublets(adatas)

        adata_list: list = [(name, adata) for name, adata in zip(filenames, adatas)]

    # AnnDataSet
    merge_filename: str = os.path.join(output_path, merge_key + ".h5ad") if output_path is not None else None
    data = snap.AnnDataSet(adatas=adata_list, filename=merge_filename)

    # id unique
    data.obs['barcodes'] = data.obs_names
    unique_cell_ids = [sa + '_' + bc for sa, bc in zip(data.obs['sample'], data.obs_names)]
    data.obs_names = unique_cell_ids

    selected_list: collection = np.array([])

    if need_features is not None:
        snap.pp.select_features(data, n_features=get_feature_count(data.shape[1]))
        selected_list = np.array(list(data.var["selected"]))

    # spectral
    snap.tl.spectral(data, features=features)

    # Batch correction
    log.info("Batch correction.")
    snap.pp.mnc_correct(data, batch="sample")
    snap.pp.harmony(data, batch="sample", max_iter_harmony=max_iter_harmony)

    # close
    data.close()

    # read file
    sc_atac = read_sc_atac(merge_filename)

    # form count matrix
    data_matrix = []
    adata_path_list = list(sc_atac.uns["AnnDataSet"]["file_path"])

    for _adata_path_ in adata_path_list:
        _adata_ = read_h5ad(_adata_path_)
        data_matrix.append(_adata_.X)

        if is_selected and need_features is not None:
            selected_list = np.logical_and(selected_list, np.array(list(_adata_.var["selected"])))

    sc_atac.X = vstack(data_matrix)

    if need_features is not None:
        sc_atac = sc_atac[:, selected_list]

    sc_atac.obs.index = sc_atac.obs.index.astype(str)
    sc_atac.var.index = sc_atac.var.index.astype(str)

    if output_path is not None:
        save_h5ad(sc_atac, os.path.join(output_path, f"{merge_key}_sc_atac.h5ad"))

    log.info("End integrating scATAC-seq data.")
    return sc_atac
