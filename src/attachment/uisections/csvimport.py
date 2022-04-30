#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uiwidgets.elidedlabel import ElidedLabel

class CsvImport(QtWidgets.QWidget):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # self.setFixedWidth(600)
        # self.setMaximumWidth(600)
        # self.setContentsMargins(200, 0, 200, 0)
        # self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        # self.shadow.setBlurRadius(15)
        # self.setGraphicsEffect(self.shadow)

        # ___ Properties ___
        self.filename = None
        self.header = None

        # ___ Container ___
        # Top level layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.layout)

        # Filename
        self.filename_layout = QtWidgets.QHBoxLayout()
        self.filename_layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.filename_layout)

        self.filename_label = QtWidgets.QLabel(text='Arquivo scv')
        self.filename_layout.addWidget(
            self.filename_label, 2, QtCore.Qt.AlignRight)
        
        self.filename_button_layout = QtWidgets.QHBoxLayout()
        self.filename_button_layout.setContentsMargins(0, 0, 0, 0)
        self.filename_layout.addLayout(self.filename_button_layout, 8)
        
        self.pixmapi_filename_button = getattr(
            QtWidgets.QStyle, 'SP_DialogOpenButton')
        self.icon_filename_button = self.style().standardIcon(
            self.pixmapi_filename_button)

        self.filename_button = QtWidgets.QPushButton(text='Selecionar')
        self.filename_button.setIcon(self.icon_filename_button)
        self.filename_button_layout.addWidget(
            self.filename_button, 0, QtCore.Qt.AlignLeft)

        self.filename_url_label = ElidedLabel(elide_side='middle')
        self.filename_url_label.setFixedWidth(250)
        self.filename_button_layout.addWidget(
            self.filename_url_label, 1, QtCore.Qt.AlignLeft)

        self.pixmapi_filename_clear = getattr(
            QtWidgets.QStyle, 'SP_DialogResetButton')
        self.icon_filename_clear = self.style().standardIcon(
            self.pixmapi_filename_clear)

        self.filename_clear_button = QtWidgets.QPushButton()
        self.filename_clear_button.setIcon(self.icon_filename_clear)
        self.filename_clear_button.setFlat(True)
        self.filename_clear_button.setVisible(False)
        self.filename_button_layout.addWidget(
            self.filename_clear_button, 0, QtCore.Qt.AlignRight)

        # Header
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.header_layout)

        self.header_label = QtWidgets.QLabel(text='Cabeçalho')
        self.header_layout.addWidget(
            self.header_label, 2, QtCore.Qt.AlignRight)

        self.header_entry_layout = QtWidgets.QHBoxLayout()
        self.header_entry_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.addLayout(self.header_entry_layout, 8)

        self.header_entry = QtWidgets.QLineEdit()
        self.header_entry.setClearButtonEnabled(True)
        self.header_entry_layout.addWidget(self.header_entry, 10)

        # End
        self.pixmapi_end_button = getattr(
            QtWidgets.QStyle, 'SP_BrowserReload')
        self.icon_end_button = self.style().standardIcon(
            self.pixmapi_end_button)

        self.end_button = QtWidgets.QPushButton(text='Procesar')
        self.end_button.setIcon(self.icon_end_button)
        self.layout.addWidget(self.end_button, 0, QtCore.Qt.AlignRight)
