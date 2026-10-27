# SPDX-License-Identifier: GPL-2.0-or-later
import sys
import os

from PyQt6.QtCore import pyqtSignal, QProcess, Qt, QIODeviceBase
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication

from keycodes.keycodes import Keycode
from macro.macro_key import KeyUp, KeyDown
from util import tr


class LinuxRecorder(QWidget):

    keystroke = pyqtSignal(object)
    stopped = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.on_output)

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.X11BypassWindowManagerHint)

        layout = QVBoxLayout()
        btn = QPushButton(tr("MacroRecorder", "Stop recording"))
        btn.clicked.connect(self.on_stop)
        layout.addWidget(btn)

        self.setLayout(layout)

    def start(self):
        self.show()

        center = QApplication.primaryScreen().availableGeometry().center()
        self.move(round(center.x() - self.width() * 0.5), 0)

        args = [sys.executable]
        args += sys.argv
        args += ["--linux-recorder"]

        self.process.start("pkexec", args, QIODeviceBase.OpenModeFlag.Unbuffered | QIODeviceBase.OpenModeFlag.ReadWrite)

    def on_stop(self):
        self.stop()

    def stop(self):
        self.process.write(b"q")
        self.process.waitForFinished()
        self.process.close()
        self.hide()
        self.stopped.emit()

    def on_output(self):
        if self.process.canReadLine():
            line = bytes(self.process.readLine()).decode("utf-8")
            action, key = line.strip().split(":")
            code = Keycode.find_by_recorder_alias(key)
            if code is not None:
                action2cls = {"down": KeyDown, "up": KeyUp}
                self.keystroke.emit(action2cls[action](code))
