#!/usr/bin env python3
import json
import logging
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
        self.__app_name = 'XCellApp'
        self.__app_id = 'xcellapp'
        self.__home_path = str(pathlib.Path.home())
        self.__settings_path = self.__get_settings_path()
        self.__settings_file = os.path.join(self.__settings_path, 'conf.json')
        self.__create_settings()
        self.__settings = self.__load_settings()
        self.__app = QtWidgets.QApplication([])
        self.__ui = MainWindow()
        self.__model = Model()

        # Import Tables connections
        self.__ui.navigation_stack.imp_tables.filename_button.clicked.connect(
            self.on_imp_tables_filename_button)
        
        (self.__ui.navigation_stack.imp_tables.
            filename_clear_button.clicked.connect(
                self.on_imp_tables_filename_clear_button))
        
        self.__ui.navigation_stack.imp_tables.process_button.clicked.connect(
            self.on_imp_tables_process_button)
        
        # Menu buttons
        icons_sender = (
            self.__ui.navigation_stack.vertical_nav.get_button_by_id(
                'cfg_icones'))
        icons_sender.clicked.connect(lambda: self.on_nav_button(
            icons_sender, self.__ui.navigation_stack.icons))

        imp_tables_sender = (
            self.__ui.navigation_stack.vertical_nav.get_button_by_id(
                'cfg_imp_tabelas'))
        imp_tables_sender.clicked.connect(lambda: self.on_nav_button(
            imp_tables_sender, self.__ui.navigation_stack.imp_tables))
            
        # UI connetions
        self.__ui.resize_control.connect(self.on_resize_control)

        self.__ui.fullscreen_button.clicked.connect(
            self.on_fullscreen_button)
    
    # Import Tables
    @QtCore.Slot()
    def on_imp_tables_filename_button(self) -> None:
        """..."""
        dialog = QtWidgets.QFileDialog.getOpenFileName(
            self.__ui.navigation_stack.imp_tables,
            "Seletor de arquivos",
            self.__settings['dialog-path'],
            "Arquivos do Microsoft Excel (*.xlsx *.xls *.XLSX *.XLS)")

        if (
            dialog[0][-5:].lower() == '.xlsx' or
            dialog[0][-4:].lower() == '.xls'
        ):
            # Get text
            txt_file = dialog[0]
            txt_path = os.path.dirname(txt_file)
            txt_filename = txt_file.replace(txt_path + '/', '')
            
            # Set text
            self.__ui.navigation_stack.imp_tables.filename = txt_file
            self.__ui.navigation_stack.imp_tables.filename_url_label.setText(
                txt_filename)
            
            # Update dialog settings
            self.__settings['dialog-path'] = txt_path
            self.__save_settings()
            
            # Clear Button
            (self.__ui.navigation_stack.imp_tables.
                filename_clear_button.setVisible(True))
    
    @QtCore.Slot()
    def on_imp_tables_filename_clear_button(self) -> None:
        """..."""
        self.__ui.navigation_stack.imp_tables.filename = ''
        self.__ui.navigation_stack.imp_tables.filename_url_label.setText('')
        (self.__ui.navigation_stack.imp_tables
            .filename_clear_button.setVisible(False))
    
    @QtCore.Slot()
    def on_imp_tables_process_button(self) -> None:
        """..."""
        csv = self.__model.csv_file_processing(
            file_url=self.__ui.navigation_stack.imp_tables.filename)
        if csv:
            for l in csv.csv_datas:
                for i in l:
                    print(i)
                print('---')
        else:
            print("Nope")
    
    # Menu pages
    @QtCore.Slot()
    def on_nav_button(self, sender, widget = None):
        current_index = self.__ui.navigation_stack.stacked_layout.currentIndex()
        new_index = 0

        if sender.button_id == 'cfg_imp_tabelas':
            new_index = 1
            self.__ui.navigation_stack.stacked_layout.setCurrentIndex(new_index)

        elif sender.button_id == 'cfg_icones':
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
            self.__ui.showNormal()
            self.__ui.fullscreen_button.setToolTip('Janela em tela cheia')
            self.__ui.fullscreen_button.setIcon(self.__ui.icon_fullscreen)
        else:
            self.__ui.showFullScreen()
            self.__ui.fullscreen_button.setToolTip('Sair da tela cheia')
            self.__ui.fullscreen_button.setIcon(self.__ui.icon_view_restore)
    
    @QtCore.Slot()
    def on_exit_button(self) -> None:
        """..."""
        self.__app.quit()
    
    # Settings
    def __get_settings_path(self):
        if sys.platform == 'win32':
            # AppData\Roaming\
            return os.path.join(self.__home_path, 'AppData', self.__app_id)
        else:  # 'linux' 'darwin' 'cygwin' 'aix'
            return os.path.join(self.__home_path, '.config', self.__app_id)

    def __create_settings(self):
        """..."""
        if not os.path.isdir(self.__settings_path):
            os.makedirs(self.__settings_path)
        
        if not os.path.isfile(self.__settings_file):
            data_settings = {
                'platform': 'desktop',
                'dialog-path': self.__home_path,
            }
            with open(self.__settings_file, 'w') as settings_file:
                json.dump(data_settings, settings_file)
    
    def __load_settings(self):
        if not os.path.isfile(self.__settings_file):
            logging.error('Settings file not found! creating now...')
            self.__create_settings()
        
        with open(self.__settings_file, 'r') as f:
            return json.load(f)
    
    def __save_settings(self):
        """..."""
        with open(self.__settings_file, 'w') as settings_file:
            json.dump(self.__settings, settings_file)

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
