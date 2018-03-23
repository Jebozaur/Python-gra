import random
import pygame
import funkcje
import klasy

black,white,red,astr_c,green,hud = funkcje.kolory()

block_list = pygame.sprite.Group()
all_spr = pygame.sprite.Group()
pociski = pygame.sprite.Group()
collision = pygame.sprite.Group()
player_group = pygame.sprite.Group()




def main():
    hud_height = 30
    zycia = 3
    pygame.init()

    click_sound = pygame.mixer.Sound("sounds\strzal.ogg")
    explode = pygame.mixer.Sound("sounds\wybuch.ogg")
    death_sound = pygame.mixer.Sound("sounds\death.ogg")
    explode.set_volume(0.1)
    click_sound.set_volume(0.2)
    death_sound.set_volume(0.5)

    pygame.mouse.set_visible(False)

    #okno
    screen_width, screen_height = funkcje.screen()
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Gra")
    #koniec okna
    serce = pygame.image.load("serce.png").convert()
    serce2 = pygame.image.load("serce.png").convert()
    serce3 = pygame.image.load("serce.png").convert()
    sercex = serce.get_width()
    sercey = serce.get_height()


   #ASTEROIDY
    asteroid_array = []
    '''
    for i in range(1):
        asteroida = klasy.Asteroid()
        block_list.add(asteroida)
        all_spr.add(asteroida)
        asteroid_array.append(asteroida)
    '''
    '''for i in range(1):
        asteroid_array[i].rect.x = random.randrange(screen_width, screen_width + 500)
        asteroid_array[i].rect.y = random.randrange(0, screen_height)
'''

    asteroida = klasy.Asteroid(5)
    block_list.add(asteroida)
    all_spr.add(asteroida)

    #KONIEC

#stworzenie gracza
    player = klasy.Player()
    player_group.add(player)

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
#-------main loop-------#n
    while done:
        clock.tick(60)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
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

        keys = pygame.key.get_pressed()  # checking pressed keys
        velocity = 10
        if keys[pygame.K_UP]:
            player.rect.y -= velocity
        if keys[pygame.K_DOWN]:
            player.rect.y += velocity
        if keys[pygame.K_LEFT]:
            player.rect.x -= velocity
        if keys[pygame.K_RIGHT]:
            player.rect.x += velocity


        screen.fill(black)

        for i in range(len(star)):
            pygame.draw.circle(screen, white, star[i], 2)
            star[i][0] -= 1
            if star[i][0] < 0:
                star[i][0] = random.randrange(screen_width + 10, screen_width + 20)

        all_spr.update()
        asteroida.animateup()
        block_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        #if asteroid.rect.x < 0:
        #asteroid.rect.x = random.randrange[screen_width + 10, screen_width + 820]
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

            if pocisk.rect.x > screen_width+5:
                pociski.remove(pocisk)
                all_spr.remove(pocisk)
        #koniec hitboxow pociskow

        #kolizja statku z granicami

        if player.rect.x == 0:
            player.rect.x += velocity * 2
        if player.rect.x == screen_width - 25:
            player.rect.x -= velocity * 2
        if player.rect.y <= hud_height:
            player.rect.y += velocity * 2
        if player.rect.y >= screen_height - 39:
            player.rect.y -= velocity * 2

        #koniec granic

        all_spr.draw(screen)
        player_group.draw(screen)

        #hud

        pygame.draw.rect(screen, hud, [0, 0, screen_width, hud_height])

        for i in range(zycia):
            screen.blit(serce, [5, 5])
            screen.blit(serce2, [5 + (sercex * (zycia - 2)), 5])
            screen.blit(serce3, [5 + (sercex * (zycia - 1)), 5])

        if score > 0:
            punkty = pygame.font.SysFont("Fixedsys", 23)
            a_punkty = punkty.render("PUNKTY:", 1, black)

            licznik = punkty.render(str(score), 1, black)

            screen.blit(a_punkty, [540, 17])
            screen.blit(licznik, [650, 17])

        if zycia == 0:
            death_sound.play()

        if zycia <= 0:
            over = pygame.font.SysFont("Fixedsys", 100)
            game_over = over.render("Przegrałeś", 1 , white)
            screen.fill(black)
            screen.blit(game_over, [screen_width / 2.5, screen_height / 2.5])

        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()
