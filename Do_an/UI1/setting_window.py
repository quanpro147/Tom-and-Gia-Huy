from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QSizePolicy, QMessageBox,
                             QFrame)
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
import sys
class Setting_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,400)
        self.MenuButton = QPushButton(self)

        #background
        def button(self):
            play_button = QPushButton(self)
            load_button = QPushButton(self)
            help_button = QPushButton(self)
            about_button = QPushButton(self)
            quit_button = QPushButton(self)
            Button = [play_button, load_button, help_button, about_button, quit_button]
            Rect = [QRect(400, 280 + i * 70, 200, 50) for i in range(5)]
            Text = ["MENU", "SAVE", "OPTION", "FINISH", "QUIT"]
            for i in range(5):
                Button[i].setText(Text[i])
                Button[i].setGeometry(Rect[i])
                Button[i].setStyleSheet(u"QPushButton{\n"
                                        "border: 3px  solid green;border-radius:25px;\n"
                                        "background-color:rgb(82,204, 206);\n"
                                        "text-align:Center;\n"
                                        "color:White;\n"
                                        "font: bold 10pt \"MS Shell Dlg 2\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border: 3px  solid black;\n"
                                        "border-radius:25px;\n"
                                        "background-color: rgb(3, 57, 108);\n"
                                        "\n"
                                        "color:White;\n"
                                        "font: bold 10pt \"MS Shell Dlg 2\";text-align: Center;\n"
                                        "	\n"
                                        "}\n"
                                        "")
            return Button