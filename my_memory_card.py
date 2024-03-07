from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel,QButtonGroup)
from random import shuffle , randint


class Question():
    def __init__(self,question1,right_answer,wrong1,wrong2,wrong3):
        self.question = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



question_list = []
question_list.append(Question("Koliko je 3 + 3",'6','3','4','5'))
question_list.append(Question("Kada je poceo Prvi Svijetski rat",'1914','1918','1917','1916'))
question_list.append(Question("Koli je poceo Prvi Srpski ustanak",'1804','1803','1805','1806'))
question_list.append(Question("Koja je najveca zemlja na svijetu",'Rusija','Kina','SAD','Kanada'))
question_list.append(Question("KOliko miliona stanovnika ima Srbija",'7','9','10','11'))
question_list.append(Question("KOje godine se desio Boj na Kosovu?",'1389','1380','1390','1387'))
question_list.append(Question("Koje godine se desila bitka na Marici?",'1971','1972','1970','1975'))
question_list.append(Question("Kako se zvao prvi srpski car",'Dusan','Marko',"Nemanja","Uros"))
question_list.append(Question("Koliko miliona stanovnika ima Hrvatska",'4','6','2','7'))
question_list.append(Question("Koliko miliona stanovnika ima Bosna",'3','5','2','6'))











app=QApplication([])
my_win = QWidget()

my_win.setWindowTitle("Memory Card")
text = QLabel ('')
RadioGrupBox = QGroupBox( 'answer question')
button = QPushButton('Answer')
radio1 = QRadioButton('Enetes')
radio2 = QRadioButton('Chulyms')
radio3 = QRadioButton('Smurfs')
radio4 = QRadioButton('Aleuts')

RadioGroup = QButtonGroup()
RadioGroup.addButton(radio1)
RadioGroup.addButton(radio2)
RadioGroup.addButton(radio3)
RadioGroup.addButton(radio4)




layaout_ans1 = QHBoxLayout()
layaout_ans2 = QVBoxLayout()
layaout_ans3 = QVBoxLayout()

layaout_ans2.addWidget(radio1)
layaout_ans2.addWidget(radio2)
layaout_ans3.addWidget(radio3)
layaout_ans3.addWidget(radio4)
layaout_ans1.addLayout(layaout_ans2)
layaout_ans1.addLayout(layaout_ans3)


RadioGrupBox.setLayout(layaout_ans1)


AnsGrupBox = QGroupBox('Test result')
lb_results = QLabel('Are you correct or not ?')
lb_correct = QLabel('The answer will be here!')
layaout_res = QVBoxLayout()
layaout_res.addWidget(lb_results,alignment = (Qt.AlignLeft | Qt.AlignTop))
layaout_res.addWidget(lb_correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGrupBox.setLayout(layaout_res)






hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()
main_line = QVBoxLayout()

hline1.addWidget(text , (Qt.AlignHCenter| Qt.AlignVCenter))
hline2.addWidget(RadioGrupBox)
hline2.addWidget(AnsGrupBox)
AnsGrupBox.hide()



hline3.addStretch(1)
hline3.addWidget(button, stretch=2)
hline3.addStretch(1)

main_line.addLayout(hline1,stretch=2)
main_line.addLayout(hline2,stretch=8)
main_line.addStretch(1)
main_line.addLayout(hline3,stretch=1)
main_line.addStretch(1)
main_line.addStretch(5)


def show_result():
    RadioGrupBox.hide()
    AnsGrupBox.show()
    button.setText('Next Question')

def show_question():
    AnsGrupBox.hide()
    RadioGrupBox.show()
    button.setText('Answer')
    RadioGroup.setExclusive(False)
    radio1.setChecked(False)
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [radio1,radio2,radio3,radio4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_results.setText(res)
    show_result()
    
        







def check_answer():
    if answers[0].isChecked():
        show_correct('Correct')
        my_win.score += 1
        print("Statistics\n-Total questions:",my_win.total,"\nRight answer:",my_win.score)
        print("Raiting :",(my_win.score / my_win.total*100),"%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect')
            print("Raiting :",(my_win.score / my_win.total*100),"%")



def next_question ():
    my_win.total += 1
    print("Statistics\n-Total questions:",my_win.total,"\nRight answer:",my_win.score)
    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask (q)
def click_ok():
    if button.text() == 'Answer':
        check_answer()
    else:
        next_question()







button.clicked.connect(click_ok)


button.clicked.connect(check_answer)
my_win.total = 0
my_win.score = 0

next_question()   


    






my_win.setLayout(main_line)
































my_win.show()
app.exec_()