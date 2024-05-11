from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
class mainwindow(QMainWindow):
    def __int__(self):
        super().__int__()
        self.setObjectName("Login_MainWindow")
        self.setFixedSize(800, 600)
        self.stWidget = QStackedWidget(self)
        self.stWidget.setGeometry(QRect(0, 0, 400, 600))
        # create widget1
        self.widget1 = QWidget()
        self.widget2 = QWidget()
        self.widget3 = QWidget()
