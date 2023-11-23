import pygame, sys
from settings import *
from level import Level


pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))

level = Level(level_map, screen)

layer_1 = pygame.image.load('./layers/1.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(layer_1, (0, 0))
    # screen.fill('blue')

    level.run()

    pygame.display.update()
    clock = pygame.time.Clock().tick(60)
