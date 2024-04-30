import pygame 
import os 
import random
from os import listdir 
from os.path import isfile, join
pygame.init()
pygame.display.set_caption("Tam an Gia Huy")

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT, = 1200, 700
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def flip(sprites):
    return [pygame.transform.flip(sprite,True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
            all_sprites[image.replace(".png", "") + "_up"] = sprites
            all_sprites[image.replace(".png", "") + "_down"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def get_block(size1, size2):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size1, size2), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 0, size1, size2)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


class Player(pygame.sprite.Sprite):
    COLOR = (255, 255, 0)
    SPRITES = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
    ANIMATION_DELAY = 1
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
        
        if self.x_vel != 0 or self.y_vel != 0 or (self.x_vel != 0 and self.y_vel != 0):
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

    def draw(self, win):
        
        win.blit(self.sprite, (self.rect.x, self.rect.y))


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Block(Object):
    def __init__(self, x, y, size1, size2):
        super().__init__(x, y, size1, size2)
        block = get_block(size1, size2)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    titles = []
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            token = [i * width, j * height]
            titles.append(token)
    return titles, image

def draw(window, background, bg_image, player, Object):
    for title in background:
        window.blit(bg_image, tuple(title)) 
    for obj in Object:
        obj.draw(window)

    player.draw(window)
    pygame.display.update()


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
def handle_move(player, objects: Block):

    keys = pygame.key.get_pressed()
    player.x_vel = 0
    player.y_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2 , 0)
    collide_right = collide(player, objects, PLAYER_VEL * 2, 0)
    collide_up = collide(player, objects, 0, -PLAYER_VEL * 2 )
    collide_down = collide(player, objects, 0, PLAYER_VEL * 2 )
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not collide_left:
        player.move_left(PLAYER_VEL)
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not collide_right:
        player.move_right(PLAYER_VEL)
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not collide_down:
        player.move_down(PLAYER_VEL)
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not collide_up :
        player.move_up(PLAYER_VEL)



def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Yellow.png")
    player = Player(200, 100, 20, 20)
    block = [Block(200, 300, 96, 8)]
    run = True
    while run:
        clock.tick(FPS)
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
                break
        player.loop(FPS)
        handle_move(player, block)
        draw(window, background, bg_image, player, block)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)