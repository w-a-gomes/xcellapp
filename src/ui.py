#!/usr/bin env python3
import os

# from BlurWindow.blurWindow import GlobalBlur
from PySide6 import QtCore, QtWidgets

from attachment.uisections.sectionverticalmenu import SectionVerticalMenu
import attachment.uitools.qticons as qticons


class MainWindow(QtWidgets.QMainWindow):
    """..."""
    resize_control = QtCore.Signal(object)

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # ___ Properties ___
        self.app_path = os.path.abspath(os.path.dirname(__file__))

        # ___ Icons ___
        self.icons = qticons.QtGuiIcon()

        self.app_icon = self.icons.fromPath(
            os.path.join(self.app_path, 'static', 'icons', 'app_logo.png'))
        
        self.icon_fullscreen = self.icons.fromSystem('view-fullscreen')
        self.icon_view_restore = self.icons.fromSystem('view-restore')

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
        self.header_layout.setAlignment(QtCore.Qt.AlignRight)  # type: ignore
        self.header_layout.setSpacing(0)
        self.top_level_layout.addLayout(self.header_layout)

        self.fullscreen_button = QtWidgets.QPushButton()
        self.fullscreen_button.setIcon(self.icon_fullscreen)
        self.fullscreen_button.setFlat(True)
        self.fullscreen_button.setIconSize(QtCore.QSize(24, 24))
        self.fullscreen_button.setToolTip('Janela em tela cheia')
        self.header_layout.addWidget(self.fullscreen_button)

        # ___ Body ___
        self.body_layout = QtWidgets.QVBoxLayout()
        # self.body_layout.setContentsMargins(10, 10, 10, 10)
        self.top_level_layout.addLayout(self.body_layout)
        
        # Nav
        self.lateral_menu = SectionVerticalMenu()
        self.body_layout.addWidget(
            self.lateral_menu, 0, QtCore.Qt.AlignTop)  # type: ignore
    
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
