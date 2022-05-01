#!/usr/bin env python3
import os
import pathlib
import sys

from model import Model
from ui import MainWindow, CsvImport
from PySide6 import QtCore, QtWidgets, QtGui

class Application(object):
    """..."""
    def __init__(self):
        """..."""
        self.__app = QtWidgets.QApplication([])
        self.__ui = MainWindow()
        self.__model = Model()

        # CsvImport connections
        self.__ui.navigation_stack.csv_import.filename_button.clicked.connect(
            self.on_csv_import_filename_button)
        
        self.__ui.navigation_stack.csv_import.header_entry.textChanged.connect(
            self.on_csv_import_header_entry)
        
        (self.__ui.navigation_stack.csv_import.
            filename_clear_button.clicked.connect(
                self.on_csv_import_filename_clear_button))
        
        self.__ui.navigation_stack.csv_import.end_button.clicked.connect(
            self.on_csv_import_end_button)
        
        # Menu
        (self.__ui.navigation_stack.vertical_nav.get_button_by_index(0, 0)
        .clicked.connect(self.on_nav_button_home))

        (self.__ui.navigation_stack.vertical_nav.get_button_by_index(1, 0)
        .clicked.connect(self.on_nav_button_settings))

        (self.__ui.navigation_stack.vertical_nav.get_button_by_index(1, 1)
        .clicked.connect(self.on_nav_button_csv_settings))

        (self.__ui.navigation_stack.vertical_nav.get_button_by_index(1, 2)
        .clicked.connect(self.on_nav_button_icons))

        # Menu pages
        self.__ui.navigation_stack.stack_btn_set.clicked.connect(
            self.on_nav_button_settings_menu)

        # UI connetions
        self.__ui.fullscreen_button.clicked.connect(
            self.on_fullscreen_button)
        
        self.__ui.exit_button.clicked.connect(
            self.on_exit_button)
    
    @QtCore.Slot()
    def on_csv_import_filename_button(self) -> None:
        """..."""
        dialog = QtWidgets.QFileDialog.getOpenFileName(
            self.__ui.navigation_stack.csv_import,
            "Seletor de arquivos",
            str(pathlib.Path.home()),
            "Arquivos CSV (*.csv *.CSV)")

        if dialog[0][-4:].lower() =='.csv':
            # Text
            self.__ui.navigation_stack.csv_import.filename = dialog[0]

            txt = self.__ui.navigation_stack.csv_import.filename
            self.__ui.navigation_stack.csv_import.filename_url_label.setText(
                txt.replace(os.path.dirname(txt) + '/', ''))
            
            # Clear Button
            (self.__ui.navigation_stack.csv_import.
                filename_clear_button.setVisible(True))
    
    @QtCore.Slot()
    def on_csv_import_filename_clear_button(self) -> None:
        """..."""
        self.__ui.navigation_stack.csv_import.filename = ''
        self.__ui.navigation_stack.csv_import.filename_url_label.setText('')
        (self.__ui.navigation_stack.csv_import
            .filename_clear_button.setVisible(False))
    
    @QtCore.Slot()
    def on_csv_import_header_entry(self, text) -> None:
        """..."""
        self.__ui.navigation_stack.csv_import.header = text
    
    @QtCore.Slot()
    def on_csv_import_end_button(self) -> None:
        """..."""
        self.__model.csv_file_processing(
            file_url=self.__ui.navigation_stack.csv_import.filename,
            header=self.__ui.navigation_stack.csv_import.header)
    
    @QtCore.Slot()
    def on_nav_button_home(self) -> None:
        self.__ui.navigation_stack.stacked_layout.setCurrentIndex(0)

    @QtCore.Slot()
    def on_nav_button_settings(self) -> None:
        self.__ui.navigation_stack.stacked_layout.setCurrentIndex(1)
    
    @QtCore.Slot()
    def on_nav_button_settings_menu(self) -> None:
        if not self.__ui.navigation_stack.vertical_nav.get_button_by_index(1, 1).isVisible():
            self.__ui.navigation_stack.vertical_nav.get_button_by_index(1, 0).click()
        self.__ui.navigation_stack.vertical_nav.get_button_by_index(1, 1).click()

    @QtCore.Slot()
    def on_nav_button_csv_settings(self) -> None:
        self.__ui.navigation_stack.stacked_layout.setCurrentIndex(2)
    
    @QtCore.Slot()
    def on_nav_button_icons(self) -> None:
        self.__ui.navigation_stack.stacked_layout.setCurrentIndex(3)
    
    @QtCore.Slot()
    def on_fullscreen_button(self) -> None:
        """..."""
        if self.__ui.isFullScreen():
            self.__ui.showMaximized()
            self.__ui.fullscreen_button.setToolTip('Janela em tela cheia')
            self.__ui.exit_button.setVisible(False)
        else:
            self.__ui.showFullScreen()
            self.__ui.fullscreen_button.setToolTip('Sair da tela cheia')
            self.__ui.exit_button.setVisible(True)
    
    @QtCore.Slot()
    def on_exit_button(self) -> None:
        """..."""
        self.__app.quit()
    
    def main(self) -> None:
        """..."""
        self.__ui.showMaximized()
        self.__ui.fullscreen_button.setVisible(True)
        self.__ui.fullscreen_button.setToolTip('Sair da tela cheia')
        
        self.__ui.exit_button.setVisible(False)

        style_path = (
            os.path.join(
                self.__ui.app_path,
                'static', 'style', 'style.qss'
            )
        )
        with open(style_path, 'r') as f:
            _style = f.read()
            self.__ui.setStyleSheet(_style)
        
        self.__ui.show()
        sys.exit(self.__app.exec())


if __name__ == '__main__':
    app = Application()
    app.main()
