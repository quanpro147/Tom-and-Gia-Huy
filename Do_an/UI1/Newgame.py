from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QSizePolicy, QMessageBox,
                             QFrame)
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
import sys
class NewGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)
        #Playbutton
        self.PlayButton = QPushButton(self)
        self.PlayButton.setGeometry(QRect(600,650,200,50))
        self.PlayButton.setStyleSheet("QPushButton{background-color:rgb(82,204, 206);border-radius:25px ;border: 3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}\n QPushButton:hover{background-color: rgb(3, 57, 108);border-radius:25px ;border :3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}")
        self.PlayButton.setText("PLAY")
        #Backbutton
        self.BackButton = QPushButton(self)
        self.BackButton.setGeometry(QRect(200, 650, 200, 50))
        self.BackButton.setText("Back")
        self.BackButton.setStyleSheet("QPushButton{background-color:rgb(82,204, 206);border-radius:25px ;border: 3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}\n QPushButton:hover{background-color: rgb(3, 57, 108);border-radius:25px ;border :3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}")

        self.Box_1 = QtWidgets.QGroupBox(self)
        self.Box_1.setGeometry(QtCore.QRect(200, 100, 600, 100))
        self.Box_1.setStyleSheet("border:1px solid black")
        #Human
        self.human = QtWidgets.QRadioButton(self.Box_1)
        self.human.setGeometry(QRect(20,20,120,60))
        self.human.setStyleSheet("border:none")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.human.setFont(font)
        self.human.setText("Player")
        #Bot

        self.cpt = QtWidgets.QRadioButton(self.Box_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cpt.setFont(font)
        self.cpt.setGeometry(QRect(300, 20, 120, 60))
        self.cpt.setStyleSheet("border:none")
        self.cpt.setText("BOT")
        #Box 2
        self.Box_2 = QtWidgets.QGroupBox(self)
        self.Box_2.setGeometry(QtCore.QRect(200, 300, 600, 100))
        self.Box_2.setStyleSheet("border:1px solid black")
        # easy
        self.ez = QtWidgets.QRadioButton(self.Box_2)
        self.ez.setGeometry(QRect(20, 20, 120, 60))
        self.ez.setStyleSheet("border:none")
        self.ez.setText("easy")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ez.setFont(font)
        # medium

        self.medium = QtWidgets.QRadioButton(self.Box_2)
        self.medium.setFont(font)
        self.medium.setGeometry(QRect(220, 20, 120, 60))
        self.medium.setStyleSheet("border:none")
        self.medium.setText("Medium")
        #Hard
        self.hard = QtWidgets.QRadioButton(self.Box_2)
        self.hard.setFont(font)
        self.hard.setGeometry(QRect(420, 20, 120, 60))
        self.hard.setStyleSheet("border:none")
        self.hard.setText("Hard")
        #Box 3
        self.Box_3 = QtWidgets.QGroupBox(self)
        self.Box_3.setGeometry(QtCore.QRect(200, 500, 600, 100))
        self.Box_3.setStyleSheet("border:1px solid black")
        # random
        self.random = QtWidgets.QRadioButton(self.Box_3)
        self.random.setGeometry(QRect(20, 20, 120, 60))
        self.random.setStyleSheet("border:none")
        self.random.setText("Random")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.random.setFont(font)
        #Option
        self.option = QtWidgets.QRadioButton(self.Box_3)
        self.option.setGeometry(QRect(320, 20, 120, 60))
        self.option.setStyleSheet("border:none")
        self.option.setText("OPTION")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option.setFont(font)



#app = QApplication(sys.argv)
#newgame = NewGame()
#newgame.show()
#sys.exit(app.exec_())


