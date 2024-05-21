import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer
from game import Game
class PygameWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initPygame()

    def initPygame(self):
        pygame.init()
        self.size = (640, 480)
        self.screen = pygame.display.set_mode(self.size)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.pygameLoop)
        self.timer.start(16)  # Khoảng thời gian 16ms tương đương với 60 FPS
        self.pygame_running = True

    def pygameLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.pygame_running = False
                pygame.quit()
                self.timer.stop()
                self.parent().show()  # Hiển thị lại cửa sổ PyQt5
                self.hide()  # Ẩn cửa sổ Pygame
        if self.pygame_running:
            game = Game('easy','not_auto',True,'Frog')
            game.run()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pygame trong PyQt5')
        self.setGeometry(100, 100, 640, 480)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)
        self.button = QPushButton('Chạy Pygame', self.centralWidget)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.runPygame)

    def runPygame(self):
        self.hide()  # Ẩn cửa sổ PyQt5
        self.pygameWindow = PygameWindow(self)
        self.pygameWindow.show()  # Hiển thị cửa sổ Pygame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
