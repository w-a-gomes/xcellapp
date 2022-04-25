#!/usr/bin env python3
import sys

from model import Model
from view import View
from PySide6 import QtCore, QtWidgets, QtGui


class Controller(object):
    def __init__(self):
        self.__app = QtWidgets.QApplication([])
        self.__view = View(self)
        self.__model = Model()
    
    def on_button_click(self, hello):
        # Get logics
        result = self.__model.calculate(hello=hello)

        # Set logic returns
        self.__view.text.setText(result)
    
    def on_button_close(self):
        self.__app.quit()
    
    def main(self):
        # self.__view.resize(800, 600)
        self.__view.show()
        sys.exit(self.__app.exec())


if __name__ == '__main__':
    app = Controller()
    app.main()

    
