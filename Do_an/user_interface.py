import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QMessageBox
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QFont 
from PyQt5.QtCore import Qt
import json
def load_data():
    with open("Do_an/account.json", "r") as file:
        data = json.load(file)
    return data
def save_data(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
def check_account(username, password):
    data = load_data()
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            return True
    return False
def add_user(username, password):
    data = load_data()
    data["users"].append({"username": username, "password": password})
    save_data(data, "Do_an/account.json")
class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Đăng Nhập")
        self.username_label = QLabel("Tên người dùng:")
        
        self.password_label = QLabel("Mật khẩu:")
        label_font = QFont("Arial")
        label_font.setPointSize(12)
        self.username_label.setFont(label_font)
        self.password_label.setFont(label_font)
        self.username_label.sizePolicy()
        self.password_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Đăng Nhập")
        self.login_button.clicked.connect(self.login)
        self.username_edit.setAlignment(Qt.AlignCenter)
        self.password_edit.setAlignment(Qt.AlignCenter)

        self.register_button = QPushButton("Đăng Ký")
        self.register_button.clicked.connect(self.register)
        self.register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.login_button.setStyleSheet("QPushButton { border: 2px solid black; }")
        self.register_button.setStyleSheet("QPushButton { border: 2px solid black; }")
        dx = 50
        dy = 50
        self.login_button.move(self.login_button.x() + dx, self.login_button.y() + dy)
        self.register_button.move(self.register_button.x() + dx, self.register_button.y() + dy)


        layout = QVBoxLayout()
        layout.addWidget(self.username_label,alignment=Qt.AlignCenter)
        layout.addWidget(self.username_edit,alignment=Qt.AlignCenter)
        layout.addWidget(self.password_label,alignment=Qt.AlignCenter)
        layout.addWidget(self.password_edit,alignment=Qt.AlignCenter)
        layout.addWidget(self.login_button,alignment=Qt.AlignCenter)
        layout.addWidget(self.register_button,alignment=Qt.AlignCenter)


        self.setLayout(layout)
        self.username_label.setMinimumSize(100,50)
        self.username_edit.setMinimumSize(200,100)
        self.setMinimumSize(400, 400) 
        self.login_button.setFixedSize(200, 50)
        self.register_button.setFixedSize(500, 50)
        self.password_edit.setFixedSize(200,50)
        

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        # Thực hiện kiểm tra tên người dùng và mật khẩu ở đây
        if check_account(username,password):
            self.close()
            self.w = MenuWidget()
            self.w.show()
        else:
            QMessageBox.warning(self, "Lỗi", "Tên người dùng hoặc mật khẩu không đúng!")

    def register(self):
        username = self.username_edit.text().strip()
        password = self.password_edit.text().strip()
        if check_account(username, password):
            QMessageBox.warning(self, "Lỗi", "Tài khoản đã tồn tại")
        else:
            add_user(username, password)
            QMessageBox.information(self, "Thông Báo", "Đăng Ký Thành Công!")
        # Lưu thông tin đăng ký vào tệp account.txt

    def show_new_window(self, checked):
        if self.w is None:
            self.close()
            self.w = MenuWidget()
            self.w.show()

        else:
            self.w.close()  # Close window.
            self.w = None

class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")
        self.play_button = QPushButton("Play")
        self.help_button = QPushButton("Help")
        self.load_button = QPushButton("Load")
        self.exit_button = QPushButton("Exit")

        # Đặt chế độ mở rộng cho các nút
        self.play_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.help_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.load_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.help_button.setFixedSize(200,50)

        self.exit_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.play_button)
        layout.addWidget(self.help_button)
        layout.addWidget(self.load_button)
        layout.addWidget(self.exit_button)
        self.setLayout(layout)
        self.setMinimumSize(400, 400) 

def ui():
    app = QApplication(sys.argv)
    login = LoginWidget()
    login.show()
    sys.exit(app.exec_())
ui()
