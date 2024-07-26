#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import functools
import logging
import signal
import sys
import silx
from silx.gui import qt

from tomwer.core.process.reconstruction.axis.axis import (
    AxisMode,
    AxisTask,
    NoAxisUrl,
)
from tomwer.core.process.reconstruction.darkref.darkrefs import (
    requires_reduced_dark_and_flat,
)
from tomwer.core.scan.scanfactory import ScanFactory
from tomwer.core.utils.resource import increase_max_number_file
from tomwer.gui import icons
from tomwer.gui.reconstruction.axis import AxisWindow
from tomwer.gui.utils.splashscreen import getMainSplashScreen
from tomwer.synctools.axis import QAxisRP

logging.basicConfig(level=logging.WARNING)
_logger = logging.getLogger(__name__)


class _AxisProcessGUI(AxisWindow):
    def __init__(self, scan, axis_params, backend=None):
        axis_params.frame_width = scan.dim_1
        super().__init__(axis_params=axis_params, backend=backend)
        self.hideLockButton()
        self.hideApplyButton()
        self.setScan(scan=scan)

        # connect Signal / Slot
        callback = functools.partial(self.compute, scan)
        self.sigComputationRequested.connect(callback)
        self.setWindowIcon(icons.getQIcon("tomwer"))

    def compute(self, scan, wait=True):
        mess = " ".join(
            ("start axis calculation with", scan.axis_params.axis_url_1.url.path())
        )
        _logger.info(mess)
        process = AxisTask(
            inputs={
                "data": scan,
                "axis_params": self._axis_params,
                "wait": wait,
                "serialize_output_data": False,
            }
        )
        try:
            process.run()
        except NoAxisUrl:
            msg = qt.QMessageBox(self)
            msg.setIcon(qt.QMessageBox.Warning)
            text = (
                "Unable to find url to compute the axis, please select them "
                "from the `axis input` tab"
            )
            msg.setText(text)
            msg.exec_()
            return None
        else:
            position = scan.axis_params.relative_cor_value
            assert isinstance(position, (float, type(None)))
            frm = "sinogram" if scan.axis_params.use_sinogram else "radio"
            AxisWindow.setPosition(self, frm=frm, value=position)
            return position

    def _updatePosition(self, scan):
        self._widget.setPosition(frm=None, value=scan.axis_params.relative_cor_value)


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "scan_path",
        help="For EDF acquisition: provide folder path, for HDF5 / nexus "
        "provide the master file",
    )
    parser.add_argument(
        "--entry", help="For Nexus files: entry in the master file", default=None
    )
    parser.add_argument(
        "--use-sinogram",
        help="use the signoram from radio for computing COR. This only work"
        "with the =scan-path option",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="Set logging system in debug mode",
    )
    parser.add_argument(
        "--mode",
        default=None,
        help=f"Use a specific mode. Available modes are {AxisMode.values()}",
    )
    parser.add_argument(
        "--full-image",
        action="store_true",
        default=False,
        help="Define the mode 'full' when display shifted images from manual" " mode",
    )
    parser.add_argument(
        "--use-opengl-plot",
        help="Use OpenGL for plots (instead of matplotlib)",
        action="store_true",
        default=False,
    )
    options = parser.parse_args(argv[1:])

    if options.debug:
        logging.root.setLevel(logging.DEBUG)

    if options.use_opengl_plot:
        silx.config.DEFAULT_PLOT_BACKEND = "gl"
    else:
        silx.config.DEFAULT_PLOT_BACKEND = "matplotlib"

    increase_max_number_file()

    global app  # QApplication must be global to avoid seg fault on quit
    app = qt.QApplication.instance() or qt.QApplication(["tomwer"])
    splash = getMainSplashScreen()
    qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)
    qt.QApplication.processEvents()

    qt.QLocale.setDefault(qt.QLocale(qt.QLocale.English))
    qt.QLocale.setDefault(qt.QLocale.c())
    signal.signal(signal.SIGINT, sigintHandler)
    sys.excepthook = qt.exceptionHandler

    timer = qt.QTimer()
    timer.start(500)
    # Application have to wake up Python interpreter, else SIGINT is not
    # catch
    timer.timeout.connect(lambda: None)

    mode = options.mode
    if mode is not None:
        mode = AxisMode.from_value(mode)

    try:
        scan = ScanFactory.create_scan_object(
            scan_path=options.scan_path, entry=options.entry
        )
    except ValueError:
        scan = ScanFactory.mock_scan()

    requires_reduced_dark_and_flat(scan=scan, logger_=_logger)
    # define the process_index is any tomwer_processes_existing
    scan.set_process_index_frm_tomwer_process_file()
    if scan.axis_params is None:
        scan.axis_params = QAxisRP()

    if options.debug:
        _logger.setLevel(logging.DEBUG)

    axis_params = QAxisRP()
    axis_params.use_sinogram = options.use_sinogram
    if scan.dim_2 is not None:
        axis_params.sinogram_line = scan.dim_2 // 2

    window = _AxisProcessGUI(scan=scan, axis_params=axis_params)
    window.setWindowTitle("axis")
    window.setWindowIcon(icons.getQIcon("tomwer"))
    if mode is not None:
        window.setMode(mode)
    if options.full_image:
        window.manual_uses_full_image(True)

    splash.finish(window)
    window.show()
    qt.QApplication.restoreOverrideCursor()
    app.exec_()


def getinputinfo():
    return "tomwer axis [scanDir]"


def sigintHandler(*args):
    """Handler for the SIGINT signal."""
    qt.QApplication.quit()


if __name__ == "__main__":
    main(sys.argv)
