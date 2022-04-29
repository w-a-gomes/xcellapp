#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui


class NavigationButton(QtWidgets.QPushButton):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)

        self.__leave_state = False
        self.__state = 'hover'

        self.__new_palette = self.palette()
        self.__active_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Highlight))
        
        self.__hover_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Button))
        
        self.__new_palette.setColor(
            QtGui.QPalette.Button, self.__hover_color)
        
        self.setStyleSheet('text-align:left;')
    
    def setStateColor(self, state: str) -> None:
        if state == 'active':
            self.__state = 'active'
            self.__new_palette.setColor(
                QtGui.QPalette.Button, self.__active_color)
        else:
            self.__state = 'hover'
            self.__new_palette.setColor(
            QtGui.QPalette.Button, self.__hover_color)

    def enterEvent(self, event) -> None:
        """..."""
        self.setPalette(self.__new_palette)
        self.setAutoFillBackground(True)

    def leaveEvent(self, event) -> None:
        """..."""
        self.setAutoFillBackground(self.__leave_state)
    
    def setKeepEnterEvent(self, state: bool) -> None:
        self.__leave_state = state
        
        if self.__leave_state:
            self.setStateColor('active')
        else:
            self.setStateColor('hover')

        self.setPalette(self.__new_palette)

        self.setAutoFillBackground(self.__leave_state)


if __name__ == '__main__':
    pass
