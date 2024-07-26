# coding: utf-8
# /*##########################################################################
# Copyright (C) 2016 European Synchrotron Radiation Facility
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
#############################################################################*/

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "22/01/2017"


import shutil
import tempfile

import pytest
from silx.gui.utils.testutils import TestCaseQt

from tomwer.core.utils.scanutils import MockEDF
from tomwer.gui.control.scanselectorwidget import ScanSelectorWidget
from tomwer.tests.utils import skip_gui_test


@pytest.mark.skipif(skip_gui_test(), reason="skip gui test")
class TestScanSelector(TestCaseQt):
    """
    Simple test for the ScanSelectorWidget
    """

    def setUp(self):
        self._folder1 = tempfile.mkdtemp()
        self._folder2 = tempfile.mkdtemp()
        self._folder3 = tempfile.mkdtemp()
        for _folder in (self._folder1, self._folder2, self._folder3):
            MockEDF.mockScan(scanID=_folder, nRadio=5, nRecons=5, nPagRecons=0, dim=10)

        self.widget = ScanSelectorWidget(parent=None)

    def tearDown(self):
        shutil.rmtree(self._folder1)
        shutil.rmtree(self._folder2)
        shutil.rmtree(self._folder3)

    def test(self):
        self.widget.add(self._folder1)
        self.widget.add(self._folder2)
        self.widget.add(self._folder3)
        self.assertEqual(self.widget.dataList.n_data(), 3)
        self.widget.remove(self._folder3)
        self.assertEqual(self.widget.dataList.n_data(), 2)
