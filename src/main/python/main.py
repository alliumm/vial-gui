# SPDX-License-Identifier: GPL-2.0-or-later
import traceback
from functools import cached_property
from importlib import metadata, resources

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon

import sys

from vial.main_window import MainWindow


from vial.fbs_signal_handler import SignalWakeupHandler
# http://timlehr.com/python-exception-hooks-with-qt-message-box/
from vial.util import init_logger


def show_exception_box(log_msg):
    if QtWidgets.QApplication.instance() is not None:
        errorbox = QtWidgets.QMessageBox()
        errorbox.setText(log_msg)
        errorbox.exec()


class UncaughtHook(QtCore.QObject):
    _exception_caught = pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super(UncaughtHook, self).__init__(*args, **kwargs)

        # this registers the exception_hook() function as hook with the Python interpreter
        sys._excepthook = sys.excepthook
        sys.excepthook = self.exception_hook

        # connect signal to execute the message box function always on main thread
        self._exception_caught.connect(show_exception_box)

    def exception_hook(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            # ignore keyboard interrupt to support console applications
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
        else:
            log_msg = '\n'.join([''.join(traceback.format_tb(exc_traceback)),
                                 '{0}: {1}'.format(exc_type.__name__, exc_value)])

            # trigger message box show
            self._exception_caught.emit(log_msg)
        sys._excepthook(exc_type, exc_value, exc_traceback)

class VialApplicationContext:
    def __init__(self):
        # Many Qt classes require a QApplication to have been instantiated.
        # Do this here, before everything else, to achieve this:
        app = self.app
        SignalWakeupHandler(app).install()
        icon_path = resources.path("vial", "resources/Icon.ico")
        app.setWindowIcon(QIcon(str(icon_path)))

    @cached_property
    def app(self):
        # Override the app definition in order to set WM_CLASS.
        result = QtWidgets.QApplication(sys.argv)
        result.setApplicationName("Vial")
        result.setOrganizationDomain("vial.today")

        #TODO: Qt sets applicationVersion on non-Linux platforms if the exe/pkg metadata is correctly configured.
        # https://doc.qt.io/qt-5/qcoreapplication.html#applicationVersion-prop
        # Verify it is, and only set manually on Linux.
        #if sys.platform.startswith("linux"):
        result.setApplicationVersion(metadata.version("vial-gui"))
        return result

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--linux-recorder":
        from vial.linux_keystroke_recorder import linux_keystroke_recorder

        linux_keystroke_recorder()
    else:
        appctxt = VialApplicationContext()       # 1. Instantiate ApplicationContext
        init_logger()
        qt_exception_hook = UncaughtHook()
        window = MainWindow(appctxt)
        window.show()
        return appctxt.app.exec()
