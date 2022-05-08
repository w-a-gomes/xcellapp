#!/usr/bin env python3
import json
import os
from pathlib import Path

from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uiwidgets.elidedlabel import ElidedLabel

class CsvImport(QtWidgets.QWidget):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # Settings
        self.settings = self.__settings()
        
        # ___ Properties ___
        self.filename = None
        self.header = None
        self.label_size = 75
        self.desktop_margin = (100, 150)

        # ___ Container ___
        # Top level layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.layout)

        self.top_layout = QtWidgets.QVBoxLayout()
        if self.settings['platform'] == 'desktop':
            self.top_layout.setContentsMargins(
                self.desktop_margin[0], 0, self.desktop_margin[1], 0)
        self.layout.addLayout(self.top_layout)

        # Filename
        self.filename_layout = QtWidgets.QHBoxLayout()
        self.top_layout.addLayout(self.filename_layout)

        self.filename_label = ElidedLabel(text='Arquivo scv', elide_side='right')
        self.filename_label.setFixedWidth(self.label_size)
        self.filename_label.setEnabled(False)
        self.filename_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.filename_layout.addWidget(
            self.filename_label, 0, QtCore.Qt.AlignLeft)
        
        self.pixmapi_filename_button = getattr(
            QtWidgets.QStyle, 'SP_DialogOpenButton')
        self.icon_filename_button = self.style().standardIcon(
            self.pixmapi_filename_button)

        self.filename_button = QtWidgets.QPushButton(text='Selecionar')
        self.filename_button.setIcon(self.icon_filename_button)
        self.filename_layout.addWidget(
            self.filename_button, 0, QtCore.Qt.AlignLeft)

        self.filename_url_label = ElidedLabel(elide_side='middle')
        self.filename_url_label.setFixedWidth(250)
        self.filename_layout.addWidget(
            self.filename_url_label, 1, QtCore.Qt.AlignLeft)

        self.pixmapi_filename_clear = getattr(
            QtWidgets.QStyle, 'SP_DialogResetButton')
        self.icon_filename_clear = self.style().standardIcon(
            self.pixmapi_filename_clear)

        self.filename_clear_button = QtWidgets.QPushButton()
        self.filename_clear_button.setIcon(self.icon_filename_clear)
        self.filename_clear_button.setFlat(True)
        self.filename_clear_button.setVisible(False)
        self.filename_layout.addWidget(
            self.filename_clear_button, 0, QtCore.Qt.AlignRight)

        # Header
        self.header_layout = QtWidgets.QHBoxLayout()
        self.top_layout.addLayout(self.header_layout)

        self.header_label = ElidedLabel(text='Cabeçalho', elide_side='right')
        self.header_label.setFixedWidth(self.label_size)
        self.header_label.setEnabled(False)
        self.header_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.header_layout.addWidget(
            self.header_label, 0, QtCore.Qt.AlignLeft)

        self.header_entry = QtWidgets.QLineEdit()
        self.header_entry.setClearButtonEnabled(True)
        self.header_layout.addWidget(self.header_entry)

        # Process
        self.process_layout = QtWidgets.QHBoxLayout()
        self.top_layout.addLayout(self.process_layout)

        self.pixmapi_process_button = getattr(
            QtWidgets.QStyle, 'SP_BrowserReload')
        self.icon_process_button = self.style().standardIcon(
            self.pixmapi_process_button)

        self.process_button = QtWidgets.QPushButton(text='Procesar')
        self.process_button.setIcon(self.icon_process_button)
        self.process_layout.addWidget(self.process_button, 0, QtCore.Qt.AlignRight)

    def __settings(self):
        root_path = Path(__file__).resolve().parent.parent.parent
        f = os.path.join(root_path, 'static', 'settings', 'settings.json')
        with open(f, 'r') as f:
            return json.load(f)
