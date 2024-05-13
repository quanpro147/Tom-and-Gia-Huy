from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from UI.user_interface.music import Sound
from game import *

class NewGame_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NewGame_label = QtWidgets.QLabel(self.centralwidget)
        self.NewGame_label.setGeometry(QtCore.QRect(210, 30, 371, 131))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(72)
        self.NewGame_label.setFont(font)
        self.NewGame_label.setObjectName("NewGame_label")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(600, 500, 150, 70))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.play_button.setFont(font)
        self.play_button.setObjectName("play_button")
        self.Box_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.Box_1.setGeometry(QtCore.QRect(100, 160, 571, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Box_1.setFont(font)
        self.Box_1.setObjectName("Box_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Box_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.human = QtWidgets.QRadioButton(self.Box_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.human.setFont(font)
        self.human.setObjectName("human")
        self.horizontalLayout.addWidget(self.human)
        self.cpt = QtWidgets.QRadioButton(self.Box_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cpt.setFont(font)
        self.cpt.setObjectName("cpt")
        self.horizontalLayout.addWidget(self.cpt)
        self.Box_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.Box_2.setGeometry(QtCore.QRect(100, 280, 571, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Box_2.setFont(font)
        self.Box_2.setObjectName("Box_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Box_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ez = QtWidgets.QRadioButton(self.Box_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ez.setFont(font)
        self.ez.setObjectName("ez")
        self.horizontalLayout_2.addWidget(self.ez)
        self.medium = QtWidgets.QRadioButton(self.Box_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.medium.setFont(font)
        self.medium.setObjectName("medium")
        self.horizontalLayout_2.addWidget(self.medium)
        self.hard = QtWidgets.QRadioButton(self.Box_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hard.setFont(font)
        self.hard.setObjectName("hard")
        self.horizontalLayout_2.addWidget(self.hard)
        self.Box_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.Box_3.setGeometry(QtCore.QRect(100, 390, 571, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Box_3.setFont(font)
        self.Box_3.setObjectName("Box_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Box_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.random = QtWidgets.QRadioButton(self.Box_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.random.setFont(font)
        self.random.setObjectName("random")
        self.horizontalLayout_3.addWidget(self.random)
        self.edit = QtWidgets.QRadioButton(self.Box_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edit.setFont(font)
        self.edit.setObjectName("edit")
        self.horizontalLayout_3.addWidget(self.edit)
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(40, 40, 50, 50))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NewGame_label.setText(_translate("MainWindow", " New Game"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.Box_1.setTitle(_translate("MainWindow", "Chế độ Chơi"))
        self.human.setText(_translate("MainWindow", "Người chơi"))
        self.cpt.setText(_translate("MainWindow", "Máy chơi"))
        self.Box_2.setTitle(_translate("MainWindow", "Độ Khó"))
        self.ez.setText(_translate("MainWindow", "Dễ"))
        self.medium.setText(_translate("MainWindow", "Vừa"))
        self.hard.setText(_translate("MainWindow", "Khó"))
        self.Box_3.setTitle(_translate("MainWindow", "Tạo Mê Cung"))
        self.random.setText(_translate("MainWindow", "Ngẫu Nhiên"))
        self.edit.setText(_translate("MainWindow", "Tùy Chỉnh"))
        self.back_button.setIcon(QIcon("Do_an/UI/image/back.png"))
        self.back_button.clicked.connect(lambda: self.menu(MainWindow))
        self.play_button.clicked.connect(lambda: self.play(MainWindow))
        #khởi tạo âm thanh
        self.sound = Sound()
        self.sound.setUp()


    def menu(self, MainWindow):
        from UI.user_interface.menu import MenuWidget
        self.sound.clickSound()
        #self.sound.pause_bgSound()
        self.MenuWindow = QtWidgets.QMainWindow()
        self.Menu = MenuWidget()
        self.Menu.setupUi(self.MenuWindow)
        self.MenuWindow.show()
        MainWindow.close()
    
    def play(self, MainWindow):
        MainWindow.close()
        if self.human.isChecked():
            if self.ez.isChecked():
                if self.random.isChecked():  
                    game = Game('easy', 'not_auto', 'random')
                    game.run()
                else:
                    game = Game('easy', 'not_auto', 'edit')
                    game.run()
                    
            elif self.medium.isChecked():
                if self.random.isChecked():  
                    game = Game('medium', 'not_auto')
                    game.run()
                else:
                    game = Game('medium', 'not_auto')
                    #game.set_start_end()
                    game.run()
            else:
                if self.random.isChecked():  
                    game = Game('hard', 'not_auto')
                    game.run()
                else:
                    game = Game('hard', 'not_auto')
                    #game.set_start_end()
                    game.run()
        else:
            if self.ez.isChecked():
                if self.random.isChecked():  
                    game = Game('easy', 'auto')
                    game.run()
                else:
                    game = Game('easy', 'auto')
                    #game.set_start_end()
                    game.run()
            elif self.medium.isChecked():
                if self.random.isChecked():  
                    game = Game('medium', 'auto')
                    game.run()
                else:
                    game = Game('medium', 'auto')
                    #game.set_start_end()
                    game.run()
            else:
                if self.random.isChecked():  
                    game = Game('hard', 'auto')
                    game.run()
                else:
                    game = Game('hard', 'auto')
                    #game.set_start_end()
                    game.run()





