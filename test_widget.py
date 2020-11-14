from PyQt5.QtWidgets import QWidget, QButtonGroup
from PyQt5.QtCore import pyqtSignal
from test_widget_ui import Ui_Form
from reference_source import test_questions

class TestWidget(QWidget):
    test_finished = pyqtSignal(str)
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.question_number = 0
        self.rb_answers = [self.ui.rb1, self.ui.rb2, self.ui.rb3, self.ui.rb4]

        self.rb_group = QButtonGroup(self)
        for i in range(4):
            self.rb_group.addButton(self.rb_answers[i], i)
        self.answers = [-1]*10

        # self.ui.finishBt.h+ide()

        self.ui.backBt.clicked.connect(self.previosQuestion)
        self.ui.forwardBt.clicked.connect(self.nextQuestion)
        self.ui.finishBt.clicked.connect(self.finish_test)
        self.rb_group.buttonToggled.connect(self.checkAnswer)

    def previosQuestion(self):
        self.answers[self.question_number] = self.rb_group.checkedId()
        self.question_number -= 1
        if self.answers[self.question_number] != -1:
            self.rb_answers[self.answers[self.question_number]].setChecked(True)
        elif self.rb_group.checkedId() is not None and self.rb_group.checkedId() != -1:
            self.resetRadioButtons()
        if self.question_number == 0:
            self.ui.backBt.setEnabled(False)
        elif self.question_number == 8:
            self.ui.forwardBt.setEnabled(True)
        que = test_questions[self.question_number]
        self.setQuestion(que)

    def nextQuestion(self):
        self.answers[self.question_number] = self.rb_group.checkedId()
        self.question_number += 1
        if self.answers[self.question_number] != -1:
            self.rb_answers[self.answers[self.question_number]].setChecked(True)
        elif self.rb_group.checkedId() is not None and self.rb_group.checkedId() != -1:
            self.resetRadioButtons()
        if self.question_number == 9:
            self.ui.forwardBt.setEnabled(False)
        elif self.question_number == 1:
            self.ui.backBt.setEnabled(True)
        que = test_questions[self.question_number]
        self.setQuestion(que)

    def setQuestion(self, question):
        self.ui.question_label.setText(f'{self.question_number + 1}. ' + question[0])
        for i in range(4):
            self.rb_answers[i].setText(question[1][i])

    def checkAnswer(self):
        self.answers[self.question_number] = self.rb_group.checkedId()

    def resetRadioButtons(self):
        id = self.rb_group.checkedId()
        if id is not None:
            self.rb_group.setExclusive(False)
            self.rb_answers[self.rb_group.checkedId()].toggle()
            self.rb_group.setExclusive(True)

    def finish_test(self):
        self.hide()
        res = self.get_test_result()
        self.test_finished.emit(('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\
<html><head><meta name="qrichtext" content="1" /><style type="text/css">\
p, li { white-space: pre-wrap; }\
</style></head><body style=" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;">\
<p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\
 -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:7.8pt;"><br /></p>'+
f'<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; \
text-indent:0px;"><span style=" font-family:\'Times New Roman\'; font-size:14pt;">Вы набрали </span><span style=" \
font-family:\'Times New Roman\'; font-size:14pt; font-weight:600;">{res[0]}</span><span style=" font-family:\'Times\
 New Roman\'; font-size:14pt;">!</span></p>\
<p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\
 -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:14pt;"><br /></p>\
<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; \
text-indent:0px;"><span style=" font-family:\'Times New Roman\'; font-size:12pt;">Ваши результаты:</span></p> {res[1]}\
<p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\
 -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:12pt;"><br /></p></body></html>'))
        self.resetResults()


    def get_test_result(self):
        result = ''
        score = 0
        for i in range(10):
            text = 'не'
            if self.answers[i] == test_questions[i][2]:
                score += 1
                text =''
            result += f'<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:20px; \
            margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\';\
             font-size:12pt;">	Вопрос {i+1} - {text}правильно</span></p>'
        if score == 0 or score >= 5:
            score = f'{score} баллов'
        elif score == 1:
            score = '1 балл'
        else:
            score = f'{score} балла'
        return score, result

    def resetResults(self):
        self.resetRadioButtons()
        self.answers = [-1] * 10
        self.question_number = 0
        self.setQuestion(test_questions[0])
        self.ui.backBt.setEnabled(False)
        self.ui.forwardBt.setEnabled(True)