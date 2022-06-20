#!/usr/bin env python3
import os

from PySide6 import QtWidgets, QtGui, QtCore


class SectionTablesScheme(QtWidgets.QWidget):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # Frame border
        # self.setFrameStyle(
        #     QtWidgets.QFrame.StyledPanel |  # type: ignore
        #     QtWidgets.QFrame.Plain)

        # Border
        # self.setObjectName('Lol')
        # self.setStyleSheet(
        # Border
        #    '#Lol {border: 2px solid #2c633a; border-radius: 10px;}')
        # Background
        #    '#Lol {border-radius: 10px; background: rgba(0, 255, 50, 20);}')

        # Background color
        self.background_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Midlight))

        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Window, self.background_color)

        # self.setAutoFillBackground(True)
        # self.setPalette(self.color_palette)

        # ___ Container ___
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Scroll Area
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
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

        # Scroll Widget
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_widget.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setWidget(self.scroll_widget)

        # Scroll Widget BG color
        self.scroll_widget.setAutoFillBackground(True)
        self.scroll_widget.setPalette(self.color_palette)

        # Scroll Widget Layout
        self.scroll_widget_layout = QtWidgets.QVBoxLayout()
        self.scroll_widget.setLayout(self.scroll_widget_layout)

        # Tables Widget
        self.tables_widgets_list = []

    def update_tables(self, tables_schema_path: str) -> None:
        # Remove old widgets
        if self.tables_widgets_list:
            for w in self.tables_widgets_list:
                w.deleteLater()
            self.tables_widgets_list = []

        # Add new widgets
        config_files_list = os.listdir(tables_schema_path)
        if config_files_list:
            for n, w in enumerate(config_files_list):
                lbl = QtWidgets.QLabel(f'{n + 1} {w}')
                self.tables_widgets_list.append(lbl)
                self.scroll_widget_layout.addWidget(lbl)

