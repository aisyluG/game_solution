from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QKeyEvent, QFocusEvent

class HeaderEdit(QLineEdit):
    header_entered = pyqtSignal(int, int, str)
    def __init__(self, parent):
        super().__init__(parent)
        self.hide()
        self.section = None
        self.orientation = None

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        super().keyPressEvent(a0)
        if a0.key() == Qt.Key_Insert or a0.key() == Qt.Key_Enter or a0.key() == Qt.Key_Return:
            self.header_entered.emit(self.section, self.orientation, str(self.text()))
            self.hide()
        if a0.key() == Qt.Key_Escape:
            self.hide()

    def focusOutEvent(self, a0:QFocusEvent) -> None:
        super().focusOutEvent(a0)
        self.hide()