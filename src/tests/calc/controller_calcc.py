#!/usr/bin env python3
from model import Model
from view import View


class Controller(object):
    def __init__(self):
        self.__view = View(self)
        self.__model = Model()
    
    def main(self):
        self.__view.main()
    
    def on_button_click(self, caption):
        result = self.__model.calculate(caption)
        self.__view.value_var.set(result)


if __name__ == '__main__':
    app = Controller()
    app.main()
