#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets

from attachment.uiwidgets.widgetgetfilename import WidgetGetFilename
from attachment.uisections.sectiontablespreview import SectionTablesPreview
from attachment.uisections.sectiontableseditor import SectionTablesEditor
import attachment.uitools.qticons as qticons


class SectionTablesImport(QtWidgets.QWidget):
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
        self.setLayout(self.layout)

        # ___ Stacked layout ___
        self.stacked_layout = QtWidgets.QStackedLayout()
        self.stacked_layout.setContentsMargins(0, 0, 0, 0)
        self.stacked_layout.setSpacing(0)
        self.stacked_layout.setAlignment(QtCore.Qt.AlignTop)  # type: ignore
        self.layout.addLayout(self.stacked_layout, 1)

        # ___ Add tables ___
        self.add_tables_page = QtWidgets.QWidget()
        # self.add_tables_page.setContentsMargins(18, 0, 18, 0)
        self.stacked_layout.addWidget(self.add_tables_page)

        self.add_tables_layout = QtWidgets.QVBoxLayout()
        self.add_tables_layout.setContentsMargins(0, 0, 0, 0)
        self.add_tables_page.setLayout(self.add_tables_layout)

        self.add_tables_h_layout = QtWidgets.QHBoxLayout()
        self.add_tables_h_layout.setAlignment(
            QtCore.Qt.AlignCenter)  # type: ignore
        self.add_tables_layout.addLayout(self.add_tables_h_layout)
        self.add_tables_label = QtWidgets.QLabel(text='Adicionar tabelas')
        self.add_tables_h_layout.addWidget(self.add_tables_label)
        self.add_tables_button = QtWidgets.QPushButton(icon=self.icon_list_add)
        self.add_tables_h_layout.addWidget(self.add_tables_button)

        # ___ XLSX page ___
        self.xls_import_page = QtWidgets.QWidget()
        self.xls_import_page.setContentsMargins(18, 0, 18, 0)
        self.stacked_layout.addWidget(self.xls_import_page)

        self.xls_import_layout = QtWidgets.QVBoxLayout()
        self.xls_import_layout.setAlignment(QtCore.Qt.AlignTop)  # type: ignore
        self.xls_import_layout.setContentsMargins(0, 0, 0, 0)
        self.xls_import_page.setLayout(self.xls_import_layout)
        
        self.xls_import_title = QtWidgets.QLabel(
            'Importar as tabela apartir de um arquivo do Microsoft Excel')
        self.xls_import_title.setAlignment(
            QtCore.Qt.AlignCenter)  # type: ignore
        # self.xls_import_title.setContentsMargins(0, 0, 0, 0)
        self.xls_import_layout.addWidget(self.xls_import_title)

        self.xls_get_filename = WidgetGetFilename(
            description_text='Arquivo XLSX',
            # text_width=200,
            button_icon=self.icon_document_open,
            button_text='Selecionar',
            clear_icon=self.icon_edit_clear,
            dialog_title='Selecione o arquivo XLSX',
            dialog_filter_description='Arquivos XLSX',
            dialog_filter_extensions=['xlsx'],
            # dialog_path is auto (os.environ)
        )
        # self.xls_get_filename.setContentsMargins(0, 0, 0, 0)
        self.xls_import_layout.addWidget(self.xls_get_filename)

        self.xls_action_buttons_layout = QtWidgets.QHBoxLayout()
        self.xls_action_buttons_layout.setAlignment(
            QtCore.Qt.AlignRight)  # type: ignore
        self.xls_import_layout.addLayout(self.xls_action_buttons_layout)

        self.xls_import_button = QtWidgets.QPushButton('Importar')
        # self.xls_import_button.setFixedWidth(200)
        self.xls_action_buttons_layout.addWidget(self.xls_import_button)

        # ___ CSV page ___
        self.csv_import_page = QtWidgets.QWidget()
        self.csv_import_page.setContentsMargins(18, 0, 18, 0)
        self.stacked_layout.addWidget(self.csv_import_page)

        self.csv_import_layout = QtWidgets.QVBoxLayout()
        self.csv_import_layout.setAlignment(QtCore.Qt.AlignTop)  # type: ignore
        self.csv_import_layout.setContentsMargins(0, 0, 0, 0)
        self.csv_import_page.setLayout(self.csv_import_layout)

        self.csv_page_title = QtWidgets.QLabel()
        self.csv_page_title.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        self.csv_import_layout.addWidget(self.csv_page_title)

        self.csv_get_filename = WidgetGetFilename(
            description_text='Arquivo CSV',
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

        self.csv_action_buttons_layout = QtWidgets.QHBoxLayout()
        self.csv_action_buttons_layout.setAlignment(
            QtCore.Qt.AlignRight)  # type: ignore
        self.csv_import_layout.addLayout(self.csv_action_buttons_layout)

        self.csv_import_button = QtWidgets.QPushButton('Importar')
        # self.csv_import_button.setContentsMargins(0, 0, 0, 0)
        # self.csv_import_button.setFixedWidth(200)
        self.csv_action_buttons_layout.addWidget(self.csv_import_button)

        # ___ Tables ___
        # Stack
        self.table_stacked_layout = QtWidgets.QStackedLayout()
        self.table_stacked_layout.setContentsMargins(0, 0, 0, 0)
        self.table_stacked_layout.setSpacing(0)
        # self.table_stacked_layout.setAlignment(
        #    QtCore.Qt.AlignTop)  # type: ignore
        self.layout.addLayout(self.table_stacked_layout, 9)

        # The tables
        self.tables_schema_page = SectionTablesPreview(self)
        self.tables_schema_page.setContentsMargins(0, 0, 0, 0)
        # self.layout.addWidget(self.tables_schema_page, 9)
        self.table_stacked_layout.addWidget(self.tables_schema_page)

        # The tables editor
        self.tables_schema_editor = SectionTablesEditor()
        self.tables_schema_editor.setContentsMargins(0, 0, 0, 0)
        self.table_stacked_layout.addWidget(self.tables_schema_editor)
