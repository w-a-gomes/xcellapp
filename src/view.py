#!/usr/bin env python3
import os

from BlurWindow.blurWindow import GlobalBlur
from PySide6 import QtCore, QtWidgets, QtGui


class ElidedLabel(QtWidgets.QLabel):
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        metrics = QtGui.QFontMetrics(self.font())
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


class View(QtWidgets.QMainWindow):
    def __init__(self, controller,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Flag controller
        self.controller = controller

        # ___ Screen info ___
        self.screen = QtWidgets.QApplication.primaryScreen()
        self.screen_size = self.screen.size()
        
        # ___ Window Style ___

        # Fixed size
        # self.setFixedSize(QSize(400, 300))

        # Remove title bar
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Window opacity
        # self.setWindowOpacity(0.5)

        # Transparent background
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Background color
        self.setStyleSheet(
            'border: 0px;'
            'background: transparent;'
            'background-color: rgba(37, 37, 38, 0.5);')
        
        # Background blur
        window_id = self.winId()
        GlobalBlur(window_id, Dark=True, QWidget=self)  # blur(window_id)

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

        self.exit_button = CloseButton()
        self.exit_button.setFlat(True)
        self.exit_button.clicked.connect(self.on_button_close)
        self.header_layout.addWidget(self.exit_button)

        # ___ Body ___
        self.body_layout = QtWidgets.QVBoxLayout()
        # self.body_layout.setAlignment(QtCore.Qt.AlignRight)
        self.body_layout.setContentsMargins(10, 10, 10, 10)
        # self.body_layout.setSpacing(10)
        self.top_level_layout.addLayout(self.body_layout)

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.text = QtWidgets.QLabel('Hello', alignment=QtCore.Qt.AlignCenter)
        self.body_layout.addWidget(self.text)

        self.button = Button('Click me!')
        self.button.clicked.connect(self.on_button_click)
        self.body_layout.addWidget(self.button)

        # Full screen
        # self.showFullScreen()
        self.showMaximized()
        # self.showMinimized()

    @QtCore.Slot()
    def on_button_click(self):
        self.controller.on_button_click(self.hello)
    
    @QtCore.Slot()
    def on_button_close(self):
        self.controller.on_button_close()

# https://doc.qt.io/qtforpython/
# https://doc.qt.io/qtforpython/api.html
# https://docs.python-guide.org/shipping/freezing/
