#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets

from attachment.uiwidgets.widgetgetfilename import WidgetGetFilename
import attachment.uitools.qticons as qticons


class SectionImportTables(QtWidgets.QWidget):
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
        self.layout.setAlignment(QtCore.Qt.AlignTop)  # type: ignore
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
        self.tables_page_layout.setAlignment(
            QtCore.Qt.AlignTop)  # type: ignore
        self.tables_page.setLayout(self.tables_page_layout)

        self.add_tables = QtWidgets.QHBoxLayout()
        self.add_tables.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
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
        self.xls_import_layout.setAlignment(QtCore.Qt.AlignTop)  # type: ignore
        self.xls_import_page.setLayout(self.xls_import_layout)
        
        lbl = QtWidgets.QLabel('XLSX page')
        self.xls_import_layout.addWidget(lbl)

        self.xls_get_filename = WidgetGetFilename(
            description_text='Selecione o arquivo XLSX',
            text_width=200,
            button_icon=self.icon_document_open,
            button_text='Selecionar',
            clear_icon=self.icon_edit_clear,
            dialog_title='Selecione o arquivo XLSX',
            dialog_filter_description='Arquivos XLSX',
            dialog_filter_extensions=['xlsx'],
            # dialog_path is auto (os.environ)
        )
        self.xls_import_layout.addWidget(self.xls_get_filename)

        self.xls_process_button = QtWidgets.QPushButton('Processar')
        self.xls_import_layout.addWidget(self.xls_process_button)

        # ___ CSV page ___
        self.csv_import_page = QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.csv_import_page)

        self.csv_import_layout = QtWidgets.QVBoxLayout()
        self.csv_import_layout.setAlignment(QtCore.Qt.AlignTop)  # type: ignore
        self.csv_import_page.setLayout(self.csv_import_layout)

        # CSV numbers title
        self.csv_page_title_filename = QtWidgets.QLabel()
        self.csv_page_title_filename.setEnabled(False)
        self.csv_import_layout.addWidget(self.csv_page_title_filename)

        self.csv_page_title = QtWidgets.QLabel()
        self.csv_import_layout.addWidget(self.csv_page_title)

        self.csv_get_filename = WidgetGetFilename(
            description_text='Arquivos CSV',
            # text_width=200,
            button_icon=self.icon_document_open,
            button_text='Selecionar',
            clear_icon=self.icon_edit_clear,
            dialog_title='Selecionar os arquivos CSV',
            dialog_filter_description='Arquivos CSV',
            dialog_filter_extensions=['csv'],
            select_multiple=True
            # dialog_path is auto (os.environ)
            )
        self.csv_get_filename.setContentsMargins(10, 0, 0, 10)
        self.csv_import_layout.addWidget(self.csv_get_filename)

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
