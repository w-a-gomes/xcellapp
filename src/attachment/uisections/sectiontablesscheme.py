#!/usr/bin env python3
from PySide6 import QtWidgets, QtGui, QtCore


class WidgetTablesScheme(QtWidgets.QWidget):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # Border
        # self.setFrameStyle(
        #     QtWidgets.QFrame.StyledPanel |  # type: ignore
        #     QtWidgets.QFrame.Plain)

        # Background color
        self.background_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Midlight))

        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Window, self.background_color)

        self.setAutoFillBackground(True)
        self.setPalette(self.color_palette)

        # self.setObjectName('Lol')
        # self.setStyleSheet(
        # Border
        #    '#Lol {border: 2px solid #2c633a; border-radius: 10px;}')
        # Background
        #    '#Lol {border-radius: 10px; background: rgba(0, 255, 50, 20);}')

        # Layout
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        for i in range(200):
            lbl = QtWidgets.QLabel(f'{i}')
            self.layout.addWidget(lbl)


class SectionTablesScheme(QtWidgets.QWidget):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # ___ Container ___
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Scroll Area
        self.scroll_area = QtWidgets.QScrollArea()
        # self.scroll_area.setMinimumHeight(400)
        # self.scroll_area.setMaximumHeight(500)
        # self.scroll_area.setFixedHeight(self.parent().height())
        # self.scroll_area.setFixedWidth(500)
        self.scroll_area.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)

        self.layout.addWidget(self.scroll_area)

        self.scroll_widget = WidgetTablesScheme()
        self.scroll_area.setWidget(self.scroll_widget)
