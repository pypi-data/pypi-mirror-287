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

__authors__ = ["C. Nemoz", "H. Payno"]
__license__ = "MIT"
__date__ = "18/02/2018"


import functools

from silx.gui import qt

from tomwer.core.process.control.datawatcher import status
from tomwer.core.process.control.datawatcher.datawatcher import _DataWatcher


class _DWConfigurationWidget(qt.QWidget):
    startByOldestStateChanged = qt.Signal(bool)

    def __init__(self, parent):
        qt.QWidget.__init__(self, parent)
        self.setLayout(qt.QVBoxLayout())
        self._observationMethod = _ObservationMethodSelector(parent=self)
        self.layout().addWidget(self._observationMethod)

        # checkbox start scan from oldest
        self._qcboldest = qt.QCheckBox("Start scan by the oldest", parent=self)
        tooltip = (
            "If NOT activated will explore folders from the latest to "
            "the newest. Otherwise will explore the folders from the "
            "newest to the oldest."
        )
        self._qcboldest.setToolTip(tooltip)
        self.startByOldestStateChanged = self._qcboldest.toggled
        self.layout().addWidget(self._qcboldest)

    def getMode(self) -> tuple:
        return self._observationMethod.getMode()

    def setMode(self, mode: tuple):
        self._observationMethod.setMode(mode)


