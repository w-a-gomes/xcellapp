#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uisections.csvimport import CsvImport
from attachment.uiwidgets.navbutton import NavButton, SubNavButton
from attachment.uiwidgets.verticalnav import VerticalNav

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
        
        # 0
        self.nav_buttons_0 = NavButton(text='Item index 0')
        self.stack_nav_layout.addWidget(self.nav_buttons_0)

        self.stacked_layout.addWidget(
            QtWidgets.QLabel(text='Item index 0'))

        # 1
        self.nav_buttons_1 = NavButton(text='Item index 1')
        self.stack_nav_layout.addWidget(self.nav_buttons_1)

        self.stacked_layout.addWidget(
            QtWidgets.QLabel(text='Item index 1'))

        # 2
        self.nav_buttons_2 = NavButton(text='Item index 2')
        self.stack_nav_layout.addWidget(self.nav_buttons_2)

        self.stacked_layout.addWidget(
            QtWidgets.QLabel(text='Item index 2'))

        # Settings
        self.nav_button_settings = NavButton(text='Configurações')
        self.stack_nav_layout.addWidget(self.nav_button_settings)
        
        self.csv_import = CsvImport()
        self.csv_import.setContentsMargins(200, 20, 200, 0)
        self.stacked_layout.addWidget(
            self.csv_import)
        
        self.nav_button_settings_sublay = QtWidgets.QVBoxLayout()
        self.nav_button_settings_sublay.setContentsMargins(20, 1, 3, 0)
        self.stack_nav_layout.addLayout(self.nav_button_settings_sublay)

        self.nav_button_settings_0 = SubNavButton('Sub settings 0')
        self.nav_button_settings_0.setVisible(False)
        self.nav_button_settings_sublay.addWidget(self.nav_button_settings_0)
        
        self.nav_button_settings_1 = SubNavButton('Sub settings 1')
        self.nav_button_settings_1.setVisible(False)
        self.nav_button_settings_sublay.addWidget(self.nav_button_settings_1)

        self.navigation_st = VerticalNav()
        self.stack_nav_layout.addWidget(
            self.navigation_st, 0, QtCore.Qt.AlignTop)


if __name__ == '__main__':
    pass
