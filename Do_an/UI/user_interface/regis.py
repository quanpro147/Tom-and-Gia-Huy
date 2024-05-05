from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from UI.user_interface.music import Sound
from UI.user_interface.data_process import *



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
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(40, 350, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        font.setWeight(50)
        self.register_button.setFont(font)
        self.register_button.setObjectName("register_button")
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.bg_label = QtWidgets.QLabel(self.centralwidget)
        self.bg_label.setGeometry(QtCore.QRect(40, -50, 771, 351))
        self.bg_label.setText("")
        self.bg_label.setPixmap(QtGui.QPixmap("Do_an/UI/image/bg_register.webp"))
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
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Tên Đăng Nhập:"))
        self.password_label.setText(_translate("MainWindow", "Mật khẩu: "))
        self.register_button.setText(_translate("MainWindow", "Đăng Kí"))
        self.back_button.setIcon(QIcon("Do_an/UI/image/back.png"))

        self.register_button.clicked.connect(self.register)
        self.back_button.clicked.connect(lambda: self.login(MainWindow))
        self.sound = Sound()
        self.sound.setUp()
        #self.sound.bgSound()
    #Bắt đầu xử lí
    def register(self):
        self.sound.clickSound()
        filename = "Do_an/UI/user_interface/account.json"
        username = self.username_edit.text()
        password = self.password_edit.text()

        # Thực hiện kiểm tra tên người dùng và mật khẩu ở đây
        if check_account(filename, username,password) == 1:
            QMessageBox.warning(self, "Lỗi", "Tên người dùng đã tồn tại!")
        elif check_account(filename, username, password) == -1:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập và mật khẩu phải có ít nhất 6 kí tự!")
        else:
            add_user(filename, username, password)
            QMessageBox.information(self, "Thông Báo", "Đăng Ký Thành Công!")
        
    def login(self, MainWindow):
        from UI.user_interface.login import LoginWidget
        self.sound.clickSound()
        #self.sound.pause_bgSound()
        self.LoginWindow = QtWidgets.QMainWindow()
        self.Log = LoginWidget()
        self.Log.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        MainWindow.close()