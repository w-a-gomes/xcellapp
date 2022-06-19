#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets

from attachment.uiwidgets.widgetverticalmenu import WidgetVerticalMenu
# from attachment.uiwidgets.icons import Icons


class SectionVerticalMenu(QtWidgets.QWidget):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # ___ Container ___
        # Top level layout
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        # Nav layout
        """
        self.nav_scroll = QtWidgets.QScrollArea()
        self.nav_scroll.setFixedHeight(500)
        self.nav_scroll.setFixedWidth(200)
        self.nav_scroll.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.nav_scroll.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.nav_scroll.setWidgetResizable(True)
        self.layout.addWidget(
            self.nav_scroll, 2, QtCore.Qt.AlignTop)
        """
        # Navigation menu buttons
        self.vertical_nav = WidgetVerticalMenu([
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
                    {'id': 'cfg_imp_tabelas', 'text': 'Tabelas'},
                    {'id': 'cfg_db', 'text': 'Bancos de dados'},
                ]
            },
            {
                'id': 'about', 'text': 'Sobre',
            },
        ])
        """
        # self.vertical_nav.setFixedHeight(self.vertical_nav.expanded_height())
        self.nav_scroll.setWidget(self.vertical_nav)
        """
        self.layout.addWidget(
           self.vertical_nav, 0, QtCore.Qt.AlignTop)  # type: ignore


if __name__ == '__main__':
    pass
