from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QKeyEvent
from game_edit_window import Ui_Dialog
from lineEdit import HeaderEdit

class Edit_Window(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.gameView.setStyleSheet(
            "QHeaderView::section { background-color:rgb(122, 179, 138); selection-background-color:rgb(180, 199, 220);}")

        self.headerEdit = HeaderEdit(self)
        self.headerEdit.setStyleSheet("background-color: rgb(243, 253, 219)")

        self.ui.probabylityTable.setStyleSheet(
            "QHeaderView::section { background-color:rgb(122, 179, 138); selection-background-color:rgb(180, 199, 220);}")

        self.ui.addStateBt.clicked.connect(self.addState)
        self.ui.addStrategyBt.clicked.connect(self.addStrategy)
        self.ui.delStateBt.clicked.connect(self.deleteState)
        self.ui.delStrategyBt.clicked.connect(self.deleteStrategy)
        self.ui.gameView.verticalHeader().sectionDoubleClicked.connect(self.editVerticalHeader)
        self.ui.gameView.horizontalHeader().sectionDoubleClicked.connect(self.editHorizontalHeader)
        self.headerEdit.header_entered.connect(self.setHeaderData)

    def addState(self):
        self.ui.gameView.model().addState()

    def addStrategy(self):
        self.ui.gameView.model().addStrategy()

    def deleteState(self):
        self.ui.gameView.model().deleteState()

    def deleteStrategy(self):
        self.ui.gameView.model().deleteStrategy()
        
    def editVerticalHeader(self, h):
        width = self.ui.gameView.verticalHeader().sectionSizeFromContents(h).width()
        height = self.ui.gameView.verticalHeader().sectionSizeFromContents(h).height()
        j = self.ui.gameView.verticalHeader().sectionViewportPosition(h)
        hhh = self.ui.gameView.horizontalHeader().sectionSizeFromContents(0).height()
        self.headerEdit.setGeometry(QRect(self.ui.gameView.x()+3, j + hhh+self.ui.gameView.y()+3, width-5, height))
        self.headerEdit.section = h
        self.headerEdit.orientation = Qt.Vertical
        self.headerEdit.setFocus()
        self.headerEdit.setText(self.ui.gameView.model().headerData(h, Qt.Vertical, Qt.EditRole))
        self.headerEdit.show()

    def setHeaderData(self, section, orientation, value):
        if orientation == Qt.Vertical:
            self.ui.gameView.model().setHeaderData(section, Qt.Vertical, value, Qt.EditRole)
        else:
            self.ui.gameView.model().setHeaderData(section, Qt.Horizontal, value, Qt.EditRole)

    def editHorizontalHeader(self, h):
        width = self.ui.gameView.horizontalHeader().sectionSizeFromContents(h).width()
        height = self.ui.gameView.horizontalHeader().sectionSizeFromContents(h).height()
        j = self.ui.gameView.horizontalHeader().sectionViewportPosition(h)
        vhw= self.ui.gameView.verticalHeader().sectionSizeFromContents(0).width()
        i = self.ui.gameView.horizontalHeader().sectionSize(h)
        if i > width:
            width = i
        self.headerEdit.setGeometry(QRect(vhw + j+self.ui.gameView.x()+3,self.ui.gameView.y()+3, width-5, height-3))
        self.headerEdit.section = h
        self.headerEdit.orientation = Qt.Horizontal
        self.headerEdit.setFocus()
        self.headerEdit.setText(self.ui.gameView.model().headerData(h, Qt.Horizontal, Qt.EditRole))
        self.headerEdit.show()

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() != 16777220:
            super().keyPressEvent(a0)