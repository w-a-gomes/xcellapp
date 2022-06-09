#!/usr/bin env python3
import math
import os
import sys

from PySide6 import QtWidgets, QtGui


class QtGuiIcon(object):
    def __init__(self):
        self.icons_path = self.__icons_path()
    
    def __icons_path(self):
        dir_prefix = ''
        if self.__widget_is_dark():
            dir_prefix = 'symbolic-'
        
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), f'{dir_prefix}icons')
    
    @staticmethod
    def __widget_is_dark() -> bool:
        widget = QtWidgets.QWidget()
        color = widget.palette().color(QtGui.QPalette.Window)
        r, g, b = (color.red(), color.green(), color.blue())
        hsp = math.sqrt(0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b))

        # 'light'
        if (hsp > 127.5):
            return False
        
        # 'dark'
        return True

    def fromSystem(self, icon_name: str) -> QtGui.QIcon:
        # Window and Mac
        if sys.platform != 'linux':
            return QtGui.QIcon(
                QtGui.QPixmap(
                    os.path.join(self.icons_path, icon_name + '.svg')))
        # Linux
        else:
            return QtGui.QIcon.fromTheme(icon_name)
    
    def fromPath(self, icon_path: str) -> QtGui.QIcon:
        return QtGui.QIcon(QtGui.QPixmap(icon_path))
