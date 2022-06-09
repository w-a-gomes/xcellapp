#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui

from attachment.uiwidgets.elidedlabel import ElidedLabel
from attachment.uitools.opendialog import OpenDialog

class ImportFile(QtWidgets.QWidget):
    """..."""
    def __init__(
        self,
        text: str = None,
        text_width: int = None,
        button_icon = None,
        button_text: str = None,
        clear_icon = None,
        *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.layout.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(self.layout)

        if text:
            self.description = ElidedLabel(
                text=text, elide_side='right')
            self.description.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.layout.addWidget(self.description)
            
            if text_width:
                self.description.setFixedWidth(text_width)
        
        self.button = QtWidgets.QPushButton()
        self.button.clicked.connect(self.open_dialog)
        self.layout.addWidget(self.button)

        if button_text:
            self.button.setText(button_text)
        if button_icon:
            self.button.setIcon(button_icon)
        
        self.label = ElidedLabel(elide_side='middle')
        self.layout.addWidget(self.label)

        if not clear_icon:
            pixmapi = getattr(QtWidgets.QStyle, 'SP_DialogResetButton')
            clear_icon = self.style().standardIcon(pixmapi)
        
        self.clear_button = QtWidgets.QPushButton(icon=clear_icon)
        self.clear_button.setFlat(True)
        self.clear_button.setVisible(False)
        self.layout.addWidget(self.clear_button)

    @QtCore.Slot()
    def open_dialog(
        self,
        title: str = None,
        path: str = None,
        filter_description: str = None,
        filter_extensions: list = [],
        ) -> None:

        dialog = OpenDialog()
        filename_url = dialog.open_filename(
            parent=self.sender(),
            title=title,
            path=path,
            filter_description=filter_description,
            filter_extensions=filter_extensions)
        
        #         # Get text
        #         txt_path = os.path.dirname(filename_url)
        #         txt_filename = filename_url.replace(txt_path + '/', '')
                
        #         # Set text
        #         self.__ui.navigation_stack.imp_tables.filename = filename_url
        #         self.__ui.navigation_stack.imp_tables.filename_url_label.setText(
        #             txt_filename)
                
        #         # Update dialog settings
        #         self.__settings['dialog-path'] = txt_path
        #         self.__save_settings()
                
        #         # Clear Button
        #         (self.__ui.navigation_stack.imp_tables.
        #             filename_clear_button.setVisible(True))


if __name__ == '__main__':
    pass
