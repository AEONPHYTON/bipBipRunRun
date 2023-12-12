# use python 3.12

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import pygame
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont


class RunnerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pygame.init()

    def initUI(self):
        self.resize(500, 500)
        self.setStyleSheet("background-color : #FFFFFF")
        
        layout = QVBoxLayout()
        font = QFont("Arial", 15)
        bigFont = QFont("Arial", 18)
        gigaFont = QFont("Arial", 25, QFont.Bold)
        

        # make element for interface
        self.description = QLabel("Imposta il passo/1000 (ad es 05.15)\n usa il punto (.) per separare i min dai sec", self)
        self.description.setFont(bigFont)
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.description)
        
        self.paceInput = QLineEdit(self)
        self.paceInput.setFont(font)
        self.paceInput.setPlaceholderText("Passo/1000 (min.sec)")
        self.paceInput.setStyleSheet("background-color: #FFFFFF")
        layout.addWidget(self.paceInput)

        self.speedDisplay = QLabel("Velocità (km/h): ", self)
        self.speedDisplay.setFont(font)
        layout.addWidget(self.speedDisplay)

        self.distance = QLabel("A quale distanza sono i birilli? ", self)
        self.distance.setFont(bigFont)
        self.distance.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.distance)

        self.coneDistanceInput = QLineEdit(self)
        self.coneDistanceInput.setFont(font)
        self.coneDistanceInput.setPlaceholderText("Distanza tra i birilli (m)")
        layout.addWidget(self.coneDistanceInput)

        self.beepTimeDisplay = QLabel("Tempo per 'bip' (sec): ", self)
        self.beepTimeDisplay.setFont(font)
        layout.addWidget(self.beepTimeDisplay)

        self.infoCalculation = QLabel("Premi CALCOLA per impostare il timer", self)
        self.infoCalculation.setFont(bigFont)
        self.infoCalculation.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.infoCalculation) 

        calcButton = QPushButton("Calcola", self)
        calcButton.clicked.connect(self.calculate)
        calcButton.setFont(gigaFont)
        calcButton.setStyleSheet("background-color: #F95C39")
        calcButton.setMinimumSize(120, 70)
        layout.addWidget(calcButton)

        self.setLayout(layout)
        self.setWindowTitle('Bip Bip App')
        
        self.startBeep = QLabel("Premi AVVIA BIP per partire", self)
        self.startBeep.setFont(bigFont)
        self.startBeep.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.startBeep) 
        
        self.beepButton = QPushButton("Avvia Bip", self)
        self.beepButton.setFont(gigaFont)
        self.beepButton.setMinimumSize(120, 70)
        self.beepButton.clicked.connect(self.startBeeping)
        self.beepButton.setStyleSheet("background-color : green")
        layout.addWidget(self.beepButton)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.playBeep)

        self.setLayout(layout)
        self.setWindowTitle('Bip Bip App')

    def calculate(self):
        # split the pace
        pace = self.paceInput.text().split('.')
        pace_min = int(pace[0])
        pace_sec = int(pace[1])
        distance = int(self.coneDistanceInput.text())

        # calculation of the velocity
        total_min = pace_min + pace_sec / 60
        speed = 60 / total_min
        self.speedDisplay.setText(f"Velocità (km/h): {speed:.2f}")

        # calculation of the time between "bip"
        total_sec = pace_min * 60 + pace_sec
        time_per_km = total_sec / 1000
        beep_time = time_per_km * distance
        self.beepTimeDisplay.setText(f"Tempo per 'bip' ogni {distance} metri: {beep_time:.2f} secondi")

        self.beep_interval = int(beep_time * 1000)
        
    def startBeeping(self):
        if self.timer.isActive():
            self.timer.stop()
            self.beepButton.setText("Avvia Bip")
        else:
            self.timer.start(self.beep_interval)
            self.beepButton.setText("Ferma Bip")

    def playBeep(self):
        # upload and start the sound file
        beep_sound = pygame.mixer.Sound('beep.mp3')
        beep_sound.play()


def main():
    app = QApplication(sys.argv)
    ex = RunnerApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
