
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.user_interface.data_process import *
from UI.user_interface.music import Sound


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
        #self.bg_music_button = QtWidgets.QPushButton(self.centralwidget)
        #self.bg_music_button.setGeometry(QtCore.QRect(700, 30, 50, 50))
        #self.bg_music_button_2 = QtWidgets.QPushButton(self.centralwidget)
        #self.bg_music_button_2.setGeometry(QtCore.QRect(700, 80, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.login_button.setFont(font)
        self.login_button.setObjectName("Âm thanh")
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
        self.jerry_label.setPixmap(QtGui.QPixmap("Do_an/UI/image/jerry.png"))
        self.jerry_label.setObjectName("jerry_label")
        self.tom_label = QtWidgets.QLabel(self.centralwidget)
        self.tom_label.setGeometry(QtCore.QRect(0, 210, 231, 331))
        self.tom_label.setText("")
        self.tom_label.setPixmap(QtGui.QPixmap("Do_an/UI/image/Tom.png"))
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
        #self.bg_music_button.setIcon(QIcon("Do_an/UI/image/music.png"))
        #self.bg_music_button_2.setIcon(QIcon("Do_an/UI/image/mute.png"))

        #khởi tạo âm thanh
        self.sound = Sound()
        self.sound.setUp()
        self.sound.bgSound()

        #Xử lí click chuột
        self.login_button.clicked.connect(lambda: self.login(MainWindow))
        self.Register.clicked.connect(lambda: self.register(MainWindow))
        #self.bg_music_button.clicked.connect(self.sound.bgSound)
        #self.bg_music_button_2.clicked.connect(self.sound.pause_bgSound)

    def login(self, MainWindow):
        self.sound.clickSound()
        filename = "Do_an/UI/user_interface/account.json"
        username = self.username_edit.text()
        password = self.password_edit.text()

        # Thực hiện kiểm tra tên người dùng và mật khẩu ở đây
        if check_account(filename, username,password) == 1:
            self.sound.pause_bgSound()
            from UI.user_interface.menu import MenuWidget
            self.MenuWindow = QtWidgets.QMainWindow()
            self.Menu = MenuWidget()
            self.Menu.setupUi(self.MenuWindow)
            self.MenuWindow.show()
            MainWindow.close()
        else:
            QMessageBox.warning(self, "Lỗi", "Tên người dùng hoặc mật khẩu không đúng!")

    def register(self, MainWindow):
        from UI.user_interface.regis import RegisterWidget
        self.sound.clickSound()
        self.sound.pause_bgSound()
        self.RegWindow = QtWidgets.QMainWindow()
        self.Reg = RegisterWidget()
        self.Reg.setupUi(self.RegWindow)
        self.RegWindow.show()
        MainWindow.close()



