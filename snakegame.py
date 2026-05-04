import pygame
pygame.init()

WIN_SIZE = 800 
SQUARE_COUNT = 20 # Anzahl 20 Squares für Raster implementieren (3)
SQUARE_SIZE = WIN_SIZE / SQUARE_COUNT # Square einzeln definiert durch Gesamtgröße : Anzahl der Squares (3)

screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE)) #erstellt ein Fenster mit den angegebenen Maßen
pygame.display.set_caption("Snake Game") #setzt den Titel des Fensters

head_column = 0 #Position Kopf ( Reihe 0) (3)
head_row = 0

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


    # Video 3 der Playlist

    #Raster Programmieren (3)
    screen.fill((0, 0, 0))  # schwarzer Hintergrund (3)

    head_x = head_column * SQUARE_SIZE 
    head_y=head_row* SQUARE_SIZE
    pygame.draw.rect(screen, (0, 255, 0), (head_x , head_y, SQUARE_SIZE, SQUARE_SIZE )) #zeichnet ein Rechteck auf den Bildschirm (Farbe, Position und Größe) + angepasst an das Raster

    for i in range(SQUARE_COUNT) : # Linien als Raster (3)
        line_pos = SQUARE_SIZE * i
        pygame.draw.line(screen, (255, 255, 255), (line_pos, 0), (line_pos, WIN_SIZE), 2 ) # Linienfarbe weiß + Startposition / Endposition +  Liniendicke ( Senkrecht) (3) 
        pygame.draw.line(screen, (255, 255, 255), (0 , line_pos), (WIN_SIZE , line_pos), 2 ) # Horizontal



    
    pygame.display.update() #aktualisiert den Inhalt des Fensters

pygame.display.quit() #schließt das fenster 































































































































































































































