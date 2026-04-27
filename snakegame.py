import pygame
pygame.init()

WIN_SIZE = 600 
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))

run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
pygame.display.quit()