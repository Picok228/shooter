from random import randint

import pygame
from raketa import Player
from ufo import UFO
def start_game():
    window = pygame.display.set_mode((700, 500))
    fps = pygame.time.Clock()

    patron = Player(270, 390, 20, 20, "optimys_prime/bullet.png", 4)
    roket = Player(270, 390, 100, 100, "optimys_prime/rocket.png", 4)

    ufo1 = []
    for i in range(2):
        ufo1.append(UFO(randint(0, 700), randint(-400, 0), 90, 60, "optimys_prime/ufo.png", 3))
        ufo1.append(UFO(randint(0, 700), randint(-200, 0), 90, 60, "optimys_prime/ufo.png", 3))
        ufo1.append(UFO(randint(0, 700), randint(-300, 0), 90, 60, "optimys_prime/ufo.png", 3))
        ufo1.append(UFO(randint(0, 700), randint(-400, 0), 90, 60, "optimys_prime/ufo.png", 3))
        ufo1.append(UFO(randint(0, 700), randint(-300, 0), 90, 60, "optimys_prime/ufo.png", 3))
        ufo1.append(UFO(randint(0, 700), randint(-200, 0), 90, 60, "optimys_prime/ufo.png", 3))

    bacground = pygame.transform.scale(
        pygame.image.load("optimys_prime/galaxy.jpg"), (720, 540)
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

        window.blit(bacground, (5, 5))
        for nlo in ufo1:
            nlo.draw(window)
            nlo.move()

        patron.move()
        roket.draw(window)
        patron.draw(window)
        roket.move()
        pygame.display.flip()
        fps.tick(60)

