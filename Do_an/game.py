import pygame
from pygame.time import get_ticks
from maze import *
from algrithms import *
import pickle
import time
from os import listdir 
from os.path import isfile, join
from tkinter import *
from tkinter import messagebox

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
    def __init__(self, duration, font = None):
        self.duration = duration 
        self.active = False
        self.font = font
        self.start = 0
        self.time = time
        self.pause = False

    def activate(self):
        self.active = True
        self.start = get_ticks()

    def deactivate(self):
        self.active = False
        self.start = 0

    def update(self):
        if self.active:
            if self.pause:
                cur_time = get_ticks()
                if cur_time - self.tmp >= self.duration:
                    self.pause = False
                    self.deactivate()
            else:
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

    def set_duration(self, new_duration):
        self.duration = new_duration

class Player:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size

    def move(self, direction):
        if direction == 'top':
            self.row -= 1
        elif direction == 'bot':
            self.row += 1
        elif direction == 'right':
            self.col += 1
        elif direction == 'left':
            self.col -= 1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.col*self.size + 2, self.row*self.size + 2, self.size - 4, self.size - 4))

class saveloadsystem:
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
            if game_manager is None:
                return {name_file: game}
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

class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int) -> None:
        self.pos = pos
        self.size = size
        self.clicked = False

        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos-self.slider_left_pos)*initial_val # <- percentage

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])

    def draw(self, screen):
        #draw button on screen
        pygame.draw.rect(screen, "darkgray", self.container_rect)
        pygame.draw.rect(screen, 'red', self.button_rect)

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos
        return (button_val/val_range)*(self.max-self.min)+self.min
    
    def display_value(self, screen, font):       
        self.text = font.render(str(int(self.get_value())), True, "black", None)
        self.label_rect = self.text.get_rect(center = (self.pos[0], self.slider_top_pos - 15))
        screen.blit(self.text, self.label_rect) 

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("Do_an","Assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]
    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(int(sprite_sheet.get_width()//width)):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(surface)

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
            all_sprites[image.replace(".png", "") + "_up"] = sprites
            all_sprites[image.replace(".png", "") + "_down"] = sprites
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, dx, dy):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.width = width
        self.height = height
        self.dx = dx
        self.dy = dy
    def draw(self, win, offset_x, offset_y):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))   

