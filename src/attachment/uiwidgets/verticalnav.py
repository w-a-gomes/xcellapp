#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui


class NavButton(QtWidgets.QPushButton):
    """..."""
    def __init__(
            self,
            button_index: int = None,
            submenu_index: int = None,
            exec_func: callable = None,
            *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # Set
        self.setFlat(True)

        # Prop
        self.button_index = button_index
        self.submenu_index = submenu_index
        self.exec_func = exec_func

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


class VerticalNav(QtWidgets.QWidget):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.buttons_schema = [
            {
                'index': 0,
                'submenu-index': 0,
                'text': 'button 0',
                'icon': None,
                'exec': None,
            },
            {
                'index': 1,
                'submenu-index': 0,
                'text': 'button 1',
                'icon': None,
                'exec': None,
            },
            {
                'index': 1,
                'submenu-index': 1,
                'text': 'sub button 1',
                'icon': None,
                'exec': None,
            },
            {
                'index': 1,
                'submenu-index': 2,
                'text': 'sub button 2',
                'icon': None,
                'exec': None,
            },
            {
                'index': 2,
                'submenu-index': 0,
                'text': 'button 2',
                'icon': None,
                'exec': None,
            },
        ]
        
        self.all_buttons = []

        for btn_schm in self.buttons_schema:
            self.nav_button = NavButton(
                text=btn_schm['text'],
                button_index=btn_schm['index'],
                submenu_index=btn_schm['submenu-index'],
                exec_func=btn_schm['exec'],
            )
            self.nav_button.clicked.connect(self.on_exec_func)
            self.layout.addWidget(self.nav_button)

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
    
    @QtCore.Slot()
    def on_exec_funcx(self):
        # Click Style
        if self.sender().marked_state:
            # Visibility off
            if self.sender().submenu_index == 0:
                for item_button in self.all_buttons:
                    if (
                        item_button['schema']['submenu-index'] != 0 and
                        item_button['schema']['index'] == self.sender().button_index
                    ):
                        item_button['widget'].setVisible(False)
            # Desmarca
            self.sender().marked_state = False
            
        else:
            # Visibility on
            if self.sender().submenu_index == 0:
                for item_button in self.all_buttons:
                    if item_button['schema']['submenu-index'] != 0:
                        if item_button['schema']['index'] == self.sender().button_index:
                            item_button['widget'].setVisible(True)
            
            # Desmarcar
            for item_button in self.all_buttons:
                item_button['widget'].marked_state = False
                item_button['widget'].set_keep_ctive_state(False)
            
            # Marca
            self.sender().marked_state = True
            self.sender().set_keep_ctive_state(True)
