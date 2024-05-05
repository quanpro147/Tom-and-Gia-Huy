import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
import os

def check_account(username:str,password:str):
    with open(os.path.join('Do_an', 'GUI', 'account.json'), 'r') as file:
        data = json.load(file)
        for acc in data:
            if acc['username'] == username:
                if acc['password'] == password:
                    return 1
                else:
                    return 0
        return -1
class registerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.label_frame = QLabel(self)
        self.label_frame.setGeometry(0,120,400,100)
        self.label_frame.setStyleSheet(u"background-color:rgba(0, 146, 255, 0.65);\n"
        "font: 28pt \"Work Sans\";\n"
        "border-radius:0px")
        self.label_frame.setText("REGISTER")
        self.label_frame.setAlignment(Qt.AlignCenter)
        # icon and icon_button
        pass_icon = QIcon()
        user_icon = QIcon()
        pass_icon.addFile('icon/password.jpg')
        user_icon.addFile('icon/username.jpg')
        self.pass_icon_button = QPushButton(self)
        self.user_icon_button = QPushButton(self)
        self.user_icon_button.setGeometry(QRect(50, 310, 40, 40))
        self.pass_icon_button.setGeometry(QRect(50, 380, 40, 40))
        self.user_icon_button.setIcon(user_icon)
        self.pass_icon_button.setIcon(pass_icon)
        #user_name
        self.User_name = QLineEdit(self)
        self.User_name.setObjectName(u"lineEdit")
        self.User_name.setGeometry(QRect(90, 310, 220, 40))
        self.User_name.setStyleSheet(u"border:none;\n"
                                    "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                    "background-color:rgba(39, 89, 245, 0.13);border-radius:14px;font: 10pt \"Work Sans\";")
        self.User_name.setPlaceholderText("username")
        #password
        self.Password = QLineEdit(self)
        self.Password.setObjectName(u"lineEdit_2")
        self.Password.setGeometry(QRect(90, 380, 220, 40))
        self.Password.setStyleSheet(u"border:none;\n"
                                      "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                      "background-color:rgba(39, 89, 245, 0.13);border-radius:15px;font: 10pt \"Work Sans\";")
        self.Password.setPlaceholderText("password")
        self.Password.setEchoMode(QLineEdit.Password)

        #create "Dont have an account ?"
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(70, 530, 161, 20))
        self.label_2.setStyleSheet(u"font: 9pt \"Space Grotesk\";color: rgba(0, 0, 245, 0.81);\n"
                                   "text-decoration: underline;qlineargradient(x1: 0.338569, y1: 0.94055, x2: 0.992115, y2: 0.123027, stop: 0.071 rgba(255, 244, 228, 255), stop: 0.674 rgba(240, 246, 238, 255));border-radius:20px;box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5)"
                                   "\n"
                                   "")
        self.label_2.setText("Already have an account ?")


        #create button "Sign Up"
        self.sign_up_button = QPushButton(self)
        self.sign_up_button.setObjectName(u"pushButton")
        self.sign_up_button.setGeometry(QRect(80, 480, 240, 40))
        self.sign_up_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.sign_up_button.setStyleSheet(
            u"background-color:qradialgradient(cx: 0.1, cy: 0.2, radius: 1, fx: 1, fy: 1, stop: 0 rgba(97, 186, 255, 255), stop: 0.901 rgba(166, 239, 253, 255));\n"
            "border-radius:10px;column-gap: 5px;\n"
            "border :2px solid gray;\n"
            "font: bold 8pt \"Space Grotesk\";font: 10pt \"Work Sans\";")
        self.sign_up_button.setText("Sign Up")
        self.sign_up_button.clicked.connect(self.register)
        # create "Sign up"
        self.login_button = QPushButton(self)
        self.login_button.setObjectName(u"pushButton_3")
        self.login_button.setGeometry(QRect(240, 530, 80, 20))
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_button.setStyleSheet(u"color:rgb(0, 85, 255);\n"
                                        "font: 75 10pt \"Work Sans\";\n"
                                        "text-decoration: underline;\n"
                                        "")
        self.login_button.setText("Login")
        
    def register(self):
        username = self.User_name.text()
        password = self.Password.text()
        if(check_account(username,password)!= -1):
            QMessageBox.warning(self,"loi","tai khoan da ton tai")
        else:
            with open(os.path.join('Do_an', 'GUI', 'account.json'),mode ='r',encoding= 'utf8') as file:
                data = json.load(file)
            with open(os.path.join('Do_an', 'GUI', 'account.json'),mode ='w',encoding= 'utf8') as file:
                newinf = {'username':username,'password':password}
                data.append(newinf)
                json.dump(data,file,indent= 4)
            QMessageBox.information(self,"thong bao","dang ki thanh cong")
