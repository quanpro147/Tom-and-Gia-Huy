import sys


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QMessageBox,QFrame
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
import json

import login_window


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
class menu_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        #create mainFrame
        self.mainFrame = QFrame()
        self.mainFrame.setFixedSize(900,700)


        # create Frame
        self.main_frame = QFrame(self.mainFrame)
        self.main_frame.setGeometry(QRect(100,150,700,500))
        self.main_frame.setStyleSheet(u"border: 2px solid black;border-radius:60px")
        self.main_frame.setGraphicsEffect(QGraphicsDropShadowEffect())
        # create playbutton

        self.play_button = QPushButton(self.main_frame)
        self.play_button.setGeometry(QRect(250, 130, 200, 40))
        self.play_button.setStyleSheet(u"QPushButton{\n"
"border: 3px  solid green;border-radius:15px;\n"
"background-color:rgb(0, 153, 153);\n"
"text-align:left;\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px  solid black;\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 128, 255), stop:0.51 rgba(38, 208, 206, 255), stop:1 rgba(26, 41, 128, 255));\n"
"\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"	\n"
"}\n"
"")

        icon = QIcon()
        icon.addFile("icon/radio-button.png")
        self.play_button.setText("              PLAY")
        self.play_button.setIcon(icon)
        # create load_button
        self.load_button = QPushButton(self.main_frame)
        self.load_button.setGeometry(QRect(250, 190, 200, 40))
        self.load_button.setStyleSheet(u"QPushButton{\n"
"border: 3px  solid green;border-radius:15px;\n"
"background-color:rgb(0, 153, 153);\n"
"text-align:left;\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px  solid black;\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 128, 255), stop:0.51 rgba(38, 208, 206, 255), stop:1 rgba(26, 41, 128, 255));\n"
"\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"	\n"
"}\n"
"")
        self.load_button.setIcon(icon)
        self.load_button.setText("              LOAD")
        # create helpbutton
        self.help_button = QPushButton(self.main_frame)
        self.help_button.setGeometry(QRect(250, 260, 200, 40))
        self.help_button.setStyleSheet(u"QPushButton{\n"
"border: 3px  solid green;border-radius:15px;\n"
"background-color:rgb(0, 153, 153);\n"
"text-align:left;\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px  solid black;\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 128, 255), stop:0.51 rgba(38, 208, 206, 255), stop:1 rgba(26, 41, 128, 255));\n"
"\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"	\n"
"}\n"
"")
        self.help_button.setIcon(icon)
        self.help_button.setText("              help")
        # crate log_out button
        self.log_out_button = QPushButton(self.main_frame)
        self.log_out_button.setGeometry(QRect(250, 320, 200, 40))
        self.log_out_button.setStyleSheet( u"QPushButton{\n"
"border: 3px  solid green;border-radius:15px;\n"
"background-color:rgb(0, 153, 153);\n"
"text-align:left;\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px  solid black;\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 128, 255), stop:0.51 rgba(38, 208, 206, 255), stop:1 rgba(26, 41, 128, 255));\n"
"\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"	\n"
"}\n"
"")
        self.log_out_button.setIcon(icon)
        self.log_out_button.setText("              BACK")
        self.log_out_button.clicked.connect(self.back)
        # create WELCOME
        self.label = QLabel(self.mainFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0,20,900,100))
        self.label.setStyleSheet(u"\n"
                                 "font: bold 28pt \"Segoe UI\";")
        self.label.setText("WELCOME TO TOM AND GIA HUY")
        self.label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()

        layout.addWidget(self.mainFrame, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.setMinimumSize(800,800)
    def back(self):
        self.W = login_window.loginWidget()
        self.close()
        self.W.show()







