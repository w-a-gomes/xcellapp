#!/usr/bin env python3
import json
import logging
import os
import pathlib
import sys

from PySide6 import QtCore, QtWidgets

from model import Model
from ui import MainWindow


class Application(object):
    """..."""
    def __init__(self):
        """..."""
        self.__anim_group = None
        self.__table_anim_duration = 200
        self.__app_name = 'XCellApp'
        self.__app_id = 'xcellapp'
        self.__home_path = str(pathlib.Path.home())
        self.__settings_path = self.__get_settings_path()
        self.__settings_file = os.path.join(self.__settings_path, 'conf.json')
        self.__create_settings()
        self.__settings = self.__load_settings()
        os.environ["DIALOG-PATH"] = self.__settings['dialog-path']
        self.__app = QtWidgets.QApplication([])
        self.__ui = MainWindow()
        self.__model = Model()

        # Import Tables connections
        self.__ui.lateral_menu.imp_tables.add_tables_button.clicked.connect(
            self.on_add_tables_button)
        # XLSX import button
        self.__ui.lateral_menu.imp_tables.xls_import_button.clicked.connect(
            self.on_xlsx_import_button)
        # CSV import button
        self.__ui.lateral_menu.imp_tables.csv_import_button.clicked.connect(
            self.on_csv_import_button)

        # Menu buttons
        # icons_sender = (
        #     self.__ui.navigation_stack.vertical_nav.get_button_by_id(
        #         'cfg_icones'))
        # icons_sender.clicked.connect(lambda: self.on_nav_button(
        #     icons_sender, self.__ui.navigation_stack.icons))

        imp_tables_sender = (
            self.__ui.lateral_menu.vertical_nav.get_button_by_id(
                'cfg_imp_tabelas'))
        imp_tables_sender.clicked.connect(lambda: self.on_nav_button(
            imp_tables_sender, self.__ui.lateral_menu.imp_tables))
            
        # UI connections
        self.__ui.resize_control.connect(self.on_resize_control)

        self.__ui.fullscreen_button.clicked.connect(
            self.on_fullscreen_button)

    # Import Tables
    @QtCore.Slot()
    def on_add_tables_button(self) -> None:
        # 0: Tables, 1: XLS, 2: CSV
        self.__ui.lateral_menu.imp_tables.stacked_layout.setCurrentIndex(1)

        self.__anim_group = QtCore.QSequentialAnimationGroup()
        w = self.__ui.lateral_menu.imp_tables.xls_import_page.width()
        y = self.__ui.lateral_menu.imp_tables.xls_import_page.y()
        x = self.__ui.lateral_menu.imp_tables.xls_import_page.x()

        anim_p = QtCore.QPropertyAnimation(
            self.__ui.lateral_menu.imp_tables.xls_import_page, b"pos")
        anim_p.setStartValue(QtCore.QPoint(w, y))
        anim_p.setEndValue(QtCore.QPoint(x, y))
        anim_p.setDuration(self.__table_anim_duration)
        self.__anim_group.addAnimation(anim_p)
        self.__anim_group.start()

    @QtCore.Slot()
    def on_xlsx_import_button(self) -> None:
        # 0: Tables, 1: XLS, 2: CSV
        if self.__ui.lateral_menu.imp_tables.xls_get_filename.filenameUrl():
            # Save dialog path
            self.__settings['dialog-path'] = os.environ["DIALOG-PATH"]
            self.__save_settings()

            # Reset CSV page infos
            self.__ui.lateral_menu.imp_tables.csv_page_title.setText('')
            self.__ui.lateral_menu.imp_tables.csv_get_filename.reset()

            # Set CSV page infos
            self.__ui.lateral_menu.imp_tables.csv_page_title.setText(
                'Selecione os arquivos CSV das tabelas:')

            (self.__ui.lateral_menu.imp_tables.csv_get_filename
                .setDescriptionText(
                    self.__ui.lateral_menu.imp_tables.xls_get_filename
                    .filename()))

            # Switch to CSV page
            self.__ui.lateral_menu.imp_tables.stacked_layout.setCurrentIndex(2)

            # Animation
            self.__anim_group = QtCore.QSequentialAnimationGroup()
            y = self.__ui.lateral_menu.imp_tables.csv_import_page.y()
            x = self.__ui.lateral_menu.imp_tables.csv_import_page.x()
            w = self.__ui.lateral_menu.imp_tables.csv_import_page.width()
            anim_p = QtCore.QPropertyAnimation(
                self.__ui.lateral_menu.imp_tables.csv_import_page, b"pos")
            anim_p.setStartValue(QtCore.QPoint(w, y))
            anim_p.setEndValue(QtCore.QPoint(x, y))
            anim_p.setDuration(self.__table_anim_duration)
            self.__anim_group.addAnimation(anim_p)
            self.__anim_group.start()

    @QtCore.Slot()
    def on_csv_import_button(self):
        if self.__ui.lateral_menu.imp_tables.csv_get_filename.filenameList():
            # Save dialog path
            os.environ["DIALOG-PATH"] = (
                self.__ui.lateral_menu.imp_tables.csv_get_filename
                .filenamePathList()[0])
            self.__settings['dialog-path'] = os.environ["DIALOG-PATH"]
            self.__save_settings()

            # CSV schema
            csv_schema = {
                'schema-name': (self.__ui.lateral_menu.imp_tables
                                .csv_get_filename.descriptionText()),
                'schema-datas': []
            }

            # CSV schema items
            csv_files_url_list = (self.__ui.lateral_menu.imp_tables
                                  .csv_get_filename.filenameUrlList())
            for csv_file_url in csv_files_url_list:
                csv_obj = self.__model.csv_file_processing(csv_file_url)

                csv_schema['schema-datas'].append(
                    {f'{csv_obj.filename}': csv_obj.csv_datas}
                )

            # CSV schema path
            xlsx_table_schema_path = os.path.join(
                self.__settings['tables-schema-path'],
                (
                    self.__ui.lateral_menu.imp_tables.csv_get_filename
                    .descriptionText()
                    .replace('.xlsx', '')
                    .replace('.xlsm', '')
                    .replace('.xls', '')
                ) + '.json'
            )
            # Save CSV schema
            with open(xlsx_table_schema_path, 'w') as settings_file:
                json.dump(csv_schema, settings_file)

    # Menu pages
    @QtCore.Slot()
    def on_nav_button(self, sender, widget=None):
        current_index = self.__ui.lateral_menu.stacked_layout.currentIndex()
        new_index = 0

        if sender.button_id == 'cfg_imp_tabelas':
            # Go back to first table page
            if (self.__ui.lateral_menu.imp_tables.stacked_layout
                    .currentIndex()) != new_index:
                self.__anim_group = QtCore.QSequentialAnimationGroup()
                w = -self.__ui.lateral_menu.imp_tables.add_tables_page.width()
                y = self.__ui.lateral_menu.imp_tables.add_tables_page.y()
                x = self.__ui.lateral_menu.imp_tables.add_tables_page.x()

                anim_p = QtCore.QPropertyAnimation(
                    self.__ui.lateral_menu.imp_tables.add_tables_page, b"pos")
                anim_p.setStartValue(QtCore.QPoint(w, y))
                anim_p.setEndValue(QtCore.QPoint(x, y))
                anim_p.setDuration(self.__table_anim_duration)
                self.__anim_group.addAnimation(anim_p)
                self.__anim_group.start()

            new_index = 1
            self.__ui.lateral_menu.stacked_layout.setCurrentIndex(new_index)
            self.__ui.lateral_menu.imp_tables.stacked_layout.setCurrentIndex(0)
            self.__ui.lateral_menu.imp_tables.xls_get_filename.clear_filename()

        # elif sender.button_id == 'cfg_icones':
        #     new_index = 2
        #     self.__ui.navigation_stack.stacked_layout.setCurrentIndex(new_index)

        # Animation
        if new_index != current_index:
            self.__anim_group = QtCore.QSequentialAnimationGroup()
            x = widget.x()
            h = widget.height()
            y = h if new_index < current_index else -h
            anim_p = QtCore.QPropertyAnimation(widget, b"pos")
            anim_p.setStartValue(QtCore.QPoint(x, y))
            anim_p.setEndValue(QtCore.QPoint(x, 0))
            anim_p.setDuration(self.__table_anim_duration)
            self.__anim_group.addAnimation(anim_p)
            self.__anim_group.start()
    
    # Ui
    @QtCore.Slot()
    def on_resize_control(self, size):
        """..."""
        print(f'Width: {size["width"]}, Height: {size["height"]}')
    
    @QtCore.Slot()
    def on_fullscreen_button(self) -> None:
        """..."""
        if self.__ui.isFullScreen():
            # self.__ui.showNormal()
            self.__ui.showMaximized()
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
            os.makedirs(os.path.join(self.__settings_path, 'tables-schema'))
        
        if not os.path.isfile(self.__settings_file):
            data_settings = {
                'platform': 'desktop',
                'dialog-path': self.__home_path,
                'settings-path': self.__settings_path,
                'tables-schema-path': os.path.join(
                    self.__settings_path, 'tables-schema'),
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
        self.__ui.showMaximized()
        # self.__ui.resize(1000, 500)

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
