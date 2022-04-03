#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked)
        
        # Slider + Label Anzeige Dezimalwert
        self.slider = QSlider(Qt.Horizontal)
        self.label = QLabel('0') 
        sliderbox = QHBoxLayout()
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)

        # Labels fuer 4 Bits
        self.bitlabels = [] # Liste 
        # hier bitlabels erstellen      
        bitbox = QHBoxLayout()
        for bitlabel in self.bitlabels:
            bitbox.addWidget(bitlabel)

        # Layout zusammenbauen
        vbox = QVBoxLayout()
        vbox.addLayout(sliderbox)
        vbox.addLayout(bitbox)

        # vbox anzeigen in QWidget
        self.setLayout(vbox)

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()