class _ObservationMethodSelector(qt.QWidget):
    sigSelectionChanged = qt.Signal(tuple)
    """Return the selection made as a string and some information if needed in
    a dictionary"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.__button_group = qt.QButtonGroup(self)

        self.setLayout(qt.QVBoxLayout())
        self._edfObservations = _SpecEDFObservationMethodSelector(self)
        self.layout().addWidget(self._edfObservations)
        self._blissScanObservations = _BlissHDF5ObservationMethodSelector(self)
        self.layout().addWidget(self._blissScanObservations)
        self._nxtomoObservations = _NXtomoObservationMethodSelector(self)
        self.layout().addWidget(self._nxtomoObservations)

        self._edfObservations.sigSelectionChanged.connect(
            self._propagateSigSelectionChanged
        )

        self.__button_group.addButton(self._edfObservations._qrbInfo)
        self.__button_group.addButton(self._edfObservations._qrbUserEntry)
        self.__button_group.addButton(self._edfObservations._qrbXml)
        self.__button_group.addButton(self._blissScanObservations._qrbBlissHDF5)
        self.__button_group.addButton(self._nxtomoObservations._qrbNXtomo)

        # connect signal / slot
        self._edfObservations.sigSelectionChanged.connect(
            self._propagateSigSelectionChanged
        )
        self._blissScanObservations._qrbBlissHDF5.toggled.connect(
            functools.partial(
                self._propagateSigSelectionChanged, (status.BLISS_SCAN_END,)
            )
        )
        self._nxtomoObservations._qrbNXtomo.toggled.connect(
            functools.partial(self._propagateSigSelectionChanged, (status.NXtomo_END,))
        )

    def _propagateSigSelectionChanged(self, infos: tuple):
        self.sigSelectionChanged.emit(infos)

    def getMode(self):
        if self._blissScanObservations._qrbBlissHDF5.isChecked():
            return (status.BLISS_SCAN_END,)
        elif self._nxtomoObservations._qrbNXtomo.isChecked():
            return (status.NXtomo_END,)
        else:
            return self._edfObservations.getMode()

    def setMode(self, mode: tuple):
        if mode[0] == status.BLISS_SCAN_END:
            self._blissScanObservations._qrbBlissHDF5.setChecked(True)
        elif mode[0] == status.NXtomo_END:
            self._nxtomoObservations._qrbNXtomo.setChecked(True)
        else:
            self._edfObservations.setMode(mode)


class _NXtomoObservationMethodSelector(qt.QGroupBox):
    def __init__(self, parent):
        super().__init__(parent, title="End acquisition observation method for NXtomo")
        self.setLayout(qt.QVBoxLayout())

        self._qrbNXtomo = qt.QRadioButton(status.NXtomo_END, parent=self)
        self.layout().addWidget(self._qrbNXtomo)


class _BlissHDF5ObservationMethodSelector(qt.QGroupBox):
    def __init__(self, parent):
        super().__init__(
            parent, title="End acquisition observation method for bliss-hdf5"
        )
        self.setLayout(qt.QVBoxLayout())

        self._qrbBlissHDF5 = qt.QRadioButton(status.BLISS_SCAN_END, parent=self)
        self.layout().addWidget(self._qrbBlissHDF5)


class _SpecEDFObservationMethodSelector(qt.QGroupBox):
    """Group box allowing selection of an observation method"""

    sigSelectionChanged = qt.Signal(tuple)
    """Return the selection made as a string and some information if needed in
    a dictionary"""

    def __init__(self, parent):
        super().__init__(parent, title="End acquisition observation method for edf")
        self.setLayout(qt.QVBoxLayout())

        self._qrbXml = qt.QRadioButton(status.DET_END_XML, parent=self)
        self.layout().addWidget(self._qrbXml)
        self._qrbInfo = qt.QRadioButton(status.PARSE_INFO_FILE, parent=self)
        self.layout().addWidget(self._qrbInfo)
        self._qrbAnyEDF = qt.QRadioButton(status.EDF_SCAN_END, parent=self)
        self.layout().addWidget(self._qrbAnyEDF)

        self._qwUserEntry = qt.QWidget(parent=self)
        self.layout().addWidget(self._qwUserEntry)
        self._qrbUserEntry = qt.QRadioButton(status.DET_END_USER_ENTRY, parent=self)
        self.layout().addWidget(self._qrbUserEntry)

        widgetFilePtrn = qt.QWidget(parent=self)
        widgetFilePtrn.setLayout(qt.QHBoxLayout())

        widgetFilePtrn.layout().addWidget(
            qt.QLabel(text="pattern: ", parent=widgetFilePtrn)
        )
        self._qleFilePattern = qt.QLineEdit(text="", parent=self._qwUserEntry)
        widgetFilePtrn.layout().addWidget(self._qleFilePattern)
        self.widgetFilePtrn = widgetFilePtrn
        self.layout().addWidget(self.widgetFilePtrn)

        self._qrbXml.setChecked(_DataWatcher.DEFAULT_OBS_METH == status.DET_END_XML)
        self._qrbInfo.setChecked(
            _DataWatcher.DEFAULT_OBS_METH == status.PARSE_INFO_FILE
        )
        self._qrbUserEntry.setChecked(
            _DataWatcher.DEFAULT_OBS_METH == status.DET_END_USER_ENTRY
        )

        self.widgetFilePtrn.setVisible(self._qrbUserEntry.isVisible())

        spacer = qt.QWidget(self)
        spacer.setSizePolicy(qt.QSizePolicy.Minimum, qt.QSizePolicy.Expanding)
        self.layout().addWidget(spacer)

        # set up
        self._qrbAnyEDF.hide()  # by default for the DataWatcher compatibility this one is hidded

        # deal with connections
        self._qrbUserEntry.toggled.connect(self.widgetFilePtrn.setVisible)
        self._qrbXml.toggled.connect(self._selectionChanged)
        self._qrbInfo.toggled.connect(self._selectionChanged)
        self._qrbAnyEDF.toggled.connect(self._selectionChanged)
        self._qrbUserEntry.toggled.connect(self._selectionChanged)
        self._qleFilePattern.editingFinished.connect(self._selectionChanged)

        # add some tooltips
        t = """If a file with this pattern is found in the [scan] folder then
            we will consider the acquisition as ended"""
        self._qrbUserEntry.setToolTip(t)

        t = """Wild charracter allowed"""
        self._qleFilePattern.setToolTip(t)

        t = """If we founf the [scan].xml in the [scan] folder then
            we will consider the acquisition ended"""
        self._qrbXml.setToolTip(t)

        t = """We will look for the [scan].info file in the [scan]
            directory. If it exists then we will parse it to get the number of
            .edf file we should have and wait for all of them to be acquired
            (also checking file size)"""
        self._qrbInfo.setToolTip(t)

    def _selectionChanged(self):
        mode = self.getMode()
        if mode is not None:
            self.sigSelectionChanged.emit((mode,))

    def getMode(self):
        if self._qrbXml.isChecked():
            return (status.DET_END_XML,)
        elif self._qrbInfo.isChecked():
            return (status.PARSE_INFO_FILE,)
        elif self._qrbAnyEDF.isChecked():
            return (status.EDF_SCAN_END,)
        elif self._qrbUserEntry.isChecked():
            return (status.DET_END_USER_ENTRY, {"pattern": self._qleFilePattern.text()})
        else:
            return None

    def setMode(self, mode: tuple):
        if mode[0] == status.DET_END_XML:
            self._qrbXml.setChecked(True)
        elif mode[0] == status.PARSE_INFO_FILE:
            self._qrbInfo.setChecked(True)
        elif mode[0] == status.EDF_SCAN_END:
            self._qrbAnyEDF.setChecked(True)
        elif mode[0] == status.DET_END_USER_ENTRY:
            self._qrbUserEntry.setChecked(True)
            if mode[1] not in (None, ""):
                self._qleFilePattern.setText(mode[1])
