#!/usr/bin env python3
import json
import math
import os
import pathlib
import sys

from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uiwidgets.elidedlabel import ElidedLabel
from attachment.uiwidgets.importfile import ImportFile
import attachment.uitools.qticons as qticons


class ImportTables(QtWidgets.QWidget):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # ___ Properties ___
        self.filename = None
        self.header = None
        self.label_size = 100
        self.desktop_margin = (100, 150)

        # ___ Icons ___
        self.icons = qticons.QtGuiIcon()
        
        self.icon_list_add = self.icons.fromSystem('list-add')
        self.icon_edit_clear = self.icons.fromSystem('edit-clear')
        self.icon_folder_open = self.icons.fromSystem('document-open-folder')
        self.icon_document_open = self.icons.fromSystem('document-open')

        # ___ Container ___
        # Top level layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.layout)

        # ___ Stacked layout ___
        # A importação será visualizada em slides de um QStackedLayout
        # Cada slide/page é um widget com um layout para as visualizações
        self.stacked_layout = QtWidgets.QStackedLayout()
        self.stacked_layout.setContentsMargins(0, 0, 0, 0)
        self.stacked_layout.setSpacing(0)
        self.layout.addLayout(self.stacked_layout)

        # ___ Tables page ___
        self.tables_page = QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.tables_page)

        self.tables_page_layout = QtWidgets.QVBoxLayout()
        self.tables_page_layout.setAlignment(QtCore.Qt.AlignTop)
        self.tables_page.setLayout(self.tables_page_layout)

        self.add_tables = QtWidgets.QHBoxLayout()
        self.add_tables.setAlignment(QtCore.Qt.AlignCenter)
        self.tables_page_layout.addLayout(self.add_tables)
        self.add_tables_label = QtWidgets.QLabel(text='Adicionar tabelas')
        self.add_tables.addWidget(self.add_tables_label)
        self.add_tables_button = QtWidgets.QPushButton(icon=self.icon_list_add)
        self.add_tables.addWidget(self.add_tables_button)


        for i in range(10):
            lbl = QtWidgets.QLabel(f'{i}')
            self.tables_page_layout.addWidget(lbl)

        # ___ XLSX page ___
        self.xls_import_page = QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.xls_import_page)

        self.xls_import_layout = QtWidgets.QVBoxLayout()
        self.xls_import_layout.setAlignment(QtCore.Qt.AlignTop)
        self.xls_import_page.setLayout(self.xls_import_layout)
        
        lbl = QtWidgets.QLabel('XLSX page')
        self.xls_import_layout.addWidget(lbl)

        # ___ CSV page ___
        self.csv_import_page = QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.csv_import_page)

        self.csv_import_layout = QtWidgets.QVBoxLayout()
        self.csv_import_layout.setAlignment(QtCore.Qt.AlignTop)
        self.csv_import_page.setLayout(self.csv_import_layout)
        
        lbl = QtWidgets.QLabel('CSV page')
        self.csv_import_layout.addWidget(lbl)

        self.import_xls_file = ImportFile(
            text='Selecione o arquivo CSV', 
            text_width=200,
            button_icon=self.icon_document_open,
            button_text='Selecionar',
            clear_icon=self.icon_edit_clear,
            )
        self.csv_import_layout.addWidget(self.import_xls_file)
        
        # self.filename_page_layout = QtWidgets.QWidget()
        # self.stacked_layout.addWidget(self.filename_page_layout)

        # self.filename_layout = QtWidgets.QHBoxLayout()
        # self.filename_page_layout.setLayout(self.filename_layout)

        # self.filename_label = WidgetElidedLabel(
        #     text='Arquivo do Excell', elide_side='right')
        # self.filename_label.setFixedWidth(self.label_size)
        # self.filename_label.setEnabled(False)
        # self.filename_label.setAlignment(
        #     QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        # self.filename_layout.addWidget(
        #     self.filename_label, 0, QtCore.Qt.AlignLeft)

        # self.filename_button = QtWidgets.QPushButton(text='Selecionar')
        # self.filename_button.setIcon(self.icon_document_open)
        # self.filename_layout.addWidget(
        #     self.filename_button, 0, QtCore.Qt.AlignLeft)

        # self.filename_url_label = WidgetElidedLabel(elide_side='middle')
        # self.filename_url_label.setFixedWidth(250)
        # self.filename_layout.addWidget(
        #     self.filename_url_label, 1, QtCore.Qt.AlignLeft)

        # self.filename_clear_button = QtWidgets.QPushButton()
        # self.filename_clear_button.setIcon(self.icon_erase)
        # self.filename_clear_button.setToolTip('Limpar o nome do arquivo')
        # self.filename_clear_button.setFlat(True)
        # self.filename_clear_button.setVisible(False)
        # self.filename_layout.addWidget(
        #     self.filename_clear_button, 0, QtCore.Qt.AlignRight)

        # # Process
        # self.process_page_layout = QtWidgets.QWidget()
        # self.stacked_layout.addWidget(self.process_page_layout)

        # self.process_layout = QtWidgets.QHBoxLayout()
        # self.process_page_layout.setLayout(self.process_layout)

        # self.pixmapi_process_button = getattr(
        #     QtWidgets.QStyle, 'SP_BrowserReload')
        # self.icon_process_button = self.style().standardIcon(
        #     self.pixmapi_process_button)

        # self.process_button = QtWidgets.QPushButton(text='Procesar')
        # self.process_button.setIcon(self.icon_process_button)
        # self.process_layout.addWidget(
        #     self.process_button, 0, QtCore.Qt.AlignRight)
