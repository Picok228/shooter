import pygame
from raketa import Player

window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()




roket = Player(1,1,60,50, "optimys_prime/rocket.png",4 )

bacground = pygame.transform.scale(
    pygame.image.load("optimys_prime/galaxy.jpg"),(700,500)
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
    roket.draw(window)
    window.blit(bacground,(5,5))
    pygame.display.flip()

    fps.tick(60)
