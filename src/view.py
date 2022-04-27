#!/usr/bin env python3
import os
import typing

from BlurWindow.blurWindow import GlobalBlur
from PySide6 import QtCore, QtWidgets, QtGui


class ElidedLabel(QtWidgets.QLabel):
    def __init__(self, elide_side: str = 'right', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__side = elide_side

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        metrics = QtGui.QFontMetrics(self.font())
        if self.__side == 'left':
            elided = metrics.elidedText(
                self.text(), QtCore.Qt.ElideLeft, self.width())
        elif self.__side == 'middle':
            elided = metrics.elidedText(
                self.text(), QtCore.Qt.ElideMiddle, self.width())
        else:
            elided = metrics.elidedText(
                self.text(), QtCore.Qt.ElideRight, self.width())

        painter.drawText(self.rect(), self.alignment(), elided)


class Button(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedHeight(30)
        self.normal_style = (
            'background: transparent;'
            'background-color: rgba(40, 40, 40, 0.5);'
            'border: 1px solid rgba(100, 100, 100, 0.5);'
            'border-radius: 3px;')
        self.setStyleSheet(self.normal_style)
    
    def enterEvent(self, event):
        self.setStyleSheet(
            'background: transparent;'
            'background-color: rgba(50, 50, 50, 0.5);'
            'border: 1px solid rgba(150, 150, 150, 0.5);'
            'border-radius: 3px;')

    def leaveEvent(self, event):
        self.setStyleSheet(self.normal_style)


class CloseButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet('background: transparent;')
        self.setFixedHeight(40)
        self.setFixedWidth(60)

        icon_url = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'static', 'icons', 'close.svg')

        self.setIcon(QtGui.QIcon(icon_url))
        self.setIconSize(QtCore.QSize(24, 24))
    
    def enterEvent(self, event):
        self.setStyleSheet(
            'background: transparent;'
            'background-color: rgba(60, 60, 60, 0.5);')

    def leaveEvent(self, event):
        self.setStyleSheet('background: transparent;')


class ActionButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('border: 0px;')
        """
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor('red'))
        self.setPalette(palette)
        """


class CsvImport(QtWidgets.QWidget):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedWidth(500)
        # self.setContentsMargins(20, 20, 20, 20)
        # self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        # self.shadow.setBlurRadius(15)
        # self.setGraphicsEffect(self.shadow)
        self.controller = controller

        # ___ Properties ___
        self.filename = None
        self.header = None

        # ___ Container ___
        # Top level layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.setLayout(self.layout)

        # Filename
        self.filename_layout = QtWidgets.QHBoxLayout()
        self.filename_layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.filename_layout)

        self.filename_label = QtWidgets.QLabel(text='Arquivo scv')
        self.filename_layout.addWidget(
            self.filename_label, 2, QtCore.Qt.AlignRight)
        
        self.filename_button_layout = QtWidgets.QHBoxLayout()
        self.filename_button_layout.setContentsMargins(0, 0, 0, 0)
        self.filename_layout.addLayout(self.filename_button_layout, 8)
        
        self.filename_button = QtWidgets.QPushButton(
            icon=QtGui.QIcon.fromTheme('document-open-folder'),
            text='Selecionar')
        self.filename_button_layout.addWidget(
            self.filename_button, 0, QtCore.Qt.AlignLeft)

        self.filename_url_label = ElidedLabel(elide_side='middle')
        self.filename_url_label.setFixedWidth(265)
        self.filename_button_layout.addWidget(
            self.filename_url_label, 1, QtCore.Qt.AlignLeft)

        self.filename_clear_button = ActionButton(
            icon=QtGui.QIcon.fromTheme('edit-clear'))
        self.filename_clear_button.setVisible(False)
        self.filename_button_layout.addWidget(
            self.filename_clear_button, 0, QtCore.Qt.AlignRight)

        # Header
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.header_layout)

        self.header_label = QtWidgets.QLabel(text='Cabeçalho')
        self.header_layout.addWidget(
            self.header_label, 2, QtCore.Qt.AlignRight)

        self.header_entry_layout = QtWidgets.QHBoxLayout()
        self.header_entry_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.addLayout(self.header_entry_layout, 8)

        self.header_entry = QtWidgets.QLineEdit()
        self.header_entry.setClearButtonEnabled(True)
        self.header_entry_layout.addWidget(self.header_entry, 10)

        # End
        self.end_button = QtWidgets.QPushButton(
            text='Procesar', icon=QtGui.QIcon.fromTheme('view-refresh'))
        self.layout.addWidget(self.end_button, 0, QtCore.Qt.AlignRight)


class View(QtWidgets.QMainWindow):
    def __init__(self, controller,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Flag controller
        self.controller = controller

        # ___ Container ___
        # Top level container
        self.top_level_container = QtWidgets.QWidget()
        self.setCentralWidget(self.top_level_container)

        # Top level layout
        self.top_level_layout = QtWidgets.QVBoxLayout()
        self.top_level_layout.setContentsMargins(0, 0, 0, 0)
        self.top_level_layout.setSpacing(0)

        self.top_level_container.setLayout(self.top_level_layout)

        # ___ Header ___
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.setAlignment(QtCore.Qt.AlignRight)
        self.header_layout.setSpacing(0)
        self.top_level_layout.addLayout(self.header_layout)

        self.fullscreen_button = ActionButton(
            icon=QtGui.QIcon.fromTheme('zoom-fit-best'))
        self.fullscreen_button.setIconSize(QtCore.QSize(24, 24))
        self.fullscreen_button.setVisible(False)
        # self.fullscreen_button.setFlat(True)
        self.header_layout.addWidget(self.fullscreen_button)

        # ___ Body ___
        self.body_layout = QtWidgets.QVBoxLayout()
        self.body_layout.setAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.body_layout.setContentsMargins(10, 10, 10, 10)
        self.top_level_layout.addLayout(self.body_layout)

        self.csv_import = CsvImport(self.controller)
        self.body_layout.addWidget(
            self.csv_import, 0,
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


if __name__ == '__main__':
    # https://doc.qt.io/qtforpython/
    # https://doc.qt.io/qtforpython/api.html
    # https://www.pythonguis.com/tutorials/pyside-layouts/
    # https://docs.python-guide.org/shipping/freezing/
    pass
