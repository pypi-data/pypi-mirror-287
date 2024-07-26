# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
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
"""
material for radio and sinogram normalization
"""


__authors__ = [
    "H. Payno",
]
__license__ = "MIT"
__date__ = "25/06/2021"


import typing

from silx.utils.enum import Enum as _Enum
from tomoscan.normalization import Method


class _ValueSource(_Enum):
    MONITOR = "intensity monitor"
    MANUAL_ROI = "manual ROI"
    AUTO_ROI = "automatic ROI"
    DATASET = "from dataset"
    MANUAL_SCALAR = "scalar"
    NONE = "none"


class _ValueCalculationFct(_Enum):
    MEAN = "mean"
    MEDIAN = "median"


class _DatasetScope(_Enum):
    LOCAL = "local"
    GLOBAL = "global"


class _DatasetInfos:
    def __init__(self):
        self._scope = _DatasetScope.GLOBAL
        self._file_path = None
        self._data_path = None

    @property
    def scope(self) -> _DatasetScope:
        return self._scope

    @scope.setter
    def scope(self, scope: typing.Union[str, _DatasetScope]):
        self._scope = _DatasetScope.from_value(scope)

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        self._file_path = file_path

    @property
    def data_path(self):
        return self._data_path

    @data_path.setter
    def data_path(self, data_path: str):
        self._data_path = data_path


class _ROIInfo:
    def __init__(self, x_min=None, x_max=None, y_min=None, y_max=None):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max


class SinoNormalizationParams:
    """Information regarding the intensity normalization to be done"""

    def __init__(self, method=Method.NONE, source=_ValueSource.NONE, extra_infos=None):
        self._method = Method.NONE
        self._source = _ValueSource.NONE
        self._extra_infos = {}

        self.method = method
        self.extra_infos = extra_infos if extra_infos is not None else {}
        self.source = source

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method: typing.Union[str, Method, None]):
        if method is None:
            method = Method.NONE
        self._method = Method.from_value(method)

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        if source is None:
            source = _ValueSource.NONE
        self._source = _ValueSource.from_value(source)

    @property
    def extra_infos(self):
        return self._extra_infos

    @extra_infos.setter
    def extra_infos(self, extra_infos: dict):
        if not isinstance(extra_infos, dict):
            raise TypeError("extra infos is expected to be a dictionary")
        elif "method" in extra_infos:
            raise KeyError("'method' is a reserved key name")
        else:
            self._extra_infos = extra_infos

    def to_dict(self):
        _dict = self._extra_infos
        _dict["method"] = self.method.value
        _dict["source"] = self.source.value
        return _dict

    @staticmethod
    def from_dict(dict_):
        params = SinoNormalizationParams()
        params.load_from_dict(dict_=dict_)
        return params

    def load_from_dict(self, dict_):
        tmp_dict = dict_.copy()
        if "method" in tmp_dict:
            self.method = tmp_dict["method"]
            del tmp_dict["method"]
        if "source" in tmp_dict:
            self.source = tmp_dict["source"]
            del tmp_dict["source"]
        self.extra_infos = tmp_dict
