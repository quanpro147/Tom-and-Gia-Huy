import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QSizePolicy, QMessageBox,
                             QFrame)
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
import sys
class skin_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)
        self.image_display = QLabel(self)
        self.image_display.setGeometry(QRect(300,100,400,400))
        self.image_display.setStyleSheet("border:2px solid black")

        self.list_image = []
        self.change_button1 = QPushButton(self)
        self.change_button1.setGeometry(QRect(300,550,100,50))
        self.current_index = 0
        self.setList_image()
        self.image_display.setPixmap(QPixmap(self.list_image[0]))
        self.change_button1.clicked.connect(self.change_img_right)
        self.change_button2 = QPushButton(self)
        self.change_button2.setGeometry(QRect(600,550,100,50))
        self.change_button2.clicked.connect(self.change_img_left)
        QIcon1 = QIcon()
        QIcon1.addFile("Do_an/UI1/Image/left_next.png")
        self.change_button1.setIcon(QIcon1)
        QIcon2 = QIcon()
        QIcon2.addFile("Do_an/UI1/Image/right_next.png")
        self.change_button2.setIcon(QIcon2)


    def setList_image(self):
        a1 = "Do_an/UI1/Image/cat1"
        a2 = "Do_an/UI1/Image/cat2"
        a3 = "Do_an/UI1/Image/cat3"
        a4 = "Do_an/UI1/Image/cat4"
        self.list_image = [a1,a2,a3,a4]
    def change_img_right(self):
        self.current_index = (self.current_index+1)%4
        self.image_display.setPixmap(QPixmap(self.list_image[self.current_index]))
    def change_img_left(self):
        self.current_index = (self.current_index-1)%4
        self.image_display.setPixmap(QPixmap(self.list_image[self.current_index]))
app = QApplication(sys.argv)
app1 = skin_widget()
app1.show()
sys.exit(app.exec_())