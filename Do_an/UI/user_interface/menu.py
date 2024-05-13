from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from UI.user_interface.music import Sound
from UI.user_interface.data_process import *
from UI.Menu.new import NewGame_Window

class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.newgame_button = QtWidgets.QPushButton(self.centralwidget)
        self.newgame_button.setGeometry(QtCore.QRect(330, 160, 141, 48))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.newgame_button.setFont(font)
        self.newgame_button.setObjectName("newgame_button")
        self.loadgame_button = QtWidgets.QPushButton(self.centralwidget)
        self.loadgame_button.setGeometry(QtCore.QRect(330, 240, 141, 48))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loadgame_button.setFont(font)
        self.loadgame_button.setObjectName("loadgame_button")
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(330, 320, 141, 48))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.help_button.setFont(font)
        self.help_button.setObjectName("help_button")
        self.About_button = QtWidgets.QPushButton(self.centralwidget)
        self.About_button.setGeometry(QtCore.QRect(330, 400, 141, 48))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.About_button.setFont(font)
        self.About_button.setObjectName("About_button")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(40, 40, 50, 50))

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(330, 480, 141, 48))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")


        font = QtGui.QFont()
        font.setPointSize(16)
        self.GameName_label = QtWidgets.QLabel(self.centralwidget)
        self.GameName_label.setGeometry(QtCore.QRect(180, 40, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(36)
        self.GameName_label.setFont(font)
        self.GameName_label.setObjectName("GameName_label")
        self.tom_label = QtWidgets.QLabel(self.centralwidget)
        self.tom_label.setGeometry(QtCore.QRect(20, 190, 231, 331))
        self.tom_label.setText("")
        self.tom_label.setPixmap(QtGui.QPixmap("Do_an/UI/image/Tom.png"))
        self.tom_label.setObjectName("tom_label")
        self.jerry_label = QtWidgets.QLabel(self.centralwidget)
        self.jerry_label.setGeometry(QtCore.QRect(540, 300, 241, 221))
        self.jerry_label.setText("")
        self.jerry_label.setPixmap(QtGui.QPixmap("Do_an/UI/image/jerry.png"))
        self.jerry_label.setObjectName("jerry_label")
        self.bg_music_button = QtWidgets.QPushButton(self.centralwidget)
        self.bg_music_button.setGeometry(QtCore.QRect(700, 30, 50, 50))
        self.bg_music_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bg_music_button_2.setGeometry(QtCore.QRect(700, 80, 50, 50))
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newgame_button.setText(_translate("MainWindow", "New Game"))
        self.loadgame_button.setText(_translate("MainWindow", "Load Game"))
        self.help_button.setText(_translate("MainWindow", "Help"))
        self.About_button.setText(_translate("MainWindow", "About Us"))
        self.exit_button.setText(_translate("MainWindow", "Exit Game"))
        self.GameName_label.setText(_translate("MainWindow", "Tâm và Gia Huy"))
        self.bg_music_button.setIcon(QIcon("Do_an/UI/image/music.png"))
        self.bg_music_button_2.setIcon(QIcon("Do_an/UI/image/mute.png"))
        self.back_button.setIcon(QIcon("Do_an/UI/image/back.png"))

        self.sound = Sound()
        self.sound.setUp()
        self.sound.bgSound()



        self.newgame_button.clicked.connect(lambda: self.newGame(MainWindow))
        self.loadgame_button.clicked.connect(lambda: self.loadGame(MainWindow))
        self.help_button.clicked.connect(lambda: self.help(MainWindow))
        self.About_button.clicked.connect(lambda: self.about(MainWindow))
        self.exit_button.clicked.connect(lambda: self.exit(MainWindow))
        self.bg_music_button.clicked.connect(self.sound.bgSound)
        self.bg_music_button_2.clicked.connect(self.sound.pause_bgSound)
        self.back_button.clicked.connect(lambda: self.login(MainWindow))

    def newGame(self, MainWindow):
        self.sound.clickSound()
        self.sound.pause_bgSound()
        
        self.NewWindow = QtWidgets.QMainWindow()
        self.New = NewGame_Window()
        self.New.setupUi(self.NewWindow)
        MainWindow.close()
        self.NewWindow.show()
        
    def loadGame(self, MainWindow):
        self.sound.clickSound()
        self.sound.pause_bgSound()

        from UI.Menu.load import LoadWindow
        self.LoadWindow = QtWidgets.QMainWindow()
        self.Load = LoadWindow()
        self.Load.setupUi(self.LoadWindow)
        self.LoadWindow.show()
        MainWindow.close()

    def help(self, MainWindow):
        self.sound.clickSound()
        self.sound.pause_bgSound()
        from UI.Menu.help import HelpWindow
        self.HelpWindow = QtWidgets.QMainWindow()
        self.Help = HelpWindow()
        self.Help.setupUi(self.HelpWindow)
        self.HelpWindow.show()
        MainWindow.close()
    def about(self, MainWindow):
        self.sound.clickSound()
        self.sound.pause_bgSound()
        from UI.Menu.about import AboutWindow
        self.AboutWindow = QtWidgets.QMainWindow()
        self.About = AboutWindow()
        self.About.setupUi(self.AboutWindow)
        self.AboutWindow.show()
        MainWindow.close()
    def exit(self, MainWindow):
        self.sound.clickSound()
        question = QMessageBox.question(self,"Exit App?",
                                        "Do you want to quit?",
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            MainWindow.close()
        

    def login(self, MainWindow):
        self.sound.clickSound()
        self.sound.pause_bgSound()
        from UI.user_interface.login import LoginWidget
        self.LoginWindow = QtWidgets.QMainWindow()
        self.Log = LoginWidget()
        self.Log.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        MainWindow.close()