#подключение библиотек

#создание элементов интерфейса

#привязка элементов к вертикальной линии

#обработка событий

#запуск приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel , QVBoxLayout
from random import randint


def show_winer():
    winer = randint(1 , 100)
    number.setText(str(winer))



app = QApplication([])
window = QWidget()
v_line = QVBoxLayout()
number =QLabel('?')
q = QLabel('рандомное число')
button = QPushButton('сгенерировать')
button.clicked.connect(show_winer)
v_line.addWidget(q)
v_line.addWidget(number)
v_line.addWidget(button)
window.setLayout(v_line)
window.show()
app.exec()