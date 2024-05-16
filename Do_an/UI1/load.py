from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QSizePolicy, QMessageBox,
                             QFrame)
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
import sys
class LoadWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)
        #Label
        self.Label = QLabel(self)
        self.Label.setGeometry(QRect(300,100,400,100))
        
        self.Label.setStyleSheet("border:2px solid black;font: bold 40pt \"Freestyle Script\"")
        self.Label.setAlignment(Qt.AlignCenter)
        self.Label.setText("LOAD GAME")
        #Play_Button
        self.Play_Button = QPushButton(self)
        self.Play_Button.setGeometry(QtCore.QRect(600, 600, 200, 60))
        self.Play_Button.setText("PLAY")
        #Delete_Butotn
        self.Delete_Button = QPushButton(self)
        self.Delete_Button.setGeometry(QtCore.QRect(200, 600, 200, 60))
        self.Delete_Button.setText("DELETE")
        #List_game
        self.listGame = QListWidget(self)
        self.listGame.setGeometry(QRect(200,250,600,300))
        #add Icon
        Icon = QIcon()
        Icon.addFile('Do_an/UI/UI1/Icon/Back.webp')
        self.Back_Button = QPushButton(self)
        self.Back_Button.setGeometry(QRect(0, 0,100, 40))
        self.Back_Button.setIcon(Icon)
        self.Back_Button.setText("Back")



