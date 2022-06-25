#!/usr/bin env python3
# import os
# import json

from PySide6 import QtWidgets, QtGui, QtCore

# import attachment.uitools.qtcolor as qtcolor
# import attachment.uitools.qticons as qticons


# noinspection PyPep8Naming
class SectionTablesEditor(QtWidgets.QFrame):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # Args
        self.__table_schema = None

        # Frame border
        self.setFrameStyle(
            QtWidgets.QFrame.StyledPanel |  # type: ignore
            QtWidgets.QFrame.Plain)

        # Background color
        self.background_color = QtGui.QColor(
            QtGui.QPalette().color(
                # ToolTipBase: Light
                # Button: Light
                # Window: Normal
                # AlternateBase: Dark
                QtGui.QPalette.Active, QtGui.QPalette.AlternateBase))

        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Window, self.background_color)

        self.setAutoFillBackground(True)
        self.setPalette(self.color_palette)

        # Property
        self.__sender = None

        # ___ Container ___
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Scroll Area
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
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

        # self.scroll_widget_layout.addWidget(table_preview)

    def setSchema(self, schema):
        self.__table_schema = schema

    def updateEditor(self):
        """
        {
            'table-name': 'cadastro.csv',
            'edited': False,
            'edited-date': None,
            'table-data': [
                [
                    {'field': '', 'value': {'': ''}},
                    {'field': '', 'value': {'': ''}},
                ],
                [
                    {'field': '', 'value': {'Funcionário': 'Funcionário'}},
                    {'field': '', 'value': {'Cargo': 'Cargo'}},
                ]
            ]
        }
        """
        print(self.__table_schema)
        print('Update Editor...')
