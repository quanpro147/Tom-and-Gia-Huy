import pygame 
import os 
import random
import pygame
from os import listdir 
from os.path import isfile, join
from PyQt5 import QtWidgets
from UI.mainUI import GiaoDien
from maze import *
menu_check = [False]
mode = [True] 
Path1 = join("Do_an","button")
button = [['LoadButton.png',(650,200,150,45)],['MenuButton.png',(650,100,150,45)],['QuitButton.png',(650,400,150,45)],['Resume.png',(650,300,150,45)]]
makebutton = [[pygame.image.load(join(Path1,a[0])),a[1]] for a in button]

pygame.init()
pygame.display.set_caption("Tam an Gia Huy")
mazes = maze(20, 20)
mazes.generate_maze()
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT, = 1400, 800
FPS = 60
PLAYER_VEL = 10
window = pygame.display.set_mode((WIDTH, HEIGHT))


def get_index(mazes):
    index = []
    for i in range(mazes.num_rows):
        for j in range(mazes.num_cols):
            if i == 0 and mazes.grid[i][j].walls["top"] == False:
                index.append([i, j])
            if j == 0 and mazes.grid[i][j].walls["left"] == False:
                index.append([i, j])

            if j == mazes.num_rows - 1 and mazes.grid[i][j].walls["right"] == False:
                index.append([i, j])
            if i == mazes.num_rows - 1 and mazes.grid[i][j].walls["bot"] == False:
                index.append([i, j])
    return index
