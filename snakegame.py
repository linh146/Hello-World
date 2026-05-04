import pygame
pygame.init()

WIN_SIZE = 800 
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE)) #erstellt ein Fenster mit den angegebenen Maßen
pygame.display.set_caption("Snake Game") #setzt den Titel des Fensters

x = 50
y= 70

run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():    #kommuniziert mit betriebssystem für verhalten von fenster (gibt Liste mit infos was passiert)
        if event.type == pygame.QUIT: # erkennt wenn das Event= Schließen des Fensters
            run = False #bricht die schleife ab
    
    x += 1 #ändert die x-Position des Rechtecks um 5 Pixel pro Schleifendurchlauf, Bewegung
    y += 2 #ändert die y-Position des Rechtecks um 5 Pixel pro Schleifendurchlauf, Bewegung

    keys = pygame.key.get_pressed() #gibt eine Liste zurück, die den Status aller Tasten auf der Tastatur enthält (True oder False)

    if keys[pygame.K_LEFT]:
        x -= 2
    if keys[pygame.K_RIGHT]:
        x += 2
    if keys[pygame.K_UP]:
        y -= 2
    if keys[pygame.K_DOWN]:
        y += 2

    screen.fill((120,0,0)) #füllt den Bildschirm mit der Farbe schwarz (RGB Werte)
    pygame.draw.rect(screen, (0,255,0), (x,y,50,50)) #zeichnet ein Rechteck auf den Bildschirm (Farbe, Position und Größe)
    pygame.display.update() #aktualisiert den Inhalt des Fensters

pygame.display.quit() #schließt das fenster 































































































































































































































