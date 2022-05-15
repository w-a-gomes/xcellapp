#!/usr/bin env python3
import sys

from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uisections.sectionimptables import SectionImpTables
from attachment.uiwidgets.widgetverticalnav import WidgetVerticalNav
from attachment.uiwidgets.icons import Icons


class SectionNav(QtWidgets.QWidget):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # ___ Container ___
        # Top level layout
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setMinimumWidth(100)
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

        # Navigation menu buttons
        self.buttons_schema = [
            {
                'id': 'db', 'text': 'Banco de Dados', 'sub-buttons': [
                    {'id': 'db-insumos', 'text': 'Insumos'},
                    {'id': 'db-colaboradores', 'text': 'Colaboradores'},
                    {'id': 'db-relatorio', 'text': 'Relatório'},
                ]
            },
            {
                'id': 'fc', 'text': 'Formação Custo', 'sub-buttons': [
                    {'id': 'fc-custo_producao', 'text': 'Custo Produção'},
                    {'id': 'fc-resumo_producao', 'text': 'Resumo Produção'},
                    {'id': 'fc-relatorio', 'text': 'Relatório'},
                ]
            },
            {
                'id': 'mk', 'text': 'Markup', 'sub-buttons': [
                    {'id': 'mk-cadastro_markup', 'text': 'Cadastro Markup'},
                    {'id': 'mk-produtos_markup', 'text': 'Produtos Markup'},
                    {'id': 'mk-relatorio', 'text': 'Relatório'},
                ]
            },
            {
                'id': 'cpv', 'text': 'CPV', 'sub-buttons': [
                    {'id': 'cpv-producao', 'text': 'Produção'},
                    {'id': 'cpv-relatorio', 'text': 'Relatório'},
                ]
            },
            {
                'id': 'config', 'text': 'Configurações', 'sub-buttons': [
                    {'id': 'cfg_imp_tabelas', 'text': 'Importar tabelas'},
                    {'id': 'cfg_icones', 'text': 'Ícones'},
                    {'id': 'cfg_tabelas', 'text': 'Tabelas'},
                    {'id': 'cfg_db', 'text': 'Bancos de dados'},
                ]
            },
            {
                'id': 'about', 'text': 'Sobre',
            },
        ]
        
        self.vertical_nav = WidgetVerticalNav(self.buttons_schema)
        self.stack_nav_layout.addWidget(
            self.vertical_nav, 0, QtCore.Qt.AlignTop)
        
        # Stack pages
        
        # 0
        self.home_page = QtWidgets.QLabel(text='Página Inicial')
        self.stacked_layout.addWidget(self.home_page)
        
        # 1 xls
        self.imp_tables = SectionImpTables()
        self.stacked_layout.addWidget(self.imp_tables)

        # 2 Icons
        self.icons = Icons()
        self.stacked_layout.addWidget(self.icons)


if __name__ == '__main__':
    pass
