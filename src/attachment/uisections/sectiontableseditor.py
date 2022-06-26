#!/usr/bin env python3
# import os
# import json

from PySide6 import QtWidgets, QtGui, QtCore

# import attachment.uitools.qtcolor as qtcolor
# import attachment.uitools.qticons as qticons


# noinspection PyPep8Naming
class SectionTablesEditor(QtWidgets.QFrame):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        # Args
        self.__table_schema = None

        # Frame border
        self.setFrameStyle(
            QtWidgets.QFrame.StyledPanel |  # type: ignore
            QtWidgets.QFrame.Plain)

        # Background color
        self.background_color = QtGui.QColor(
            QtGui.QPalette().color(
                # ToolTipBase: Light
                # Button: Light
                # Window: Normal
                # AlternateBase: Dark
                QtGui.QPalette.Active, QtGui.QPalette.AlternateBase))

        self.color_palette = self.palette()
        self.color_palette.setColor(
            QtGui.QPalette.Window, self.background_color)

        self.setAutoFillBackground(True)
        self.setPalette(self.color_palette)

        # Property
        self.__widgets_to_remove = []

        # ___ Container ___
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Lines info
        self.lines_info_layout = QtWidgets.QHBoxLayout()
        self.lines_info_layout.setAlignment(
            QtCore.Qt.AlignCenter)  # type: ignore
        self.layout.addLayout(self.lines_info_layout)

        self.lines_info_current = QtWidgets.QLabel()
        self.lines_info_layout.addWidget(self.lines_info_current)

        self.lines_info_total = QtWidgets.QLabel()
        self.lines_info_layout.addWidget(self.lines_info_total)

        # Scroll Area
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setWidgetResizable(True)

        self.layout.addWidget(self.scroll_area)

        # Scroll Widget
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_widget.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setWidget(self.scroll_widget)

        # Scroll Widget BG color
        self.scroll_widget.setAutoFillBackground(True)
        self.scroll_widget.setPalette(self.color_palette)

        # Scroll Widget Layout
        self.scroll_widget_layout = QtWidgets.QVBoxLayout()
        self.scroll_widget_layout.setContentsMargins(12, 12, 12, 12)
        self.scroll_widget_layout.setSpacing(12)
        self.scroll_widget_layout.setAlignment(
            QtCore.Qt.AlignTop)  # type: ignore
        self.scroll_widget.setLayout(self.scroll_widget_layout)

        # Timer
        self.timer = QtCore.QTimer()
        self.line_counter = 0
        self.total = 0

    def setSchema(self, schema):
        self.__table_schema = schema
        self.total = len(self.__table_schema['table-data'])
        self.lines_info_total.setText(str(self.total))
        self.line_counter = 0

    def __add_line(self):
        # Item layout
        line_layout = QtWidgets.QHBoxLayout()
        self.scroll_widget_layout.addLayout(line_layout)
        self.__widgets_to_remove.append(line_layout)

        # Item
        for item in self.__table_schema['table-data'][self.line_counter]:
            print(item[0], item[1], item[2], item[3], item[4])
            item_widget = QtWidgets.QLabel(f'{item}')
            line_layout.addWidget(item_widget)
            self.__widgets_to_remove.append(item_widget)

        # Lines
        self.lines_info_current.setText(str(self.line_counter + 1))

        if self.line_counter + 1 == self.total:
            self.timer.stop()

        self.line_counter += 1

    def updateEditor(self):
        """
        {
            'table-name': 'cadastro.csv',
            'edited': False,
            'edited-date': None,
            'table-data': [
                [
                    (column, line-num, original-value, new-value, value-type),
                    ('Café', 2, '10,99', 10.99, 'float'),
                ],
                [
                    (column, line-num, original-value, new-value, value-type),
                    ('mouse', 3, '30,00', 30.0, 'float'),
                ]
            ]
        }
        """
        if self.__widgets_to_remove:
            for w in self.__widgets_to_remove:
                w.deleteLater()
            self.__widgets_to_remove = []

        self.timer.setInterval(10)
        self.timer.timeout.connect(self.__add_line)  # type: ignore
        self.timer.start()
