from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QSizePolicy, QMessageBox,
                             QFrame)
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
import sys
from login import LoginWidget
from register import RegisterWidget
from menu import MenuWidget
from load import LoadWidget
from about import AboutWidget
from music import Sound
from data_process import check_account,add_user
from Newgame import NewGame
from game import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)
        self.gameWindow = None
        self.user_name = ""
        #background
        self.background = QLabel(self)
        self.background.setGeometry(QRect(0,0,1000,800))
        self.background.setPixmap(QtGui.QPixmap("Do_an/UI1/blue1.png"))
        # Stacked WIdget
        self.stWidget = QStackedWidget(self)
        self.stWidget.setGeometry(QRect(0,0,1000,800))
        #Login Window
        self.Login_window = LoginWidget()
        #Register_window
        self.Register_window = RegisterWidget()
        #Menu_Window
        self.Menu_Window = MenuWidget()
        #Load_Window
        self.Load_Window = LoadWidget()
        #About_Window
        self.About_Window = AboutWidget()
        # Play
        self.New_Window = NewGame()
        self.stWidget.addWidget(self.Login_window)
        self.stWidget.addWidget(self.Register_window)
        self.stWidget.addWidget(self.Menu_Window)
        self.stWidget.addWidget(self.Load_Window)
        self.stWidget.addWidget(self.About_Window)
        self.stWidget.addWidget(self.New_Window)
        self.stWidget.setCurrentIndex(0)
        #setup Sound
        self.sound = Sound()
        self.sound.setUp()
        # login -> Menu
        self.Login_window.login_button.clicked.connect(self.login)
        # login -> register
        self.Login_window.sign_up_button.clicked.connect(self.register)
        # register -> login
        self.Register_window.login_button.clicked.connect(self.LOG_IN)
        # menu -> load
        self.Menu_Window.load_button.clicked.connect(self.Load)
        #menu -> about
        self.Menu_Window.about_button.clicked.connect(self.about)
        # load -> menu
        self.Load_Window.Back_Button.clicked.connect(self.back)
        #about -> menu
        self.About_Window.Back_Button.clicked.connect(self.back)
        #Newgame -> Menu
        self.New_Window.BackButton.clicked.connect(self.back)
        #Menu -> NewGame
        self.Menu_Window.play_button.clicked.connect(self.newgame)
        #quit
        self.Menu_Window.quit_button.clicked.connect(self.quit)
        #Create new account
        self.Register_window.sign_up_button.clicked.connect(self.Create_account)
        #Vao game
        self.New_Window.PlayButton.clicked.connect(self.play)
        #Load Old game
        self.Load_Window.Play_Button.clicked.connect(self.LoadGame)
        #
        self.Menu_Window.log_out_button.clicked.connect(self.LOG_OUT)

    def login(self):
        self.sound.clickSound()
        filename = "Do_an/UI/user_interface/account.json"
        username = self.Login_window.User_name.text()
        password = self.Login_window.Password.text()

        # Thực hiện kiểm tra tên người dùng và mật khẩu ở đây
        if check_account(filename, username, password) == 1:
            self.user_name = username
            self.Load_Window.user_name = username
            self.Login_window.User_name.clear()
            self.Login_window.Password.clear()
            self.stWidget.setCurrentIndex(2)
            self.Menu_Window.change_Vol()
        else:
            QMessageBox.warning(self, "Lỗi", "Tên người dùng hoặc mật khẩu không đúng!")
    def register(self):
        self.sound.clickSound()
        self.Login_window.User_name.clear()
        self.Login_window.Password.clear()
        self.stWidget.setCurrentIndex(1)
    def LOG_OUT(self):
        self.stWidget.setCurrentIndex(0)
    def LOG_IN(self):
        self.sound.clickSound()
        self.Register_window.User_name.clear()
        self.Register_window.Password.clear()
        
        self.stWidget.setCurrentIndex(0)
    def Load(self):
        self.sound.clickSound()
        
        self.stWidget.setCurrentIndex(3)
    def about(self):
        self.sound.clickSound()
        
        self.stWidget.setCurrentIndex(4)

    def back(self):
        self.sound.clickSound()
        if(self.New_Window.Custom):
            self.New_Window.Custom = False
            self.New_Window.Off_Custom()
        else:
            self.stWidget.setCurrentIndex(2)
    def quit(self):
        self.close()
    def Create_account(self):
        self.sound.clickSound()
        filename = "Do_an/UI/user_interface/account.json"
        username = self.Register_window.User_name.text()
        password = self.Register_window.Password.text()

        # Thực hiện kiểm tra tên người dùng và mật khẩu ở đây
        if check_account(filename, username, password) == 1:
            QMessageBox.warning(self, "Lỗi", "Tên người dùng đã tồn tại!")
        elif check_account(filename, username, password) == -1:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập và mật khẩu phải có ít nhất 6 kí tự!")
        else:
            add_user(filename, username, password)
            QMessageBox.information(self, "Thông Báo", "Đăng Ký Thành Công!")
            self.stWidget.setCurrentIndex(0)
    def newgame(self):
        
        self.stWidget.setCurrentIndex(5)
        

    def play(self):
        self.Menu_Window.off_volume()
        #self.close()
        self.close()
        a1 = self.New_Window.difficult
        a2 = self.New_Window.mode
        a3 = self.New_Window.option
        a4 = self.New_Window.skin
        a5 = self.New_Window.Map
        if(a4 == "Default"):
            a4 = "Square"
        if(a2 == "auto"):
            game = Game(a1,a2,a3,'Square','green', self.user_name)
        else:
            game = Game(a1,a2,a3,a4,a5, self.user_name)
        game.run()
        #self.show()
            
    def LoadGame(self):
        
        currentIndex = self.Load_Window.listGame.currentRow()
        
        item = self.Load_Window.listGame.item(currentIndex)
        game = Game()
        
        if game.load(item.text()):
            if game.user_name == self.user_name:
                self.Menu_Window.sound.off_volume()
                self.close()
                
                game.run()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = MainWindow()
    login.show()
    sys.exit(app.exec_())



