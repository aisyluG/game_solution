from PyQt5.QtWidgets import QDialog, QTreeWidgetItem
from PyQt5.QtGui import QFont
from reference_window import Ui_referenceDialog
from reference_source import theory_source, user_guide
from test_widget import TestWidget

class ReferenceWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_referenceDialog()
        self.ui.setupUi(self)

        self.ui.content_tree.setStyleSheet('QHeaderView::section { background-color:rgb(122, 179, 138);}')

        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        # font.setBold(True)

        self.test_widget = TestWidget(self.ui.reference_text)
        self.test_widget.hide()
        self.ui.test_againBt.hide()

        self.ui.content_tree.headerItem().setFont(0, font)

        self.ui.content_tree.setCurrentItem(self.ui.item_1)
        self.ui.content_tree.currentItemChanged.connect(self.setReferenceText)
        self.test_widget.test_finished.connect(self.test_finished)
        self.ui.test_againBt.clicked.connect(self.open_test)

    def setReferenceText(self, current:QTreeWidgetItem, previos):
        if previos.text(0) == 'Проверка знаний':
            self.test_widget.hide()
            self.test_widget.resetResults()
            self.ui.test_againBt.hide()
        if current.text(0) == 'Проверка знаний':
            self.ui.reference_text.clear()
            self.test_widget.show()
        elif current.text(0) == 'Критерий Вальда':
            self.ui.reference_text.setHtml(theory_source[1])
        elif current.text(0) == 'Критерий Байеса-Лапласа':
            self.ui.reference_text.setHtml(theory_source[2])
        elif current.text(0) == 'Критерий Сэвиджа':
            self.ui.reference_text.setHtml(theory_source[3])
        elif current.text(0) == 'Критерий Гурвица':
            self.ui.reference_text.setHtml(theory_source[4])
        elif current.text(0) == 'Понятие игры с природой':
            self.ui.reference_text.setHtml(theory_source[0])
        elif current.text(0) == 'Как работать с программой':
            self.ui.reference_text.setHtml(user_guide)
        elif current.text(0) == 'Критерии выбора оптимальных решений':
            if self.ui.content_tree.currentItem().isExpanded() == True:
                self.ui.content_tree.currentItem().setExpanded(False)
            else:
                self.ui.content_tree.currentItem().setExpanded(True)

    def test_finished(self, result):
        self.ui.reference_text.setHtml(result)
        self.ui.test_againBt.show()

    def open_test(self):
        self.ui.content_tree.setCurrentItem(self.ui.item_0)
        self.test_widget.resetResults()
        self.ui.test_againBt.hide()
        self.ui.reference_text.clear()
        self.test_widget.show()

