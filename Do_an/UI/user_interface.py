
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont 
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl

import json

#Các hàm quản lí tài khoản người dùng
def load_data(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data
def save_data(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
def check_account(file_name, username, password):
    data = load_data(file_name)
    if len(username) < 3 or len(password) < 6:
        return -1
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            return 1
    return 0
def add_user(file_name, username, password):
    data = load_data(file_name)
    data["users"].append({"username": username, "password": password})
    save_data(data, file_name)

class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Login_MainWindow")
        MainWindow.setFixedSize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(130, 170, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(220, 240, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(270, 330, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(380, 480, 151, 51))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(12)
        self.Register.setFont(font)
        self.Register.setObjectName("Register")
        self.GameName_label = QtWidgets.QLabel(self.centralwidget)
        self.GameName_label.setGeometry(QtCore.QRect(180, 40, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(36)
        self.GameName_label.setFont(font)
        self.GameName_label.setObjectName("GameName_label")
        self.jerry_label = QtWidgets.QLabel(self.centralwidget)
        self.jerry_label.setGeometry(QtCore.QRect(550, 320, 241, 221))
        self.jerry_label.setText("")
        self.jerry_label.setPixmap(QtGui.QPixmap("UI/image/jerry.png"))
        self.jerry_label.setObjectName("jerry_label")
        self.tom_label = QtWidgets.QLabel(self.centralwidget)
        self.tom_label.setGeometry(QtCore.QRect(-10, 210, 231, 331))
        self.tom_label.setText("")
        self.tom_label.setPixmap(QtGui.QPixmap("UI/image/Tom.png"))
        self.tom_label.setObjectName("tom_label")
        self.noAccount_label = QtWidgets.QLabel(self.centralwidget)
        self.noAccount_label.setGeometry(QtCore.QRect(170, 480, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.noAccount_label.setFont(font)
        self.noAccount_label.setObjectName("noAccount_label")
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(370, 170, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_edit.setFont(font)
        self.username_edit.setText("")
        self.username_edit.setObjectName("username_edit")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(370, 250, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password_edit.setFont(font)
        self.password_edit.setText("")
        self.password_edit.setObjectName("password_edit")
        MainWindow.setCentralWidget(self.centralwidget)

        # Tạo và cấu hình âm thanh (chưa xong)
        self.sound_effect = QSoundEffect(self)
        self.sound_effect.setSource(QUrl.fromLocalFile("Tom-and-Gia-huy/Do_an/UI/sound/clickSound.m4a"))

        #Xử lí click chuột
        self.login_button.clicked.connect(self.play_sound)
        self.login_button.clicked.connect(self.login)
        self.Register.clicked.connect(self.register)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Tên Đăng Nhập:"))
        self.password_label.setText(_translate("MainWindow", "Mật khẩu: "))
        self.login_button.setText(_translate("MainWindow", "Đăng Nhập"))
        self.Register.setText(_translate("MainWindow", "Đăng kí ngay"))
        self.GameName_label.setText(_translate("MainWindow", "Tâm và Gia Huy"))
        self.noAccount_label.setText(_translate("MainWindow", "Chưa có Tài Khoản?"))


    def login(self):
        filename = "UI/account.json"
        username = self.username_edit.text()
        password = self.password_edit.text()

        # Thực hiện kiểm tra tên người dùng và mật khẩu ở đây
        if check_account(filename, username,password) == 1 :
            self.close()
            self.MenuWindow = QtWidgets.QMainWindow()
            self.Menu = MenuWidget()
            self.Menu.setupUi(self.MenuWindow)
            self.MenuWindow.show()

        else:
            QMessageBox.warning(self, "Lỗi", "Tên người dùng hoặc mật khẩu không đúng!")

    def register(self):
        self.RegWindow = QtWidgets.QMainWindow()
        self.close()
        self.Reg = RegisterWidget()
        self.Reg.setupUi(self.RegWindow)
        self.RegWindow.show()
    
    #chưa xong
    def play_sound(self):
        # Phát âm thanh khi click vào nút
        self.sound_effect.play()
        
class RegisterWidget(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(120, 310, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(210, 380, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(250, 450, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        font.setWeight(50)
        self.register_button.setFont(font)
        self.register_button.setObjectName("register_button")
        self.bg_label = QtWidgets.QLabel(self.centralwidget)
        self.bg_label.setGeometry(QtCore.QRect(40, -50, 771, 351))
        self.bg_label.setText("")
        self.bg_label.setPixmap(QtGui.QPixmap("UI/image/bg_register.webp"))
        self.bg_label.setObjectName("bg_label")
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(360, 310, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_edit.setFont(font)
        self.username_edit.setText("")
        self.username_edit.setObjectName("username_edit")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(360, 380, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password_edit.setFont(font)
        self.password_edit.setText("")
        self.password_edit.setObjectName("password_edit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.register_button.clicked.connect(self.register)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Tên Đăng Nhập:"))
        self.password_label.setText(_translate("MainWindow", "Mật khẩu: "))
        self.register_button.setText(_translate("MainWindow", "Đăng Kí"))

    #Bắt đầu xử lí
    def register(self):
        filename = "UI/account.json"
        username = self.username_edit.text()
        password = self.password_edit.text()

        # Thực hiện kiểm tra tên người dùng và mật khẩu ở đây
        if check_account(filename, username,password) == 1 :
            QMessageBox.warning(self, "Lỗi", "Tên người dùng đã tồn tại!")
        elif check_account(filename, username, password) == -1:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đủ độ dài!")
        else:
            add_user(filename, username, password)
            QMessageBox.information(self, "Thông Báo", "Đăng Ký Thành Công!")
        
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
        self.newgame_button.setGeometry(QtCore.QRect(330, 160, 141, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.newgame_button.setFont(font)
        self.newgame_button.setObjectName("newgame_button")
        self.loadgame_button = QtWidgets.QPushButton(self.centralwidget)
        self.loadgame_button.setGeometry(QtCore.QRect(330, 240, 141, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loadgame_button.setFont(font)
        self.loadgame_button.setObjectName("loadgame_button")
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(330, 320, 141, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.help_button.setFont(font)
        self.help_button.setObjectName("help_button")
        self.About_button = QtWidgets.QPushButton(self.centralwidget)
        self.About_button.setGeometry(QtCore.QRect(330, 400, 141, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.About_button.setFont(font)
        self.About_button.setObjectName("About_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(330, 480, 141, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
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
        self.tom_label.setPixmap(QtGui.QPixmap("UI/image/Tom.png"))
        self.tom_label.setObjectName("tom_label")
        self.jerry_label = QtWidgets.QLabel(self.centralwidget)
        self.jerry_label.setGeometry(QtCore.QRect(540, 300, 241, 221))
        self.jerry_label.setText("")
        self.jerry_label.setPixmap(QtGui.QPixmap("UI/image/jerry.png"))
        self.jerry_label.setObjectName("jerry_label")
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

def login():
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = LoginWidget()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

login()





