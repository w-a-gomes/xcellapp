#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui


class NavigationButton(QtWidgets.QPushButton):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)

        self.leave_state = False

    def enterEvent(self, event):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Button, '#264f9d')
        self.setPalette(palette)

    def leaveEvent(self, event):
        self.setAutoFillBackground(self.leave_state)
    
    def setKeepEnterEvent(self, state: bool) -> None:
        self.leave_state = state
        self.setAutoFillBackground(self.leave_state)


if __name__ == '__main__':
    pass
