#!/usr/bin env python3
import os
import json

from PySide6 import QtWidgets, QtGui, QtCore

# import attachment.uitools.qtcolor as qtcolor


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
        self.scroll_widget_layout.setContentsMargins(12, 12, 12, 12)
        self.scroll_widget_layout.setSpacing(12)
        self.scroll_widget_layout.setAlignment(
            QtCore.Qt.AlignTop)  # type: ignore
        self.scroll_widget.setLayout(self.scroll_widget_layout)

        # Tables Widget
        self.tables_widgets_list = []

    def update_tables(
            self,
            table_schema_path: str,
            tables_schema_filenames: list) -> None:

        ls_command = os.listdir(table_schema_path)

        # Remove old widgets
        if self.tables_widgets_list:
            for w in self.tables_widgets_list:
                w.deleteLater()
            self.tables_widgets_list = []

        # Add new widgets
        if ls_command and tables_schema_filenames:
            for filename in tables_schema_filenames:
                with open(os.path.join(table_schema_path, filename), 'r') as f:
                    file_schema = json.load(f)

                table_preview = WidgetTablePreview(filename, file_schema)
                self.tables_widgets_list.append(table_preview)
                self.scroll_widget_layout.addWidget(table_preview)


class WidgetTablePreview(QtWidgets.QFrame):
    """..."""
    def __init__(
            self,
            filename: str,
            table_schema: dict,
            *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Frame border
        # self.setFrameStyle(
        #     QtWidgets.QFrame.StyledPanel |  # type: ignore
        #     QtWidgets.QFrame.Plain)

        # Border
        # self.setObjectName('TablePreview')
        # self.setStyleSheet('#TablePreview {border-radius: 10px;}')

        # Style
        # color = qtcolor.QtGuiColor()
        # if color.widget_is_dark():
        #     self.setStyleSheet("""
        #         #TablePreview {
        #             border: 1px solid rgba(58, 127, 74, 0.2);
        #             border-radius: 10px;
        #             background: rgba(58, 127, 74, 0.1);
        #         }""")
        # else:
        #     self.setStyleSheet("""
        #         #TablePreview {
        #             border: 1px solid rgba(0, 255, 50, 0.2);
        #             border-radius: 10px;
        #             background: rgba(0, 255, 50, 0.1);
        #         }""")

        # Background color
        self.palette_color = QtGui.QColor(
            QtGui.QPalette().color(  # Active, AlternateBase
                QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase))

        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Window, self.palette_color)

        self.setAutoFillBackground(True)
        self.setPalette(self.color_palette)

        # Args
        self.table_schema = table_schema
        self.filename = filename

        # ___ Container ___
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # __ info __
        self.info_layout = QtWidgets.QHBoxLayout()
        # self.info_layout.setAlignment(QtCore.Qt.AlignLeft)  # type: ignore
        self.layout.addLayout(self.info_layout)

        # ID
        self.id_label = QtWidgets.QLabel(self.table_schema['id'])
        self.info_layout.addWidget(self.id_label)

        # Filename
        self.filename_label = QtWidgets.QLabel(self.table_schema['filename'])
        self.filename_label.setEnabled(False)
        self.filename_label.setAlignment(QtCore.Qt.AlignLeft)  # type: ignore
        self.info_layout.addWidget(self.filename_label, 1)

        # Date
        self.date_label = QtWidgets.QLabel(self.table_schema['date'])
        self.date_label.setEnabled(False)
        self.date_label.setAlignment(QtCore.Qt.AlignRight)  # type: ignore
        self.info_layout.addWidget(self.date_label)

        for schema_item in self.table_schema['datas']:
            name = (' ' * 5) + schema_item['table-name'].rstrip('.scv')
            data = schema_item['table-data']
            self.layout.addWidget(QtWidgets.QLabel(name))
