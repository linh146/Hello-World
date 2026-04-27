import pygame
pygame.init()

WIN_SIZE = 800 
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE)) #erstellt ein Fenster mit den angegebenen Maßen
pygame.display.set_caption("Snake Game") #setzt den Titel des Fensters

run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():    #kommuniziert mit betriebssystem für verhalten von fenster (gibt Liste mit infos was passiert)
        if event.type == pygame.QUIT: # erkennt wenn das Event= Schließen des Fensters
            run = False #bricht die schleife ab
pygame.display.quit() #schließt das fenster 