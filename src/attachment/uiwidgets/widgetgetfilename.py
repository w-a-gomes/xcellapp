#!/usr/bin env python3
import os

from PySide6 import QtCore, QtWidgets

from attachment.uiwidgets.widgetelidedlabel import WidgetElidedLabel
from attachment.uitools.opendialog import OpenDialog


# noinspection PyPep8Naming
class WidgetGetFilename(QtWidgets.QWidget):
    """..."""
    def __init__(
        self,
        description_text: str = None,
        text_width: int = None,
        button_icon=None,
        button_text: str = None,
        clear_icon=None,
        dialog_title: str = None,
        dialog_path: str = None,
        dialog_filter_description: str = None,
        dialog_filter_extensions: list = None,
        *args, **kwargs
    ):
        """..."""
        super().__init__(*args, **kwargs)
        # Properties
        self.__description_text = description_text
        self.__text_width = text_width
        self.__button_icon = button_icon
        self.__button_text = button_text
        self.__clear_icon = clear_icon
        self.__dialog_title = dialog_title
        self.__dialog_path = dialog_path
        self.__dialog_filter_description = dialog_filter_description
        self.__dialog_filter_extensions = dialog_filter_extensions

        self.__filename = None
        self.__filename_path = None
        self.__filename_url = None

        # Layout
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.layout.setAlignment(QtCore.Qt.AlignLeft)  # type: ignore
        self.setLayout(self.layout)

        if self.__description_text:
            self.__description_label = WidgetElidedLabel(
                text=self.__description_text, elide_side='right')
            self.__description_label.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)  # type: ignore
            self.layout.addWidget(self.__description_label)
            
            if self.__text_width:
                self.__description_label.setFixedWidth(self.__text_width)
        
        self.__get_filename_button = QtWidgets.QPushButton()
        self.__get_filename_button.clicked.connect(self.__open_dialog)  # type: ignore
        self.layout.addWidget(self.__get_filename_button)

        if self.__button_text:
            self.__get_filename_button.setText(self.__button_text)
        if self.__button_icon:
            self.__get_filename_button.setIcon(self.__button_icon)
        
        self.__filename_label = WidgetElidedLabel(elide_side='middle')
        self.layout.addWidget(self.__filename_label)

        if not self.__clear_icon:
            pixmapi = getattr(QtWidgets.QStyle, 'SP_DialogResetButton')
            self.__clear_icon = self.style().standardIcon(pixmapi)
        
        self.__clear_button = QtWidgets.QPushButton(icon=self.__clear_icon)
        self.__clear_button.setFlat(True)
        self.__clear_button.setVisible(False)
        self.__clear_button.clicked.connect(self.__clear_filename)  # type: ignore
        self.layout.addWidget(self.__clear_button)

    @QtCore.Slot()
    def filenameUrl(self) -> str:
        """..."""
        return self.__filename_url

    @QtCore.Slot()
    def __open_dialog(self) -> None:
        if 'DIALOG-GET-FILENAME-PATH' in os.environ.keys():
            self.__dialog_path = os.environ["DIALOG-GET-FILENAME-PATH"]

        dialog = OpenDialog()
        filename_url = dialog.open_filename(
            parent=self.sender(),
            title=self.__dialog_title,
            path=self.__dialog_path,
            filter_description=self.__dialog_filter_description,
            filter_extensions=self.__dialog_filter_extensions)
        
        # Get text
        if filename_url:
            self.__filename_path = os.path.dirname(filename_url)
            self.__filename = filename_url.replace(self.__filename_path + '/', '')
            self.__filename_url = filename_url

            # Set text
            self.__filename_label.setText(self.__filename)
            self.__clear_button.setVisible(True)

    @QtCore.Slot()
    def __clear_filename(self):
        self.__filename = None
        self.__filename_url = None
        self.__filename_path = None

        self.__filename_label.setText('')
        self.__clear_button.setVisible(False)


if __name__ == '__main__':
    pass
