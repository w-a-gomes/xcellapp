#!/usr/bin env python3
import datetime
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
        self.can_generate_first_tables = True
        self.__ui.imp_tables.add_tables_button.clicked.connect(
            self.tables__add_tables_button)
        # XLSX import button
        self.__ui.imp_tables.xls_import_button.clicked.connect(
            self.tables__xlsx_import_button)
        # CSV import button
        self.__ui.imp_tables.csv_import_button.clicked.connect(
            self.tables__csv_import_button)

        # Edit
        (self.__ui.imp_tables.tables_schema_page.edit_table_button_clicked
         .connect(self.tables__edit_table_button))

        # Menu buttons
        # icons_sender = (
        #     self.__ui.navigation_stack.vertical_nav.get_button_by_id(
        #         'cfg_icones'))
        # icons_sender.clicked.connect(lambda: self.on_nav_button(
        #     icons_sender, self.__ui.navigation_stack.icons))

        imp_tables_sender = (
            self.__ui.lateral_menu.vertical_nav.get_button_by_id(
                'cfg_imp_tabelas'))
        imp_tables_sender.clicked.connect(
            lambda: self.verticalmenu__on_buttons(
                imp_tables_sender, self.__ui.imp_tables))
            
        # UI connections
        self.__ui.resize_control.connect(self.main__resize_event)

        self.__ui.fullscreen_button.clicked.connect(
            self.main__fullscreen_button)

    # ___ MAIN ___
    def main(self) -> None:
        """..."""
        self.__ui.showMaximized()
        self.__ui.setWindowTitle(self.__app_name)
        self.__ui.setMinimumHeight(500)
        self.__ui.setMinimumWidth(1000)
        # self.__ui.resize(1000, 500)

        # Style
        style_path = (
            os.path.join(
                self.__ui.app_path,
                'static', 'style', 'style.qss'
            )
        )
        with open(style_path, 'r') as f:
            _style = f.read()
            self.__ui.setStyleSheet(_style)

        # Show
        self.__ui.show()
        sys.exit(self.__app.exec())

    @QtCore.Slot()
    def main__resize_event(self, size):
        """..."""
        print(f'Width: {size["width"]}, Height: {size["height"]}')

    @QtCore.Slot()
    def main__fullscreen_button(self) -> None:
        """..."""
        if self.__ui.isFullScreen():
            # self.__ui.showNormal()
            self.__ui.showMaximized()
            self.__ui.fullscreen_button.setToolTip('Janela em tela cheia')
            self.__ui.fullscreen_button.setIcon(self.__ui.icon_fullscreen)
        else:
            self.__ui.showFullScreen()
            self.__ui.fullscreen_button.setToolTip('Sair da tela cheia')
            self.__ui.fullscreen_button.setIcon(
                self.__ui.icon_view_restore)

    @QtCore.Slot()
    def main__exit_button(self) -> None:
        """..."""
        self.__app.quit()

    # ___ VERTICAL MENU ___
    @QtCore.Slot()
    def verticalmenu__on_buttons(self, sender, widget=None):
        current_index = self.__ui.stacked_layout.currentIndex()
        new_index = 0

        if sender.button_id == 'cfg_imp_tabelas':
            # Go back to first table page
            self.tables__enable_section_tables_import(True)

            if self.__ui.imp_tables.stacked_layout.currentIndex() != new_index:
                # add_tables_page 'slide-to-right'
                self.animate_widget(
                    widget=self.__ui.imp_tables.add_tables_page,
                    animation_type='slide-to-right')

            # Set stacked_layout index
            new_index = 1

            # Go to: First main page
            self.__ui.stacked_layout.setCurrentIndex(new_index)

            # Go to: Add table section
            self.__ui.imp_tables.stacked_layout.setCurrentIndex(0)

            # Reset: Add tables section
            self.__ui.imp_tables.xls_get_filename.clear_filename()

            # Go to: tables preview
            if self.__ui.imp_tables.table_stacked_layout.currentIndex() != 0:
                # Go to: tables section
                self.__ui.imp_tables.table_stacked_layout.setCurrentIndex(
                    0)

                # tables_schema_page 'opacity-fade'
                self.animate_widget(
                    widget=self.__ui.imp_tables.tables_schema_page,
                    animation_type='opacity-fade')

            # Update tables
            if self.can_generate_first_tables:
                self.__ui.imp_tables.tables_schema_page.update_tables(
                    self.__settings['tables-schema-path'],
                    self.__settings['tables-schema-filenames'])
                self.can_generate_first_tables = False

        # elif sender.button_id == 'cfg_icones':
        #     new_index = 2
        #     self.__ui.navigation_stack.stacked_layout.setCurrentIndex(new_index)

        # slide main pages
        if new_index != current_index:
            if new_index < current_index:
                self.animate_widget(
                    widget=widget, animation_type='slide-to-top')
            else:
                self.animate_widget(
                    widget=widget, animation_type='slide-to-bottom')

    # ___ TABLES ___
    @QtCore.Slot()
    def tables__add_tables_button(self) -> None:
        # 0: Tables, 1: XLS, 2: CSV
        self.__ui.imp_tables.stacked_layout.setCurrentIndex(1)

        # xls_import_page 'slide-to-left'
        self.animate_widget(
            widget=self.__ui.imp_tables.xls_import_page,
            animation_type='slide-to-left')

    @QtCore.Slot()
    def tables__xlsx_import_button(self) -> None:
        # 0: Tables, 1: XLS, 2: CSV
        if self.__ui.imp_tables.xls_get_filename.filenameUrl():
            # Save dialog path
            self.__settings['dialog-path'] = os.environ["DIALOG-PATH"]
            self.__save_settings()

            # Reset CSV page infos
            self.__ui.imp_tables.csv_page_title.setText('')
            self.__ui.imp_tables.csv_get_filename.reset()

            # Set CSV page infos
            self.__ui.imp_tables.csv_page_title.setText(
                'Selecione os arquivos CSV das tabelas:')

            (self.__ui.imp_tables.csv_get_filename
                .setDescriptionText(
                    self.__ui.imp_tables.xls_get_filename
                    .filename()))

            # Switch to CSV page
            self.__ui.imp_tables.stacked_layout.setCurrentIndex(2)

            # csv_import_page 'slide-to-left'
            self.animate_widget(
                widget=self.__ui.imp_tables.csv_import_page,
                animation_type='slide-to-left')

    @QtCore.Slot()
    def tables__csv_import_button(self):
        if self.__ui.imp_tables.csv_get_filename.filenameList():
            # Save dialog path
            os.environ["DIALOG-PATH"] = (
                self.__ui.imp_tables.csv_get_filename
                .filenamePathList()[0])
            self.__settings['dialog-path'] = os.environ["DIALOG-PATH"]

            # CSV schema
            csv_schema = {
                'id': '',
                'filename': '',
                'date': '',
                'edited': False,
                'edited-date': None,
                'datas': [],
            }
            # Set id
            schema_id = str(len(
                os.listdir(self.__settings['tables-schema-path'])) + 1)
            csv_schema['id'] = schema_id

            # Set filename
            schema_name = (
                self.__ui.imp_tables.csv_get_filename.descriptionText()
                .replace('.xlsx', '').replace('.xlsm', '').replace('.xls', ''))
            csv_schema['filename'] = schema_name

            # Set date
            now = datetime.datetime.now()  # '%H:%M:%S on %A, %B the %dth, %Y'
            csv_schema['date'] = now.strftime('%d/%m/%Y %H:%M')

            # Set datas
            for csv_file_url in (
                    self.__ui.imp_tables.csv_get_filename.filenameUrlList()):
                csv_obj = self.__model.csv_file_processing(csv_file_url)
                csv_schema['datas'].append(
                    {
                        'table-name': f'{csv_obj.filename}',
                        'edited': False,
                        'edited-date': None,
                        'table-header': csv_obj.header,
                        'table-header-index': csv_obj.header_index,
                        'table-data': csv_obj.csv_datas,
                    })

            # Save CSV schema
            name_to_save = schema_id + '_' + schema_name + '.json'
            with open(
                os.path.join(
                    self.__settings['tables-schema-path'], name_to_save),
                'w'
            ) as settings_file:
                json.dump(csv_schema, settings_file)

            # Update filename list
            self.__settings['tables-schema-filenames'].insert(0, name_to_save)

            # Update tables
            self.__ui.imp_tables.tables_schema_page.update_tables(
                self.__settings['tables-schema-path'],
                self.__settings['tables-schema-filenames'])

            # Save
            self.__save_settings()

            # Go back to first table page
            self.__ui.imp_tables.stacked_layout.setCurrentIndex(0)
            self.__ui.imp_tables.xls_get_filename.clear_filename()

            # add_tables_page 'slide-to-right'
            self.animate_widget(
                widget=self.__ui.imp_tables.add_tables_page,
                animation_type='slide-to-right')

    @QtCore.Slot()
    def tables__edit_table_button(self):
        # Set Schema to edit
        self.__ui.imp_tables.tables_schema_editor.setSchema(
            self.__ui.imp_tables.tables_schema_page.getEditTableButtonClicked()
            .getSchema())

        # Update Editor
        self.__ui.imp_tables.tables_schema_editor.updateEditor()

        # Block 'add tables'
        self.tables__enable_section_tables_import(False)

        # Go to editor
        self.__ui.imp_tables.table_stacked_layout.setCurrentIndex(1)

        # tables_schema_editor 'opacity-fade'
        self.animate_widget(
            widget=self.__ui.imp_tables.tables_schema_editor,
            animation_type='open-from-center')

    def tables__enable_section_tables_import(self, enable: bool) -> None:
        if enable:
            self.__ui.imp_tables.add_tables_page.setEnabled(True)
            self.__ui.imp_tables.xls_import_page.setEnabled(True)
            self.__ui.imp_tables.csv_import_page.setEnabled(True)
        else:
            self.__ui.imp_tables.add_tables_page.setEnabled(False)
            self.__ui.imp_tables.xls_import_page.setEnabled(False)
            self.__ui.imp_tables.csv_import_page.setEnabled(False)

    # ___ BG SETTINGS ___
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
            os.makedirs(
                os.path.join(self.__settings_path, 'tables-schema'))

        if not os.path.isfile(self.__settings_file):
            data_settings = {
                'platform': 'desktop',
                'dialog-path': self.__home_path,
                'settings-path': self.__settings_path,
                'tables-schema-path': os.path.join(
                    self.__settings_path, 'tables-schema'),
                'tables-schema-filenames': [],
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

    # ___ ANIMATIONS ___
    def animate_widget(
            self,
            widget,
            animation_type='slide-to-left',
            animation_duration=200):

        if animation_type == 'slide-to-left':
            self.__anim_group = QtCore.QSequentialAnimationGroup()
            anim_p = QtCore.QPropertyAnimation(widget, b"pos")
            anim_p.setStartValue(QtCore.QPoint(widget.width(), widget.y()))
            anim_p.setEndValue(QtCore.QPoint(widget.x(), widget.y()))
            anim_p.setDuration(animation_duration)
            self.__anim_group.addAnimation(anim_p)

        elif animation_type == 'slide-to-right':
            self.__anim_group = QtCore.QSequentialAnimationGroup()
            anim_p = QtCore.QPropertyAnimation(widget, b"pos")
            anim_p.setStartValue(
                QtCore.QPoint(-widget.width(), widget.y()))
            anim_p.setEndValue(QtCore.QPoint(widget.x(), widget.y()))
            anim_p.setDuration(animation_duration)
            self.__anim_group.addAnimation(anim_p)

        elif animation_type == 'slide-to-top':
            self.__anim_group = QtCore.QSequentialAnimationGroup()
            anim_p = QtCore.QPropertyAnimation(widget, b"pos")
            anim_p.setStartValue(
                QtCore.QPoint(widget.x(), widget.height()))
            anim_p.setEndValue(QtCore.QPoint(widget.x(), widget.y()))
            anim_p.setDuration(animation_duration)
            self.__anim_group.addAnimation(anim_p)

        elif animation_type == 'slide-to-bottom':
            self.__anim_group = QtCore.QSequentialAnimationGroup()
            anim_p = QtCore.QPropertyAnimation(widget, b"pos")
            anim_p.setStartValue(
                QtCore.QPoint(widget.x(), -widget.height()))
            anim_p.setEndValue(QtCore.QPoint(widget.x(), widget.y()))
            anim_p.setDuration(animation_duration)
            self.__anim_group.addAnimation(anim_p)

        elif animation_type == 'opacity-fade':
            self.__anim_group = QtCore.QSequentialAnimationGroup()
            effect = QtWidgets.QGraphicsOpacityEffect(widget)
            widget.setGraphicsEffect(effect)
            anim_o = QtCore.QPropertyAnimation(effect, b"opacity")
            anim_o.setStartValue(0)
            anim_o.setEndValue(1)
            anim_o.setDuration(animation_duration * 2)
            self.__anim_group.addAnimation(anim_o)

        elif animation_type == 'open-from-center':
            self.__anim_group = QtCore.QParallelAnimationGroup()

            # Center to top left
            anim_p = QtCore.QPropertyAnimation(widget, b"pos")
            anim_p.setStartValue(QtCore.QPoint(
                int(widget.width() / 2), int(widget.height() / 2)))
            anim_p.setEndValue(QtCore.QPoint(widget.x(), widget.y()))
            anim_p.setDuration(animation_duration)
            self.__anim_group.addAnimation(anim_p)

            # Animation - size (min to max)
            anim_s = QtCore.QPropertyAnimation(widget, b"size")
            h = widget.height()
            w = widget.width()
            widget.resize(100, 100)
            anim_s.setEndValue(QtCore.QSize(w, h))
            anim_s.setDuration(animation_duration)
            self.__anim_group.addAnimation(anim_s)

        self.__anim_group.start()


if __name__ == '__main__':
    app = Application()
    app.main()
