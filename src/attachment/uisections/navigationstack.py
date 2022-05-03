#!/usr/bin env python3
import sys

from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uisections.csvimport import CsvImport
from attachment.uiwidgets.verticalnav import VerticalNav
from attachment.uiwidgets.icons import Icons

class NavigationStack(QtWidgets.QWidget):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # ___ Container ___
        # Top level layout
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setMinimumWidth(100)
        self.setLayout(self.layout)

        # Nav layout
        self.stack_nav_layout = QtWidgets.QVBoxLayout()
        self.stack_nav_layout.setSpacing(0)
        self.layout.addLayout(self.stack_nav_layout, 1)

        # Pages layout
        self.stack_pages_layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.stack_pages_layout, 9)

        self.stacked_layout = QtWidgets.QStackedLayout()
        self.stacked_layout.setContentsMargins(0, 0, 0, 0)
        self.stacked_layout.setSpacing(0)
        self.stack_pages_layout.addLayout(self.stacked_layout)

        # Navigation menu buttons
        self.buttons_schema = [
            {
                'id': 'inicio', 'text': 'Início'
            },
            {
                'id': 'config', 'text': 'Configurações', 'sub-buttons': [
                    {'id': 'icones', 'text': 'Ícones'},
                    {'id': 'csv', 'text': 'Importar arquivos CSV'},
                ]
            },
            {
                'id': 'penultimo', 'text': 'Penúltimo'
            },
            {
                'id': 'ultimo', 'text': 'Último', 'sub-buttons': [
                    {'id': 'test', 'text': 'Teste'},
                    {'id': 'testa', 'text': 'Testa'},
                ]
            },
            {
                'id': 'pan', 'text': 'Paann'
            },
        ]
        
        self.vertical_nav = VerticalNav(self.buttons_schema)
        self.stack_nav_layout.addWidget(
            self.vertical_nav, 0, QtCore.Qt.AlignTop)
        
        # Stack pages
        
        # 0
        self.stacked_layout.addWidget(
            QtWidgets.QLabel(text='Página Inicial'))
        
        # 1 Settings
        self.stack_btn_set = QtWidgets.QPushButton(text='Importar arquivos CSV')
        self.stacked_layout.addWidget(self.stack_btn_set)

        # 2 CSV
        self.csv_import = CsvImport()
        self.stacked_layout.addWidget(self.csv_import)

        # 3 Icons
        self.icons = Icons()
        self.stacked_layout.addWidget(self.icons)


if __name__ == '__main__':
    pass
