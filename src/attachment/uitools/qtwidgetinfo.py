#!/usr/bin env python3
import math

from PySide6 import QtWidgets, QtGui

def widget_is_dark(widget: QtWidgets.QWidget) -> bool:
    color = widget.palette().color(QtGui.QPalette.Window)
    r, g, b = (color.red(), color.green(), color.blue())
    hsp = math.sqrt(0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b))

    # 'light'
    if (hsp > 127.5):
        return False
    
    # 'dark'
    return True    
