import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt,QRect
from PyQt5.QtGui import QPainter, QBrush, QColor
from UI.user_interface.menu import MenuWidget
import pygame

class LoadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.save_check = False

        # Thiết lập các thuộc tính cho cửa sổ
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # Thiết lập màu nền trong suốt
        #text nhap ten game
        self.Text = QLineEdit(self)
        self.Text.setGeometry(QRect(50,50,300,40))
        #Save Button
        self.Save = QPushButton(self)
        self.Save.setGeometry(QRect(50,200,100,40))
        self.Save.setStyleSheet('border-radius:5px;border: 1px solid black')
        self.Save.setText("Save")
        self.Save.clicked.connect(self.save)
        #Cancel Button
        self.Cancel = QPushButton(self)
        self.Cancel.setGeometry(QRect(250,200,100,40))
        self.Cancel.setStyleSheet('border-radius:5px;border: 1px solid black')
        self.Cancel.setText("Cancel")
        self.Cancel.clicked.connect(self.exit_window)

        self.setGeometry(780, 300, 400, 300)
        self.setWindowTitle('Custom Window')
    def exit_window(self):
        self.close()
        print(123)
        del self
    def save(self):
        self.save_check = not self.save_check
        self.close()

        


    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoadWindow()
    window.show()
    sys.exit(app.exec_())
