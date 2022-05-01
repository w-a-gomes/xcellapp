#!/usr/bin env python3
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

        # Navigation menu
        self.buttons_schema = [
            {
                'index': 0,
                'submenu-index': 0,
                'text': 'Início',
            },
            {
                'index': 1,
                'submenu-index': 0,
                'text': 'Configurações',
            },
            {
                'index': 1,
                'submenu-index': 1,
                'text': 'Importar arquivos CSV',
            },
            {
                'index': 1,
                'submenu-index': 2,
                'text': 'Ícones do sistema',
            },
            {
                'index': 2,
                'submenu-index': 0,
                'text': 'Penultima pagina',
            },
            {
                'index': 3,
                'submenu-index': 0,
                'text': 'Última pagina',
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
        self.csv_import = CsvImport()
        self.csv_import.setContentsMargins(200, 20, 200, 0)
        self.stacked_layout.addWidget(self.csv_import)

        # 2 Icons
        self.icons = Icons()
        self.stacked_layout.addWidget(self.icons)


if __name__ == '__main__':
    pass
