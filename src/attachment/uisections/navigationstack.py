#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uisections.csvimport import CsvImport
from attachment.uiwidgets.navigationbutton import NavigationButton

class NavigationStack(QtWidgets.QWidget):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # ___ Container ___
        # Top level layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.setLayout(self.layout)

        # Body
        self.stack_body_layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.stack_body_layout)

        # Nav layout
        self.stack_nav_layout = QtWidgets.QVBoxLayout()
        self.stack_nav_layout.setSpacing(0)
        self.stack_body_layout.addLayout(self.stack_nav_layout, 1)
        
        self.nav_buttons_0 = NavigationButton(text='Item index 0')
        self.nav_buttons_0.setFlat(True)
        self.stack_nav_layout.addWidget(self.nav_buttons_0)

        self.nav_buttons_1 = NavigationButton(text='Item index 1')
        self.nav_buttons_1.setFlat(True)
        self.stack_nav_layout.addWidget(self.nav_buttons_1)

        self.nav_buttons_2 = NavigationButton(text='Item index 2')
        self.nav_buttons_2.setFlat(True)
        self.stack_nav_layout.addWidget(self.nav_buttons_2)

        self.nav_button_settings = NavigationButton(text='Configurações')
        self.nav_button_settings.setFlat(True)
        self.stack_nav_layout.addWidget(self.nav_button_settings)

        # Pages layout
        self.stack_pages_layout = QtWidgets.QVBoxLayout()
        self.stack_body_layout.addLayout(self.stack_pages_layout, 9)

        self.stacked_layout = QtWidgets.QStackedLayout()
        self.stacked_layout.setContentsMargins(0, 0, 0, 0)
        self.stacked_layout.setSpacing(0)
        self.stack_pages_layout.addLayout(self.stacked_layout)
        
        # Pages test
        self.stacked_layout.addWidget(
            QtWidgets.QLabel(text='Item index 0'))
        self.stacked_layout.addWidget(
            QtWidgets.QLabel(text='Item index 1'))
        self.stacked_layout.addWidget(
            QtWidgets.QLabel(text='Item index 2'))
        
        # Page settings
        self.csv_import = CsvImport()
        self.stacked_layout.addWidget(
            self.csv_import)
            

if __name__ == '__main__':
    pass
