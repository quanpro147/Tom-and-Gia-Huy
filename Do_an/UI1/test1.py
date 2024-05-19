import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class Rectangle(QWidget):
    def __init__(self, x, y, size, parent=None, color=QColor(0, 0, 255)):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.step = 10  # Bước di chuyển mỗi lần nhấn phím

        # Đặt vị trí và kích thước của widget
        self.setGeometry(self.x, self.y, self.size, self.size)

    def move_up(self):
        self.y -= self.step
        self.update_position()

    def move_down(self):
        self.y += self.step
        self.update_position()

    def move_left(self):
        self.x -= self.step
        self.update_position()

    def move_right(self):
        self.x += self.step
        self.update_position()

    def update_position(self):
        self.setGeometry(self.x, self.y, self.size, self.size)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.color)
        painter.drawRect(0, 0, self.size, self.size)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Di chuyển hình chữ nhật')
        self.setGeometry(100, 100, 600, 400)  # Kích thước cửa sổ chính

        # Khởi tạo hình chữ nhật
        self.rect = Rectangle(50, 50, 20, self)
        self.rect.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.rect.move_up()
        elif event.key() == Qt.Key_Down:
            self.rect.move_down()
        elif event.key() == Qt.Key_Left:
            self.rect.move_left()
        elif event.key() == Qt.Key_Right:
            self.rect.move_right()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = MainWidget()
    mainWidget.show()
    sys.exit(app.exec_())
