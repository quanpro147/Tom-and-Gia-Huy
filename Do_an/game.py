import pygame
from pygame.time import get_ticks
from maze import *
from algrithms import *
import pickle
import time

class Button:
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
    
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

class saveloadsystem():
    def __init__(self, file_extension, folder):
        self.file_extension = file_extension
        self.folder = folder
    
    def save_game(self, name_file, game):
        """ Ham luu maze voi ten file vao game_manager """
        self.add_file_name(name_file)
        data = self.process_game_to_save(name_file, game)
        with open(self.folder + self.file_extension, 'wb+') as f:          
            pickle.dump(data, f)

    def process_game_to_save(self,name_file, game):
        """ Ham nay dung de them game muon luu vao game_manager """
        try:
            game_manager = self.load_data()
            game_manager[name_file] = game
            return game_manager
        except EOFError:
            return {name_file: game}
        
    def load_data(self):
        """ Ham phu tro de lay maze_manager """
        with open( self.folder + self.file_extension, 'rb') as f:
            data = pickle.load(f)
        return data
        
    def load_game(self, name_file):
        """ Ham nay dung de load game tu ten file da luu """
        if self.check_file_name(name_file):
            game_manager = self.load_data()
            for key, val in game_manager.items():
                if key == name_file:
                    return val
        else:
            # raise error
            return False
        
    def add_file_name(self, name_file):
        with open('Do_an/SaveLoad/saveload.txt', 'a') as f:
            f.write(name_file + '\n')

    def check_file_name(self, name_file):
        with open('Do_an/SaveLoad/saveload.txt', 'r') as f:
            name_files = f.readlines()
            for _name_file in name_files:
                _name_file = _name_file[:-1]
                if name_file == _name_file:
                    return True
        return False
    
    def readfile(path):
        #doc cac file game co trong file txt
        with open(path, 'r') as f:
            l = f.readlines()
            return [s.strip() for s in l]
        
    def delete_file(self, name_file):
        # xoa ten file trong file txt
        with open('Do_an/SaveLoad/saveload.txt', 'r') as f:
            name_files = f.readlines()
            name_files.remove(name_file+'\n')
        with open('Do_an/SaveLoad/saveload.txt', 'w') as f:
            f.writelines(name_files)
        # xoa data cua file
        game_manager = self.load_data()
        game_manager.pop(name_file)
        if game_manager == {}:
            game_manager = None
        with open(self.folder + self.file_extension, 'wb') as f:
            pickle.dump(game_manager, f)
        
        
