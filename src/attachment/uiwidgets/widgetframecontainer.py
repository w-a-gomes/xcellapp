#!/usr/bin env python3
from PySide6 import QtWidgets, QtGui


class WidgetFrameContainer(QtWidgets.QWidget):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)

        self.active_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Highlight))

        self.active_color_unfocused = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Midlight))

        self.hover_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Button))

        # Settings
        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Window, self.active_color_unfocused)

        self.setAutoFillBackground(True)
        self.setPalette(self.color_palette)
