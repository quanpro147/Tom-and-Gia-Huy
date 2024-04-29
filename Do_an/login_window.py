import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QMessageBox,QFrame
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
import json
import menu
import Register
def check_account(username:str,password:str):
    with open('account.json', 'r') as file:
        data = json.load(file)
        for acc in data:
            if acc['username'] == username:
                if acc['password'] == password:
                    return 1
                else:
                    return 0
        return -1
class loginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GAME")
        self.setStyleSheet(u"background-color:qradialgradient(cx: 0.1, cy: 0.2, radius: 1, fx: 1, fy: 1, stop: 0.42 rgba(176, 229, 208, 255), stop: 0.936 rgba(92, 202, 238, 105));\n"
"\n"
"")

        #create Frame
        self.frame_main = QFrame()
        self.frame_main.setFixedSize(400,600)
        self.frame_main.setStyleSheet("background-color:qlineargradient(x1: 0.338569, y1: 0.94055, x2: 0.992115, y2: 0.123027, stop: 0.071 rgba(255, 244, 228, 255), stop: 0.674 rgba(240, 246, 238, 255));border-radius:20px;box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5)")
        self.frame_main.setGraphicsEffect(QGraphicsDropShadowEffect())
        #create "WELCOME" line
        self.label_frame = QLabel(self.frame_main)
        self.label_frame.setGeometry(0,120,400,100)
        self.label_frame.setStyleSheet(u"background-color:rgba(0, 146, 255, 0.65);\n"
        "font: 28pt \"Work Sans\";\n"
        "border-radius:0px")
        self.label_frame.setText("WELCOME")
        self.label_frame.setAlignment(Qt.AlignCenter)
        #user_name
        self.User_name = QLineEdit(self.frame_main)
        self.User_name.setObjectName(u"lineEdit")
        self.User_name.setGeometry(QRect(80, 310, 211, 41))
        self.User_name.setStyleSheet(u"border:none;\n"
                                    "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                    "background-color:rgba(39, 89, 245, 0.13);border-radius:14px;font: 10pt \"Work Sans\";")
        self.User_name.setPlaceholderText("username")
        #password
        self.Password = QLineEdit(self.frame_main)
        self.Password.setObjectName(u"lineEdit_2")
        self.Password.setGeometry(QRect(80, 380, 211, 41))
        self.Password.setStyleSheet(u"border:none;\n"
                                      "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                      "background-color:rgba(39, 89, 245, 0.13);border-radius:15px;font: 10pt \"Work Sans\";")
        self.Password.setPlaceholderText("password")
        self.Password.setEchoMode(QLineEdit.Password)

        #create "Dont have an account ?"
        self.label_2 = QLabel(self.frame_main)
        self.label_2.setGeometry(QRect(70, 530, 161, 20))
        self.label_2.setStyleSheet(u"font: 9pt \"Space Grotesk\";color: rgba(0, 0, 245, 0.81);\n"
                                   "text-decoration: underline;qlineargradient(x1: 0.338569, y1: 0.94055, x2: 0.992115, y2: 0.123027, stop: 0.071 rgba(255, 244, 228, 255), stop: 0.674 rgba(240, 246, 238, 255));border-radius:20px;box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5)"
                                   "\n"
                                   "")
        self.label_2.setText("Dont have an account ?")


        #create button "login"
        self.login_button = QPushButton(self.frame_main)
        self.login_button.setObjectName(u"pushButton")
        self.login_button.setGeometry(QRect(70, 480, 231, 40))
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_button.setStyleSheet(
            u"background-color:qradialgradient(cx: 0.1, cy: 0.2, radius: 1, fx: 1, fy: 1, stop: 0 rgba(97, 186, 255, 255), stop: 0.901 rgba(166, 239, 253, 255));\n"
            "border-radius:10px;column-gap: 5px;\n"
            "border :2px solid gray;\n"
            "font: bold 8pt \"Space Grotesk\";font: 10pt \"Work Sans\";")
        self.login_button.setText("Login")
        self.login_button.clicked.connect(self.login1)
        # create "Sign up"
        self.sign_up_button = QPushButton(self.frame_main)
        self.sign_up_button.setObjectName(u"pushButton_3")
        self.sign_up_button.setGeometry(QRect(240, 530, 81, 20))
        self.sign_up_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.sign_up_button.setStyleSheet(u"color:rgb(0, 85, 255);\n"
                                        "font: 75 10pt \"Work Sans\";\n"
                                        "text-decoration: underline;\n"
                                        "")
        self.sign_up_button.setText("Sign up")
        self.sign_up_button.clicked.connect(self.register_window)

        #
        layout = QVBoxLayout()
        layout.addWidget(self.frame_main, alignment=Qt.AlignCenter)
        self.setMinimumSize(860, 900)
        self.setLayout(layout)
    def login1(self):
        username = self.User_name.text()
        password = self.Password.text()
        X = check_account(username,password)
        if(X ==0):
            QMessageBox.warning(self,"loi","wrong password ")
        elif (X == -1):
            QMessageBox.warning(self,"loi","account is not exist")
        else:
            self.menu_window()
    def register_window(self):
        self.W = Register.registerWidget()
        self.close()
        self.W.show()
    def menu_window(self):
        self.W =menu.MenuWidget()
        self.close()
        self.W.show()
















































































































































































































