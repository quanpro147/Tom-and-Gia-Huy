import sys


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QMessageBox,QFrame
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
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
#abc
class menu_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setStyleSheet('background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 rgba(48, 67, 82), stop: 1 rgba(215, 210, 204));border-radius:40px')
        #create Qlabel for image background

        #create mainFrame
        self.mainFrame = QFrame()
        self.mainFrame.setFixedSize(1600,900)
        self.mainFrame.setStyleSheet('background-color:qlineargradient(x1: 0.338569, y1: 0.94055, x2: 0.992115, y2: 0.123027, stop: 0.071 rgba(255, 244, 228, 255), stop: 0.674 rgba(240, 246, 238, 255));border-radius:20px;box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5)')
        self.imgFrame = QLabel(self.mainFrame)
        self.imgFrame.setGeometry(QRect(0,0,900,700))

        # create Frame
        self.main_frame = QFrame(self.mainFrame)
        self.main_frame.setGeometry(QRect(0,0,1600,900))


        #self.main_frame.setGraphicsEffect(QGraphicsDropShadowEffect())
        # create Widget1
        # help_UI
        self.help_UI = help_UI()
        self.stWidget = QStackedWidget(self.main_frame)
        self.stWidget.setGeometry(QRect(0, 0, 1600, 900))
        self.Widget1 = QWidget()
        self.stWidget.setStyleSheet('border: 0px solid white')
        self.stWidget.addWidget(self.Widget1)
        self.stWidget.addWidget(self.help_UI)
        #image background for frame
        #self.img_frame = QLabel(self.Widget1)
        #self.img_frame.setGeometry(QRect(0,0,700,500))
        #self.img_frame.setScaledContents(True)
        # create playbutton

        self.play_button = QPushButton(self.Widget1)
        self.play_button.setGeometry(QRect(700, 360, 200, 40))
        self.play_button.setStyleSheet(u"QPushButton{\n"
"border: 3px  solid green;border-radius:20px;\n"
"background-color:rgb(0, 153, 153);\n"
"text-align:left;\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px  solid black;\n"
"border-radius:20px;\n"
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
        self.load_button = QPushButton(self.Widget1)
        self.load_button.setGeometry(QRect(700, 430, 200, 40))
        self.load_button.setStyleSheet(u"QPushButton{\n"
"border: 3px  solid green;border-radius:20px;\n"
"background-color:rgb(0, 153, 153);\n"
"text-align:left;\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px  solid black;\n"
"border-radius:20px;\n"
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
        self.help_button = QPushButton(self.Widget1)
        self.help_button.setGeometry(QRect(700, 500, 200, 40))
        self.help_button.setStyleSheet(u"QPushButton{\n"
"border: 3px  solid green;border-radius:20px;\n"
"background-color:rgb(0, 153, 153);\n"
"text-align:left;\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px  solid black;\n"
"border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 128, 255), stop:0.51 rgba(38, 208, 206, 255), stop:1 rgba(26, 41, 128, 255));\n"
"\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"	\n"
"}\n"
"")
        self.help_button.setIcon(icon)
        self.help_button.setText("              HELP")
        self.help_button.clicked.connect(self.help)
        # create about_button
        self.about_button = QPushButton(self.Widget1)
        self.about_button.setGeometry(QRect(700, 570, 200, 40))
        self.about_button.setStyleSheet(u"QPushButton{\n"
                                       "border: 3px  solid green;border-radius:20px;\n"
                                       "background-color:rgb(0, 153, 153);\n"
                                       "text-align:left;\n"
                                       "color:White;\n"
                                       "font: bold 8pt \"MS Shell Dlg 2\";\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "border: 3px  solid black;\n"
                                       "border-radius:20px;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 128, 255), stop:0.51 rgba(38, 208, 206, 255), stop:1 rgba(26, 41, 128, 255));\n"
                                       "\n"
                                       "color:White;\n"
                                       "font: bold 8pt \"MS Shell Dlg 2\";\n"
                                       "	\n"
                                       "}\n"
                                       "")

        icon = QIcon()
        icon.addFile("icon/radio-button.png")
        self.about_button.setText("              ABOUT")
        self.about_button.setIcon(icon)
        # crate log_out button
        self.log_out_button = QPushButton(self.Widget1)
        self.log_out_button.setGeometry(QRect(700, 640, 200, 40))
        self.log_out_button.setStyleSheet( u"QPushButton{\n"
"border: 3px  solid green;border-radius:20px;\n"
"background-color:rgb(0, 153, 153);\n"
"text-align:left;\n"
"color:White;\n"
"font: bold 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px  solid black;\n"
"border-radius:20px;\n"
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
        # create exit_button

        self.exit_button = QPushButton(self.Widget1)
        self.exit_button.setGeometry(QRect(700, 710, 200, 50))
        self.exit_button.setStyleSheet(u"QPushButton{\n"
                                       "border: 3px  solid green;border-radius:25px;\n"
                                       "background-color:rgb(0, 153, 153);\n"
                                       "text-align:left;\n"
                                       "color:White;\n"
                                       "font: bold 8pt \"MS Shell Dlg 2\";\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "border: 3px  solid black;\n"
                                       "border-radius:25px;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 128, 255), stop:0.51 rgba(38, 208, 206, 255), stop:1 rgba(26, 41, 128, 255));\n"
                                       "\n"
                                       "color:White;\n"
                                       "font: bold 8pt \"MS Shell Dlg 2\";\n"
                                       "	\n"
                                       "}\n"
                                       "")
        icon = QIcon()
        icon.addFile("icon/radio-button.png")
        self.exit_button.setText("              EXIT")
        self.exit_button.setIcon(icon)
        self.exit_button.clicked.connect(self.exit)
        #tom and jerry
        self.jerry = QLabel(self.Widget1)
        self.jerry.setGeometry(QRect(100,100,300,400))
        self.jerry.setStyleSheet('background-image:url(Jerry.png)')
        self.tom = QLabel(self.Widget1)
        self.tom.setGeometry(QRect(1200,100, 300, 400))
        self.tom.setStyleSheet('background-image:url(Tom.png)')
        # create WELCOME
        self.label = QLabel(self.Widget1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(800-250,20,500,280))
        self.label.setStyleSheet("background-image:url(TGH.png)")
        self.label.setAlignment(Qt.AlignCenter)


        layout = QVBoxLayout()

        layout.addWidget(self.mainFrame, alignment=Qt.AlignCenter)
        self.stWidget.setCurrentIndex(0)

        self.setLayout(layout)
        self.setMinimumSize(800,800)
    def back(self):
        self.W = login_window.loginWidget()
        self.close()
        self.W.show()
    def exit(self):
        self.close()
    def help(self):
        self.stWidget.setCurrentIndex(1)
        print(123)
class help_UI(QWidget):
    def __int__(self):
        super().__int__()
        self.setGeometry(QRect(0,0,700,500))
        self.img = QLabel(self)
        self.img.setGeometry(QRect(0,0,700,500))
        self.butt = QPushButton(self)
        self.butt.setStyleSheet("border:2px solid black")
        self.butt.setGeometry(0,0,0,0)
        self.img.setStyleSheet('background-image:url(gameframe.png)')







