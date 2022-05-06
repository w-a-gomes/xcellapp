#!/usr/bin env python3
import os
import typing

from BlurWindow.blurWindow import GlobalBlur
from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uisections.csvimport import CsvImport
from attachment.uisections.navigationstack import NavigationStack


class MainWindow(QtWidgets.QMainWindow):
    """..."""
    resize_control = QtCore.Signal(object)

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # ___ Properties ___
        self.app_path = os.path.abspath(os.path.dirname(__file__))
        self.app_icon = QtGui.QIcon(
            QtGui.QPixmap(
                os.path.join(self.app_path, 'static', 'icons', 'app_logo.svg')
            )
        )
        self.setWindowIcon(self.app_icon)

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

        self.pixmapi_fullscreen_button = getattr(
            QtWidgets.QStyle, 'SP_TitleBarNormalButton')
        self.icon_fullscreen_button = self.style().standardIcon(
            self.pixmapi_fullscreen_button)

        self.fullscreen_button = QtWidgets.QPushButton()
        self.fullscreen_button.setIcon(self.icon_fullscreen_button)
        self.fullscreen_button.setFlat(True)
        self.fullscreen_button.setIconSize(QtCore.QSize(24, 24))
        self.fullscreen_button.setToolTip('Janela em tela cheia')
        self.header_layout.addWidget(self.fullscreen_button)

        # ___ Body ___
        self.body_layout = QtWidgets.QVBoxLayout()
        # self.body_layout.setContentsMargins(10, 10, 10, 10)
        self.top_level_layout.addLayout(self.body_layout)
        
        self.navigation_stack = NavigationStack()
        self.body_layout.addWidget(
            self.navigation_stack, 0, QtCore.Qt.AlignTop)
    
    @QtCore.Slot()
    def resizeEvent(self, event):
        self.resize_control.emit(
            {'width': self.width(), 'height': self.height()}
        )


if __name__ == '__main__':
    # https://doc.qt.io/qtforpython/
    # https://doc.qt.io/qtforpython/api.html
    
    # https://www.pythonguis.com/pyside6-tutorial/
    # https://www.pythonguis.com/tutorials/pyside-layouts/
    # https://www.pythonguis.com/tutorials/pyside-animated-widgets/

    # https://docs.python-guide.org/shipping/freezing/
    pass
