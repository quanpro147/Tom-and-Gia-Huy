from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from UI.user_interface.music import Sound
from PyQt5.QtWidgets import *

from game import saveloadsystem, Game


class LoadWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.load_label = QtWidgets.QLabel(self.centralwidget)
        self.load_label.setGeometry(QtCore.QRect(230, 20, 341, 131))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(72)
        self.load_label.setFont(font)
        self.load_label.setObjectName("load_label")
        self.listGame = QtWidgets.QListWidget(self.centralwidget)
        self.listGame.setGeometry(QtCore.QRect(270, 160, 291, 361))
        self.listGame.setObjectName("listGame")
        self.Play_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Play_Button.setGeometry(QtCore.QRect(650, 500, 111, 61))
        font = QtGui.QFont()
        font.setFamily("STZhongsong")
        font.setPointSize(20)
        self.Play_Button.setFont(font)
        self.Play_Button.setObjectName("pushButton")
        self.Del_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Del_Button.setGeometry(QtCore.QRect(40, 500, 111, 61))
        font = QtGui.QFont()
        font.setFamily("STZhongsong")
        font.setPointSize(20)
        self.Del_Button.setFont(font)
        self.Del_Button.setObjectName("pushButton_2")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(40, 40, 50, 50))
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.path = 'Do_an/SaveLoad/saveload.txt'
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.sound = Sound()
        self.sound.setUp()

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_label.setText(_translate("MainWindow", " Load Game"))
        self.Play_Button.setText(_translate("MainWindow", "Play"))
        self.Del_Button.setText(_translate("MainWindow", "Delete"))
        self.back_button.setIcon(QIcon("Do_an/UI/image/back.png"))
        self.back_button.clicked.connect(lambda: self.menu(MainWindow))

        self.Del_Button.clicked.connect(lambda: self.removeGame(MainWindow))
        self.Play_Button.clicked.connect(lambda: self.LoadGame(MainWindow))
        self.loadfilegame()


    def menu(self, MainWindow):
        from UI.user_interface.menu import MenuWidget
        self.sound.clickSound()
        #self.sound.pause_bgSound()
        self.MenuWindow = QtWidgets.QMainWindow()
        self.Menu = MenuWidget()
        self.Menu.setupUi(self.MenuWindow)
        self.MenuWindow.show()
        MainWindow.close()

    def loadfilegame(self):
        self.oldgame = saveloadsystem.readfile(self.path)
        self.listGame.addItems(self.oldgame)

    def removeGame(self, MainWindow):
        currentIndex = self.listGame.currentRow()
        item = self.listGame.item(currentIndex)
        if item is None:
            return
        question = QMessageBox.question(MainWindow, "Remove Student",
                                        "Do you want to remove this Game?" + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.listGame.takeItem(currentIndex)
            saveloadmanager = saveloadsystem('.save', 'Do_an/SaveLoad/game_manager')
            saveloadmanager.delete_file(item.text())
            del item

    def LoadGame(self, MainWindow):
        currentIndex = self.listGame.currentRow()
        item = self.listGame.item(currentIndex)
        game = Game()
        print(item.text())
        game.load(item.text())
        game.run()




    

