#!/usr/bin/env python3
#Qt5 & Python dec2bin
#Ivan Dzido

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LED, LEDBoard
from signal import pause

# Klasse für das Hauptfenster
class MyWindow(QMainWindow): #Konstruktor in Python
    def __init__(self):
        super().__init__()
        self.leds = LEDBoard(18, 23, 24, 25)
        self.setGeometry(710, 440, 500, 200)
        self.setWindowTitle('dec2bin')

        # vbox anzeigen in QWidget
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        # Layout zusammenbauen
        vbox = QtWidgets.QVBoxLayout()
        wid.setLayout(vbox)
        
        # Slider + Label Anzeige Dezimalwert
        self.slider = QSlider(Qt.Horizontal,wid)
        self.slider.setMinimum(0)
        self.slider.setMaximum(15)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.valueChanged[int].connect(self.setValue)
        self.label = QLabel('0')
        
        # Sliderbox
        sliderbox = QHBoxLayout()
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)
        vbox.addLayout(sliderbox)
        
        # Labels fuer 4 Bits
        self.bitlabels = [QLabel("8"), QLabel("4"), QLabel("2"), QLabel("1")]
        bitbox = QHBoxLayout()
        
        
        vboxBitboxes = QVBoxLayout()
        vboxBitboxes.addLayout(bitbox)
        vboxBitboxes.setAlignment(Qt.AlignCenter)
        vbox.addLayout(vboxBitboxes)
        
        
        for index, bitlabel in enumerate(self.bitlabels):
            bitbox.addWidget(bitlabel)            
            bitlabel.setStyleSheet("background-color: rgb(140, 140, 140)")
            bitlabel.setFixedWidth(20)
            bitlabel.setFixedHeight(20)
            bitlabel.setAlignment(Qt.AlignCenter)
            
            
    def setValue(self, value):
        showValue=str(value)
        #print(value)
        self.label.setText(showValue)
        onColor = "background-color: rgb(255, 0, 0)"
        offColor = "background-color: rgb(140, 140, 140)"
        for i in range(4):
            div = 2 ** (3 - i)
            valueToCheck = int(value / div)
            if valueToCheck % 2 == 1:
                self.bitlabels[i].setStyleSheet(onColor)
                self.leds[i].on()
            else:
                self.bitlabels[i].setStyleSheet(offColor)
                self.leds[i].off()
                

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
