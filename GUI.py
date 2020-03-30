from os import system
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

app=QApplication([]) # make this a comment later

label=QLabel('RJ SENTIMENT ANALYSIS')
window=QWidget()
layout=QVBoxLayout()
app.setStyle('Fusion')

palette=QPalette()
palette.setColor(QPalette.ButtonText, Qt.blue)
palette.setColor(QPalette.Window,Qt.blue)
palette.setColor(QPalette.WindowText,Qt.blue)
palette.setColor(QPalette.Background,Qt.blue)
palette.setColor(QPalette.Foreground,Qt.blue)
app.setPalette(palette)

window.resize(1920,1080)
window.setWindowTitle('RJ SENTIMENT ANALYSIS')

app.setStyleSheet("QPushButton {margin: 75ex;}")

button1=QPushButton('1) Twitter Sentiment Analysis')
button1.resize(480,480)
button2=QPushButton('2) Enter your own sentence')
button3=QPushButton('3) Try to make a NN and then use sa')
screen = QtGui.QDesktopWidget().screenGeometry()

def run_sa1():
    import sa1

def run_sa2():
    import sa2

button1.clicked.connect(run_sa1)
layout.addWidget(button1)

button2.clicked.connect(run_sa2)
layout.addWidget(button2)

layout.addWidget(button3)

window.setLayout(layout)
window.show()

# label.show()

app.exec_()