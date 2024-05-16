from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QSizePolicy, QMessageBox,
                             QFrame)
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
import sys
class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)

        #background


         #Label
        self.label = QLabel(self)
        self.label.setGeometry(200,100,600,100)
        self.label.setStyleSheet(
        "font: 32pt \"Segoe Print\";\n"
        "border-radius:0px")
        self.label.setText("WELCOME")
        self.label.setAlignment(Qt.AlignCenter)
        # Icon
        #pass_icon = QIcon()
        #user_icon = QIcon()
        # pass_icon.addFile('icon/password.jpg')
        # user_icon.addFile('icon/username.jpg')
        # self.pass_icon_button = QPushButton(self)
        # self.user_icon_button = QPushButton(self)
        # self.user_icon_button.setGeometry(QRect(50, 310, 40, 40))
        # self.pass_icon_button.setGeometry(QRect(50, 380, 40, 40))
        # self.user_icon_button.setIcon(user_icon)
        # self.pass_icon_button.setIcon(pass_icon)
        # login button
        self.login_button = QPushButton(self)
        self.login_button.setGeometry(QRect(380, 500, 240, 40))
        self.login_button.setStyleSheet(
            u"background-color:qradialgradient(cx: 0.1, cy: 0.2, radius: 1, fx: 1, fy: 1, stop: 0 rgba(97, 186, 255, 255), stop: 0.901 rgba(166, 239, 253, 255));\n"
            "border-radius:10px;column-gap: 5px;\n"
            "border :2px solid gray;\n"
            "font: bold 8pt \"Segoe Print\";"
        )
        self.login_button.setText("Login")
        # Sign up Button
        self.sign_up_button = QPushButton(self)
        self.sign_up_button.setObjectName(u"pushButton_3")
        self.sign_up_button.setGeometry(QRect(460+100, 560, 80, 40))
        self.sign_up_button.setCursor(QCursor(Qt.PointingHandCursor))
        style = 0
        self.sign_up_button.setStyleSheet("font: 75 10pt \"Segoe Print\";text-decoration: underline;border: 0px")
        self.sign_up_button.setText("Sign up")
        # create "Dont have an account ?"
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(260+100, 560, 200, 40))
        self.label_2.setStyleSheet("font: 9pt \"Segoe Print\";border :0px solid black")
        self.label_2.setText("Dont have an account ?")
        # User_name
        self.User_name = QLineEdit(self)
        self.User_name.setObjectName(u"lineEdit")
        self.User_name.setGeometry(QRect(290+100, 310, 220, 40))
        self.User_name.setStyleSheet(u"border:1px solid black;\n"
                                     "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                     "background-color:rgba(39, 89, 245, 0.13);font: 10pt \"Segoe Script\";")
        self.User_name.setPlaceholderText("username")
        #password
        self.Password = QLineEdit(self)
        self.Password.setObjectName(u"lineEdit_2")
        self.Password.setGeometry(QRect(290+100, 390, 220, 40))
        self.Password.setStyleSheet(u"border:1px solid black;\n"
                                    "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                    "background-color:rgba(39, 89, 245, 0.13);font: 10pt \"Segoe Script\";")
        self.Password.setPlaceholderText("password")
        self.Password.setEchoMode(QLineEdit.Password)




