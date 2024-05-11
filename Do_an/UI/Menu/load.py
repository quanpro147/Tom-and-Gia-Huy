import sys      
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QMessageBox,QFrame
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
import json
import os

def getdata(filename):
        with open(filename,encoding = 'utf8',mode = 'r') as file:
            data = json.load(file)
            print(data)
            gameData = []
            for i in data:
                gameData.append(i['name'])
            return gameData
print(getdata(os.path.join("Do_an","UI","Menu","loadgame.json")))

class LoadWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(660, 660)
        self.load = QListWidget(self)
        self.load.setGeometry(QRect(100,100,400,300))
        self.load.setStyleSheet('font-size: 20px;')

        data = getdata(os.path.join("Do_an","UI","Menu","loadgame.json"))

        for i in data:
            self.load.addItem(i)

        self.load.itemDoubleClicked.connect(self.getItem)
        self.back_button = QPushButton(self)
        self.back_button.setGeometry(QRect(100,550,200,50))
        self.back_button.setText("BACK")
        self.back_button.clicked.connect(self.back)


    def getItem(self, lstItem):
        print(self.load.currentItem().text())
        print(lstItem.text())
        print(self.load.currentRow())
    def back(self):
        from UI.user_interface.menu import MenuWidget
        self.MenuWindow = QtWidgets.QMainWindow()
        self.Menu = MenuWidget()
        self.Menu.setupUi(self.MenuWindow)
        self.MenuWindow.show()
        self.close()
         


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = LoadWidget()
    demo.show()

    sys.exit(app.exec_())