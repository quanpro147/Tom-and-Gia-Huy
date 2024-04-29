import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QMessageBox,QFrame
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
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

