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
        select_multiple: bool = False,
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
        self.__select_multiple = select_multiple

        self.__filename = None
        self.__filename_path = None
        self.__filename_url = None
        self.__filename_list = []
        self.__filename_path_list = []
        self.__filename_url_list = []

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
        self.__get_filename_button.clicked.connect(  # type: ignore
            self.__open_dialog)
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
        # noinspection PyUnresolvedReferences
        self.__clear_button.clicked.connect(self.clear_filename)
        self.layout.addWidget(self.__clear_button)

    @QtCore.Slot()
    def filenameUrl(self) -> str:
        """..."""
        return self.__filename_url

    @QtCore.Slot()
    def filenamePath(self) -> str:
        """..."""
        return self.__filename_path

    @QtCore.Slot()
    def filename(self) -> str:
        """..."""
        return self.__filename

    @QtCore.Slot()
    def filenameUrlList(self) -> list:
        """..."""
        return self.__filename_url_list

    @QtCore.Slot()
    def filenamePathList(self) -> list:
        """..."""
        return self.__filename_path_list

    @QtCore.Slot()
    def filenameList(self) -> list:
        """..."""
        return self.__filename_list

    @QtCore.Slot()
    def __open_dialog(self) -> None:
        self.clear_filename()

        if 'DIALOG-PATH' in os.environ.keys():
            self.__dialog_path = os.environ["DIALOG-PATH"]

        dialog = OpenDialog()
        filename_url = dialog.open_filename(
            parent=self.sender(),
            title=self.__dialog_title,
            path=self.__dialog_path,
            filter_description=self.__dialog_filter_description,
            filter_extensions=self.__dialog_filter_extensions,
            select_multiple=self.__select_multiple)
        
        # Get text
        if filename_url and isinstance(filename_url, str):
            if self.__select_multiple:
                for item in filename_url.split(' /'):
                    item = f'/{item}' if item[0] != '/' else item

                    item_path = os.path.dirname(item)
                    self.__filename_path_list.append(item_path)

                    item_filename = item.replace(item_path + '/', '')
                    self.__filename_list.append(item_filename)

                    self.__filename_url_list.append(item)

                # Set text
                self.__filename_label.setText(', '.join(self.__filename_list))
                self.__clear_button.setVisible(True)

            else:
                self.__filename_path = os.path.dirname(filename_url)
                self.__filename = filename_url.replace(
                    self.__filename_path + '/', '')
                self.__filename_url = filename_url
                os.environ["DIALOG-PATH"] = self.__filename_path

                # Set text
                self.__filename_label.setText(self.__filename)
                self.__clear_button.setVisible(True)

        elif filename_url and isinstance(filename_url, list):
            for item in filename_url:
                item_path = os.path.dirname(item)
                self.__filename_path_list.append(item_path)

                item_filename = item.replace(item_path + '/', '')
                self.__filename_list.append(item_filename)

                self.__filename_url_list.append(item)

            # Set text
            self.__filename_label.setText(', '.join(self.__filename_list))
            self.__clear_button.setVisible(True)

    @QtCore.Slot()
    def clear_filename(self):
        self.__filename = None
        self.__filename_url = None
        self.__filename_path = None
        self.__filename_list = []
        self.__filename_path_list = []
        self.__filename_url_list = []

        self.__filename_label.setText('')
        self.__clear_button.setVisible(False)


if __name__ == '__main__':
    pass
