#!/usr/bin env python3
import json
import os
import pathlib
import sys

from PySide6 import QtCore, QtWidgets, QtGui

from model import Model
from ui import MainWindow


class Application(object):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        self.__create_settings()
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
        
        self.__ui.navigation_stack.csv_import.process_button.clicked.connect(
            self.on_csv_import_process_button)
        
        # Menu buttons
        icons_sender = (
            self.__ui.navigation_stack.vertical_nav.get_button_by_id('icones'))
        icons_sender.clicked.connect(lambda: self.on_nav_button(
            icons_sender, self.__ui.navigation_stack.icons))

        csv_sender = (
            self.__ui.navigation_stack.vertical_nav.get_button_by_id('csv'))
        csv_sender.clicked.connect(lambda: self.on_nav_button(
            csv_sender, self.__ui.navigation_stack.csv_import))
            
        # UI connetions
        self.__ui.resize_control.connect(self.on_resize_control)

        self.__ui.fullscreen_button.clicked.connect(
            self.on_fullscreen_button)
    
    # CSV import
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
    def on_csv_import_process_button(self) -> None:
        """..."""
        csv = self.__model.csv_file_processing(
            file_url=self.__ui.navigation_stack.csv_import.filename,
            header=self.__ui.navigation_stack.csv_import.header)
        if csv:
            for k, v in csv.csv_datas[6].items():
                print(k, v, end=' | ')
                print(type(k), type(v))
            """
            for item in csv.csv_datas:
                print(item)
            print(csv.header_found)
            """
        else:
            print("Nope")
    
    # Menu pages
    @QtCore.Slot()
    def on_nav_button(self, sender, widget = None):
        current_index = self.__ui.navigation_stack.stacked_layout.currentIndex()
        new_index = 0
        if sender.button_id == 'icones':
            new_index = 1
            self.__ui.navigation_stack.stacked_layout.setCurrentIndex(new_index)

        elif sender.button_id == 'csv':
            new_index = 2
            self.__ui.navigation_stack.stacked_layout.setCurrentIndex(new_index)

        # Animation
        if new_index != current_index:
            self.anim_group = QtCore.QSequentialAnimationGroup()
            
            x = widget.x()
            y = 600 if new_index < current_index else -600

            anim_p = QtCore.QPropertyAnimation(widget, b"pos")
            anim_p.setStartValue(QtCore.QPoint(x, y))
            anim_p.setEndValue(QtCore.QPoint(x, 0))
            anim_p.setDuration(150)
            self.anim_group.addAnimation(anim_p)

            self.anim_group.start()
    
    # Ui
    @QtCore.Slot()
    def on_resize_control(self, size):
        """..."""
        print(f'Width: {size["width"]}, Height: {size["height"]}')
    
    @QtCore.Slot()
    def on_fullscreen_button(self) -> None:
        """..."""
        if self.__ui.isFullScreen():
            self.__ui.showMaximized()
            self.__ui.fullscreen_button.setToolTip('Janela em tela cheia')
        else:
            self.__ui.showFullScreen()
            self.__ui.fullscreen_button.setToolTip('Sair da tela cheia')
    
    @QtCore.Slot()
    def on_exit_button(self) -> None:
        """..."""
        self.__app.quit()
    
    def __create_settings(self):
        """..."""
        # self.__ui.app_path is next
        file_settings_path = os.path.join(
            pathlib.Path(__file__).resolve().parent,
            'static', 'settings', 'settings.json')
        
        if not os.path.isfile(file_settings_path):
            data_settings = {
                'platform': 'desktop',
            }
            with open(file_settings_path, 'w') as file_settings: 
                json.dump(data_settings, file_settings)
    
    def main(self) -> None:
        """..."""
        # self.__ui.showMaximized()
        self.__ui.resize(1000, 500)

        # UI Style
        style_path = (
            os.path.join(
                self.__ui.app_path,
                'static', 'style', 'style.qss'
            )
        )
        with open(style_path, 'r') as f:
            _style = f.read()
            self.__ui.setStyleSheet(_style)
        
        # UI Show
        self.__ui.show()
        sys.exit(self.__app.exec())


if __name__ == '__main__':
    app = Application()
    app.main()
