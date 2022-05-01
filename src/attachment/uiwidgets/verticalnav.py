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
        
        self.setStyleSheet(
            'text-align: left;'
            'padding-right: 25px;'
            'border-radius: 5px;')

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
    
    def set_active_color_unfocused(self, state: bool) -> None:
        if state:
            self.active_color = QtGui.QColor(
                QtGui.QPalette().color(
                    QtGui.QPalette.Active, QtGui.QPalette.Midlight))
        else:
            self.active_color = QtGui.QColor(
                QtGui.QPalette().color(
                    QtGui.QPalette.Active, QtGui.QPalette.Highlight))
    
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
        self.marked_state = False
        self.leave_state = False
        self.state = 'hover'

        # Layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.buttons_schema = buttons_schema
        self.all_buttons = []

        for btn_schm in self.buttons_schema:
            # SubNavButton example
            # if btn_schm['submenu-index'] != 0: SubNavButton else NavButton
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
        self.sender().set_active_color_unfocused(False)
        self.sender().set_keep_ctive_state(True)

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
                self.anim_group = QtCore.QParallelAnimationGroup()
                
                for item_button in self.all_buttons:
                    if item_button['schema']['submenu-index'] != 0:
                        if item_button['schema']['index'] == self.sender().button_index:
                            item_button['widget'].setVisible(True)

                            # Animate fade
                            effect = QtWidgets.QGraphicsOpacityEffect(item_button['widget'])
                            item_button['widget'].setGraphicsEffect(effect)

                            anim = QtCore.QPropertyAnimation(effect, b"opacity")
                            anim.setStartValue(0)
                            anim.setEndValue(1)
                            anim.setDuration(300)
                            self.anim_group.addAnimation(anim)

                            # Animate position
                            anim_p = QtCore.QPropertyAnimation(item_button['widget'], b"pos")
                            anim_p.setEndValue(QtCore.QPoint(20, item_button['widget'].pos().y()))
                            anim_p.setDuration(100)
                            self.anim_group.addAnimation(anim_p)
                
                self.anim_group.start()
            
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
                        item_button['widget'].set_active_color_unfocused(True)
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


class NavButtonB(QtWidgets.QPushButton):
    """..."""
    def __init__(self, button_id, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # Flags
        self.is_checked = False
        self.is_active_state = False
        self.is_sub_layouts_active = False

        # Properties
        self.button_id = button_id
        self.sub_buttons_id = []
        self.sub_layout_id = None

        self.active_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Highlight))
        
        self.active_color_unfocused = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Midlight))
        
        self.hover_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Button))
        
        # Settings
        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Button, self.hover_color)
        
        self.setStyleSheet(
            'text-align: left;'
            'padding-right: 25px;'
            'border-radius: 5px;')

    def enterEvent(self, event) -> None:
        """..."""
        self.setAutoFillBackground(True)
        self.setPalette(self.color_palette)
        
    def leaveEvent(self, event) -> None:
        """..."""
        if not self.is_checked:
            self.setAutoFillBackground(False)
    
    def set_active_color(self) -> None:
        """..."""
        self.is_checked = True
        self.setAutoFillBackground(True)
        
        self.color_palette.setColor(
            QtGui.QPalette.Button, self.active_color)
        
        self.setPalette(self.color_palette)
        
    def unset_active_color(self) -> None:
        """..."""
        self.is_checked = False

        self.color_palette.setColor(
            QtGui.QPalette.Button, self.hover_color)

        self.setAutoFillBackground(False)


class SubLayoutWidget(QtWidgets.QWidget):
    """..."""
    def __init__(self, sub_layout_id: str = None, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)

        # Properties
        self.sub_layout_id = sub_layout_id
        self.all_items = []

        # Layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        # Style
        self.normal_color = QtGui.QColor(
            QtGui.QPalette().color(
                QtGui.QPalette.Active, QtGui.QPalette.Midlight))

        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Window, self.normal_color)
        
        self.setAutoFillBackground(True)
        self.setPalette(self.color_palette)

    def add_item(self, item):
        self.layout.addWidget(item)
    
    def set_visible(self, visible: bool):
        if self.all_items and visible:
            for item in self.all_items:
                item.setVisible(True)
        elif not visible and self.all_items:
            for item in self.all_items:
                item.setVisible(False)
    
    def get_item_by_id(self, item_id):
        if self.all_items:
            for item in self.all_items:
                if item.button_id == item_id:
                    return item


