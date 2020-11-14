# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(863, 667)
        Dialog.setStyleSheet("background-color: rgb(245, 255, 238)")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(440, 600, 361, 61))
        self.buttonBox.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gameView = QtWidgets.QTableView(Dialog)
        self.gameView.setGeometry(QtCore.QRect(10, 10, 781, 381))
        self.gameView.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.gameView.setObjectName("gameView")
        self.addStrategyBt = QtWidgets.QToolButton(Dialog)
        self.addStrategyBt.setGeometry(QtCore.QRect(800, 350, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addStrategyBt.setFont(font)
        self.addStrategyBt.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.addStrategyBt.setObjectName("addStrategyBt")
        self.delStrategyBt = QtWidgets.QToolButton(Dialog)
        self.delStrategyBt.setGeometry(QtCore.QRect(800, 290, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delStrategyBt.setFont(font)
        self.delStrategyBt.setStyleSheet("background-color:  rgb(129, 223, 167)")
        self.delStrategyBt.setObjectName("delStrategyBt")
        self.addStateBt = QtWidgets.QToolButton(Dialog)
        self.addStateBt.setGeometry(QtCore.QRect(740, 400, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addStateBt.setFont(font)
        self.addStateBt.setStyleSheet("background-color: rgb(85, 170, 127)")
        self.addStateBt.setObjectName("addStateBt")
        self.delStateBt = QtWidgets.QToolButton(Dialog)
        self.delStateBt.setGeometry(QtCore.QRect(670, 400, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delStateBt.setFont(font)
        self.delStateBt.setStyleSheet("background-color:  rgb(129, 223, 167)")
        self.delStateBt.setObjectName("delStateBt")
        self.probabylityTable = QtWidgets.QTableView(Dialog)
        self.probabylityTable.setGeometry(QtCore.QRect(10, 460, 781, 69))
        self.probabylityTable.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.probabylityTable.setObjectName("probabylityTable")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 540, 321, 51))
        self.widget.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.widget.setObjectName("widget")
        self.weightSB = QtWidgets.QDoubleSpinBox(self.widget)
        self.weightSB.setGeometry(QtCore.QRect(220, 10, 81, 31))
        self.weightSB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.weightSB.setDecimals(3)
        self.weightSB.setMaximum(1.0)
        self.weightSB.setSingleStep(0.001)
        self.weightSB.setProperty("value", 0.5)
        self.weightSB.setObjectName("weightSB")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Редактирование игры"))
        self.addStrategyBt.setToolTip(_translate("Dialog", "Добавить стратегию"))
        self.addStrategyBt.setText(_translate("Dialog", "+"))
        self.delStrategyBt.setToolTip(_translate("Dialog", "Удалить стратегию"))
        self.delStrategyBt.setText(_translate("Dialog", "-"))
        self.addStateBt.setToolTip(_translate("Dialog", "Добавить состояние"))
        self.addStateBt.setText(_translate("Dialog", "+"))
        self.delStateBt.setToolTip(_translate("Dialog", "Удалить состояние"))
        self.delStateBt.setText(_translate("Dialog", "-"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Коэффициент пессимизма</p></body></html>"))
