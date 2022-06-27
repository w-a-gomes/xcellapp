#!/usr/bin env python3
from PySide6 import QtWidgets, QtGui, QtCore


# noinspection PyPep8Naming
class SectionTablesEditor(QtWidgets.QFrame):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # Args
        self.__table_schema = None

        # Frame border
        # self.setFrameStyle(
        #     QtWidgets.QFrame.StyledPanel |  # type: ignore
        #     QtWidgets.QFrame.Plain)

        # Background color
        # self.background_color = QtGui.QColor(
        #     QtGui.QPalette().color(
        #         # ToolTipBase: Light
        #         # Button: Light
        #         # Window: Normal
        #         # AlternateBase: Dark
        #         QtGui.QPalette.Active, QtGui.QPalette.AlternateBase))
        #
        # self.color_palette = self.palette()
        # self.color_palette.setColor(
        #     QtGui.QPalette.Window, self.background_color)
        #
        # self.setAutoFillBackground(True)
        # self.setPalette(self.color_palette)

        # ___ Container ___
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Table
        self.table = QtWidgets.QTableView()
        # self.table.horizontalHeader().setVisible(False)
        self.layout.addWidget(self.table)

    def setSchema(self, schema):
        self.__table_schema = schema

    def __data_model(self):
        datas = [self.__table_schema['table-header']]
        for row in self.__table_schema['table-data']:
            data_item = []
            for item in row:
                data_item.append(item['value'])
            datas.append(data_item)

        return datas

    def updateEditor(self):
        """
        self.__table_schema =
        {
            'table-name': 'cadastro.csv',
            'edited': False,
            'edited-date': None,
            'table-header: ['first', 'last']
            'table-header-index: 3'
            'table-data': [
                [
                    (col-name, col-index, row-index, data, value, value-type),
                    ('Café',   0,         0,        '1,9', 1.90, 'float'),
                ],
                [
                    ('code', 1, 0, '8,00', 8.0, 'float'),
                    ('mouse', 1, 1, '30,00', 30.0, 'float'),
                ]
            ]
        }
        """
        model = TableModel(self.__data_model())

        self.table.setModel(model)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

        if role == QtCore.Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int):
                return QtGui.QColor('#00557f')

            if isinstance(value, float):
                return QtGui.QColor('#aa557f')

            if isinstance(value, bool):
                return QtGui.QColor('#ffaf3e')

            return value

        if role == QtCore.Qt.BackgroundRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, str):
                if 'field: ' in value:
                    return QtGui.QColor('blue')

            return value

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self._data[0])

# def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
#     # section, orientation[, role=Qt.DisplayRole
#     # section is the index of the column/row.
#     if role == QtCore.Qt.DisplayRole:
#         if orientation == QtCore.Qt.Horizontal:
#             return str(self._data.columns[section])
#
#         if orientation == QtCore.Qt.Vertical:
#             return str(self._data.index[section])
