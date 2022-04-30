#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui


class NavButton(QtWidgets.QPushButton):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.setFlat(True)

        self.marked = False
        self.leave_state = False
        self.state = 'hover'

        self.new_palette = self.palette()
        self.active_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Highlight))
        
        self.hover_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Button))
        
        self.new_palette.setColor(
            QtGui.QPalette.Button, self.hover_color)
        
        self.setStyleSheet('text-align:left;')

    def enterEvent(self, event) -> None:
        """..."""
        self.setPalette(self.new_palette)
        self.setAutoFillBackground(True)

    def leaveEvent(self, event) -> None:
        """..."""
        self.setAutoFillBackground(self.leave_state)
    
    def set_state_color(self, state: str) -> None:
        """..."""
        if state == 'active':
            self.state = 'active'
            self.new_palette.setColor(
                QtGui.QPalette.Button, self.active_color)
        else:
            self.state = 'hover'
            self.new_palette.setColor(
            QtGui.QPalette.Button, self.hover_color)
    
    def set_keep_ctive_state(self, state: bool) -> None:
        """..."""
        self.leave_state = state
        
        if self.leave_state:
            self.set_state_color('active')
        else:
            self.set_state_color('hover')

        self.setPalette(self.new_palette)

        self.setAutoFillBackground(self.leave_state)


class SubNavButton(QtWidgets.QPushButton):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.setFlat(True)

        self.marked = False
        self.leave_state = False
        self.state = 'hover'

        self.new_palette = self.palette()
        self.active_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Dark))
        
        self.hover_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Button))
        
        self.new_palette.setColor(
            QtGui.QPalette.Button, self.hover_color)
        
        self.setStyleSheet('text-align:left;')

    def enterEvent(self, event) -> None:
        """..."""
        self.setPalette(self.new_palette)
        self.setAutoFillBackground(True)

    def leaveEvent(self, event) -> None:
        """..."""
        self.setAutoFillBackground(self.leave_state)
    
    def set_state_color(self, state: str) -> None:
        """..."""
        if state == 'active':
            self.state = 'active'
            self.new_palette.setColor(
                QtGui.QPalette.Button, self.active_color)
        else:
            self.state = 'hover'
            self.new_palette.setColor(
            QtGui.QPalette.Button, self.hover_color)
    
    def set_keep_ctive_state(self, state: bool) -> None:
        """..."""
        self.leave_state = state
        
        if self.leave_state:
            self.set_state_color('active')
        else:
            self.set_state_color('hover')

        self.setPalette(self.new_palette)

        self.setAutoFillBackground(self.leave_state)

if __name__ == '__main__':
    pass
