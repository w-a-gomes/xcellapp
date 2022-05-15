#!/usr/bin env python3
import os
import pathlib
import sys

from PySide6 import QtCore, QtWidgets, QtGui


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


class NavButton(QtWidgets.QPushButton):
    """..."""
    def __init__(self, button_id, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # Flags
        self.is_checked = False
        self.is_clicked = False
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
        
        self.setStyleSheet('text-align: left;')

    def enterEvent(self, event) -> None:
        """..."""
        self.setAutoFillBackground(True)
        self.setPalette(self.color_palette)
        
    def leaveEvent(self, event) -> None:
        """..."""
        if not self.is_clicked:
            self.setAutoFillBackground(False)
    
    def set_active_color(self) -> None:
        """..."""
        self.setAutoFillBackground(True)
        
        self.color_palette.setColor(
            QtGui.QPalette.Button, self.active_color)

        self.setPalette(self.color_palette)
    
    def set_active_color_for_unchecked_state(self) -> None:
        """..."""
        self.setAutoFillBackground(True)
        
        self.color_palette.setColor(
            QtGui.QPalette.Button, self.active_color)
        
        self.setPalette(self.color_palette)
        
    def unset_active_color(self) -> None:
        """..."""
        self.color_palette.setColor(
            QtGui.QPalette.Button, self.hover_color)

        self.setAutoFillBackground(False)


class WidgetVerticalNav(QtWidgets.QWidget):
    """..."""
    def __init__(self, buttons_schema, *args, **kwargs):
        """
        buttons_schema example:
        [
            {
                'id': 'inicio', 'text': 'Início'
            },
            {
                'id': 'config', 'text': 'Configurações', 'sub-buttons': [
                    {'id': 'icones', 'text': 'Ícones'},
                    {'id': 'csv', 'text': 'Importar CSV'},
                ]
            },
        ]
        """
        super().__init__(*args, **kwargs)
        self.setMinimumWidth(190)
        self.buttons_schema = buttons_schema

        # Icons
        self.icon_space = QtGui.QIcon(
            QtGui.QPixmap(
                os.path.join(pathlib.Path(__file__).resolve().parent,
                'icons', 'verticalnavspacing.svg')))

        if sys.platform != 'linux':
            self.icon_arrow_right = QtGui.QIcon(
                QtGui.QPixmap(
                    os.path.join(pathlib.Path(__file__).resolve().parent,
                    'icons', 'go-next.svg')))
            
            self.icon_arrow_down = QtGui.QIcon(
                QtGui.QPixmap(
                    os.path.join(pathlib.Path(__file__).resolve().parent,
                    'icons', 'go-down.svg')))
        else:
            self.icon_arrow_right = QtGui.QIcon.fromTheme('go-next')
            self.icon_arrow_down = QtGui.QIcon.fromTheme('go-down')
            
        # Layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.all_top_buttons = []
        self.all_sub_buttons = []
        self.all_buttons = []
        self.all_sub_layouts = []
        
        is_first_button = True
        for schema in self.buttons_schema:
            # Top Buttons
            button = NavButton(button_id=schema['id'])
            
            button.setIcon(self.icon_space)
            button.setFlat(True)
            button.clicked.connect(self.on_button_click)

            if is_first_button:
                is_first_button = False
            else:
                sep = QtWidgets.QFrame()
                sep.setObjectName('Separator')
                sep.setFrameShape(QtWidgets.QFrame.HLine)
                sep.setFrameShadow(QtWidgets.QFrame.Plain)
                sep.setLineWidth(1)
                self.layout.addWidget(sep)

            self.layout.addWidget(button)
            self.all_buttons.append(button)
            self.all_top_buttons.append(button)

            if 'text' in schema.keys():
                button.setText(schema["text"])
                
            if 'icon' in schema.keys():
                button.setIcon(schema['icon'])

            # Sub buttons
            if 'sub-buttons' in schema.keys():
                if 'text' in schema.keys():
                    button.setIcon(self.icon_arrow_right)
                    button.setText(schema["text"])

                sub_layout = SubLayoutWidget(sub_layout_id=schema['id'])
                sub_layout.setContentsMargins(15, 5, 5, 5)
                self.layout.addWidget(sub_layout)
                self.all_sub_layouts.append(sub_layout)

                for sub_schema in schema['sub-buttons']:
                    sub_button = NavButton(button_id=sub_schema['id'])
                    if 'text' in sub_schema.keys():
                        sub_button.setText('•   ' + sub_schema['text'])
                        
                    if 'icon' in sub_schema.keys():
                        sub_button.setIcon(sub_schema['icon'])
                    
                    sub_button.setFlat(True)
                    sub_button.clicked.connect(self.on_button_click)

                    sub_layout.add_item(sub_button)
                    self.all_buttons.append(sub_button)
                    self.all_sub_buttons.append(sub_button)
        
        for sub_layout in self.all_sub_layouts:
            sub_layout.setVisible(False)
    
    @QtCore.Slot()
    def on_button_click(self):
        # (Checked) -> Unchecked
        if self.sender().is_checked:
            # Sub layout not visible
            for sub_layout in self.all_sub_layouts:
                if sub_layout.sub_layout_id == self.sender().button_id:
                    self.sender().setIcon(self.icon_arrow_right)
                    self.sender().setText(self.sender().text())
                    self.sender().is_sub_layouts_active = False
                    sub_layout.setVisible(False)
            
            # Unset buttons
            for button in self.all_buttons:
                button.unset_active_color()
                button.is_clicked = False
                button.is_checked = False
                
                if button.is_sub_layouts_active:  # Fix: one click hide subs
                    button.is_checked = True
            
            # End state
            self.sender().set_active_color()
            self.sender().is_checked = False
            self.sender().is_clicked = True
        
        # (Unchecked) -> Checked
        else:
            # Unset buttons
            for button in self.all_buttons:
                button.unset_active_color()
                button.is_checked = False
                button.is_clicked = False

                if button.is_sub_layouts_active:  # Fix: one click hide subs
                    button.is_checked = True
            
            # Sub layout visible
            sub_layout_visible = False
            for sub_layout in self.all_sub_layouts:
                if sub_layout.sub_layout_id == self.sender().button_id:
                    if not self.sender().is_sub_layouts_active:
                        self.sender().setIcon(self.icon_arrow_down)
                        self.sender().setText(self.sender().text())
                        self.sender().is_sub_layouts_active = True
                        sub_layout.setVisible(True)
                        sub_layout_visible = True
            
            # Animate sub layout
            if sub_layout_visible:
                self.anim_group = QtCore.QSequentialAnimationGroup()

                for sub_layout in self.all_sub_layouts:
                    if sub_layout.sub_layout_id == self.sender().button_id:

                        vertical_size = (
                            (len(sub_layout.all_items) * button.height())
                            + sub_layout.height()
                        )

                        anim = QtCore.QPropertyAnimation(sub_layout, b"size")
                        anim.setStartValue(QtCore.QSize(sub_layout.width(), 0))
                        anim.setEndValue(
                            QtCore.QSize(sub_layout.width(), vertical_size))
                        anim.setDuration(40)
                        self.anim_group.addAnimation(anim)
                        
                        """
                        anim_p = QtCore.QPropertyAnimation(sub_layout, b"pos")
                        anim_p.setStartValue(QtCore.QPoint(0, sub_layout.y()))
                        anim_p.setEndValue(QtCore.QPoint(20, sub_layout.y()))
                        anim_p.setDuration(40)
                        self.anim_group.addAnimation(anim_p)
                        """
                
                self.anim_group.start()

            # End state
            self.sender().set_active_color()
            self.sender().is_checked = True
            self.sender().is_clicked = True
    
    def get_button_by_id(self, button_id):
        for button in self.all_buttons:
            if button.button_id == button_id:
                return button


if __name__ == '__main__':
    pass
