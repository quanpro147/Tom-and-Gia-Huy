from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QSizePolicy, QMessageBox,
                             QFrame)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
import sys
from algrithms import *
from maze import *
import random
global app
import time
import copy

class Rect(QWidget):
    def __init__(self, init_x, init_y, rect_size=38):
        super().__init__()
        self.rect_x = init_x
        self.rect_y = init_y

class RectWidget(QWidget):
    def __init__(self, init_x, init_y, rect_size=38):
        super().__init__()
        self.setMouseTracking(True)
        self.rect_x = init_x
        self.rect_y = init_y
        self.col = self.rect_x//40
        self.row = self.rect_y//40
        self.rect_size = rect_size
        self.dragging = True
        self.start = []
        self.Index = []
        self.start1 = []
        self.listPoint = []
        self.drawHint = False
    def setListPoint(self,listPoint):
        self.listPoint = listPoint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(204, 255, 255))
        painter.drawRect(self.rect_x, self.rect_y, self.rect_size, self.rect_size)
        if(self.drawHint):
            painter.setPen(Qt.red)
            for i in range(len(self.listPoint) - 1):
                x1 = self.listPoint[i][1]
                y1 = self.listPoint[i][0]
                x2 = self.listPoint[i + 1][1]
                y2 = self.listPoint[i + 1][0]
                painter.drawLine(x1 * 40 + 20, y1 * 40 + 20, x2 * 40 + 20, y2 * 40 + 20)

    def move_rect(self, dx, dy):
        self.rect_x += dx
        self.rect_y += dy
        self.update()

    def mousePressEvent(self, event):
        self.start = [int(self.rect_x), int(self.rect_y)]
        self.start1 = self.start[::-1]
        self.Index = [self.start[0] // 40, self.start[0] // 40]
        #print(self.start)
        #print(self.start1)
        self.dragging = False

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.rect_x = event.x() - event.x() % 40
            self.rect_y = event.y() - event.y() % 40
            self.col = self.rect_x//40
            self.row = self.rect_y//40
            self.update()

    def get_rect_position(self):
        return [self.rect_x, self.rect_y]
    def index_pos(self):
        col = self.col
        row = self.row
        return  [col,row]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1000, 900)
        init_x, init_y = 0, 0  # Tọa độ khởi tạo tùy
        self.rect_widget = RectWidget(init_x, init_y)
        self.setCentralWidget(self.rect_widget)
        self.running = True
        self.path_solve = []
        self.end = (19,19)

        # background


        self.Maze = maze(20, 20)
        self.Maze.generate_maze()
        self.Grid = self.Maze.grid
        self.list_sqr = []

    def keyPressEvent(self, event):
        #x, y = self.rect_widget.get_rect_position()
        #col = self.rect_widget.col
        #row = self.rect_widget.row
        #print(f'Current position: ({x}, {y})')
        #print(f'Current position: ({col}, {row})')
        #print(self.Grid[y // 40][x // 40].walls)

        if event.key() == Qt.Key_Up:
            self.move_up()
        elif event.key() == Qt.Key_Down:
            self.move_down()

        elif event.key() == Qt.Key_Left:
            self.move_left()
        elif event.key() == Qt.Key_Right:
             self.move_right()
        elif event.key() == Qt.Key_R:
            self.bot_play()
        elif event.key() == Qt.Key_Q:
            self.print_maze()
            self.running = False
        elif event.key() == Qt.Key_E:
            self.rect_widget.drawHint = True
            self.rect_widget.update()

        #self.bot_play()

    def print_maze(self):
        for i in range(len(self.Maze.grid)):
            for j in range(len(self.Maze.grid[0])):
                print(self.Maze.grid[i][j].is_visited,end = ' ')
            print()
    def bot_play(self):
        self.running = True
        self.remove_path()
        tmp_start = [self.rect_widget.rect_y // 40, self.rect_widget.rect_x // 40]

        cur_cell = tmp_start.copy()
        path_dfs = [cur_cell]
        visited_cells = []
        run_solution = False
        running = True
        Maze = copy.deepcopy(self.Maze)
        neighbour_list = Maze.find_neighbours(cur_cell[0], cur_cell[1])
        neighbour_list = Maze.validate_neighbours_generate(neighbour_list)
        neighbour_list = unblock_neighbours(Maze, cur_cell[0], cur_cell[1], neighbour_list)
        Maze.grid[cur_cell[0]][cur_cell[1]].is_visited = True

        tmp_path = []
        #solution_path = dfs(self.Maze, tmp_start)
        while self.running:
            neighbour_list = Maze.find_neighbours(cur_cell[0], cur_cell[1])
            neighbour_list = Maze.validate_neighbours_generate(neighbour_list)
            neighbour_list = unblock_neighbours(Maze, cur_cell[0], cur_cell[1], neighbour_list)
            if not run_solution:
                if neighbour_list is not None:
                    visited_cells.append(cur_cell)
                    next_cell = random.choice(neighbour_list)
                    Maze.grid[next_cell[0]][next_cell[1]].is_visited = True
                    if next_cell == self.end:
                        run_solution = True
                    cur_cell = next_cell
                    path_dfs.append(cur_cell)
                    self.move_coor(cur_cell)
                else:

                    cur_cell = visited_cells.pop()
                    path_dfs.pop()
                    self.move_coor(cur_cell)
                QApplication.processEvents()
                time.sleep(0.01)
            else:
                self.running = False
        self.path_solve = path_dfs.copy()
        self.rect_widget.setListPoint(path_dfs)
        self.remove_path()
        self.rect_widget.move_rect(tmp_start[1]*40-self.rect_widget.rect_x,tmp_start[0]*40-self.rect_widget.rect_y)
    def remove_path(self):
        while(self.list_sqr !=[]):
            self.list_sqr[-1].setStyleSheet("background-color:None")
            self.list_sqr.pop()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_E:
            self.rect_widget.drawHint = False
            self.rect_widget.update()
    #def draw_hint(self):
        #qp = QPainter(self)
        #pen = QPen(Qt.black, 2, Qt.SolidLine)
        #qp.setPen(pen)

    def position(self):
        print(f"row: {self.rect_widget.row}")
        print(f"col {self.rect_widget.col}")

    def draw_sqr(self,row,col):
        a = QLabel(self)
        a.setGeometry(QRect(col* 40 + 5, row * 40 + 5, 30, 30))
        self.list_sqr.append(a)
        self.list_sqr[-1].setStyleSheet("background-color:green;")
        self.list_sqr[-1].show()
    def drawpath(self,path):
        path_dfs = self.rect_widget.start

    def paintEvent(self, event):
        qp = QPainter(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)

        for i in range(20):
            for j in range(20):
                if (self.Grid[i][j].walls['top']):
                    qp.drawLine(40 * j, 40 * i, 40 * j + 40, 40 * i)
                if (self.Grid[i][j].walls['bot']):
                    qp.drawLine(40 * j, 40 * i + 40, 40 * j + 40, 40 * i + 40)
                if (self.Grid[i][j].walls['left']):
                    qp.drawLine(40 * j, 40 * i + 40, 40 * j, 40 * i)
                if (self.Grid[i][j].walls['right']):
                    qp.drawLine(40 * j + 40, 40 * i, 40 * j + 40, 40 * i + 40)

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        print(f"Mouse Coordinates: ({x}, {y})")
    def move_up(self):
        x, y = self.rect_widget.get_rect_position()

        if (y > 0 and not self.Grid[y // 40][x // 40].walls['top']):
            self.rect_widget.row -= 1
            if (self.list_sqr != []):
                rect = self.list_sqr[-1].geometry()
                X = rect.x() - 5
                Y = rect.y() - 5

                if (X == self.rect_widget.rect_x and Y == self.rect_widget.rect_y - 40):
                    self.list_sqr[-1].setStyleSheet("background-color:None")
                    self.list_sqr.pop()
                else:
                    self.draw_sqr(y // 40, x // 40)
            else:
                self.draw_sqr(y // 40, x // 40)
            self.rect_widget.move_rect(0, -40)
            self.update()

    def move_down(self):
        x, y = self.rect_widget.get_rect_position()
        if (y < 800 - 40 and not self.Grid[y // 40][x // 40].walls['bot']):
            self.rect_widget.row += 1
            if (self.list_sqr != []):
                rect = self.list_sqr[-1].geometry()
                X = rect.x() - 5
                Y = rect.y() - 5

                if (X == self.rect_widget.rect_x and Y == self.rect_widget.rect_y + 40):
                    self.list_sqr[-1].setStyleSheet("background-color:None")
                    self.list_sqr.pop()
                else:
                    self.draw_sqr(y // 40, x // 40)
            else:
                self.draw_sqr(y // 40, x // 40)
            self.rect_widget.move_rect(0, 40)
            self.update()
    def move_left(self):
        x, y = self.rect_widget.get_rect_position()
        if (x > 0 and not self.Grid[y // 40][x // 40].walls['left']):
            self.rect_widget.col -= 1
            if (self.list_sqr != []):
                rect = self.list_sqr[-1].geometry()
                X = rect.x() - 5
                Y = rect.y() - 5

                if (X == self.rect_widget.rect_x - 40 and Y == self.rect_widget.rect_y):
                    self.list_sqr[-1].setStyleSheet("background-color:None")
                    self.list_sqr.pop()
                else:
                    self.draw_sqr(y // 40, x // 40)
            else:
                self.draw_sqr(y // 40, x // 40)
            self.rect_widget.move_rect(-40, 0)
            self.update()
    def move_right(self):
        x, y = self.rect_widget.get_rect_position()
        if (x < 800 - 40 and not self.Grid[y // 40][x // 40].walls['right']):
            self.rect_widget.col += 1
            if (self.list_sqr != []):
                rect = self.list_sqr[-1].geometry()
                X = rect.x() - 5
                Y = rect.y() - 5

                if (X == self.rect_widget.rect_x + 40 and Y == self.rect_widget.rect_y):
                    self.list_sqr[-1].setStyleSheet("background-color:None")
                    self.list_sqr.pop()
                else:
                    self.draw_sqr(y // 40, x // 40)

            else:
                self.draw_sqr(y // 40, x // 40)
            self.rect_widget.move_rect(40, 0)
            self.update()
    def move_up1(self):
        x, y = self.rect_widget.get_rect_position()

        if (y > 0 and not self.Grid[y // 40][x // 40].walls['top']):
            self.rect_widget.row -= 1
            if (self.list_sqr != []):
                rect = self.list_sqr[-1].geometry()
                X = rect.x() - 5
                Y = rect.y() - 5
                print(rect.x())
                print(len(self.list_sqr))
                if (X == self.rect_widget.rect_x and Y == self.rect_widget.rect_y - 40):
                    print("NOT")
                else:
                    self.draw_sqr(y // 40, x // 40)
                    self.rect_widget.move_rect(0, -40)
            else:
                self.draw_sqr(y // 40, x // 40)
                self.rect_widget.move_rect(0, -40)

            self.update()
    def move_down1(self):
        x, y = self.rect_widget.get_rect_position()
        if (y < 800 - 40 and not self.Grid[y // 40][x // 40].walls['bot']):
            self.rect_widget.row += 1
            if (self.list_sqr != []):
                rect = self.list_sqr[-1].geometry()
                X = rect.x() - 5
                Y = rect.y() - 5
                print(rect.x())
                print(len(self.list_sqr))
                if (X == self.rect_widget.rect_x and Y == self.rect_widget.rect_y + 40):
                    print("NOT")
                else:
                    self.draw_sqr(y // 40, x // 40)
                    self.rect_widget.move_rect(0, 40)
            else:
                self.draw_sqr(y // 40, x // 40)
                self.rect_widget.move_rect(0, 40)
            self.update()
    def move_left1(self):
        x, y = self.rect_widget.get_rect_position()
        if (x > 0 and not self.Grid[y // 40][x // 40].walls['left']):
            self.rect_widget.col -= 1
            if (self.list_sqr != []):
                rect = self.list_sqr[-1].geometry()
                X = rect.x() - 5
                Y = rect.y() - 5
                print(rect.x())
                print(len(self.list_sqr))
                if (X == self.rect_widget.rect_x - 40 and Y == self.rect_widget.rect_y):
                    print("NOt")
                else:
                    self.draw_sqr(y // 40, x // 40)
                    self.rect_widget.move_rect(-40, 0)
            else:
                self.draw_sqr(y // 40, x // 40)
                self.rect_widget.move_rect(-40, 0)
            self.update()
    def move_right1(self):
        x, y = self.rect_widget.get_rect_position()
        if (x < 800 - 40 and not self.Grid[y // 40][x // 40].walls['right']):
            self.rect_widget.col += 1
            if (self.list_sqr != []):
                rect = self.list_sqr[-1].geometry()
                X = rect.x() - 5
                Y = rect.y() - 5
                print(X == self.rect_widget.rect_x)
                print(Y == self.rect_widget.rect_y)
                print(len(self.list_sqr))
                if (X == self.rect_widget.rect_x + 40 and Y == self.rect_widget.rect_y):
                    print("NOT")
                else:
                    self.draw_sqr(y // 40, x // 40)
                    self.rect_widget.move_rect(40, 0)
            else:
                self.draw_sqr(y // 40, x // 40)
                self.rect_widget.move_rect(40, 0)
            self.update()
    def move_coor(self,cur_cell):
        if (self.rect_widget.row == cur_cell[0] + 1):
            self.move_up()
        elif (self.rect_widget.row == cur_cell[0] - 1):
            self.move_down()
        else:
            if (self.rect_widget.col == cur_cell[1] + 1):
                self.move_left()
            else:
                self.move_right()

    def closeEvent(self, event):
        self.running = False
        event.accept()



        

def main():
    app = QApplication(sys.argv)
    login = MainWindow()
    login.show()
    sys.exit(app.exec_())


main()
