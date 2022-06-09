#!/usr/bin env python3
from PySide6 import QtCore, QtWidgets, QtGui


class ElidedLabel(QtWidgets.QLabel):
    """..."""
    def __init__(self, elide_side: str = 'right', *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.__side = elide_side

    def paintEvent(self, event):
        """..."""
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


if __name__ == '__main__':
    pass
