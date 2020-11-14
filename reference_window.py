# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reference_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_referenceDialog(object):
    def setupUi(self, referenceDialog):
        referenceDialog.setObjectName("referenceDialog")
        referenceDialog.resize(940, 558)
        referenceDialog.setMaximumSize(QtCore.QSize(940, 560))
        self.content_tree = QtWidgets.QTreeWidget(referenceDialog)
        self.content_tree.setGeometry(QtCore.QRect(10, 30, 281, 520))
        self.content_tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.content_tree.setAlternatingRowColors(True)
        self.content_tree.setIndentation(18)
        self.content_tree.setUniformRowHeights(False)
        self.content_tree.setObjectName("content_tree")
        item_0 = QtWidgets.QTreeWidgetItem(self.content_tree)
        self.item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.item_0 = QtWidgets.QTreeWidgetItem(self.content_tree)
        item_0 = QtWidgets.QTreeWidgetItem(self.content_tree)
        self.reference_text = QtWidgets.QTextBrowser(referenceDialog)
        self.reference_text.setGeometry(QtCore.QRect(309, 31, 621, 520))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.reference_text.setFont(font)
        self.reference_text.setObjectName("reference_text")
        self.test_againBt = QtWidgets.QPushButton(referenceDialog)
        self.test_againBt.setGeometry(QtCore.QRect(530, 440, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_againBt.setFont(font)
        self.test_againBt.setStyleSheet("background-color: rgb(85, 170, 127)")
        self.test_againBt.setObjectName("test_againBt")

        self.retranslateUi(referenceDialog)
        QtCore.QMetaObject.connectSlotsByName(referenceDialog)

    def retranslateUi(self, referenceDialog):
        _translate = QtCore.QCoreApplication.translate
        referenceDialog.setWindowTitle(_translate("referenceDialog", "Справка"))
        self.content_tree.headerItem().setText(0, _translate("referenceDialog", "Содержание"))
        __sortingEnabled = self.content_tree.isSortingEnabled()
        self.content_tree.setSortingEnabled(False)
        self.content_tree.topLevelItem(0).setText(0, _translate("referenceDialog", "Теоритические сведения"))
        self.content_tree.topLevelItem(0).child(0).setText(0, _translate("referenceDialog", "Понятие игры с природой"))
        self.content_tree.topLevelItem(0).child(1).setText(0, _translate("referenceDialog", "Критерии выбора оптимальных решений"))
        self.content_tree.topLevelItem(0).child(1).child(0).setText(0, _translate("referenceDialog", "Критерий Вальда"))
        self.content_tree.topLevelItem(0).child(1).child(1).setText(0, _translate("referenceDialog", "Критерий Байеса-Лапласа"))
        self.content_tree.topLevelItem(0).child(1).child(2).setText(0, _translate("referenceDialog", "Критерий Сэвиджа"))
        self.content_tree.topLevelItem(0).child(1).child(3).setText(0, _translate("referenceDialog", "Критерий Гурвица"))
        self.content_tree.topLevelItem(1).setText(0, _translate("referenceDialog", "Проверка знаний"))
        self.content_tree.topLevelItem(2).setText(0, _translate("referenceDialog", "Как работать с программой"))
        self.content_tree.setSortingEnabled(__sortingEnabled)
        self.reference_text.setHtml(_translate("referenceDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:10pt; font-weight:600; color:#000000; background-color:#ffffff;\">ПОНЯТИЕ ИГРЫ С ПРИРОДОЙ</span><span style=\" font-family:\'Times New Roman\'; font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">Математическая теория игр дает научно обоснованные рекомендации поведения в конфликтных ситуациях. При принятии решений в ситуации, в которой при выборе определенной стратегии действия исход зависит от неопределенных факторов, неподвластных оперирующей стороне и неизвестных ей в момент принятия решения. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">Неопределенность исхода может быть обусловлена как сознательными действиями активных противников, так и несознательными, пассивными проявлениями, например, стихийных сил природы: дождя, солнца, ветра, лавины и т.п. В таких случаях исключается возможность точного предсказания исхода. В одних конфликтах противоположной стороной выступает сознательно и целенаправленно действующий активный противник, заинтересованный в нашем поражении, который сознательно препятствует успеху, добивается победы любыми средствами. В других конфликтах такого сознательного противника нет, а действуют лишь так называемые «слепые силы природы»: погодные условия, состояние торгового оборудования на предприятии, болезни сотрудников, нестабильность экономической ситуации, рыночная конъюнктура, динамика курсов валют, уровень инфляции, налоговая политика, изменяющийся покупательский спрос и т.п. В таких случаях природа не злонамеренна и выступает пассивно, причем иногда во вред человеку, а иногда к его выгоде, однако ее состояние и проявление могут ощутимо влиять на результат деятельности. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-weight:600;\">Модель</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\"> такой конфликтной ситуации имеет вид: </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">&lt;</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">U</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">, </span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">V</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">, </span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">W</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">&gt;, </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">где </span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">U</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">={</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">u</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic; vertical-align:sub;\">i</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">} – множество стратегий (решений), </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">V</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">={</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">v</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic; vertical-align:sub;\">j</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">} – множество состояний природы, </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">W</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">=|</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">w</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic; vertical-align:sub;\">ij</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">| – матрица решений, элемент матрицы </span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">w</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic; vertical-align:sub;\">ij</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\"> содержит доходы (или потери) от выбора стратегии </span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">u</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic; vertical-align:sub;\">i</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\"> при реализации состояния природы </span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">v</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic; vertical-align:sub;\">j</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt; color:#000000; background-color:#ffffff;\">Содержательное отличие матрицы выигрышей в игре «с природой» от платежной матрицы конечной антагонистической игры заключается в том, что элементы столбцов этой матрицы не являются проигрышами «природы» при соответствующих ее состояниях. Выигрыши </span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic;\">w</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-style:italic; vertical-align:sub;\">ij</span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; color:#000000; background-color:#ffffff; vertical-align:sub;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; color:#000000; background-color:#ffffff;\">платит, естественно, не природа, а некая третья сторона или совокупность сторон, влияющих на принятие решения ЛПР, и объединенных в понятие «природа».</span><span style=\" font-family:\'Times New Roman\'; font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">В данном программном продукте реализованы 4 критерия выбора оптимальной стратегии: </span><span style=\" font-family:\'Times New Roman\'; font-size:9pt; font-weight:600;\">Вальда, Байеса-Лапласа, Сэвиджа и Гурвица. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">Общие рекомендации по выбору того или иного критерия дать затруднительно. Однако, если не допустим даже минимальный риск, рекомендуется применить критерий Вальда, иначе можно воспользоваться критерием Сэвиджа. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">Также можно одновременно применить различные критерии, после этого среди отобранных оптимальных решений выделить окончательное решение. Таким образом можно ослабить влияние субъективного фактора и лучше изучить проблему принятия решения.</span><span style=\" font-family:\'Times New Roman\'; font-size:8pt;\"> </span></p></body></html>"))
        self.test_againBt.setText(_translate("referenceDialog", "Пройти тест заново"))
