# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 700)
        MainWindow.setMaximumSize(QtCore.QSize(860, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(5, 5, 850, 641))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"border-color: rgb(44, 89, 66);")
        self.toolBox.setFrameShape(QtWidgets.QFrame.HLine)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.toolBox.setLineWidth(1)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 848, 583))
        self.page.setStyleSheet("border-color: rgb(65, 131, 97);")
        self.page.setObjectName("page")
        self.matrixPage_widget = QtWidgets.QWidget(self.page)
        self.matrixPage_widget.setGeometry(QtCore.QRect(0, 0, 850, 590))
        self.matrixPage_widget.setStyleSheet("\n"
"background-color:rgb(240, 240, 240)")
        self.matrixPage_widget.setObjectName("matrixPage_widget")
        self.gameView = QtWidgets.QTableView(self.matrixPage_widget)
        self.gameView.setGeometry(QtCore.QRect(0, 0, 850, 391))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.gameView.setPalette(palette)
        self.gameView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gameView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.gameView.setGridStyle(QtCore.Qt.SolidLine)
        self.gameView.setObjectName("gameView")
        self.gameView.horizontalHeader().setSortIndicatorShown(True)
        self.gameView.horizontalHeader().setStretchLastSection(False)
        self.gameView.verticalHeader().setCascadingSectionResizes(True)
        self.gameView.verticalHeader().setSortIndicatorShown(False)
        self.gameEditBt = QtWidgets.QPushButton(self.matrixPage_widget)
        self.gameEditBt.setGeometry(QtCore.QRect(60, 520, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(False)
        self.gameEditBt.setFont(font)
        self.gameEditBt.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.gameEditBt.setObjectName("gameEditBt")
        self.solveGameBt = QtWidgets.QPushButton(self.matrixPage_widget)
        self.solveGameBt.setGeometry(QtCore.QRect(490, 520, 300, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.solveGameBt.setFont(font)
        self.solveGameBt.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.solveGameBt.setObjectName("solveGameBt")
        self.widget = QtWidgets.QWidget(self.matrixPage_widget)
        self.widget.setGeometry(QtCore.QRect(0, 480, 311, 31))
        self.widget.setStyleSheet("background-color: rgb(197, 230, 188);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 241, 31))
        self.label.setObjectName("label")
        self.weightLabel = QtWidgets.QLabel(self.widget)
        self.weightLabel.setGeometry(QtCore.QRect(250, 0, 61, 31))
        self.weightLabel.setObjectName("weightLabel")
        self.probabylityTable = QtWidgets.QTableView(self.matrixPage_widget)
        self.probabylityTable.setGeometry(QtCore.QRect(0, 400, 850, 69))
        self.probabylityTable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.probabylityTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.probabylityTable.setObjectName("probabylityTable")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 848, 583))
        self.page_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.page_2.setObjectName("page_2")
        self.groupBox = QtWidgets.QGroupBox(self.page_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 261, 201))
        self.groupBox.setObjectName("groupBox")
        self.vald_check = QtWidgets.QCheckBox(self.groupBox)
        self.vald_check.setGeometry(QtCore.QRect(20, 30, 141, 20))
        self.vald_check.setChecked(True)
        self.vald_check.setObjectName("vald_check")
        self.bayes_check = QtWidgets.QCheckBox(self.groupBox)
        self.bayes_check.setGeometry(QtCore.QRect(20, 60, 211, 20))
        self.bayes_check.setObjectName("bayes_check")
        self.savidge_check = QtWidgets.QCheckBox(self.groupBox)
        self.savidge_check.setGeometry(QtCore.QRect(20, 90, 171, 20))
        self.savidge_check.setObjectName("savidge_check")
        self.gurvits_check = QtWidgets.QCheckBox(self.groupBox)
        self.gurvits_check.setGeometry(QtCore.QRect(20, 120, 151, 20))
        self.gurvits_check.setObjectName("gurvits_check")
        self.criteirions_choosedBt = QtWidgets.QPushButton(self.groupBox)
        self.criteirions_choosedBt.setGeometry(QtCore.QRect(130, 160, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.criteirions_choosedBt.setFont(font)
        self.criteirions_choosedBt.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.criteirions_choosedBt.setObjectName("criteirions_choosedBt")
        self.solutions_tabs = QtWidgets.QTabWidget(self.page_2)
        self.solutions_tabs.setGeometry(QtCore.QRect(300, 30, 525, 521))
        self.solutions_tabs.setAutoFillBackground(False)
        self.solutions_tabs.setStyleSheet("QTabBar::tab:selected {\n"
"    background: rgb(85, 170, 127);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: red;\n"
"}\n"
"QTabBar::tab:!selected:hover {\n"
"    background-color: green;\n"
"margin-top: 3px;\n"
"}")
        self.solutions_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.solutions_tabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.solutions_tabs.setDocumentMode(False)
        self.solutions_tabs.setTabsClosable(False)
        self.solutions_tabs.setObjectName("solutions_tabs")
        self.toolBox.addItem(self.page_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openAction = QtWidgets.QAction(MainWindow)
        self.openAction.setObjectName("openAction")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.gameSave_action = QtWidgets.QAction(MainWindow)
        self.gameSave_action.setObjectName("gameSave_action")
        self.solutionsSave_action = QtWidgets.QAction(MainWindow)
        self.solutionsSave_action.setObjectName("solutionsSave_action")
        self.file_menu.addAction(self.openAction)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.gameSave_action)
        self.file_menu.addAction(self.solutionsSave_action)
        self.menubar.addAction(self.file_menu.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(2)
        self.solutions_tabs.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Решение игр с природой"))
        self.gameEditBt.setText(_translate("MainWindow", "Редактировать"))
        self.solveGameBt.setText(_translate("MainWindow", "Решить"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Коэффициент пессимизма равен</p></body></html>"))
        self.weightLabel.setText(_translate("MainWindow", "0.5"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Матрица игры"))
        self.groupBox.setTitle(_translate("MainWindow", "Выберите критерии"))
        self.vald_check.setText(_translate("MainWindow", "Критерий Вальда"))
        self.bayes_check.setText(_translate("MainWindow", "Критерий Байеса-Лапласа"))
        self.savidge_check.setText(_translate("MainWindow", "Критерий Сэвиджа"))
        self.gurvits_check.setText(_translate("MainWindow", "Критерий Гурвица"))
        self.criteirions_choosedBt.setText(_translate("MainWindow", "Выбрать"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Критерии"))
        self.file_menu.setTitle(_translate("MainWindow", "Файл"))
        self.openAction.setText(_translate("MainWindow", "Открыть"))
        self.openAction.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_2.setText(_translate("MainWindow", "Сохранить игру"))
        self.gameSave_action.setText(_translate("MainWindow", "Сохранить игру"))
        self.gameSave_action.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.solutionsSave_action.setText(_translate("MainWindow", "Сохранить решение игры"))