class Jerry(Object):
    ANIMATION_DELAY = 6

    def __init__(self, x, y, width, height, dx, dy):
        super().__init__(x, y, width, height, dx, dy)
        self.jerry = load_sprite_sheets("MainCharacters", "Jerry", 34, 58)
        self.image = self.jerry["idlle"][0]
        self.image = pygame.transform.scale(self.image, (width, height))
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "idlle"

    def loop(self):
        sprites = self.jerry[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = pygame.transform.scale(sprites[sprite_index], (self.width, self.height))
        self.animation_count += 2

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class Player_pro(pygame.sprite.Sprite):
    ANIMATION_DELAY = 6
    def __init__(self, x, y, size, name):
        super().__init__()
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, size, size)
        self.name = name
        self.x_vel = 0.0
        self.y_vel = 0.0
        self.direction = 'left'
        self.animation_count = 0
        if name == 'Tom':
            self.sprites = load_sprite_sheets("MainCharacters", name, 56, 56, 'True')
        else:
            self.sprites = load_sprite_sheets("MainCharacters", name, 32, 32, 'True')
        self.tile = size
        self.row, self.col = y//size, x//size

    def move(self, dx: float, dy: float):
        self.x += dx
        self.rect.x = self.x
        self.y += dy
        self.rect.y = self.y

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel 
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def move_up(self, vel):
        self.y_vel = -vel
        if self.direction != "up":
            self.direction = "up"
            self.animation_count = 0

    def move_down(self, vel):
        self.y_vel = vel
        if self.direction != "down":
            self.direction = "down"
            self.animation_count = 0

    def loop(self):
        self.move(self.x_vel, self.y_vel)
        self.update_sprite()
        self.update()

    def update_sprite(self):
        if self.name == 'Tom': sprite_sheet = "run" 
        else: sprite_sheet = "idle" 
        if self.x_vel or self.y_vel:   
            sprite_sheet = 'run'
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.sprites[sprite_sheet_name]
        sprite_index = (self.animation_count //self.ANIMATION_DELAY) % len(sprites)
        self.sprite = pygame.transform.scale(sprites[sprite_index], (self.tile, self.tile))
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
    
    def draw(self, win):
        win.blit(self.sprite, (self.rect.x, self.rect.y))

class Game:
    def __init__(self, level = None, mode = None, choose = False, player_name = 'Square', map = 'green'):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Maze Game')
        self.WINDOW_SIZE = 1202, 802
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.level = level
        self.mode = mode
        self.choose = choose
        self.map = map
        self.player_name = player_name
        self.player = None
        self.maze = None
        self.algorithm = 'dfs'
        self.tile = None
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font_mini = pygame.font.Font('freesansbold.ttf', 20)
        self.buttons = self.button()
        self.start, self.end = None, None
        self.record = 0
        self.rank = None
        self.file_name = ''
        self.saveloadmanager = saveloadsystem('.save', 'Do_an/SaveLoad/game_manager')
        self.completed = False
        self.sliders = self.slider()
        self.delay = 50
        self.is_saved = False
        self.sound = self.sound_effect() 

    def button(self):
        Size_img = (160,40)
        Size_img_IG = (80, 50)
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
        gameFrame_img = pygame.image.load('Do_an/button/gameFrame.png').convert_alpha()
        delay_img = pygame.image.load('Do_an/button/DelayButton.png').convert_alpha()
        pause_img = pygame.image.load('Do_an/button/Pause_IG.png').convert_alpha()
        mute_img = pygame.image.load('Do_an/button/mute_IG.png').convert_alpha()
        hint_img = pygame.image.load('Do_an/button/hint_IG.png').convert_alpha()
        vol_on_img = pygame.image.load('Do_an/button/volume_on.png').convert_alpha()
        vol_off_img = pygame.image.load('Do_an/button/volume_off.png').convert_alpha()
        sound_img = pygame.image.load('Do_an/button/SoundButton.png').convert_alpha()
        a = [resume_img,load_img,menu_img,options_img,quit_img,save_img]
        b = [pause_img, mute_img, hint_img]
        for i in range(len(a)):
            a[i] = pygame.transform.scale(a[i],Size_img)
        for i in range(len(b)):
            b[i] = pygame.transform.scale(b[i], Size_img_IG)
        # create button
        resume_button = Button(500, 320, a[0], 1)
        load_button = Button(500, 400, a[1], 1)
        menu_button = Button(500, 240, a[2], 1)
        options_button = Button(500, 480, a[3], 1)
        quit_button = Button(500, 560, a[4], 1)
        change_alg_button = Button(500, 430, change_alg_img, 1)
        back_button = Button(530, 520, back_img, 1)
        play_again_button = Button(900, 400, play_again_img, 1)
        save_button_1 = Button(500, 400, a[5], 1)
        save_button_2 = Button(900, 450, a[5], 1)
        accept_button_1 = Button(600, 350, accept_img, 1)
        cancel_button_1 = Button(430, 350, cancel_img, 1)
        accept_button_2 = Button(600, 300, accept_img, 1)
        cancel_button_2 = Button(400, 300, cancel_img, 1)
        accept_button_3 = Button(1000, 300, accept_img, 1)
        cancel_button_3 = Button(850, 300, cancel_img, 1)
        gameFrame = Button(380,120,gameFrame_img,1)
        delay_button = Button(520, 260, delay_img, 1)
        pause_button = Button(850, 700, pause_img, 1)
        mute_button = Button(980, 700, mute_img, 1)
        hint_button = Button(1100, 700, hint_img, 1)
        vol_on_button = Button(980, 700, vol_on_img, 1)
        vol_off_button = Button(980, 700, vol_off_img, 1)
        sound_button = Button(520, 380, sound_img, 1)
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
                'cancel_2': cancel_button_2,
                'accept_3': accept_button_3,
                'cancel_3': cancel_button_3,
                'gameFrame':gameFrame,
                'delay': delay_button,
                'pause': pause_button,
                'mute' : mute_button,
                'hint' : hint_button,
                'vol_on': vol_on_button,
                'vol_off': vol_off_button,
                'sound': sound_button}

    def tile_images(self):
        img_path = pygame.image.load('Do_an/Assets/Background/Green.png').convert_alpha()
        img_path = pygame.transform.scale(img_path, (self.tile, self.tile))
        img_path_4 = pygame.image.load('Do_an/Assets/Background/grey_path.png').convert_alpha()
        img_path_4 = pygame.transform.scale(img_path_4, (self.tile, self.tile))
        img_path_5 = pygame.image.load('Do_an/Assets/Background/water_path.png').convert_alpha()
        img_path_5 = pygame.transform.scale(img_path_5, (self.tile, self.tile))
        img_path_6 = pygame.image.load('Do_an/Assets/Background/green_path.png').convert_alpha()
        img_path_6 = pygame.transform.scale(img_path_6, (self.tile, self.tile))
        img_path_2 = pygame.image.load('Do_an/Assets/Background/Gray.png').convert_alpha()
        img_path_2 = pygame.transform.scale(img_path_2, (40, 40))
        img_path_3 = pygame.image.load('Do_an/Assets/Background/Yellow.png').convert_alpha()
        img_path_3 = pygame.transform.scale(img_path_3, (40, 40))
        return {'path': img_path, 'path_2': img_path_2,'path_3': img_path_3, 'grey': img_path_4, 'blue': img_path_5,  'green': img_path_6}
    
    def slider(self):
        delay_slider = Slider((590, 350), (200, 30), 0.5, 0, 100)
        music_slider = Slider((650, 364), (150, 30), 0.5, 0, 100)
        sound_effect_slider = Slider((650, 464), (150, 30), 0.5, 0, 100)
        return {'delay': delay_slider, 'music': music_slider, 'sound_effect': sound_effect_slider}
    
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

    def handle_move_pro(self):

        self.player.x_vel, self.player.y_vel = 0, 0 
        self.player.x = round(self.player.x)
        self.player.y = round(self.player.y)  
        if self.player.x%self.tile != 0:
            if self.player.direction == 'right':
                self.player.x = (self.player.x//self.tile + 1)*self.tile
            elif self.player.direction == 'left':
                self.player.x = (self.player.x//self.tile)*self.tile
        if self.player.y%self.tile != 0:
            if self.player.direction == 'up':
                self.player.y = (self.player.y//self.tile)*self.tile
            elif self.player.direction == 'down':
                self.player.y = (self.player.y//self.tile + 1)*self.tile       
        self.player.row = self.player.y//self.tile
        self.player.col = self.player.x//self.tile 
        keys = pygame.key.get_pressed()

        if self.level == 'hard':
            vel = self.tile/1
        elif self.level == 'medium':
            vel = self.tile/6
        else:
            vel = self.tile/7
        cur_row, cur_col = self.player.row, self.player.col
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.player.col > 0 and not self.maze.grid[cur_row][cur_col].walls['left']:
            self.player.move_left(float(vel))
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.player.col < self.maze.num_cols-1 and not self.maze.grid[cur_row][cur_col].walls['right']:
            self.player.move_right(float(vel))
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.player.row < self.maze.num_rows-1 and not self.maze.grid[cur_row][cur_col].walls['bot']:
            self.player.move_down(float(vel))
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and self.player.row > 0 and not self.maze.grid[cur_row][cur_col].walls['top']:
            self.player.move_up(float(vel))
    
    def handle_hint(self):
        self.maze.start = self.start
        self.maze.end = self.end
        cur = self.player.row, self.player.col
        if self.algorithm == 'dfs': 
            hint = dfs(self.maze, cur)
        elif self.algorithm == 'bfs':
            hint = bfs(self.maze, cur)
        key = pygame.key.get_pressed()
        if self.buttons['hint'].draw(self.screen) or key[pygame.K_h]:
            self.draw_hint(hint[:])
        
    # Setting functions      
    def set_tile(self):
        if self.level == 'easy': self.tile = 40
        elif self.level == 'medium': self.tile = 20
        else: self.tile = 8
    
    def set_delay(self):   
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.sliders['delay'].container_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.sliders['delay'].clicked:
                if pos[0] < self.sliders['delay'].slider_left_pos:
                    pos[0] = self.sliders['delay'].slider_left_pos
                if pos[0] > self.sliders['delay'].slider_right_pos:
                    pos[0] = self.sliders['delay'].slider_right_pos
                self.sliders['delay'].button_rect.centerx = pos[0]
        self.sliders['delay'].draw(self.screen)
        self.sliders['delay'].display_value(self.screen, self.font_mini)
        return self.sliders['delay'].get_value()
    
    def set_volume(self, slider):
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if slider.container_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not slider.clicked:
                if pos[0] < slider.slider_left_pos:
                    pos[0] = slider.slider_left_pos
                if pos[0] > slider.slider_right_pos:
                    pos[0] = slider.slider_right_pos
                slider.button_rect.centerx = pos[0]
        slider.draw(self.screen)
        slider.display_value(self.screen, self.font_mini)
        return slider.get_value()
        
    def set_algorithm(self, algorithm):
        self.algorithm = algorithm
    
    def new_game(self):
        self.set_tile()
        self.tile_imgs = self.tile_images()
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
        else:
            self.start, self.end = self.maze.start, self.maze.end
        
    def update(self):
        pygame.display.update()
        self.clock.tick(60)

    def save(self):
        data = {'level': self.level, 'choose': self.choose, 'mode': self.mode,'maze': self.maze,'alg': self.algorithm,
                'start': self.start,'end': self.end, 'record': self.record, 'file_name': self.file_name,
                'player': self.player_name, 'completed': self.completed, 'is_saved': True, 'delay': self.delay}
        if self.saveloadmanager.check_file_name(self.file_name):
            self.message('File name has already exist')
        else:
            self.saveloadmanager.save_game(self.file_name, data)
            self.message('Save file succeeded')

    def load(self, file_name):
        if not self.saveloadmanager.check_file_name(file_name):
            self.message('Find not found')
            return False
        else:
            data = self.saveloadmanager.load_game(file_name)
            self.level = data['level']
            self.mode = data['mode']
            self.choose = data['choose']
            self.maze = data['maze']
            self.algorithm = data['alg']
            self.start = data['start']
            self.end = data['end']
            self.record = data['record']
            self.file_name = data['file_name']
            self.player_name = data['player']
            self.completed = data['completed'] 
            self.is_saved = data['is_saved']
            self.delay = data['delay']   
            self.message('Load file succeeded')
            return True

    # Draw functions
    def draw_tiles_map(self):
        for i in range(self.maze.num_rows):
            for j in range(self.maze.num_cols):
                self.screen.blit(self.tile_imgs[self.map], (j*self.tile, i*self.tile))

    def draw_tiles_map_2(self):
        for i in range(10):
            for j in range(10):
                self.screen.blit(self.tile_imgs['path_2'], (800 + j * 40, i * 40))

    def draw_tiles_map_3(self):
        for i in range(16):
            for j in range(10):
                self.screen.blit(self.tile_imgs['path_3'], (800 + j * 40, 160 + i * 40))

    def draw_text(self, text, color, x, y):
        img = self.font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def draw_text_mini(self, text, color, x, y):
        img = self.font_mini.render(text, True, color)
        self.screen.blit(img, (x, y))

    def draw_cur(self, cur_cell):
        pygame.draw.rect(self.screen, (255, 0, 0), (cur_cell[1]*self.tile + 2, cur_cell[0]*self.tile + 2, self.tile - 4, self.tile - 4))

    def draw_maze(self):
        for i in range(self.maze.num_rows):
            for j in range(self.maze.num_cols):
                self.maze.grid[i][j].draw(self.screen, self.tile)
        
    def draw_end(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.end[1]*self.tile + 2, self.end[0]*self.tile + 2, self.tile - 4, self.tile - 4))

    def draw_path(self, path):
        for cell_x, cell_y in path:
            pygame.draw.rect(self.screen, 'darkviolet', (cell_y*self.tile + 2, cell_x*self.tile + 2, self.tile - 4, self.tile - 4)) 

    def draw_solution(self, solution):
        for cell_x, cell_y in solution:
            pygame.draw.rect(self.screen, 'yellow', (cell_y*self.tile + 2, cell_x*self.tile + 2, self.tile - 4, self.tile - 4))
            if self.start == (cell_x, cell_y):
                time.sleep(3)
            
    def draw_hint(self, hint):
        
        for i in range(len(hint)-1):
            cur_cell = hint[i]
            next_cell = hint[i+1]      
            pygame.draw.line(self.screen, 'green', (cur_cell[1]*self.tile + self.tile//2, cur_cell[0]*self.tile + self.tile//2),
                                                 (next_cell[1]*self.tile + self.tile//2, next_cell[0]*self.tile + self.tile//2), 3)
                   
    def draw(self):
        self.screen.fill('white')
        self.draw_tiles_map()
        self.draw_tiles_map_2()
        self.draw_tiles_map_3()
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
  
    def draw_choose_cell(self, cell_choose):
        if cell_choose is None: return 
        pygame.draw.rect(self.screen, (0, 0, 255), (cell_choose[1]*self.tile + 2, cell_choose[0]*self.tile + 2, self.tile - 4, self.tile - 4))

    # Event funtions
    def sound_effect(self):
        ting_effect = pygame.mixer.Sound('Do_an/Assets/Sound/ting.mp3')
        return {'ting': ting_effect}
    
    def message(self, text):
        mess = Tk()
        mess.geometry('0x0')
        mess.eval('tk::PlaceWindow %s center' %mess.winfo_toplevel())
        mess.withdraw()
        mess.deiconify()
        mess.destroy()
        messagebox.showinfo('Notification', text)
        mess.quit()

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
        if game_manager is None: return games
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

    def transitions(self):
        fade_counter = 0
        while fade_counter < 1202:
            pygame.draw.rect(self.screen, 'black', (0, 0, fade_counter, 802))
            pygame.display.update()
            fade_counter += 2

    # Game funtions 
    def set_player(self, name):
        if name == 'Frog': 
            self.player = Player_pro(self.start[1]*self.tile, self.start[0]*self.tile, self.tile, 'Frog')
        elif name == 'Blueman': 
            self.player = Player_pro(self.start[1]*self.tile, self.start[0]*self.tile, self.tile, 'Blueman')
        elif name == 'Tom': 
            self.player = Player_pro(self.start[1]*self.tile, self.start[0]*self.tile, self.tile, 'Tom')
        elif name == 'MaskDude':
            self.player = Player_pro(self.start[1]*self.tile, self.start[0]*self.tile, self.tile, 'MaskDude')
        else: 
            self.player = Player(self.start[0], self.start[1], self.tile)
        
    def set_maze_visit(self):
        for i in range(self.maze.num_rows):
            for j in range(self.maze.num_cols):
                self.maze.grid[i][j].is_visited = False 

    def run(self):
        self.new_game()
        # game loop var
        running = True
        running_dfs = True
        # sound
        music = pygame.mixer.music
        music.load('Do_an/Assets/Sound/GamePlay_music.mp3')
        music.play(loops = -1)
        music.set_volume(0.5)
        music_vol = 50
        sound_effect_vol = 50
        user_turnoff = False
        # time var
        _time = self.record
        timer = Timer(1000, self.font)
        timer.activate()
        if self.level != 'hard': time_move = Timer(20 + self.delay*0.9)
        else: time_move = Timer(self.delay)
        time_move.activate()
        # menu var
        if self.is_saved: pause = True
        else: pause = False
        menu_state = 'menu'
        user_input = False
        # process random_entry_exit
        if self.choose and not self.is_saved:
            self.start = None
            self.end = None
            while self.choose:
                self.draw()     
                pos = pygame.mouse.get_pos()
                cell_choosen = None
                if pos[0] > 0 and pos[0] < 800 and pos[1] > 0 and pos[1] < 800:
                    cell_choosen = pos[1]//self.tile, pos[0]//self.tile
                    self.draw_choose_cell(cell_choosen)

                if self.start is None:
                    if pygame.mouse.get_pressed()[0] and cell_choosen is not None:          
                        self.start = cell_choosen
                    self.draw_text('Choose start: ', 'black', 850, 100)
                
                if self.end is None and self.start is not None:
                    self.draw_cur(self.start)
                    if pygame.mouse.get_pressed()[0] and cell_choosen != self.start:
                        self.end = cell_choosen
                    self.draw_text('Start: {}'.format(self.start), 'black', 850, 100)
                    self.draw_text('Choose end: ', 'black', 850, 200)
                    
                if self.start is not None and self.end is not None:
                    self.draw_cur(self.start)
                    self.draw_end()
                    self.draw_text('Start: {}'.format(self.start), 'black', 850, 100)
                    self.draw_text('End: {}'.format(self.end), 'black', 850, 200)          
                    if self.buttons['cancel_3'].draw(self.screen):
                        self.start = None
                        self.end = None
                        cell_choosen = None
                    if self.buttons['accept_3'].draw(self.screen):
                        break  

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                self.update()
        self.transitions()
        # character
        self.set_player(self.player_name)
        jerry = Jerry(self.end[1]*self.tile + 1, self.end[0]*self.tile + 1, self.tile*0.9, self.tile, 0, 0)
        if self.mode == 'auto':
            tmp_start = self.start
            end = self.end 
            solution_path = dfs(self.maze, self.start, self.end)
            run_solution = False
            tmp_path = []
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
                    jerry.draw(self.screen, 0, 0)
                    if self.buttons['pause'].draw(self.screen): # pause
                        pause = True
                    if music.get_busy():
                        if self.buttons['vol_on'].draw(self.screen): # volume on
                            if not pause:
                                music.pause()
                                user_turnoff = False
                    else:
                        if self.buttons['vol_off'].draw(self.screen): # volume off
                            if not pause:
                                music.unpause()
                                user_turnoff = True
                    self.buttons['hint'].draw(self.screen)
                    # check event
                    if pause:
                        if menu_state == 'menu':
                            
                            self.buttons['gameFrame'].draw(self.screen)
                            if self.buttons['resume'].draw(self.screen): # resume
                                self.sound['ting'].play()
                                pause = False
                                music.unpause()
                            if self.buttons['save_1'].draw(self.screen): # save
                                self.sound['ting'].play()
                                menu_state = 'save1'
                            if self.buttons['main_menu'].draw(self.screen): # main_menu
                                self.sound['ting'].play()
                            if self.buttons['options'].draw(self.screen): # options
                                self.sound['ting'].play()
                                menu_state = 'options'
                            if self.buttons['quit'].draw(self.screen): # quit 
                                self.sound['ting'].play()                              
                                running = False
                                mess = Tk()
                                mess.geometry('0x0')
                                mess.eval('tk::PlaceWindow %s center' %mess.winfo_toplevel())
                                mess.withdraw()
                                if messagebox.askyesno('Question', 'Do you really want to quit game?'): break
                                mess.quit()

                        elif menu_state == 'save1':
                            self.buttons['gameFrame'].draw(self.screen)
                            self.draw_text('Enter name of file: {}'.format(self.file_name), 'black', 400, 250)
                            user_input = True
                            if self.buttons['accept_1'].draw(self.screen):
                                self.sound['ting'].play()
                                user_input = False                            
                                menu_state = 'menu'
                                self.save()
                            if self.buttons['cancel_1'].draw(self.screen):
                                self.sound['ting'].play()
                                user_input = False
                                menu_state = 'menu'

                        elif menu_state == 'options':
                            self.buttons['gameFrame'].draw(self.screen)
                            self.buttons['delay'].draw(self.screen)
                            self.delay = self.set_delay()
                            self.draw_text('{}'.format(self.algorithm), 'black', 560, 470)
                            if self.buttons['sound'].draw(self.screen): # sound
                                self.sound['ting'].play()
                                menu_state = 'sound'
                            if self.buttons['chang_alg'].draw(self.screen): # chang_alg
                                self.sound['ting'].play()
                                self.set_algorithm('bfs') 
                                running_dfs = False
                                tmp_start = cur_cell
                                self.set_maze_visit()
                            if self.buttons['back'].draw(self.screen): # back
                                self.sound['ting'].play()
                                menu_state = 'menu'

                        elif menu_state == 'sound':
                            self.buttons['gameFrame'].draw(self.screen)
                            self.draw_text('Music', 'black', 400, 350)
                            self.draw_text('Sound effect', 'black', 400, 450)
                            self.sliders['music'].draw(self.screen)
                            music_vol = self.set_volume(self.sliders['music'])
                            self.sliders['sound_effect'].draw(self.screen)
                            sound_effect_vol = self.set_volume(self.sliders['sound_effect'])
                            if self.buttons['back'].draw(self.screen): # back
                                self.sound['ting'].play()
                                menu_state = 'options'
                        
                        elif menu_state == 'finish':
                            bg_img = pygame.image.load('Do_an/Assets/Background/tom_catch_jerry.png').convert_alpha()
                            self.screen.blit(bg_img, (0, 0))
                            self.draw_text(self.record_text(self.record), 'black', 400, 100)
                            if self.buttons['play_again'].draw(self.screen): # play_again
                                self.sound['ting'].play()
                                running = False
                                self.transitions
                                self.new_game()
                                self.record = 0
                                self.start, self.end = None, None
                                self.run()
                            if self.buttons['save_2'].draw(self.screen): # save
                                self.sound['ting'].play()
                                menu_state = 'save2'

                        elif menu_state == 'save2':
                            self.buttons['gameFrame'].draw(self.screen)
                            user_input = True
                            bg_img = pygame.image.load('Do_an/Assets/Background/tom_catch_jerry.png').convert_alpha()
                            self.screen.blit(bg_img, (0, 0))
                            self.draw_text(self.record_text(self.record), 'black', 400, 100)
                            self.buttons['play_again'].draw(self.screen)
                            self.buttons['save_2'].draw(self.screen)
                            self.draw_text('Enter name of file: {}'.format(self.file_name), 'black', 400, 250)
                            if self.buttons['accept_2'].draw(self.screen):
                                self.sound['ting'].play()
                                user_input = False
                                menu_state = 'finish'
                                self.set_maze_visit()
                                self.save()
                            if self.buttons['cancel_2'].draw(self.screen):
                                self.sound['ting'].play()
                                user_input = False
                                self.file_name = ''
                                menu_state = 'finish'

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                if menu_state == 'menu':
                                    if not pause: pause = True
                                    else: pause = False 
                                
                            elif event.key == pygame.K_BACKSPACE:
                                if user_input:                                       
                                    self.file_name = self.file_name[:-1]
                            else:
                                if user_input:
                                    if len(self.file_name) < 8: self.file_name += event.unicode
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
                            
                        neighbour_list = self.maze.find_neighbours(cur_cell[0], cur_cell[1])    
                        neighbour_list = self.maze.validate_neighbours_generate(neighbour_list)
                        neighbour_list = unblock_neighbours(self.maze, cur_cell[0], cur_cell[1], neighbour_list)
                        if not run_solution:                    
                            if neighbour_list is not None:
                                self.draw_path(path_dfs)               
                                visited_cells.append(cur_cell)             
                                next_cell = random.choice(neighbour_list)   
                                self.maze.grid[next_cell[0]][next_cell[1]].is_visited = True 
                                if next_cell == end:
                                    run_solution = True
                                cur_cell = next_cell
                                self.draw_cur(cur_cell)
                                path_dfs.append(cur_cell) 
                            else:   
                                cur_cell = visited_cells.pop()    
                                path_dfs.pop() 
                                if not run_solution:  
                                    self.draw_path(path_dfs)
                                    self.draw_cur(cur_cell)   
                        else:
                            tmp_path.append(solution_path.pop())                         
                            self.draw_path(path_dfs)
                            self.draw_solution(tmp_path)
                            if solution_path == []:
                                running = False
                                self.completed = True
                                self.record = _time
                                pause = True
                                menu_state = 'finish'
                        time.sleep(0.0015*self.delay)                     
                    self.update()
                
                # bfs
                if running_dfs == False:
                    self.maze.grid[cur_cell[0]][cur_cell[1]].is_visited = True
                    paths = [[]]
                    paths[0].append(cur_cell)
                    flag = False
                while not running_dfs:
                    self.draw()
                    jerry.draw(self.screen, 0, 0)
                    if self.buttons['pause'].draw(self.screen): # pause
                        if not pause: 
                            self.sound['ting'].play()
                            pause = True
                    if music.get_busy():
                        if self.buttons['vol_on'].draw(self.screen): # volume on
                            if not pause: 
                                self.sound['ting'].play()
                                music.pause()
                    else:
                        if self.buttons['vol_off'].draw(self.screen): # volume off
                            if not pause: 
                                self.sound['ting'].play()
                                music.unpause()
                    self.buttons['hint'].draw(self.screen)
                    # check event
                    if pause:
                        if menu_state == 'menu':
                            self.buttons['gameFrame'].draw(self.screen)
                            if self.buttons['resume'].draw(self.screen): # resume
                                self.sound['ting'].play()
                                pause = False
                            if self.buttons['save_1'].draw(self.screen): # load
                                self.sound['ting'].play()
                                menu_state = 'save_1'
                            if self.buttons['main_menu'].draw(self.screen): # main_menu
                                self.sound['ting'].play()
                                pass
                            if self.buttons['options'].draw(self.screen): # options
                                self.sound['ting'].play()
                                menu_state = 'options'
                            if self.buttons['quit'].draw(self.screen): # quit
                                self.sound['ting'].play()
                                mess = Tk()
                                mess.geometry('0x0')
                                mess.eval('tk::PlaceWindow %s center' %mess.winfo_toplevel())
                                mess.withdraw()
                                if messagebox.askyesno('Question', 'Do you really want to quit game?'): 
                                    running = False
                                    break
                                mess.quit()
                                
                        elif menu_state == 'save1':
                            self.buttons['gameFrame'].draw(self.screen)
                            self.draw_text('Enter name of file: {}'.format(self.file_name), 'black', 400, 250)
                            user_input = True
                            if self.buttons['accept_1'].draw(self.screen):
                                self.sound['ting'].play()
                                user_input = False                            
                                menu_state = 'menu'
                                self.save()
                            if self.buttons['cancel_1'].draw(self.screen):
                                self.sound['ting'].play()
                                user_input = False
                                menu_state = 'menu'

                        elif menu_state == 'options':
                            self.buttons['gameFrame'].draw(self.screen)
                            self.buttons['delay'].draw(self.screen)
                            self.delay = self.set_delay()
                            self.draw_text('{}'.format(self.algorithm), 'black', 560, 470)
                            if self.buttons['sound'].draw(self.screen): # sound
                                self.sound['ting'].play()
                                menu_state = 'sound'
                            if self.buttons['chang_alg'].draw(self.screen): # chang_alg
                                self.sound['ting'].play()
                                self.set_algorithm('dfs')
                                tmp_start = cur_cell
                                self.set_maze_visit()
                                running_dfs = True
                            if self.buttons['back'].draw(self.screen): # back
                                self.sound['ting'].play()
                                menu_state = 'menu'

                        elif menu_state == 'sound':
                            self.buttons['gameFrame'].draw(self.screen)
                            self.draw_text('Music', 'black', 400, 350)
                            self.draw_text('Sound effect', 'black', 400, 450)
                            self.sliders['music'].draw(self.screen)
                            music_vol = self.set_volume(self.sliders['music'])
                            self.sliders['sound_effect'].draw(self.screen)
                            sound_effect_vol = self.set_volume(self.sliders['sound_effect'])
                            if self.buttons['back'].draw(self.screen): # back
                                self.sound['ting'].play()
                                menu_state = 'options'
                        
                        elif menu_state == 'finish':
                            bg_img = pygame.image.load('Do_an/Assets/Background/tom_catch_jerry.png').convert_alpha()
                            self.screen.blit(bg_img, (0, 0))
                            self.draw_text(self.record_text(self.record), 'black', 400, 100)
                            if self.buttons['play_again'].draw(self.screen): # play_again
                                self.sound['ting'].play()
                                running = False
                                self.transitions
                                self.new_game()
                                self.record = 0
                                self.start, self.end = None, None
                                self.run()
                            if self.buttons['save_2'].draw(self.screen): # save
                                self.sound['ting'].play()
                                menu_state = 'save2'

                        elif menu_state == 'save2':
                            self.buttons['gameFrame'].draw(self.screen)
                            user_input = True
                            bg_img = pygame.image.load('Do_an/Assets/Background/tom_catch_jerry.png').convert_alpha()
                            self.screen.blit(bg_img, (0, 0))
                            self.draw_text(self.record_text(self.record), 'black', 400, 100)
                            self.buttons['play_again'].draw(self.screen)
                            self.buttons['save_2'].draw(self.screen)
                            self.draw_text('Enter name of file: {}'.format(self.file_name), 'black', 400, 250)
                            if self.buttons['accept_2'].draw(self.screen):
                                self.sound['ting'].play()
                                user_input = False
                                menu_state = 'finish'
                                self.set_maze_visit()
                                self.save()
                            if self.buttons['cancel_2'].draw(self.screen):
                                self.sound['ting'].play()
                                user_input = False
                                self.file_name = ''
                                menu_state = 'finish'

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                if menu_state == 'menu':
                                    if not pause: pause = True
                                    else: pause = False 
                                
                            elif event.key == pygame.K_BACKSPACE:
                                if user_input:                                       
                                    self.file_name = self.file_name[:-1]
                            else:
                                if user_input:
                                    if len(self.file_name) < 8:
                                        self.file_name += event.unicode
                        if event.type == pygame.QUIT:
                            mess = Tk()
                            mess.geometry('0x0')
                            mess.eval('tk::PlaceWindow %s center' %mess.winfo_toplevel())
                            mess.withdraw()
                            if messagebox.askyesno('Question', 'Do you really want to quit game?'): 
                                pygame.quit()
                                quit()
                            mess.quit()
                                     
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

                        if not run_solution:
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
                                        run_solution = True
                                if flag: 
                                    self.completed = True
                                    self.record = _time
                                    pause = True
                                    menu_state = 'finish'  
                        else: 
                            for i in paths:
                                self.draw_path(i)
                            if solution_path.pop() != end:
                               tmp_path.append(solution_path.pop())                         
                            self.draw_solution(tmp_path)
                            if solution_path == []:
                                running = False
                                self.completed = True
                                self.record = _time
                                pause = True
                                menu_state = 'finish' 
                        if not run_solution:             
                            time.sleep(0.0015*self.delay)
                        else:
                            time.sleep(0.001*self.delay)
                    self.update()
                
        elif self.mode == 'not_auto': # che do nguoi choi
            start = self.start
            end = self.end
            if self.player.row is None: self.player.row, self.player.col = start[0], start[1]
            while running:
                self.draw()
                if self.buttons['pause'].draw(self.screen): # pause
                    pause = True
                    music.pause()
                if music.get_busy():
                    if self.buttons['vol_on'].draw(self.screen): # volume on
                        if not pause:
                            music.pause()
                            user_turnoff = False
                else:
                    if self.buttons['vol_off'].draw(self.screen): # volume off
                        if not pause:
                            music.unpause()
                            user_turnoff = True
                if self.buttons['hint'].draw(self.screen):
                    if not pause:
                        self.handle_hint()
                jerry.draw(self.screen, 0, 0)
                jerry.loop()
                if self.player_name != 'Square':
                    self.player.loop()
                # check event
                if pause:
                    self.record = _time
                    if menu_state == 'menu':
                        self.buttons['gameFrame'].draw(self.screen)
                        if self.buttons['resume'].draw(self.screen): # resume
                            self.sound['ting'].play()
                            pause = False
                            if user_turnoff: music.unpause()
                        if self.buttons['save_1'].draw(self.screen): # save
                            self.sound['ting'].play()
                            menu_state = 'save1'                        
                        if self.buttons['main_menu'].draw(self.screen): # main_menu
                            self.sound['ting'].play()
                            pass
                        if self.buttons['options'].draw(self.screen): # options
                            self.sound['ting'].play()
                            menu_state = 'options'
                        if self.buttons['quit'].draw(self.screen): # quit
                            self.sound['ting'].play()
                            mess = Tk()
                            mess.geometry('0x0')
                            mess.eval('tk::PlaceWindow %s center' %mess.winfo_toplevel())
                            mess.withdraw()
                            if messagebox.askyesno('Question', 'Do you really want to quit game?'): 
                                running = False
                                break
                            mess.quit()                     

                    elif menu_state == 'options':                   
                        self.buttons['gameFrame'].draw(self.screen)
                        self.buttons['delay'].draw(self.screen)
                        self.delay = self.set_delay()
                        self.draw_text('{}'.format(self.algorithm), 'black', 560, 470)
                        if self.buttons['sound'].draw(self.screen): # sound
                            menu_state = 'sound'
                        if self.buttons['chang_alg'].draw(self.screen): # chang_alg
                            if self.algorithm == 'dfs': self.set_algorithm('bfs')
                            elif self.algorithm == 'bfs': self.set_algorithm('dfs')
                        if self.buttons['back'].draw(self.screen): # back
                            menu_state = 'menu'
                    
                    elif menu_state == 'sound':
                        self.buttons['gameFrame'].draw(self.screen)
                        self.draw_text('Music', 'black', 400, 350)
                        self.draw_text('Sound effect', 'black', 400, 450)
                        self.sliders['music'].draw(self.screen)
                        music_vol = self.set_volume(self.sliders['music'])
                        self.sliders['sound_effect'].draw(self.screen)
                        sound_effect_vol = self.set_volume(self.sliders['sound_effect'])
                        if self.buttons['back'].draw(self.screen): # back
                            self.sound['ting'].play()
                            menu_state = 'options'

                    elif menu_state == 'finish':
                        bg_img = pygame.image.load('Do_an/Assets/Background/tom_catch_jerry.png').convert_alpha()
                        self.screen.blit(bg_img, (0, 0))
                        self.draw_text(self.record_text(self.record), 'black', 400, 100)
                        if self.buttons['play_again'].draw(self.screen): # play_again
                            self.sound['ting'].play()
                            running = False
                            self.transitions
                            self.record = 0
                            self.maze = None
                            self.start, self.end = None, None
                            self.new_game()
                            self.run()
                        if self.buttons['save_2'].draw(self.screen): # save
                            self.sound['ting'].play()
                            menu_state = 'save2'

                    elif menu_state == 'save1':
                        self.buttons['gameFrame'].draw(self.screen)
                        self.draw_text('Enter name of file:', 'black', 430, 250)
                        self.draw_text('{}'.format(self.file_name), 'black', 460, 280)
                        user_input = True
                        if self.buttons['accept_1'].draw(self.screen):
                            self.sound['ting'].play()
                            user_input = False                            
                            menu_state = 'menu'
                            self.save()
                        if self.buttons['cancel_1'].draw(self.screen):
                            self.sound['ting'].play()
                            user_input = False
                            menu_state = 'menu'

                    elif menu_state == 'save2':
                        user_input = True
                        bg_img = pygame.image.load('Do_an/Assets/Background/tom_catch_jerry.png').convert_alpha()
                        self.screen.blit(bg_img, (0, 0))
                        self.draw_text(self.record_text(self.record), 'black', 400, 100)
                        self.buttons['play_again'].draw(self.screen)
                        self.buttons['save_2'].draw(self.screen)
                        self.draw_text('Enter name of file: {}'.format(self.file_name), 'black', 400, 250)
                        if self.buttons['accept_2'].draw(self.screen):
                            self.sound['ting'].play()
                            user_input = False
                            menu_state = 'finish'
                            self.set_maze_visit()
                            self.save()
                        if self.buttons['cancel_2'].draw(self.screen):
                            self.sound['ting'].play()
                            user_input = False
                            self.file_name = ''
                            menu_state = 'finish'

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if menu_state == 'menu':
                                if not pause: 
                                    pause = True
                                    music.pause()
                                else: 
                                    pause = False 
                                    if user_turnoff: music.unpause()
                            
                        elif event.key == pygame.K_BACKSPACE:
                            if user_input:                                       
                                self.file_name = self.file_name[:-1]
                        else:
                            if user_input:
                                if len(self.file_name) < 8:
                                    self.file_name += event.unicode
                    if event.type == pygame.QUIT:
                        self.sound['ting'].play()
                        mess = Tk()
                        mess.geometry('0x0')
                        mess.eval('tk::PlaceWindow %s center' %mess.winfo_toplevel())
                        mess.withdraw()
                        if messagebox.askyesno('Question', 'Do you really want to quit game?'): 
                            pygame.quit()
                            quit()
                        mess.quit()                  
                         
                if not pause:
                    # process move (press w,a,s,d or up,down,right,left)
                    self.player.draw(self.screen)
                    if self.player_name == 'Square':
                        self.handle_move()
                    else:
                        time_move.update()
                        if not time_move.active:
                            self.handle_move_pro()                                    
                            time_move.activate()
                    if (self.player.row, self.player.col) == end:
                        self.completed = True
                        self.record = _time
                        pause = True
                        menu_state = 'finish'
                    # process timer
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
                    if not self.choose:
                        games = self.ranking(self.take_score())
                        self.draw_rank(games)

                    # process hint(press H)
                    self.handle_hint()
                    if self.player_name == 'Square':    
                        time.sleep(0.0012*self.delay)
                                    
                music.set_volume(music_vol*0.01) 
                self.sound['ting'].set_volume(sound_effect_vol*0.01)
                if self.level == 'hard':
                    time_move.set_duration(self.delay)
                else:
                    time_move.set_duration(self.delay*0.9 + 20)
                self.update()
    
    def test(self):
        self.new_game()
        run = True
        self.set_player('MaskDude')
        menu_state = 'menu'
        pause = False
        time_move = Timer(75)
        time_move.activate()
        while run:
            self.draw()
            if not pause:
                self.player.loop()    
                self.player.draw(self.screen)
                time_move.update()
                if not time_move.active:
                    self.handle_move_pro()                                    
                    time_move.activate()
            elif pause:
                if menu_state == 'menu':
                    self.buttons['delay'].draw(self.screen)
                    self.delay = self.set_delay()  

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                if menu_state == 'menu':
                                    if not pause: pause = True
                                    else: pause = False 
            time_move.set_duration(20 + self.delay*0.9)
            self.update()
        pygame.quit()
        
if __name__ == '__main__':
    game = Game('easy', 'not_auto', True, 'Tom')
    game.run()
    # game = Game()
    # if game.load('quan3'):
    #     game.run()
    # game = Game('easy', 'not_auto')
    # game.test()
    
    

