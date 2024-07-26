# -*- coding: UTF-8 -*-

from typing import Optional

from ykenan_log import Logger

from anndata import AnnData
import scanpy as sc

log = Logger("scLift_model_preprocessing")


def filter_data(
    adata: AnnData,
    min_cells: int = 1,
    min_peaks: int = 1,
    min_peaks_counts: int = 1,
    min_cells_counts: int = 1,
    cell_rate: Optional[float] = None,
    peak_rate: Optional[float] = None,
    is_copy: bool = False,
    is_min_cell: bool = True,
    is_min_peak: bool = False
) -> AnnData:
    """
    Filter scATAC data
    :param adata: scATAC-seq data
    :param min_peaks_counts: Minimum number of counts required for a peak to pass filtering
    :param min_cells: Minimum number of cells expressed required for a peak to pass filtering
    :param min_cells_counts: Minimum number of counts required for a cell to pass filtering
    :param min_peaks: Minimum number of peaks expressed required for a cell to pass filtering
    :param cell_rate: Removing the percentage of cell count in total cell count only takes effect when the min_cells parameter is None
    :param peak_rate: Removing the percentage of peak count in total peak count only takes effect when the min_peaks parameter is None
    :param is_copy: Do you want to deeply copy data
    :param is_min_cell: Whether to screen cells
    :param is_min_peak: Whether to screen peaks
    :return: scATAC-seq data
    """
    log.info("Filter scATAC data")

    if adata.shape[0] == 0:
        log.error("The scATAC data is empty")
        raise ValueError("The scATAC data is empty")

    filter_adata = adata.copy() if is_copy else adata
    cells_count, peaks_count = filter_adata.shape

    if cell_rate is not None:

        if cell_rate <= 0 or cell_rate >= 1:
            log.error("The parameter of `cell_rate` should be between 0 and 1.")
            raise ValueError("The parameter of `cell_rate` should be between 0 and 1.")

        _min_cells_ = int(filter_adata.shape[0] * cell_rate)

        if _min_cells_ > 1:
            min_cells = _min_cells_

    if peak_rate is not None:

        if peak_rate <= 0 or peak_rate >= 1:
            log.error("The parameter of `peak_rate` should be between 0 and 1.")
            raise ValueError("The parameter of `peak_rate` should be between 0 and 1.")

        _min_peaks_ = int(filter_adata.shape[1] * peak_rate)

        if _min_peaks_ > 1:
            min_peaks = _min_peaks_

    log.info(f"min cells: {min_cells}, min peaks: {min_peaks}")
    sc.pp.filter_genes(filter_adata, min_cells=min_cells)
    sc.pp.filter_cells(filter_adata, min_genes=min_peaks)

    # filter peaks and cell
    if is_min_peak:
        sc.pp.filter_genes(filter_adata, min_counts=min_peaks_counts)

    if is_min_cell:
        sc.pp.filter_cells(filter_adata, min_counts=min_cells_counts)
    else:
        sc.pp.filter_cells(filter_adata)

    # judge cells count
    if filter_adata.shape[0] == 0:
        log.error("After screening, the number of cells was 0. Suggest setting the `is_min_peak` parameter to `False` or lowering the `cell_rate` and `peak_rate` parameters to try again")
        return filter_adata

    log.info(f"filter cells {cells_count - filter_adata.shape[0]}, filter peaks {peaks_count - filter_adata.shape[1]}")
    log.debug(f"Size of filtered scATAC data: {filter_adata.shape}")
    return filter_adata
