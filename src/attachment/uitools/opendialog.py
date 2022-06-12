#!/usr/bin env python3
import pathlib
import subprocess
import sys

from PySide6 import QtWidgets


class OpenDialog(object):
    def __init__(self):
        self.__home_path = str(pathlib.Path.home())
    
    def open_filename(
        self,
        parent,
        title: str = '',
        path: str = '',
        filter_description: str = '',
        filter_extensions: list = None,
        select_multiple: bool = False,
    ) -> str:
        filename_url = self.__open_dialog(
            parent=parent,
            dialog_type='open-filename',
            title=title,
            path=path,
            filter_description=filter_description,
            filter_extensions=filter_extensions,
            select_multiple=select_multiple)
        
        return filename_url

    def __open_dialog(
        self,
        parent,
        dialog_type: str = 'open-filename',
        title: str = 'Open file',
        path: str = None,
        filter_description: str = ' ',
        filter_extensions: list = None,
        select_multiple: bool = False,
    ) -> str:
        """Dialog
        types: 'open-filename' is default
        """
        if not path:
            path = self.__home_path
        
        if dialog_type and dialog_type not in ['open-filename']:
            raise ValueError(f'Dialog type "{dialog_type}" not found!')
        
        # Only kdialog linux
        if sys.platform == 'linux' and dialog_type == 'open-filename':
            # Check mimetype cmd
            if subprocess.run(
                    ['which', 'mimetype'], capture_output=True).returncode == 0:

                # Check Plasma dialog
                if subprocess.run(
                        ['which', 'kdialog'], capture_output=True).returncode == 0:

                    # Extensions filter to mimetype filter
                    mimetype_filters = ''
                    if filter_extensions:
                        mime_filters = ' '.join([
                            subprocess.getoutput(f'mimetype .{ext}').split()[1]
                            for ext in filter_extensions])
                        mimetype_filters = f'"{mime_filters}"'

                    # Multiple
                    select_multiple = '--multiple' if select_multiple else ''
                    
                    # Run dialog
                    filename_url = subprocess.getoutput(
                        f'kdialog {select_multiple} '
                        f'--title "{title}" --getopenfilename '
                        f'"{path}" {mimetype_filters}')

                    return filename_url
        
        # Default
        if select_multiple:
            extension_filters = ' '.join([f'*.{x}' for x in filter_extensions])
            filename_url = QtWidgets.QFileDialog.getOpenFileNames(
                parent,
                title,
                path,
                f"{filter_description} ({extension_filters})")
            # (*.xlsx *.xls *.XLSX)
            return filename_url[0]

        else:
            extension_filters = ' '.join([f'*.{x}' for x in filter_extensions])
            filename_url = QtWidgets.QFileDialog.getOpenFileName(
                parent,
                title,
                path,
                f"{filter_description} ({extension_filters})")
            # (*.xlsx *.xls *.XLSX)
            return filename_url[0]