class Game:
    def __init__(self, level = None, mode = None, choose = None):
        pygame.init()
        pygame.display.set_caption('Maze Game')
        self.WINDOW_SIZE = 1202, 802
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.level = level
        self.mode = mode
        self.maze = None
        self.algorithm = 'dfs'
        self.tile = None
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font_mini = pygame.font.Font('freesansbold.ttf', 20)
        self.player = Player(None, None)
        self.buttons = self.button()
        self.start, self.end = None, None
        self.record = 0
        self.rank = None
        self.file_name = ''
        self.saveloadmanager = saveloadsystem('.save', 'Do_an/SaveLoad/game_manager')
        self.completed = False

    def button(self):
        # load img
        resume_img = pygame.image.load('Do_an/button/Resume.png').convert_alpha()
        load_img = pygame.image.load('Do_an/button/LoadButton.png').convert_alpha()
        menu_img = pygame.image.load('Do_an/button/MenuButton.png').convert_alpha()
        options_img = pygame.image.load('Do_an/button/OptionsButton.png').convert_alpha()
        quit_img = pygame.image.load('Do_an/button/QuitButton.png').convert_alpha()
        change_alg_img = pygame.image.load('Do_an/button/Change_AlgButton.png').convert_alpha()
        back_img = pygame.image.load('Do_an/button/BackButton.png').convert_alpha()
        play_again_img = pygame.image.load('Do_an/button/Play_againButton.png').convert_alpha()
        save_img = pygame.image.load('Do_an/button/SaveButton.png').convert_alpha()
        accept_img = pygame.image.load('Do_an/button/AcceptButton.png').convert_alpha()
        cancel_img = pygame.image.load('Do_an/button/CancelButton.png').convert_alpha()
        # create button
        resume_button = Button(500, 200, resume_img, 1)
        load_button = Button(500, 300, load_img, 1)
        menu_button = Button(500, 400, menu_img, 1)
        options_button = Button(500, 500, options_img, 1)
        quit_button = Button(500, 600, quit_img, 1)
        change_alg_button = Button(500, 450, change_alg_img, 1)
        back_button = Button(500, 550, back_img, 1)
        play_again_button = Button(400, 150, play_again_img, 1)
        save_button_1 = Button(500, 300, save_img, 1)
        save_button_2 = Button(400, 200, save_img, 1)
        accept_button_1 = Button(600, 350, accept_img, 1)
        accept_button_2 = Button(600, 300, accept_img, 1)
        cancel_button_1 = Button(400, 350, cancel_img, 1)
        cancel_button_2 = Button(400, 300, cancel_img, 1)
        return {'resume': resume_button, 
                'load': load_button,
                'main_menu': menu_button,
                'options': options_button,
                'quit': quit_button,
                'chang_alg': change_alg_button,
                'back': back_button,
                'play_again': play_again_button,
                'save_1': save_button_1,
                'save_2': save_button_2,
                'accept_1': accept_button_1,
                'accept_2': accept_button_2,
                'cancel_1': cancel_button_1,
                'cancel_2': cancel_button_2}

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
        if self.algorithm == 'dfs': 
            hint = dfs(self.maze, cur)
        elif self.algorithm == 'bfs':
            hint = bfs(self.maze, cur)
        key = pygame.key.get_pressed()
        if key[pygame.K_h]:
            self.draw_hint(hint[:-1])

    # Setting functions
    def set_start_end(self, start, end):
        self.tmp_start = start
        self.end = end

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm
    
    def new_game(self):
        if self.maze is not None: return
        if self.level == 'easy':
            self.maze = maze(20, 20)
        elif self.level == 'medium':
            self.maze = maze(40, 40)
        elif self.level == 'hard':
            self.maze = maze(100, 100)  

        self.maze.generate_maze()
        if self.start is not None:
            self.maze.start = self.start
            self.maze.end = self.end
        self.tile = 800//self.maze.num_rows

    def update(self):
        pygame.display.update()
        self.clock.tick(60)

    def save(self):
        data = {'level': self.level,'mode': self.mode,'maze': self.maze,'alg': self.algorithm,'start': self.maze.start,'end': self.maze.end,'record': self.record,
                'file_name': self.file_name, 'player': self.player, 'tile': self.tile, 'completed': self.completed}
        if self.saveloadmanager.check_file_name(self.file_name):
            print('File has already exist')
        else:
            self.saveloadmanager.save_game(self.file_name, data)
            print('Save file succeeded')

    def load(self, file_name):
        if not self.saveloadmanager.check_file_name(file_name):
            print('Find not found')
        else:
            data = self.saveloadmanager.load_game(file_name)
            self.level = data['level']
            self.mode = data['mode']
            self.maze = data['maze']
            self.algorithm = data['alg']
            self.start = data['start']
            self.end = data['end']
            self.record = data['record']
            self.file_name = data['file_name']
            self.player = data['player']
            self.tile = data['tile']
            self.completed = data['completed']
            print('Load file succeeded')

    # Draw functions
    def draw_text(self, text, color, x, y):
        img = self.font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def draw_text_mini(self, text, color, x, y):
        img = self.font_mini.render(text, True, color)
        self.screen.blit(img, (x, y))

    def draw_cur(self, cur_cell):
        pygame.draw.rect(self.screen, (255, 0, 0), (cur_cell[1]*self.tile + 2, cur_cell[0]*self.tile + 2, self.tile - 4, self.tile - 4))
        pygame.display.update()

    def draw_maze(self):
        for i in range(self.maze.num_rows):
            for j in range(self.maze.num_cols):
                self.maze.grid[i][j].draw(self.screen, self.tile)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.maze.end[1]*self.tile + 2, self.maze.end[0]*self.tile + 2, self.tile - 4, self.tile - 4))

    def draw_path(self, path):
        for cell_x, cell_y in path:
            pygame.draw.rect(self.screen, 'darkviolet', (cell_y*self.tile + 2, cell_x*self.tile + 2, self.tile - 4, self.tile - 4)) 
        pygame.display.update()

    def draw_hint(self, hint):
        for cell_x, cell_y in hint:
            pygame.draw.rect(self.screen, 'green', (cell_y*self.tile + 3, cell_x*self.tile + 3, self.tile - 6, self.tile - 6)) 
        pygame.display.update()

    def draw(self):
        self.screen.fill('white')
        self.draw_maze()
    
    def draw_rank(self, games):
        rank_bg_img = pygame.image.load('Do_an/Assets/Background/rank_bg.jpg').convert_alpha()
        rank_bg_img = pygame.transform.scale(rank_bg_img, (300, 400))
        self.screen.blit(rank_bg_img, (850, 250))
        n = min(5, len(games))
        for i in range(n): 
            self.draw_text_mini(games[i]['file_name'], 'black', 910, 450 + i*43)
            self.draw_text_mini(games[i]['level'], 'black', 1000, 450 + i*43)
            self.draw_text_mini(self.record_text_mini(games[i]['record']), 'black', 1080, 450 + i*43)
    # Event funtions
    def record_text(self, _time):
        hou = _time//3600
        min = (_time - hou*3600)//60
        sec = _time - hou*3600 - min*60
        return str('Time of completion: {}:{}:{}'.format(hou, min, sec))
    def record_text_mini(self, _time):
        hou = _time//3600
        min = (_time - hou*3600)//60
        sec = _time - hou*3600 - min*60
        return str('{}:{}:{}'.format(hou, min, sec))
    
    def take_score(self):
        games = []
        try:
            game_manager = self.saveloadmanager.load_data()
        except EOFError:
            return []
        for name_file, game in game_manager.items():
            if game['completed'] and game['mode'] == 'not_auto' and game['level'] == self.level:
                games.append(game)
        if len(games) == 1: return games
        for i in range(len(games) - 1):
            for j in range(1, len(games)):
                if games[i]['record'] > games[j]['record']:
                    games[i], games[j] = games[j], games[i]  
        return games 
        
    def ranking(self, games):    
        # tra ve hang cua game hien tai
        if games == []: return [{'file_name': 'You', 'record': self.record, 'level': self.level}]
        if self.record > games[-1]['record']:
            games.append({'file_name': 'You', 'record': self.record, 'level': self.level})
        else:
            for i in range(len(games)):
                if self.record <= games[i]['record']:
                    games.insert(i, {'file_name': 'You', 'record': self.record, 'level': self.level})
                    break
        return games

    # Game funtions   
    def run(self):

        self.new_game()
        # game loop var
        running = True
        running_dfs = True
        # time var
        _time = self.record
        timer = Timer(1000, self.font)
        timer.activate()
        # menu var
        pause = False
        menu_state = 'menu'
        user_input = False
        

        if self.mode == 'auto':
            tmp_start = self.maze.start
            end = self.maze.end 
            while running:          
                cur_cell = tmp_start
                if self.algorithm == 'dfs': running_dfs = True
                else: running_dfs = False
                
                # dfs
                if running_dfs:
                    path_dfs = [cur_cell]              
                    self.maze.grid[cur_cell[0]][cur_cell[1]].is_visited = True     
                    visited_cells = []
                while running_dfs:
                    self.draw()
                    # check event
                    if pause:
                        if menu_state == 'menu':
                            if self.buttons['resume'].draw(self.screen): # resume
                                pause = False
                            if self.buttons['load'].draw(self.screen): # load
                                pass
                            if self.buttons['main_menu'].draw(self.screen): # main_menu
                                pass
                            if self.buttons['options'].draw(self.screen): # options
                                menu_state = 'options'
                            if self.buttons['quit'].draw(self.screen): # quit
                                running = False

                        elif menu_state == 'options':
                            self.draw_text('{}'.format(self.algorithm), 'black', 500, 500)
                            if self.buttons['chang_alg'].draw(self.screen): # chang_alg
                                if self.algorithm == 'dfs': 
                                    self.set_algorithm('bfs') 
                                    running_dfs = False
                                elif self.algorithm == 'bfs': 
                                    self.set_algorithm('dfs')                                   
                                    running_dfs = True
                                tmp_start = cur_cell
                                for i in range(self.maze.num_rows):
                                        for j in range(self.maze.num_cols):
                                            self.maze.grid[i][j].is_visited = False 
                            if self.buttons['back'].draw(self.screen): # back
                                menu_state = 'menu'

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                if not pause: pause = True
                                else: pause = False 
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    
                    if not pause:
                        # upload time
                        timer.update()
                        if not timer.active:
                            _time += 1      
                            timer.activate()
                        timer.draw(self.screen, _time)
                            
                        neighbour_list = self.maze.find_neighbours(cur_cell[0], cur_cell[1])    
                        neighbour_list = self.maze.validate_neighbours_generate(neighbour_list)
                        neighbour_list = unblock_neighbours(self.maze, cur_cell[0], cur_cell[1], neighbour_list)

                        self.draw_path(path_dfs)
                        self.draw_cur(cur_cell) 
                        if neighbour_list is not None:
                            
                            visited_cells.append(cur_cell)             
                            next_cell = random.choice(neighbour_list)   
                            self.maze.grid[next_cell[0]][next_cell[1]].is_visited = True     
                            cur_cell = next_cell
                            if next_cell == end:
                                running = False
                                break
                            path_dfs.append(cur_cell) 

                        else:  
                            cur_cell = visited_cells.pop()    
                            path_dfs.pop() 
                        time.sleep(0.07)
                        # visual algorithm
                        alg_text = 'Algorithm: {}'.format(self.algorithm)
                        self.draw_text(alg_text, 'black', 900, 100)
                        self.update()
                
                # bfs
                if running_dfs == False:
                    self.maze.grid[cur_cell[0]][cur_cell[1]].is_visited = True
                    paths = [[]]
                    paths[0].append(cur_cell)
                    flag = False
                while not running_dfs:
                    self.draw()
                    # check event
                    if pause:
                        if menu_state == 'menu':
                            if self.buttons['resume'].draw(self.screen): # resume
                                pause = False
                            if self.buttons['load'].draw(self.screen): # load
                                pass
                            if self.buttons['main_menu'].draw(self.screen): # main_menu
                                pass
                            if self.buttons['options'].draw(self.screen): # options
                                menu_state = 'options'
                            if self.buttons['quit'].draw(self.screen): # quit
                                running = False

                        elif menu_state == 'options':
                            self.draw_text('{}'.format(self.algorithm), 'black', 500, 500)
                            if self.buttons['chang_alg'].draw(self.screen): # chang_alg
                                if self.algorithm == 'dfs': 
                                    self.set_algorithm('bfs')
                                    self.maze.start = cur_cell
                                    running_dfs = False
                                elif self.algorithm == 'bfs': 
                                    self.set_algorithm('dfs')
                                    self.maze.start = cur_cell
                                    runnning_dfs = True
                            if self.buttons['back'].draw(self.screen): # back
                                menu_state = 'menu'

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                if not pause: pause = True
                                else: pause = False 
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    if not pause:
                        # upload time
                        timer.update()
                        if not timer.active:
                            _time += 1      
                            timer.activate()
                        timer.draw(self.screen, _time)

                        # visual algorithm
                        alg_text = 'Algorithm: {}'.format(self.algorithm)
                        self.draw_text(alg_text, 'black', 900, 100)

                        for i in paths:
                            self.draw_path(i)
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
                                    flag = True
                            if flag: break                     
                        
                        time.sleep(0.07)
                        self.update()
            time.sleep(3)
        elif self.mode == 'not_auto': # che do nguoi choi
            start = self.maze.start
            end = self.maze.end
            if self.player.row is None: self.player.row, self.player.col = start[0], start[1]

            while running:
                self.draw()
                # check event
                if pause:
                    self.record = _time
                    if menu_state == 'menu':
                        if self.buttons['resume'].draw(self.screen): # resume
                            pause = False
                        if self.buttons['save_1'].draw(self.screen): # save
                            menu_state = 'save1'                        
                        if self.buttons['main_menu'].draw(self.screen): # main_menu
                            pass
                        if self.buttons['options'].draw(self.screen): # options
                            menu_state = 'options'
                        if self.buttons['quit'].draw(self.screen): # quit
                            running = False

                    elif menu_state == 'options':
                        self.draw_text('{}'.format(self.algorithm), 'black', 500, 500)
                        if self.buttons['chang_alg'].draw(self.screen): # chang_alg
                            if self.algorithm == 'dfs': self.set_algorithm('bfs')
                            elif self.algorithm == 'bfs': self.set_algorithm('dfs')
                        if self.buttons['back'].draw(self.screen): # back
                            menu_state = 'menu'
                    
                    elif menu_state == 'finish':
                        bg_img = pygame.image.load('Do_an/Assets/tom_catch_jerry.png').convert_alpha()
                        self.screen.blit(bg_img, (0, 0))
                        self.draw_text(self.record_text(self.record), 'black', 400, 100)
                        if self.buttons['play_again'].draw(self.screen): # play_again
                            pass
                        if self.buttons['save_2'].draw(self.screen): # save
                            menu_state = 'save2'

                    elif menu_state == 'save1':
                        self.draw_text('Enter name of file: {}'.format(self.file_name), 'black', 400, 250)
                        user_input = True
                        if self.buttons['accept_1'].draw(self.screen):
                            user_input = False                            
                            menu_state = 'menu'
                            self.save()
                        if self.buttons['cancel_1'].draw(self.screen):
                            user_input = False
                            menu_state = 'menu'

                    elif menu_state == 'save2':
                        user_input = True
                        bg_img = pygame.image.load('Do_an/Assets/tom_catch_jerry.png').convert_alpha()
                        self.screen.blit(bg_img, (0, 0))
                        self.draw_text(self.record_text(self.record), 'black', 400, 100)
                        self.buttons['play_again'].draw(self.screen)
                        self.buttons['save_2'].draw(self.screen)
                        self.draw_text('Enter name of file: {}'.format(self.file_name), 'black', 400, 250)
                        if self.buttons['accept_2'].draw(self.screen):
                            user_input = False
                            menu_state = 'finish'
                            self.save()
                        if self.buttons['cancel_2'].draw(self.screen):
                            user_input = False
                            self.file_name = ''
                            menu_state = 'finish'

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if not pause: pause = True
                            else: pause = False
                        elif event.key == pygame.K_BACKSPACE:
                            if user_input:                                       
                                self.file_name = self.file_name[:-1]
                        else:
                            if user_input:
                                self.file_name += event.unicode
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                
                if not pause:
                    # process and visual time
                    timer.update()
                    if not timer.active:
                        _time += 1
                        self.record = _time      
                        timer.activate()
                    timer.draw(self.screen, _time)

                    # visual algorithm
                    alg_text = 'Algorithm: {}'.format(self.algorithm)
                    self.draw_text(alg_text, 'black', 900, 100)
                    # visual rank
                    games = self.ranking(self.take_score())
                    self.draw_rank(games)

                    # process move (press w,a,s,d or up,down,right,left)
                    self.handle_move()
                    if (self.player.row, self.player.col) == end:
                        self.completed = True
                        self.record = _time
                        pause = True
                        menu_state = 'finish'
                    self.draw_cur((self.player.row, self.player.col))

                    # process hint(press H)
                    self.handle_hint()    
                    
                self.update()
                time.sleep(0.1) 
                   

if __name__ == '__main__':
    game = Game('easy', 'not_auto')
    game.run()