LOCAL = get_index(mazes)
# lat anh
def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
# load tất cả khung ảnh để tạo chuyển động
def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("Do_an","assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]
    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
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

# lấy 1 khối chan ten
def get_block(size1, size2, dx, dy):
    path = join("Do_an","assets", "Terrain", "landscape.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size1, size2), pygame.SRCALPHA, 32)
    rect = pygame.Rect(dx ,dy, size1, size2)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

# lấy 1 khối
def get_background_block(name, size1, size2):
    path = join("Do_an","assets", "Terrain", name)
    image = pygame.image.load(path)
    subsurface = image.subsurface((0, 0, size1, size2))
    image = subsurface
    titles = []
    for i in range(WIDTH // size1 + 1):
        for j in range(HEIGHT // size2 + 1):
            token = [i * size1, j * size2]
            titles.append(token)
    return titles, image

def draw_background(name, dx, dy, size1, size2):
    image = pygame.image.load(join("Do_an","assets", "Terrain", name))
    subsurface = image.subsurface((dx, dy, size1, size2))
    image = subsurface
    titles = []
    for i in range(mazes.num_rows * 64 // size1):
        for j in range(mazes.num_cols * 64 // size2):
            token = [-LOCAL[0][1] * 64 + i * size1 + 8 + WIDTH // 2, -LOCAL[0][0]*64 + j * size2 + 8 + HEIGHT // 2]
            titles.append(token)
    return titles, image
    

# class player
class Player(pygame.sprite.Sprite):
    COLOR = (255, 255, 0)
    SPRITES = load_sprite_sheets("MainCharacters", "Square", 24, 24, True)
    ANIMATION_DELAY = 7
    def __init__(self, x, y , width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0 #van toc
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
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
    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)
        self.update_sprite()
        self.update()

    def update_sprite(self):
        sprite_sheet = "idle"
        
        if self.x_vel != 0 :
            sprite_sheet = "run"
        if self.y_vel > 0 :
            sprite_sheet = "run"
        if self.y_vel < 0 :
            sprite_sheet = "run"
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()
    ######
    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        

    def draw(self, win, offset_x, offset_y):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y - offset_y))
    

# class vat thể
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, dx, dy, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
        self.dx = dx
        self.dy = dy
    def draw(self, win, offset_x, offset_y):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
# class cho 1 khối
class Block(Object):
    def __init__(self, x, y, size1, size2, dx, dy):
        super().__init__(x, y, size1, size2, dx, dy)
        block = get_block(size1, size2, dx, dy)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Jerry(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height, dx, dy):
        super().__init__(x, y, width, height, dx, dy)
        self.jerry = load_sprite_sheets("MainCharacters", "Jerry", width, height)
        self.image = self.jerry["idlle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "idlle"
        self.name = "Jerry"

    def loop(self):
        sprites = self.jerry[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


def draw(window,background, bg_image, background2, bg_image2, player, Object, offset_x, offset_y,button,menubutton,mode): #bg_image2, background2)
    if mode[0]:
        for title in background:
            window.blit(bg_image, tuple(title)) 
        for title in background2:
            window.blit(bg_image2, tuple([title[0] - offset_x, title[1] - offset_y]))
        for obj in Object:
            obj.draw(window, offset_x, offset_y)
        
        player.draw(window, offset_x, offset_y)
        window.blit(menubutton,(1300,20,20,21))
        pygame.display.update()
    else:
        window.fill('white')
        for title in background:
            window.blit(bg_image, tuple(title)) 
        for i in button:
            window.blit(i[0],i[1])
        window.blit(menubutton,(1300,20,20,21))
        pygame.display.update()

# va chạm player với vật thể
def collide(player : Player, objects, dx, dy):
    player.move(dx, dy)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break
    player.move(-dx, -dy)
    player.update()
    return collided_object
def handle_move(player, objects):

    keys = pygame.key.get_pressed()
    player.x_vel = 0
    player.y_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL  , 0)
    collide_right = collide(player, objects, PLAYER_VEL  , 0)
    collide_up = collide(player, objects, 0, -PLAYER_VEL  )
    collide_down = collide(player, objects, 0, PLAYER_VEL)
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not collide_left :
        player.move_left(PLAYER_VEL)
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not collide_right:
        player.move_right(PLAYER_VEL) 
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not collide_down:
        player.move_down(PLAYER_VEL)
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not collide_up :
        player.move_up(PLAYER_VEL)
    to_check = [collide_down, collide_up, collide_right, collide_left]
    for obj in to_check:
        if obj and obj.name == "Jerry":
            pygame.quit()
            quit()

def get_maze_titles(mazes):
    block = []
    if mazes.num_rows >= 0:
        for i in range(mazes.num_rows):
            for j in range(mazes.num_cols):
                x = j * 64
                y = i * 64
                if mazes.grid[i][j].walls['top']:
                    block.append(Block(-LOCAL[0][1] * 64 +  x + WIDTH //2 , -LOCAL[0][0] * 64 + y + HEIGHT // 2, 80 , 32, 212, 112))
                if mazes.grid[i][j].walls['left']:
                    block.append(Block( -LOCAL[0][1] * 64 + x +  WIDTH //2,-LOCAL[0][0] * 64  + y + HEIGHT // 2, 16, 96, 212, 112))
                if mazes.grid[i][j].walls['bot']:
                    block.append(Block(-LOCAL[0][1] * 64 + x +  WIDTH //2,- LOCAL[0][0] * 64 + y + 64 + HEIGHT // 2,  80 ,32, 212, 112))
                if mazes.grid[i][j].walls['right']:
                    block.append(Block(-LOCAL[0][1]* 64 + x + 64 +  WIDTH //2, -LOCAL[0][0] * 64 + y + HEIGHT // 2, 16, 96, 212, 112))
    return block

def main(window):
    
    background, bg_image = get_background_block("Overworld.png", 16, 16)
    Menubutton = pygame.image.load(join("Do_an","Assets","Menu","Buttons","Settings.png"))
    background2, bg_image2 = draw_background("atlat.png", 0, 464, 16, 16)
    player = Player(WIDTH // 2 + 32, HEIGHT // 2 + 32, 5, 5)
    jerry = Jerry(-LOCAL[0][1] * 64 + WIDTH // 2 + (LOCAL[1][1]) * 64 + 32  ,-LOCAL[0][0] * 64 + HEIGHT // 2 + (LOCAL[1][0]) * 64 + 16 ,34,58, 0,0 )
    
    block = get_maze_titles(mazes)
    
    block.append(jerry)
    run = True
    offset_x = 0
    offset_y = 0
    scroll_area_width = 700
    scroll_area_height = 400
    while run:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
                break
            if even.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if even.button == 1 and pos[0] >= 1300 and pos[0] <= 1320 and pos[1]>=20 and pos[1] <= 41:
                    mode[0]= not mode[0]
                if even.button == 1 and pos[0] >= 650 and pos[0] <= 800 and pos[1]>=400 and pos[1] <= 445 and mode[0] == False:
                    run = False
                    break
                if even.button == 1 and pos[0] >= 650 and pos[0] <= 800 and pos[1]>=300 and pos[1] <=345 and mode[0] == False:
                    mode[0] = not mode[0]
                if even.button == 1 and pos[0] >= 650 and pos[0] <= 800 and pos[1]>=100 and pos[1] <=145 and mode[0] == False:
                    run = False
                    menu_check[0] = not menu_check[0]
                    break

    
        player.loop(FPS)
        jerry.loop()
        handle_move(player, block)
        
        draw(window,background, bg_image, background2,bg_image2 , player, block, offset_x, offset_y,makebutton,Menubutton,mode) 
        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel
        if ((player.rect.top - offset_y >= HEIGHT - scroll_area_height) and player.y_vel > 0) or (
                (player.rect.bottom - offset_y <= scroll_area_height) and player.y_vel < 0):
            offset_y += player.y_vel
        
    pygame.quit()
    #app = QtWidgets.QApplication(sys.argv)
    #sys.exit(app.exec_())
    return menu_check[0]


if __name__ == "__main__":

    main(window)


