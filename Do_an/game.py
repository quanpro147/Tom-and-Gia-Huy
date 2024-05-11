import pygame
from pygame.time import get_ticks
from maze import maze
from algrithms import *
import time

class Game():
    def __init__(self, level, mode = None, random_start_end = None):
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
        self.player = Player(None, None)
        self.random_start = random_start_end

    # Player funtions
    def handle_move(self):
        cur_row, cur_col = self.player.row, self.player.col
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.player.col > 0 and not self.maze.grid[cur_row][cur_col].walls['left']:
            self.player.move('left')
        elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.player.col < self.maze.num_cols-1 and not self.maze.grid[cur_row][cur_col].walls['right']:
            self.player.move('right')
        elif (key[pygame.K_UP] or key[pygame.K_w]) and self.player.row > 0 and not self.maze.grid[cur_row][cur_col].walls['top']:
            self.player.move('top')
        elif (key[pygame.K_DOWN] or key[pygame.K_s]) and self.player.row < self.maze.num_rows-1 and not self.maze.grid[cur_row][cur_col].walls['bot']:
            self.player.move('bot')

    def handle_hint(self):
        cur = self.player.row, self.player.col
        _hint = hint(self.maze, cur, 'dfs')
        key = pygame.key.get_pressed()
        if key[pygame.K_h]:
            if _hint == 'top':
                return self.player.row-1, self.player.col
            elif _hint == 'bot':
                return self.player.row+1, self.player.col
            elif _hint == 'right':
                return self.player.row, self.player.col+1
            elif _hint == 'left':
                return self.player.row, self.player.col-1
        else: return None

    # Setting functions
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

    # Draw functions
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

    # Game funtions   
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
        elif self.mode == 'not_auto': # che do nguoi choi
            start = self.maze.start
            end = self.maze.end
            self.player.row, self.player.col = start[0], start[1]
            
            while running:
                self.check_event()
                self.draw()
                # upload time
                timer.update()
                if not timer.active:
                    _time += 1      
                    timer.activate()
                timer.draw(self.screen, _time)
                self.handle_move()
                if (self.player.row, self.player.col) == end:
                    running = False
                self.draw_cur((self.player.row, self.player.col))
                hint_cell = self.handle_hint()
                if hint_cell is not None:
                        pygame.draw.rect(self.screen, (0, 255, 0), (hint_cell[1]*self.tile + 2, hint_cell[0]*self.tile + 2, self.tile - 4, self.tile - 4))
                self.update()
                time.sleep(0.1)
            
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
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def move(self, direction):
        if direction == 'top':
            self.row -= 1
        elif direction == 'bot':
            self.row += 1
        elif direction == 'right':
            self.col += 1
        elif direction == 'left':
            self.col -= 1

if __name__ == '__main__':
    game = Game('easy', 'not_auto')
    game.run()
