#!/usr/bin env python3
import json
import os
import pathlib
import sys

from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uiwidgets.widgetelidedlabel import WidgetElidedLabel

class SectionImpTables(QtWidgets.QWidget):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # ___ Properties ___
        self.filename = None
        self.header = None
        self.label_size = 75
        self.desktop_margin = (100, 150)

        # ___ Icons ___
        if sys.platform != 'linux':
            self.icon_folder_open = QtGui.QIcon(
                QtGui.QPixmap(
                    os.path.join(pathlib.Path(__file__).resolve().parent,
                    'icons', 'folder-open.png')))

            self.icon_erase = QtGui.QIcon(
                QtGui.QPixmap(
                    os.path.join(pathlib.Path(__file__).resolve().parent,
                    'icons', 'eraser.png')))
        else:
            folder_open = getattr(
                QtWidgets.QStyle, 'SP_DialogOpenButton')
            self.icon_folder_open = self.style().standardIcon(folder_open)

            erase = getattr(
                QtWidgets.QStyle, 'SP_DialogResetButton')
            self.icon_erase = self.style().standardIcon(erase)

        # ___ Container ___
        # Top level layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.layout)

        # ___ Stacked layout ___
        self.stacked_layout = QtWidgets.QStackedLayout()
        self.stacked_layout.setContentsMargins(0, 0, 0, 0)
        self.stacked_layout.setSpacing(0)
        self.layout.addLayout(self.stacked_layout)

        # ___ Filename page ___
        self.filename_page_layout = QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.filename_page_layout)

        self.filename_layout = QtWidgets.QHBoxLayout()
        self.filename_page_layout.setLayout(self.filename_layout)

        self.filename_label = WidgetElidedLabel(
            text='Arquivo scv', elide_side='right')
        self.filename_label.setFixedWidth(self.label_size)
        self.filename_label.setEnabled(False)
        self.filename_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.filename_layout.addWidget(
            self.filename_label, 0, QtCore.Qt.AlignLeft)

        self.filename_button = QtWidgets.QPushButton(text='Selecionar')
        self.filename_button.setIcon(self.icon_folder_open)
        self.filename_layout.addWidget(
            self.filename_button, 0, QtCore.Qt.AlignLeft)

        self.filename_url_label = WidgetElidedLabel(elide_side='middle')
        self.filename_url_label.setFixedWidth(250)
        self.filename_layout.addWidget(
            self.filename_url_label, 1, QtCore.Qt.AlignLeft)

        self.filename_clear_button = QtWidgets.QPushButton()
        self.filename_clear_button.setIcon(self.icon_erase)
        self.filename_clear_button.setFlat(True)
        self.filename_clear_button.setVisible(False)
        self.filename_layout.addWidget(
            self.filename_clear_button, 0, QtCore.Qt.AlignRight)

        # Process
        self.process_page_layout = QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.process_page_layout)

        self.process_layout = QtWidgets.QHBoxLayout()
        self.process_page_layout.setLayout(self.process_layout)

        self.pixmapi_process_button = getattr(
            QtWidgets.QStyle, 'SP_BrowserReload')
        self.icon_process_button = self.style().standardIcon(
            self.pixmapi_process_button)

        self.process_button = QtWidgets.QPushButton(text='Procesar')
        self.process_button.setIcon(self.icon_process_button)
        self.process_layout.addWidget(
            self.process_button, 0, QtCore.Qt.AlignRight)
