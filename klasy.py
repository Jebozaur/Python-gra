import random
import pygame
import funkcje

black, white, red, astr_c, green, hud = funkcje.kolory()

block_list = pygame.sprite.Group()
all_spr = pygame.sprite.Group()
pociski = pygame.sprite.Group()
collision = pygame.sprite.Group()
screen_width, screen_height = funkcje.screen()



class Asteroid(pygame.sprite.Sprite):

    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("asteroida.png")
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

        self.rect.x = 1000
        self.rect.y = random.randrange(0, screen_height)
        self.speed = speed

    def update(self):
        self.rect.x -= 6
        if self.rect.x < -10:
            self.rect.x = random.randrange(screen_width, screen_width + 500)
    def animatedown(self):
       self.rect.y += self.speed
       if self.rect.y >= screen_height:
           self.rect.y = -20
    def animateup(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.rect.y = screen_height + 20
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("gracz.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 2


class Pocisk(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([10, 1])
        self.image.fill(green)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 6

class Border(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([screen_width, 2])
        self.rect = self.image.get_rect()
        collision.add(self)
        self.rect.x = 0
        self.rect.y = 0


def coord(a,x,y):
    a.rect.x = x
    a.rect.y = y
    block_list.add(a)
    all_spr.add(a)
