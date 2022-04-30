#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui


class NavButton(QtWidgets.QPushButton):
    """..."""
    def __init__(
            self, button_index: int = None, submenu_index: int = None,
            *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # Set
        self.setFlat(True)

        # Prop
        self.button_index = button_index
        self.submenu_index = submenu_index

        # Flags
        self.marked_state = False
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
        
        self.setStyleSheet('text-align: left;')

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


class SubNavButton(NavButton):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)

        self.new_palette = self.palette()
        self.active_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Mid))
        
        self.hover_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Button))
        
        self.new_palette.setColor(
            QtGui.QPalette.Button, self.hover_color)


class VerticalNav(QtWidgets.QWidget):
    """..."""
    def __init__(self, buttons_schema, *args, **kwargs):
        """
        buttons_schema example:

        ---  0, 0
        ---  1, 0
         ___ 1, 1
         ___ 1, 2
        ___  2, 0
        
        [
            {
                'index': 0,
                'submenu-index': 0,
                'text': 'button 0',
            },
            {
                'index': 1,
                'submenu-index': 0,
                'text': 'button 1',
            },
            {
                'index': 1,
                'submenu-index': 1,
                'text': 'sub button 1',
            },
            {
                'index': 1,
                'submenu-index': 2,
                'text': 'sub button 2',
            },
            {
                'index': 2,
                'submenu-index': 0,
                'text': 'button 2',
            },
        ]
        """
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.buttons_schema = buttons_schema
        self.all_buttons = []

        for btn_schm in self.buttons_schema:
            if btn_schm['submenu-index'] != 0:
                self.nav_button = SubNavButton(
                    text=btn_schm['text'],
                    button_index=btn_schm['index'],
                    submenu_index=btn_schm['submenu-index'])
                layout = QtWidgets.QHBoxLayout()
                layout.setContentsMargins(20, 1, 3, 0)
                self.layout.addLayout(layout) 
                layout.addWidget(self.nav_button, 8)
            else:
                self.nav_button = NavButton(
                    text=btn_schm['text'],
                    button_index=btn_schm['index'],
                    submenu_index=btn_schm['submenu-index'])
                self.layout.addWidget(self.nav_button)
            
            self.nav_button.clicked.connect(self.on_exec_func)
            self.all_buttons.append(
                {'widget': self.nav_button, 'schema': btn_schm}
            )

            if btn_schm['submenu-index'] != 0:
                self.nav_button.setVisible(False)
    
    @QtCore.Slot()
    def on_exec_func(self):
        # Click/Marked
        if self.sender().marked_state:
            # Visibility off
            if self.sender().submenu_index == 0:
                for item_button in self.all_buttons:
                    if (
                        item_button['schema']['submenu-index'] != 0 and
                        item_button['schema']['index'] == self.sender().button_index
                    ):
                        item_button['widget'].setVisible(False)
            # Unmark
            self.sender().marked_state = False
        
        # "Unclick"/"Unmark"
        else:
            # Visibility on
            if self.sender().submenu_index == 0:
                for item_button in self.all_buttons:
                    if item_button['schema']['submenu-index'] != 0:
                        if item_button['schema']['index'] == self.sender().button_index:
                            item_button['widget'].setVisible(True)
            
            # Unmark
            for item_button in self.all_buttons:
                item_button['widget'].marked_state = False
                item_button['widget'].set_keep_ctive_state(False)
            
            # Mark/click
            self.sender().marked_state = True
            self.sender().set_keep_ctive_state(True)

            if self.sender().submenu_index != 0:
                for item_button in self.all_buttons:
                    # Mark parent
                    if (
                        item_button['schema']['index'] == self.sender().button_index
                        and item_button['schema']['submenu-index'] == 0
                    ):
                        item_button['widget'].marked_state = True
                        item_button['widget'].set_keep_ctive_state(True)

    def get_button_by_index(self, index, submenu_index):
        """..."""
        for item_button in self.all_buttons:
            if (
                item_button['schema']['index'] == index
                and item_button['schema']['submenu-index'] == submenu_index
            ):
                return item_button['widget']
