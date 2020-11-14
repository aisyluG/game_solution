# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_widget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 520)
        self.test_widget = QtWidgets.QWidget(Form)
        self.test_widget.setGeometry(QtCore.QRect(0, 0, 620, 520))
        self.test_widget.setObjectName("test_widget")
        self.label = QtWidgets.QLabel(self.test_widget)
        self.label.setGeometry(QtCore.QRect(0, 20, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.label.setObjectName("label")
        self.question_label = QtWidgets.QLabel(self.test_widget)
        self.question_label.setGeometry(QtCore.QRect(10, 70, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.question_label.setFont(font)
        self.question_label.setStyleSheet("background-color: rgb(180, 226, 168);")
        self.question_label.setTextFormat(QtCore.Qt.PlainText)
        self.question_label.setScaledContents(False)
        self.question_label.setObjectName("question_label")
        self.rb1 = QtWidgets.QRadioButton(self.test_widget)
        self.rb1.setGeometry(QtCore.QRect(60, 150, 541, 35))
        self.rb1.setObjectName("rb1")
        self.rb2 = QtWidgets.QRadioButton(self.test_widget)
        self.rb2.setGeometry(QtCore.QRect(60, 190, 541, 35))
        self.rb2.setObjectName("rb2")
        self.rb3 = QtWidgets.QRadioButton(self.test_widget)
        self.rb3.setGeometry(QtCore.QRect(60, 230, 541, 35))
        self.rb3.setObjectName("rb3")
        self.rb4 = QtWidgets.QRadioButton(self.test_widget)
        self.rb4.setGeometry(QtCore.QRect(60, 270, 541, 35))
        self.rb4.setObjectName("rb4")
        self.backBt = QtWidgets.QToolButton(self.test_widget)
        self.backBt.setEnabled(False)
        self.backBt.setGeometry(QtCore.QRect(340, 420, 91, 41))
        self.backBt.setStyleSheet("QToolButton:enabled{background-color:  rgb(129, 223, 167)}\n"
"QToolButton:!enabled{background-color:  rgb(223, 223, 223)}")
        self.backBt.setObjectName("backBt")
        self.forwardBt = QtWidgets.QToolButton(self.test_widget)
        self.forwardBt.setGeometry(QtCore.QRect(454, 420, 91, 41))
        self.forwardBt.setStyleSheet("QToolButton:enabled{background-color: rgb(85, 170, 127)}\n"
"QToolButton:!enabled{background-color:  rgb(223, 223, 223)}")
        self.forwardBt.setObjectName("forwardBt")
        self.finishBt = QtWidgets.QPushButton(self.test_widget)
        self.finishBt.setGeometry(QtCore.QRect(452, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.finishBt.setFont(font)
        self.finishBt.setStyleSheet("background-color: rgb(0, 222, 174);")
        self.finishBt.setObjectName("finishBt")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Проверка знаний"))
        self.question_label.setText(_translate("Form", "1. Игрой с природой называется:"))
        self.rb1.setText(_translate("Form", "Ситуация, в которых интересы сторон не совпадают"))
        self.rb2.setText(_translate("Form", "Игра, в которой участвуют два или более игроков,\n"
"и выигрыши которых противоположны"))
        self.rb3.setText(_translate("Form", "Игра, в которой игроки могут объединяться в группы, взяв на себя \n"
"некоторые обязательства перед другими игроками и координируя свои действия"))
        self.rb4.setText(_translate("Form", "Задача принятия решений в условиях неопределенности, когда игрок \n"
"взаимодействует с окружающей средой"))
        self.backBt.setText(_translate("Form", "Назад"))
        self.forwardBt.setText(_translate("Form", "Вперед"))
        self.finishBt.setText(_translate("Form", "Завершить тест"))
