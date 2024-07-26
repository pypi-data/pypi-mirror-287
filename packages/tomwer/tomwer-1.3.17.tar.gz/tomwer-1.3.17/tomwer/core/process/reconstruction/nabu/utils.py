# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2020 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "06/08/2020"


import datetime
import logging
import os
import typing
from contextlib import AbstractContextManager

from nabu.pipeline.config import generate_nabu_configfile, parse_nabu_config_file
from nabu.pipeline.fullfield.nabu_config import (
    nabu_config as nabu_fullfield_default_config,
)
from silx.utils.enum import Enum as _Enum

import tomwer.version
from tomwer.core.process.reconstruction.nabu.plane import NabuPlane
from tomwer.core.scan.edfscan import EDFTomoScan
from tomwer.core.scan.nxtomoscan import NXtomoScan
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.core.volume.edfvolume import EDFVolume
from tomwer.core.volume.hdf5volume import HDF5Volume
from tomwer.core.volume.jp2kvolume import JP2KVolume
from tomwer.core.volume.rawvolume import RawVolume
from tomwer.core.volume.tiffvolume import TIFFVolume

_logger = logging.getLogger(__name__)


class TomwerInfo(AbstractContextManager):
    """Simple context manager to add tomwer metadata to a dict before
    writing it"""

    def __init__(self, config_dict):
        self.config = config_dict

    def __enter__(self):
        self.config["other"] = {
            "tomwer_version": tomwer.version.version,
            "date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        }
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.config["other"]["tomwer_version"]
        del self.config["other"]["date"]


def retrieve_lst_of_value_from_str(my_string: str, type_) -> tuple:
    """
    Return a list of value from a string like '12,23' or '(12, 23)',
    '[12;23]', '12;23' or with the pattern from:to:step like '0:10:1'

    :param str mystring:
    :return: list of single value
    """
    if not isinstance(my_string, str):
        raise TypeError(
            f"my_string is expected to be a string. {type(my_string)} provided"
        )
    res = []
    my_string = my_string.replace("(", "")
    my_string = my_string.replace(")", "")
    my_string = my_string.replace("[", "")
    my_string = my_string.replace("]", "")
    if my_string.count(":") == 2:
        _from, _to, _step = my_string.split(":")
        _from, _to, _step = float(_from), float(_to), float(_step)
        if _from > _to:
            tmp = _to
            _to = _from
            _from = tmp
        while _from <= _to:
            res.append(_from)
            _from += _step
        return tuple(res)
    else:
        vals = my_string.replace(" ", "")
        vals = vals.replace("_", "")
        vals = vals.replace(";", ",").split(",")
        for val in vals:
            try:
                res.append(type_(val))
            except Exception:
                pass
        return tuple(res)


def get_nabu_resources_desc(scan: TomwerScanBase, method, workers=1) -> dict:
    """
    Create the descriptor of nabu's resources

    :param TomwerScanBase scan:
    :param str method:
    :return: nabu's description of resources to be used
    """
    assert isinstance(scan, TomwerScanBase)
    res = {
        "method": method,
        "cpu_workers": workers,
        "partition": "gpu",
        "memory_per_node": "90%",
        "threads_per_node": "100%",
        "walltime": "01:00:00",
    }
    return res


def get_nabu_about_desc(overwrite) -> dict:
    """
    Create the description for nabu's about

    :param self:
    :return:
    """
    return {"overwrite_results": str(bool(overwrite))}


def get_recons_volume_identifier(
    file_prefix: str,
    location: str,
    file_format: str,
    scan: TomwerScanBase,
    slice_index: typing.Union[int, None],
    axis: NabuPlane,
) -> tuple:
    """
    return tuple of DataUrl for existings slices
    """
    axis = NabuPlane.from_value(axis)
    file_format = file_format.lower()
    if file_format in ("hdf5", "h5", "hdf"):
        if slice_index is not None:
            # case of a single hdf5 file
            file_name = "_".join(
                (file_prefix, "plane", axis.value, str(slice_index).zfill(6))
            )
        else:
            file_name = file_prefix
        file_name = ".".join((file_name, file_format))
        file_path = os.path.join(location, file_name)

        if isinstance(scan, NXtomoScan):
            entry = scan.entry
        elif isinstance(scan, EDFTomoScan):
            entry = "entry"
        else:
            raise NotImplementedError(f"unrecognized scan type ({type(scan)})")

        volumes = (
            HDF5Volume(
                file_path=file_path,
                data_path="/".join([entry, "reconstruction"]),
            ),
        )
    elif file_format in ("vol", "raw"):
        if slice_index is not None:
            # case of a single hdf5 file
            file_name = "_".join(
                (file_prefix, "plane", axis.value, str(slice_index).zfill(6))
            )
        else:
            file_name = file_prefix
        file_name = ".".join((file_name, file_format))
        file_path = os.path.join(location, file_name)

        volumes = (RawVolume(file_path=file_path),)
    elif file_format in ("jp2", "jp2k", "edf", "tiff"):
        if file_format in ("jp2k", "jp2"):
            constructor = JP2KVolume
        elif file_format == "edf":
            constructor = EDFVolume
        elif file_format == "tiff":
            constructor = TIFFVolume
        else:
            raise NotImplementedError
        basename = file_prefix
        file_path = location
        volumes = (
            constructor(
                folder=location,
                volume_basename=basename,
            ),
        )

    # case of the multitiff. Not handled by tomwer
    # elif file_format == "tiff":
    #     # for single frame tiff nabu uses another convention by saving it 'directly'.
    #     volumes = (
    #         MultiTIFFVolume(
    #             file_path=os.path.join(
    #                 location,
    #                 file_prefix,
    #                 ".".join([file_prefix, file_format]),
    #             ),
    #         ),
    #     )

    else:
        raise ValueError(f"file format not managed: {file_format}")

    return tuple([volume.get_identifier() for volume in volumes])


def get_multi_cor_recons_volume_identifiers(
    scan: TomwerScanBase,
    slice_index: int,
    location: str,
    file_prefix: str,
    cors: tuple,
    file_format: str,
    axis=NabuPlane.XY,
) -> dict:
    """
    util to retrieve Volumes (identifier) reconstructed by nabu-multicor

    :param TomwerScanBase scan: scam processed by the nabu-multicor
    :param str location: location of the files
    :param tuple cors: cors for which we want the reconstructed slices. As this extension is created by nabu
                       the cor reference is in absolute.
    :param str file_format: file format of the reconstruction

    :return: a dict with absolute cor value as key and the Volume identifier as value
    """
    _logger.info("Deduce volume identifiers for nabu-multicor")
    if isinstance(slice_index, str):
        slice_index = slice_index_to_int(
            slice_index=slice_index,
            scan=scan,
            axis=axis,  # for now we always expect the multicor to be done along Z
        )
    assert isinstance(
        slice_index, int
    ), "slice_index is expected to be an int or to be converted to it"
    res = {}
    if isinstance(scan, EDFTomoScan):
        entry = "entry"
    else:
        entry = scan.entry

    for cor in cors:
        file_path = os.path.join(
            location,
            f"{file_prefix}_{cor:.3f}_{str(slice_index).zfill(5)}.{file_format}",
        )

        if file_format in ("hdf5", "h5", "hdf"):
            file_path = os.path.join(
                location,
                f"{file_prefix}_{cor:.3f}_{str(slice_index).zfill(5)}.{file_format}",
            )
            volume = HDF5Volume(
                file_path=file_path,
                data_path="/".join([entry, "reconstruction"]),
            )
        elif file_format in ("vol", "raw"):
            volume = (RawVolume(file_path=file_path),)
        elif file_format in ("jp2", "jp2k", "edf", "tiff"):
            if file_format in ("jp2k", "jp2"):
                constructor = JP2KVolume
            elif file_format == "edf":
                constructor = EDFVolume
            elif file_format == "tiff":
                constructor = TIFFVolume
            else:
                raise NotImplementedError
            file_path = location
            volume = constructor(
                folder=os.path.dirname(file_path),
                volume_basename=os.path.basename(file_path),
            )
        else:
            raise ValueError(f"file_format {file_format} is not handled for now")
        res[cor] = volume.get_identifier()
    return res


class _NabuMode(_Enum):
    FULL_FIELD = "standard acquisition"
    HALF_ACQ = "half acquisition"
    HELICAL = "helical acquisition"


class _NabuStages(_Enum):
    INI = "initialization"
    PRE = "pre-processing"
    PHASE = "phase"
    PROC = "processing"
    POST = "post-processing"
    VOLUME = "volume"

    @staticmethod
    def getStagesOrder():
        return (
            _NabuStages.INI,
            _NabuStages.PRE,
            _NabuStages.PHASE,
            _NabuStages.PROC,
            _NabuStages.POST,
        )

    @staticmethod
    def getProcessEnum(stage):
        """Return the process Enum associated to the stage"""
        stage = _NabuStages.from_value(stage)
        if stage is _NabuStages.INI:
            raise NotImplementedError()
        elif stage is _NabuStages.PRE:
            return _NabuPreprocessing
        elif stage is _NabuStages.PHASE:
            return _NabuPhase
        elif stage is _NabuStages.PROC:
            return _NabuProcessing
        elif stage is _NabuStages.POST:
            return _NabuPostProcessing
        raise NotImplementedError()


class _NabuPreprocessing(_Enum):
    """Define all the preprocessing action possible and the order they
    are applied on"""

    FLAT_FIELD_NORMALIZATION = "flat field normalization"
    CCD_FILTER = "hot spot correction"

    @staticmethod
    def getPreProcessOrder():
        return (
            _NabuPreprocessing.FLAT_FIELD_NORMALIZATION,
            _NabuPreprocessing.CCD_FILTER,
        )


class _NabuPhase(_Enum):
    """Define all the phase action possible and the order they
    are applied on"""

    PHASE = "phase retrieval"
    UNSHARP_MASK = "unsharp mask"
    LOGARITHM = "logarithm"

    @staticmethod
    def getPreProcessOrder():
        return (_NabuPhase.PHASE, _NabuPhase.UNSHARP_MASK, _NabuPhase.LOGARITHM)


class _NabuProcessing(_Enum):
    """Define all the processing action possible"""

    RECONSTRUCTION = "reconstruction"

    @staticmethod
    def getProcessOrder():
        return (_NabuProcessing.RECONSTRUCTION,)


class _NabuPostProcessing(_Enum):
    """Define all the post processing action available"""

    SAVE_DATA = "save"

    @staticmethod
    def getProcessOrder():
        return (_NabuPostProcessing.SAVE_DATA,)


class _NabuReconstructionMethods(_Enum):
    FBP = "FBP"


class _NabuPhaseMethod(_Enum):
    """
    Nabu phase method
    """

    PAGANIN = "Paganin"
    CTF = "CTF"
    NONE = "None"

    @classmethod
    def from_value(cls, value):
        if value in (None, ""):
            return _NabuPhaseMethod.NONE
        elif isinstance(value, str):
            if value.lower() == "paganin":
                return _NabuPhaseMethod.PAGANIN
            elif value.lower() == "none":
                return _NabuPhaseMethod.NONE
            elif value.lower() == "ctf":
                return _NabuPhaseMethod.CTF
        else:
            return super().from_value(value=value)


class _NabuFBPFilterType(_Enum):
    RAMLAK = "ramlak"
    SHEPP_LOGAN = "shepp-logan"
    COSINE = "cosine"
    HAMMING = "hamming"
    HANN = "hann"
    TUKEY = "tukey"
    LANCZOS = "lanczos"
    HILBERT = "hilbert"


class _NabuPaddingType(_Enum):
    ZEROS = "zeros"
    EDGES = "edges"


class RingCorrectionMethod(_Enum):
    NONE = "None"
    MUNCH = "munch"
    VO = "vo"
    MEAN_SUBTRACTION = "mean-subtraction"
    MEAN_DIVISION = "mean-division"


def nabu_std_err_has_error(errs: typing.Optional[bytes]):
    """
    small util to parse stderr where some warning can exists.
    But I don't think we want to catch all warnings from nabu so this is a (bad) concession
    This will disapear when execution will be done directly from a tomwer thread instead of a subprocess
    """

    def ignore(line) -> bool:
        return (
            "warning" in line
            or "Warning" in line
            or "cupyx.jit.rawkernel" in line
            or "deprecated" in line
            or line.replace(" ", "") == ""
            or "unable to load" in line
            or "deprecated" in line
            or "self.module = SourceModule(self.src, **self.sourcemodule_kwargs)"
            in line
            or "return SourceModule(" in line
            or "CUBLAS" in line
            or "Not supported for EDF"
            in line  # debatable but very disturbing from the gui side... anyway EDF days are coming to an end
            or "PerformanceWarning" in line
            or "jitify._init_module()" in line
        )

    if errs is None:
        return False
    else:
        for line in errs.decode("UTF-8").split("\n"):
            if not ignore(line):
                return True
    return False


def update_cfg_file_after_transfer(config_file_path, old_path, new_path):
    """
    update nabu configuration file path from /lbsram/data to /data
    """
    if old_path is None or new_path is None:
        return

    # load configucation file
    config_as_dict = parse_nabu_config_file(config_file_path)
    assert isinstance(config_as_dict, dict)

    # update paths
    paths_to_update = (
        ("dataset", "location"),
        ("output", "location"),
        ("pipeline", "steps_file"),
    )
    for section, field in paths_to_update:
        # update dataset location and output location
        if section in config_as_dict:
            location = config_as_dict[section].get(field, None)
            if location is not None:
                config_as_dict[section][field] = location.replace(old_path, new_path, 1)
    # overwrite file
    generate_nabu_configfile(
        fname=config_file_path,
        default_config=nabu_fullfield_default_config,
        config=config_as_dict,
        options_level="advanced",
    )


def slice_index_to_int(
    slice_index: typing.Union[int, str],
    scan: TomwerScanBase,
    axis=NabuPlane.XY,
) -> int:
    """
    cast a slice to an index. The slice can be a string in ['first', 'last', 'middle']
    """
    axis = NabuPlane.from_value(axis)
    if slice_index == "fisrt":
        return 0
    elif slice_index == "last":
        if scan is None:
            # backward compatibility in the case the scan is not provided. Should not happen anymore
            _logger.warning("Scan not provided. Consider the 2048 width detector")
            return 2047
        elif scan.dim_2 is not None:
            return scan.dim_2 - 1
        else:
            # this could happen on some EDF scans. Not expected to happen for HDF5
            _logger.warning("unable to get dim size, guess this is 2048 width")
            # in this
            return 2047
    elif slice_index == "middle":
        if scan is None:
            # backward compatibility in the case the scan is not provided. Should not happen anymore
            _logger.warning("Scan not provided. Consider the 1024 width detector")
            # default middle.
            return 1024
        elif axis is NabuPlane.XY:
            if scan.dim_2 is None:
                _logger.warning("unable to get dim size, guess this is 2048 height")
                return 1024
            else:
                return scan.dim_2 // 2
        elif axis in (NabuPlane.YZ, NabuPlane.XZ):
            if scan.dim_1 is None:
                _logger.warning("unable to get dim size, guess this is 2048 width")
                return 1024
            else:
                return scan.dim_1 // 2
        else:
            raise ValueError(f"axis {axis} is not handled")
    else:
        return int(slice_index)


def get_nabu_multicor_file_prefix(scan):
    if isinstance(scan, EDFTomoScan):
        dataset_path = scan.path
    elif isinstance(scan, NXtomoScan):
        dataset_path = scan.master_file
    else:
        raise TypeError(f"{type(scan)} is not handled")

    if os.path.isfile(dataset_path):  # hdf5
        file_prefix = os.path.basename(dataset_path).split(".")[0]
    elif os.path.isdir(dataset_path):
        file_prefix = os.path.basename(dataset_path)
    else:
        raise ValueError(f"dataset location {scan.path} is neither a file or directory")
    file_prefix += "_rec"  # avoid overwriting dataset
    return file_prefix
