import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        button = QPushButton( self)
        button.setText("hello")
        #button.setStyleSheet("QPushButton { text-align: center; }")  # Căn giữa văn bản trong button

        layout.addWidget(button)
        self.setLayout(layout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Center Text in Button')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
