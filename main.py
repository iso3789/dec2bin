#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer


# Klasse für das Hauptfenster
class MyWindow(QMainWindow):
    def __init__(self): #Konstruktor in Python
        super().__init__()
        self.setMinimumSize(QSize(400, 400))  # Basisfenster wird aufgerufen und die Größe wird festgelegt  
        self.setWindowTitle('dec2bin') 


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

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
