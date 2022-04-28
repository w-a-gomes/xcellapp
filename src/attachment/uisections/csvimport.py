#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uiwidgets.elidedlabel import ElidedLabel

class CsvImport(QtWidgets.QWidget):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.setFixedWidth(500)
        # self.setContentsMargins(20, 20, 20, 20)
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
        
        self.filename_button = QtWidgets.QPushButton(
            icon=QtGui.QIcon.fromTheme('document-open-folder'),
            text='Selecionar')
        self.filename_button_layout.addWidget(
            self.filename_button, 0, QtCore.Qt.AlignLeft)

        self.filename_url_label = ElidedLabel(elide_side='middle')
        self.filename_url_label.setFixedWidth(250)
        self.filename_button_layout.addWidget(
            self.filename_url_label, 1, QtCore.Qt.AlignLeft)

        self.filename_clear_button = QtWidgets.QPushButton(
            icon=QtGui.QIcon.fromTheme('edit-clear'))
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
        self.end_button = QtWidgets.QPushButton(
            text='Procesar', icon=QtGui.QIcon.fromTheme('view-refresh'))
        self.layout.addWidget(self.end_button, 0, QtCore.Qt.AlignRight)