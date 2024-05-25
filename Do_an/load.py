from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QSizePolicy, QMessageBox,
                             QFrame)
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
from data_process import *
from game import *
import sys
class LoadWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)
        self.user_name =""
        #Label
        self.Label = QLabel(self)
        self.Label.setGeometry(QRect(300,100,400,100))
        
        self.Label.setStyleSheet("border:2px solid black;font: bold 40pt \"Freestyle Script\"")
        self.Label.setAlignment(Qt.AlignCenter)
        self.Label.setText("LOAD GAME")
        #Play_Button
        self.Play_Button = QPushButton(self)
        self.Play_Button.setGeometry(QtCore.QRect(600, 600, 200, 50))
        self.Play_Button.setStyleSheet("QPushButton{background-color:rgb(82,204, 206);border-radius:25px ;border: 3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}\n QPushButton:hover{background-color: rgb(3, 57, 108);border-radius:25px ;border :3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}")
        self.Play_Button.setText("PLAY")
        #Delete_Butotn
        self.Delete_Button = QPushButton(self)
        self.Delete_Button.setGeometry(QtCore.QRect(200, 600, 200, 50))
        self.Delete_Button.setStyleSheet("QPushButton{background-color:rgb(82,204, 206);border-radius:25px ;border: 3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}\n QPushButton:hover{background-color: rgb(3, 57, 108);border-radius:25px ;border :3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}")
        self.Delete_Button.setText("DELETE")
        #List_game
        self.listGame = QListWidget(self)
        self.listGame.setGeometry(QRect(200,250,600,300))
        #add Icon
        Icon = QIcon()
        Icon.addFile('Do_an/UI1/Icon/Back.webp')
        self.Back_Button = QPushButton(self)
        self.Back_Button.setGeometry(QRect(0, 0,100, 40))
        self.Back_Button.setIcon(Icon)
        self.Back_Button.setText("Back")
        #Load file game
        self.path = 'Do_an/SaveLoad/saveload.txt'
        self.loadfilegame()


    def loadfilegame(self):
        self.oldgame = loadGame(self.user_name)
        if(self.oldgame is not None):
            self.listGame.addItems(self.oldgame)



