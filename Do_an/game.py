import pygame
from pygame.time import get_ticks
from maze import maze
from algrithms import *
import time

class Game():
    def __init__(self, level, mode = None):
        pygame.init()
        pygame.display.set_caption('Maze Game')
        self.WINDOW_SIZE = 1202, 802
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.level = level
        self.mode = mode
        self.maze = None
        self.algorithm = None
        self.tile = None
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm
    
    def new_game(self):
        if self.level == 'easy':
            self.maze = maze(20, 20)
        elif self.level == 'medium':
            self.maze = maze(40, 40)
        elif self.level == 'hard':
            self.maze = maze(100, 100)
        self.maze.generate_maze()
        self.tile = 800//self.maze.num_rows

    def update(self):
        pygame.display.update()
        self.clock.tick(60)

    def draw_text(self, text, color, x, y):
        text_font = pygame.font.SysFont('Arial', 30)
        img = text_font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def draw_cur(self, cur_cell):
        pygame.draw.rect(self.screen, (255, 0, 0), (cur_cell[1]*self.tile + 2, cur_cell[0]*self.tile + 2, self.tile - 4, self.tile - 4))

    def draw_maze(self):
        for i in range(self.maze.num_rows):
            for j in range(self.maze.num_cols):
                self.maze.grid[i][j].draw(self.screen, self.tile)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.maze.end[1]*self.tile + 2, self.maze.end[0]*self.tile + 2, self.tile - 4, self.tile - 4))

    def draw_path(self, path):
        for cell_x, cell_y in path:
            pygame.draw.rect(self.screen, 'darkviolet', (cell_y*self.tile + 2, cell_x*self.tile + 2, self.tile - 4, self.tile - 4)) 
        pygame.display.update()

    def draw_solution(self, path):
        for cell_x, cell_y in path:
            pygame.draw.rect(self.screen, 'chartreuse2', (cell_y*self.tile + self.tile//4, cell_x*self.tile + self.tile//4, self.tile//2, self.tile//2))
        pygame.display.update()

    def draw(self):
        self.screen.fill('white')
        self.draw_maze()
            
    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def run(self):
        self.new_game()
        running = True
        _time = 0
        timer = Timer(1000, self.font)
        timer.activate()

        if self.mode == 'auto': # che do may choi
            if self.algorithm == 'dfs': # dung thuat toan dfs

                solution = dfs(self.maze)
                solution_path = []
                end = self.maze.end
                cur_cell = self.maze.start         
                path = [cur_cell]              
                self.maze.grid[cur_cell[0]][cur_cell[1]].is_visited = True     
                visited_cells = [] 

                while running:
                    self.check_event()
                    self.draw()
                    # upload time
                    timer.update()
                    if not timer.active:
                        _time += 1      
                        timer.activate()
                    timer.draw(self.screen, _time)

                    neighbour_list = self.maze.find_neighbours(cur_cell[0], cur_cell[1])    
                    neighbour_list = self.maze.validate_neighbours_generate(neighbour_list)
                    neighbour_list = unblock_neighbours(self.maze, cur_cell[0], cur_cell[1], neighbour_list)

                    self.draw_path(path)
                    self.draw_cur(cur_cell) 
                    self.draw_solution(solution_path)
                    if neighbour_list is not None:
                        
                        visited_cells.append(cur_cell)             
                        next_cell = random.choice(neighbour_list)   
                        self.maze.grid[next_cell[0]][next_cell[1]].is_visited = True     
                        cur_cell = next_cell
                        if next_cell == end:
                            running = False
                        path.append(cur_cell) 

                    else:  
                        cur_cell = visited_cells.pop()    
                        path.pop() 
                    time.sleep(0.08)
                    self.update()
                time.sleep(3)
            elif self.algorithm == 'bfs': # dung thuat toan bfs

                start = self.maze.start
                end = self.maze.end
                paths = [[]]
                paths[0].append(start)
                cur_cell = start
                self.maze.grid[cur_cell[0]][cur_cell[1]].is_visited = True 

                start = self.maze.start
                end = self.maze.end
                paths = [[]]
                paths[0].append(start)
                cur_cell = start
                self.maze.grid[cur_cell[0]][cur_cell[1]].is_visited = True 

                while running:
                    self.check_event()
                    self.draw()

                    path = paths[0] 
                    paths = paths[1:]  
                    cur_cell = path[-1] 
                    neighbour_list = self.maze.find_neighbours(cur_cell[0], cur_cell[1]) 
                    neighbour_list = self.maze.validate_neighbours_generate(neighbour_list)
                    neighbour_list = unblock_neighbours(self.maze, cur_cell[0], cur_cell[1], neighbour_list)

                    if neighbour_list is not None:
                        for neighbour in neighbour_list:
                            self.draw_cur(neighbour)
                            self.maze.grid[neighbour[0]][neighbour[1]].is_visited = True 
                            add = path.copy() 
                            add.append(neighbour)
                            paths.append(add) 
                            if neighbour == end: 
                                running = False
                    time.sleep(1)
                    self.update()
        else: # che do nguoi choi
            pass
class Timer:
    def __init__(self, duration, font):
        self.duration = duration 
        self.active = False
        self.font = font
        self.start = 0
        self.time = time

    def activate(self):
        self.active = True
        self.start = get_ticks()

    def deactivate(self):
        self.active = False
        self.start = 0

    def update(self):
        if self.active:
            cur_time = get_ticks()
            if cur_time - self.start >= self.duration:
                self.deactivate()

    def time_text(self, _time):
        hou = _time//3600
        min = (_time - hou*3600)//60
        sec = _time - hou*3600 - min*60
        return str('Time: {}:{}:{}'.format(hou, min, sec))
    
    def draw(self, screen, _time):
        text_suf = self.font.render(self.time_text(_time), True, 'black')
        screen.blit(text_suf, (900, 50))     

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image 
    def move(self):
        pass

if __name__ == '__main__':
    game = Game('easy', 'auto')
    game.set_algorithm('dfs')
    game.run()
