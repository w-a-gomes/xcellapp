#!/usr/bin env python3
from PySide6 import QtWidgets, QtGui, QtCore


class SectionTablesScheme(QtWidgets.QWidget):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)

        # Background color
        self.background_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Midlight))

        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Window, self.background_color)

        self.setAutoFillBackground(True)
        self.setPalette(self.color_palette)

        # ___ Container ___
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)  # type: ignore
        self.setLayout(self.layout)

        self.layout.setAlignment(QtCore.Qt.AlignLeft)  # type: ignore

        for i in range(10):
            lbl = QtWidgets.QLabel(f'{i}')
            self.layout.addWidget(lbl)
