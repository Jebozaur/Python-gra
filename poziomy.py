import pygame
import klasy
import funkcje

black,white,red,astr_c,green,hud = funkcje.kolory()

block_list = pygame.sprite.Group()
all_spr = pygame.sprite.Group()
pociski = pygame.sprite.Group()

screen_width, screen_height = funkcje.screen()


def poziom1():
    asteroid = klasy.Asteroid()
    asteroid.rect.x = screen_width +20
    asteroid.rect.y = 20
    block_list.add(asteroid)
    all_spr.add(asteroid)

    asteroidy = []
    for i in range(50):
        asteroida = klasy.Asteroid()
        asteroida.rect.x = asteroid.rect.x + 50
        asteroida.rect.y = 20
        block_list.add(asteroida)
        all_spr.add(asteroida)
        asteroidy.append(asteroida)
        asteroid.rect.x += 40

    asteroidy[5].rect.y = 100

