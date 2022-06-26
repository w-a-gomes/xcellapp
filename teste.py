#!/usr/bin/env python3
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        # value = self._data[index.row()][index.column()]
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, str):
                if 'field: ' in value:
                    return value.replace('field: ', '')

                return value
            return value

        if role == Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int):
                return QtGui.QColor('purple')
            if isinstance(value, float):
                return QtGui.QColor('blue')
            return value

        if role == Qt.BackgroundRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, str):
                if 'field: ' in value:
                    return QtGui.QColor('blue')
            return value

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        data = [
          ['field: lol', 'field: lal', 'field: lil'],
          [111.11, 0, 0],
          [3.0, 5, 0],
          [3.55, 3, 2],
          [7.2, 8, 9],
        ]
        # self.model = QtCore.QAbstractTableModel(data)
        self.model = TableModel(data)

        self.table = QtWidgets.QTableView()
        self.table.horizontalHeader().setVisible(False)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec() 
