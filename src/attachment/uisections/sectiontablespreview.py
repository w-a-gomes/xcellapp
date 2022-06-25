#!/usr/bin env python3
import os
import json

from PySide6 import QtWidgets, QtGui, QtCore

# import attachment.uitools.qtcolor as qtcolor
import attachment.uitools.qticons as qticons


# noinspection PyPep8Naming
class SectionTablesPreview(QtWidgets.QWidget):
    """..."""
    edit_table_button_clicked = QtCore.Signal(QtGui.QMouseEvent)

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
        self.__anim_group = None
        # Background color
        self.background_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Midlight))

        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Window, self.background_color)

        # self.setAutoFillBackground(True)
        # self.setPalette(self.color_palette)

        # Property
        self.__sender = None

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
        self.scroll_widget_layout.setSpacing(6)
        self.scroll_widget_layout.setAlignment(
            QtCore.Qt.AlignTop)  # type: ignore
        self.scroll_widget.setLayout(self.scroll_widget_layout)

        # Tables Widget
        self.tables_widgets_list = []
        self.tables_layout_list = []

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

            for w in self.tables_layout_list:
                w.deleteLater()
            self.tables_layout_list = []

        # Add new widgets
        if ls_command and tables_schema_filenames:
            hbox = QtWidgets.QHBoxLayout()
            self.scroll_widget_layout.addLayout(hbox)
            self.tables_layout_list.append(hbox)

            hbox_widgets_num = 0
            for filename in tables_schema_filenames:
                with open(os.path.join(table_schema_path, filename), 'r') as f:
                    file_schema = json.load(f)

                # Grade
                if hbox_widgets_num == 3:
                    hbox_widgets_num = 0
                    hbox = QtWidgets.QHBoxLayout()
                    self.scroll_widget_layout.addLayout(hbox)
                    self.tables_layout_list.append(hbox)

                table_preview = WidgetTablePreview(filename, file_schema)
                table_preview.edit_table_button_clicked.connect(
                    self.__on_table_preview)
                hbox.addWidget(table_preview)
                hbox_widgets_num += 1
                self.tables_widgets_list.append(table_preview)

    @QtCore.Slot()
    def __on_table_preview(self):
        self.__sender = self.sender().getEditTableButtonClicked()
        self.edit_table_button_clicked.emit(self)

    @QtCore.Slot()
    def getEditTableButtonClicked(self):
        return self.__sender


# noinspection PyPep8Naming
class WidgetTablePreview(QtWidgets.QFrame):
    """..."""
    edit_table_button_clicked = QtCore.Signal(QtGui.QMouseEvent)

    def __init__(
            self,
            filename: str,
            table_schema: dict,
            *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Frame border
        self.setFrameStyle(
            QtWidgets.QFrame.StyledPanel |  # type: ignore
            QtWidgets.QFrame.Plain)

        # Style
        # self.setObjectName('TablePreview')
        # color = qtcolor.QtGuiColor()
        # if color.widget_is_dark():
        #     #
        #     self.setStyleSheet("""
        #         #TablePreview {
        #             border: 1px solid rgba(58, 127, 74, 0.2);
        #             border-radius: 3px;
        #             background: rgba(58, 127, 74, 0.1);
        #         }""")
        # else:
        #     self.setStyleSheet("""
        #         #TablePreview {
        #             border: 1px solid rgba(81, 243, 72, 0.3);
        #             border-radius: 3px;
        #             background: rgba(81, 243, 72, 0.2);
        #         }""")

        # Background color
        self.palette_color = QtGui.QColor(
            QtGui.QPalette().color(  # ToolTipBase Button Window AlternateBase
                QtGui.QPalette.Active, QtGui.QPalette.Window))

        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Window, self.palette_color)

        self.setAutoFillBackground(True)
        self.setPalette(self.color_palette)

        # Args
        self.table_schema = table_schema
        self.filename = filename

        # Property
        self.__sender = None

        # ___ Container ___
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)  # type: ignore
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

        # ___ Tables ___
        # Icon
        self.icons = qticons.QtGuiIcon()
        self.icon_document_edit = self.icons.fromSystem('document-edit')

        # Tables
        for schema_item in self.table_schema['datas']:
            layout = QtWidgets.QHBoxLayout()
            self.layout.addLayout(layout)

            # Edit
            edit_button = EditButton(
                schema=schema_item, icon=self.icon_document_edit)
            edit_button.setFlat(True)
            edit_button.clicked.connect(self.__on_edit_button)  # type: ignore
            layout.addWidget(edit_button)

            # Name
            name = schema_item['table-name'].rstrip('.scv')
            # data = schema_item['table-data']
            layout.addWidget(QtWidgets.QLabel(name), 1)

    @QtCore.Slot()
    def __on_edit_button(self):
        self.__sender = self.sender()
        self.edit_table_button_clicked.emit(self)

    @QtCore.Slot()
    def getEditTableButtonClicked(self):
        return self.__sender


# noinspection PyPep8Naming
class EditButton(QtWidgets.QPushButton):
    def __init__(self, schema, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__schema = schema

    def getSchema(self):
        return self.__schema
