from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTextBrowser, QFileDialog, QAction
from PyQt5 import QtGui, QtCore
import sys
from main_window import Ui_MainWindow
from edit_window import Edit_Window
from reference import ReferenceWindow
from model import GameModel, GamePropertiesModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = GameModel()
        self.ui.gameView.setModel(self.model)
        self.ui.gameView.setStyleSheet(
            "QHeaderView::section { background-color:rgb(122, 179, 138); selection-background-color:rgb(180, 199, 220);}")

        self.propModel = GamePropertiesModel(self.model)
        self.ui.probabylityTable.setModel(self.propModel)
        self.ui.probabylityTable.setStyleSheet(
            "QHeaderView::section { background-color:rgb(122, 179, 138); selection-background-color:rgb(180, 199, 220);}")

        self.edit_win = Edit_Window()
        self.reference_win = ReferenceWindow()

        self.createSolutionTabs()

        self.criterions = [self.ui.vald_check, self.ui.bayes_check, self.ui.savidge_check, self.ui.gurvits_check]
        self.ui.gameEditBt.clicked.connect(self.showEditWindow)
        self.edit_win.finished.connect(self.editModel)
        self.ui.solveGameBt.clicked.connect(self.getSolve)
        self.ui.criteirions_choosedBt.clicked.connect(self.getSolve)

        self.ui.gameSave_action.triggered.connect(self.save_game)
        self.ui.solutionsSave_action.triggered.connect(self.save_solution)
        self.ui.openAction.triggered.connect(self.openGame)

        self.referenceAction = QAction(self)
        self.referenceAction.setObjectName("referenceAction")
        self.ui.menubar.addAction(self.referenceAction)
        self.referenceAction.setText('Справка')
        self.referenceAction.triggered.connect(self.show_reference)


    def createSolutionTabs(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 255, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        self.vald = QWidget()
        self.vald.setObjectName("vald")
        self.valdText = QTextBrowser(self.vald)
        self.valdText.setGeometry(QtCore.QRect(0, 0, 525, 501))
        self.valdText.setPalette(palette)
        self.valdText.setStyleSheet("background-color: rgb(247, 255, 245);")
        self.valdText.setPlaceholderText("")
        self.valdText.setObjectName("valdText")
        self.ui.solutions_tabs.addTab(self.vald, '')

        _translate = QtCore.QCoreApplication.translate
        self.ui.solutions_tabs.setTabText(self.ui.solutions_tabs.indexOf(self.vald),
                                                                     _translate("MainWindow", "Критерий Вальда"))

        self.bayes = QWidget()
        self.bayes.setObjectName("bayes")
        self.bayesText = QTextBrowser(self.bayes)
        self.bayesText.setGeometry(QtCore.QRect(0, 0, 525, 501))
        self.bayesText.setPalette(palette)
        self.bayesText.setStyleSheet("background-color: rgb(247, 255, 245);")
        self.bayesText.setPlaceholderText("")
        self.bayesText.setObjectName("bayesText")

        self.savidge = QWidget()
        self.savidge.setObjectName("savidge")
        self.savidgeText = QTextBrowser(self.savidge)
        self.savidgeText.setGeometry(QtCore.QRect(0, 0, 525, 501))
        self.savidgeText.setPalette(palette)
        self.savidgeText.setStyleSheet("background-color: rgb(247, 255, 245);")
        self.savidgeText.setPlaceholderText("")
        self.savidgeText.setObjectName("savidgeText")

        self.gurvits = QWidget()
        self.gurvits.setObjectName("gurvits")
        self.gurvitsText = QTextBrowser(self.gurvits)
        self.gurvitsText.setGeometry(QtCore.QRect(0, 0, 525, 501))
        self.gurvitsText.setPalette(palette)
        self.gurvitsText.setStyleSheet("background-color: rgb(247, 255, 245);")
        self.gurvitsText.setPlaceholderText("")
        self.gurvitsText.setObjectName("gurvitsText")

        #
        #
        # self.solutions_tabs.setTabText(self.solutions_tabs.indexOf(self.bayes),
        #                                _translate("MainWindow", "Критерий Байеса-Лапласа"))
        # self.solutions_tabs.setTabText(self.solutions_tabs.indexOf(self.savidge),
        #                                _translate("MainWindow", "Критерий Сэвиджа"))
        # self.solutions_tabs.setTabText(self.solutions_tabs.indexOf(self.gurvits),
        #                                _translate("MainWindow", "Критерий Гурвица"))

    def save_game(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Сохранение исходных данных игры',
                                                  '/game_input.html',
                                                  '(*.html)')
        if _ == '(*.html)':
            self.model.saveGame(filename)
            with open(filename, 'a', encoding='utf-8') as file:
                file.write('\n<br>Коэффициент пессимизма равен ' + self.ui.weightLabel.text()+"</body></html>")
            self.ui.statusbar.showMessage(f'Исходные данные игры сохранены в {filename}', 4000)

    def save_solution(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Сохранение решения игры',
                                                  '/game_solution.html',
                                                  '(*.html)')
        if _ == '(*.html)':
            self.model.saveGame(filename)
            with open(filename, 'a', encoding='utf-8') as file:
                file.write('\n<br>Коэффициент пессимизма равен ' + self.ui.weightLabel.text())
                file.write('<h2>Решение игры:</h2>\r\n')
                if self.valdText.toPlainText() != '':
                    file.write('<h3>Критерий Вальда</h3>\r\n')
                    file.write(self.valdText.toHtml().split('Вычисление:</span></h4>')[1].replace('</body></html>', ''))
                if self.bayesText.toPlainText() != '':
                    file.write('<h3>Критерий Байеса-Лапласа</h3>\r\n')
                    file.write(self.bayesText.toHtml().split('Вычисление:</span></h4>')[1].replace('</body></html>', ''))
                if self.savidgeText.toPlainText() != '':
                    file.write('<h3>Критерий Сэвиджа</h3>\r\n')
                    file.write(self.savidgeText.toHtml().split('Вычисление:</span></h4>')[1].replace('</body></html>', ''))
                if self.gurvitsText.toPlainText() != '':
                    file.write('<h3>Критерий Гурвица</h3>\r\n')
                    file.write(self.gurvitsText.toHtml().split('Вычисление:</span></h4>')[1].replace('</body></html>', ''))
                file.write('</body></html>')
            self.ui.statusbar.showMessage(f'Решение игры сохранено в {filename}', 4000)

    def openGame(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Загрузка исходных данных игры',
                                                  'game_input.html',
                                                  '(*.html)')
        if _ == '(*.html)':
            self.model.loadGame(filename)
            with open(filename, 'r', encoding='utf-8') as file:
                f = file.readlines()
                weight = float(f[-1].split(' ')[3].split('<')[0])
                self.ui.weightLabel.setText(str(weight))
            self.ui.statusbar.showMessage(f'Загружено из {filename}', 4000)

    def showEditWindow(self):
        copy = self.model.copy()
        self.edit_win.ui.gameView.setModel(copy)
        self.edit_win.ui.probabylityTable.setModel(GamePropertiesModel(copy))
        self.edit_win.show()

    def show_reference(self):
        self.reference_win.show()

    def editModel(self):
        if self.edit_win.result() == 1:
            self.model.setfromObj(self.edit_win.ui.gameView.model())
            self.ui.gameView.resizeColumnsToContents()
            self.ui.weightLabel.setText(str(self.edit_win.ui.weightSB.value()))
            # self.ui.probabylityTable.resizeColumnsToContents()

    def getSolve(self):
        _translate = QtCore.QCoreApplication.translate
        if self.ui.vald_check.isChecked() == True:
            report = self.model.solve('vald')
            self.valdText.setHtml(report)
            if self.ui.solutions_tabs.indexOf(self.vald) == -1:
                self.ui.solutions_tabs.addTab(self.vald, '')
                self.ui.solutions_tabs.tabBar().DrawWindowBackground()
                self.ui.solutions_tabs.setTabText(self.ui.solutions_tabs.indexOf(self.vald),
                                                  _translate("MainWindow", "Критерий Вальда"))
        else:
            self.valdText.setText('')
            if self.ui.solutions_tabs.indexOf(self.vald) != -1:
                self.ui.solutions_tabs.removeTab(self.ui.solutions_tabs.indexOf(self.vald))

        if self.ui.bayes_check.isChecked() == True:
            report = self.model.solve('bayes')
            if report == 'Ошибка':
                self.ui.statusbar.showMessage('Ошибка. Проверьте правильность введенных вероятностей реализации состояний.', 4000)
            else:
                self.bayesText.setHtml(report)
                if self.ui.solutions_tabs.indexOf(self.bayes) == -1:
                    self.ui.solutions_tabs.addTab(self.bayes, '')
                    self.ui.solutions_tabs.setTabText(self.ui.solutions_tabs.indexOf(self.bayes),
                                                      _translate("MainWindow", "Критерий Байеса-Лапласа"))
        else:
            self.bayesText.setText('')
            if self.ui.solutions_tabs.indexOf(self.bayes) != -1:
                self.ui.solutions_tabs.removeTab(self.ui.solutions_tabs.indexOf(self.bayes))

        if self.ui.savidge_check.isChecked() == True:
            report = self.model.solve('savidge')
            self.savidgeText.setHtml(report)
            if self.ui.solutions_tabs.indexOf(self.savidge) == -1:
                self.ui.solutions_tabs.addTab(self.savidge, '')
                self.ui.solutions_tabs.setTabText(self.ui.solutions_tabs.indexOf(self.savidge),
                                                _translate("MainWindow", "Критерий Сэвиджа"))
        else:
            self.savidgeText.setText('')
            if self.ui.solutions_tabs.indexOf(self.savidge) != -1:
                self.ui.solutions_tabs.removeTab(self.ui.solutions_tabs.indexOf(self.savidge))

        if self.ui.gurvits_check.isChecked() == True:
            print(float(self.ui.weightLabel.text()))
            report = self.model.solve('gurvits', float(self.ui.weightLabel.text()))
            self.gurvitsText.setHtml(report)
            if self.ui.solutions_tabs.indexOf(self.gurvits) == -1:
                self.ui.solutions_tabs.addTab(self.gurvits, '')
                self.ui.solutions_tabs.setTabText(self.ui.solutions_tabs.indexOf(self.gurvits),
                                                _translate("MainWindow", "Критерий Гурвица"))
        else:
            self.gurvitsText.setText('')
            if self.ui.solutions_tabs.indexOf(self.gurvits) != -1:
                self.ui.solutions_tabs.removeTab(self.ui.solutions_tabs.indexOf(self.gurvits))
        self.ui.toolBox.setCurrentIndex(1)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())