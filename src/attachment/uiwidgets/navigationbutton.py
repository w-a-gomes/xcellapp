#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui


class NavigationButton(QtWidgets.QPushButton):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)

        self.leave_state = False

    def enterEvent(self, event) -> None:
        """..."""
        palette = self.palette()
        palette_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Highlight))
        
        palette.setColor(
            QtGui.QPalette.Button, palette_color)
        
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def leaveEvent(self, event) -> None:
        """..."""
        self.setAutoFillBackground(self.leave_state)
    
    def setKeepEnterEvent(self, state: bool) -> None:
        self.leave_state = state
        self.setAutoFillBackground(self.leave_state)


if __name__ == '__main__':
    pass
