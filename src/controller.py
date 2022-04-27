#!/usr/bin env python3
import os
import pathlib
import sys

from model import Model
from view import View, CsvImport
from PySide6 import QtCore, QtWidgets, QtGui


class Controller(object):
    def __init__(self):
        self.__app = QtWidgets.QApplication([])
        self.__view = View(self)
        self.__model = Model()

        # CsvImport connections
        self.__view.csv_import.filename_button.clicked.connect(
            self.on_csv_import_filename_button)
        
        self.__view.csv_import.header_entry.textChanged.connect(
            self.on_csv_import_header_entry)
        
        self.__view.csv_import.filename_clear_button.clicked.connect(
            self.on_csv_import_filename_clear_button)
        
        self.__view.csv_import.end_button.clicked.connect(
            self.on_csv_import_end_button)
        
        # View connetions
        self.__view.fullscreen_button.clicked.connect(
            self.on_fullscreen_button)
    
    @QtCore.Slot()
    def on_csv_import_filename_button(self) -> None:
        dialog = QtWidgets.QFileDialog.getOpenFileName(
            self.__view.csv_import,
            "Seletor de arquivos",
            str(pathlib.Path.home()),
            "Arquivos CSV (*.csv *.CSV)")

        if dialog[0][-4:].lower() =='.csv':
            # Text
            self.__view.csv_import.filename = dialog[0]

            txt = self.__view.csv_import.filename
            self.__view.csv_import.filename_url_label.setText(
                txt.replace(os.path.dirname(txt) + '/', ''))
            
            # Clear Button
            self.__view.csv_import.filename_clear_button.setVisible(True)
    
    @QtCore.Slot()
    def on_csv_import_filename_clear_button(self):
        self.__view.csv_import.filename = ''
        self.__view.csv_import.filename_url_label.setText('')
        self.__view.csv_import.filename_clear_button.setVisible(False)
    
    @QtCore.Slot()
    def on_csv_import_header_entry(self, text) -> None:
        self.__view.csv_import.header = text
    
    @QtCore.Slot()
    def on_csv_import_end_button(self):
        self.__model.csv_file_processing(
            file_url=self.__view.csv_import.filename,
            header=self.__view.csv_import.header)
    
    @QtCore.Slot()
    def on_fullscreen_button(self):
        # self.__app.quit()
        if self.__view.isFullScreen():
            self.__view.showMaximized()
        else:
            self.__view.showFullScreen()
    
    def main(self):
        self.__view.show()
        self.__view.showFullScreen()
        if self.__view.isFullScreen():
            self.__view.fullscreen_button.setVisible(True)
        # self.__view.resize(800, 600)

        sys.exit(self.__app.exec())


if __name__ == '__main__':
    app = Controller()
    app.main()

    