class VerticalNavB(QtWidgets.QWidget):
    """..."""
    def __init__(self, buttons_schema, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.buttons_schema = [
            {
                'id': 'inicio', 'text': 'Início'
            },
            {
                'id': 'config', 'text': 'Configurações', 'sub-buttons': [
                    {'id': 'icones', 'text': 'Ícones'},
                    {'id': 'csv', 'text': 'Importar CSV'},
                ]
            },
            {
                'id': 'penultimo', 'text': 'Penúltimo'
            },
            {
                'id': 'ultimo', 'text': 'Último', 'sub-buttons': [
                    {'id': 'test', 'text': 'Teste'},
                    {'id': 'testa', 'text': 'Testa'},
                ]
            },
            {
                'id': 'pan', 'text': 'Paann'
            },
        ]
        # Layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.all_top_buttons = []
        self.all_sub_buttons = []
        self.all_buttons = []
        self.all_sub_layouts = []

        for schema in self.buttons_schema:
            # Top Buttons
            button = NavButtonB(button_id=schema['id'])
            button.setCheckable(True)
            button.setFlat(True)
            button.clicked.connect(self.on_button_click)

            self.layout.addWidget(button)
            self.all_buttons.append(button)
            self.all_top_buttons.append(button)

            if 'text' in schema.keys():
                button.setText(schema['text'])
                
            if 'icon' in schema.keys():
                button.setIcon(schema['icon'])

            # Sub buttons
            if 'sub-buttons' in schema.keys():
                sub_layout = SubLayoutWidget(sub_layout_id=schema['id'])
                self.layout.addWidget(sub_layout)
                self.all_sub_layouts.append(sub_layout)

                for sub_schema in schema['sub-buttons']:
                    sub_button = NavButtonB(
                        button_id=sub_schema['id'], text=sub_schema['text'])
                    sub_button.setCheckable(True)
                    sub_button.setFlat(True)
                    sub_button.clicked.connect(self.on_sub_button_click)

                    sub_layout.add_item(sub_button)
                    self.all_buttons.append(sub_button)
                    self.all_sub_buttons.append(sub_button)
        
        for sub_layout in self.all_sub_layouts:
            sub_layout.setVisible(False)
    
    @QtCore.Slot()
    def on_button_click(self):
        # (Checked) -> Unchecked
        if self.sender().is_checked:
            self.sender().is_checked = False

            # Sub layout not visible
            for sub_layout in self.all_sub_layouts:
                if sub_layout.sub_layout_id == self.sender().button_id:
                    sub_layout.setVisible(False)
        
        # (Unchecked) -> Checked
        else:
            self.sender().set_active_color()

            # Unset Colors
            for button in self.all_buttons:
                if button.button_id != self.sender().button_id:
                    button.unset_active_color()

                    # Fix click
                    if button.is_sub_layouts_active:
                        button.is_checked = True
            
            # Sub layout visible
            for sub_layout in self.all_sub_layouts:
                if sub_layout.sub_layout_id == self.sender().button_id:
                    self.sender().is_sub_layouts_active =True
                    sub_layout.setVisible(True)
            
            for sub_layout in self.all_sub_layouts:
                if sub_layout.sub_layout_id == self.sender().button_id:
                    vertical_size = (
                        (len(sub_layout.all_items) * button.height())
                        + sub_layout.height()
                    )
                    self.anim_group = QtCore.QSequentialAnimationGroup()
                    anim = QtCore.QPropertyAnimation(sub_layout, b"size")
                    anim.setStartValue(QtCore.QSize(sub_layout.width(), 0))
                    anim.setEndValue(
                        QtCore.QSize(sub_layout.width(), vertical_size))
                    anim.setDuration(500)
                    self.anim_group.addAnimation(anim)
                    self.anim_group.start()
                    

    
    @QtCore.Slot()
    def on_sub_button_click(self):
        # (Checked) -> Unchecked
        if self.sender().is_checked:
            pass
        
        # (Unchecked) -> Checked
        else:
            self.sender().set_active_color()

            for button in self.all_buttons:
                if button.button_id != self.sender().button_id:
                    button.unset_active_color()
