import random
import pygame
#import funkcje
import klasy

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
astr_c = (127, 235, 137)
green = (0, 255, 0)
hud = (63, 52, 130)

block_list = pygame.sprite.Group()
all_spr = pygame.sprite.Group()
pociski = pygame.sprite.Group()


def main():

    zycia = 3
    pygame.init()



    click_sound = pygame.mixer.Sound("strzal.ogg")
    explode = pygame.mixer.Sound("wybuch.ogg")
    explode.set_volume(0.1)
    click_sound.set_volume(0.2)
    pygame.mouse.set_visible(False)

    #okno
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Gra")
    #koniec okna
    serce = pygame.image.load("serce.png").convert()
    serce2 = pygame.image.load("serce.png").convert()
    serce3 = pygame.image.load("serce.png").convert()
    sercex = serce.get_width()
    sercey = serce.get_height()


   #ASTEROIDY

    asteroid = klasy.Asteroid()
    asteroid.rect.x = 300
    asteroid.rect.y = screen_height/2
    block_list.add(asteroid)
    all_spr.add(asteroid)




    asteroidy = []
    for i in range(10):
        asteroida = klasy.Asteroid()
        asteroida.rect.x = asteroid.rect.x + 50
        asteroida.rect.y =  300
        block_list.add(asteroida)
        all_spr.add(asteroida)
        asteroidy.append(asteroida)
        asteroid.rect.x += 40

    asteroidy[5].rect.y=100

    #KONIEC

#stworzenie gracza
    player = klasy.Player()
    all_spr.add(player)

#gwazdy
    star = [] #pojemnik

#generacje koordynatow i wpisanie ich do pojemnika
    for i in range(100):
        x_s = random.randrange(screen_width)
        y_s = random.randrange(screen_height)
        star.append([x_s, y_s])
#koniec gwiazd


    clock = pygame.time.Clock()

    done = True
    score = 0
#-------main loop-------#
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            elif event.type == pygame.MOUSEBUTTONDOWN:

                pocisk = klasy.Pocisk()
                pocisk2 = klasy.Pocisk()

                pocisk.rect.x = player.rect.x
                pocisk.rect.y = player.rect.y + 3

                pocisk2.rect.x = player.rect.x
                pocisk2.rect.y = player.rect.y + 36

                all_spr.add(pocisk)
                pociski.add(pocisk)
                all_spr.add(pocisk2)
                pociski.add(pocisk2)

                click_sound.play()


        screen.fill(black)

        for i in range(len(star)):
            pygame.draw.circle(screen, white, star[i], 2)
            star[i][0] -= 1
            if star[i][0] < 0:
                star[i][0] = random.randrange(screen_width + 10, screen_width + 20)

        all_spr.update()

        block_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        if asteroid.rect.x < 0:
            asteroid.rect.x = random.randrange[screen_width + 10, screen_width + 820]
        for asteroid in block_hit_list:
            score += 1
            zycia -= 1
            print(score)
            explode.play()
        #hitboxy pociskow
        for pocisk in pociski:

            block_hit_list = pygame.sprite.spritecollide(pocisk, block_list, True)

            for asteroid in block_hit_list:
                pociski.remove(pocisk)
                all_spr.remove(pocisk)
                explode.play()
                score += 1
                print(score)

            if pocisk.rect.x > 805:
                pociski.remove(pocisk)
                all_spr.remove(pocisk)
        #koniec hitboxow pociskow

        all_spr.draw(screen)

        #hud
        hud_height = 58
        pygame.draw.rect(screen, hud, [0, 0, screen_width, hud_height])

        for i in range(zycia):
            screen.blit(serce, [5, 5])
            screen.blit(serce2, [5 + (sercex * (zycia - 2)), 5])
            screen.blit(serce3, [5 + (sercex * (zycia - 1)), 5])

        if score > 0:
            punkty = pygame.font.SysFont("Fixedsys", 34)
            a_punkty = punkty.render("PUNKTY:", 1, black)

            licznik = punkty.render(str(score), 1, black)

            screen.blit(a_punkty, [540, 17])
            screen.blit(licznik, [650, 17])

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()

