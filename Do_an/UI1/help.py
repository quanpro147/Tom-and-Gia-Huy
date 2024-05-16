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
        #help label
        self.Help_label = QLabel(self)


app = QApplication(sys.argv)
login = LoginWidget()
login.show()
sys.exit(app.exec_())


