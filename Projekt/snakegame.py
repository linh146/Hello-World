import os
import pygame
pygame.init()

WIN_SIZE = 800  # Fenstergröße: Breite und Höhe in Pixel
SQUARE_COUNT = 20  # Anzahl der Rasterfelder im Spiel
SQUARE_SIZE = WIN_SIZE / SQUARE_COUNT  # Größe eines einzelnen Feldes im Raster
DELAY = 100

screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))  # Fenster erstellen
pygame.display.set_caption("Snake Game")  # Fenstertitel setzen

# Hintergrundbild laden und auf Fenstergröße anpassen -> Kommentare zum verstehen noch einfügen!!
script_dir = os.path.dirname(os.path.abspath(__file__))
background_path = os.path.join(script_dir, 'background.png')
if not os.path.exists(background_path):
    raise FileNotFoundError(f"Hintergrundbild nicht gefunden: {background_path}")
background_image = pygame.image.load(background_path)
background_image = pygame.transform.scale(background_image, (WIN_SIZE, WIN_SIZE))  # Bild auf Fenstergröße skalieren

head_column = SQUARE_COUNT // 2  # Kopfposition in der Spalte (Rasterx) 
head_row = SQUARE_COUNT // 2  # Kopfposition in der Zeile (Rastery) -> Position mittig eingestellt

#Schlange bewegt sich permanent in jeweilig gedrückte Taste
step_x = 0 
step_y = 0

run = True
while run:
    pygame.time.delay(100)  # Kurze Pause, damit das Spiel nicht zu schnell läuft

    for event in pygame.event.get():  # Alle Pygame-Ereignisse abfragen
        if event.type == pygame.QUIT:  # Wenn auf das Schließen-Symbol geklickt wurde
            run = False  # Beende die Spielschleife

   

    # Benutzersteuerung per Pfeiltasten
    keys = pygame.key.get_pressed()  # Alle gedrückten Tasten prüfen
    if keys[pygame.K_RIGHT]:
        # Verhindern , dass die Schlange in eigenen Körper bewegt
        #Nur wenn Schlange nach links -> Bewegungsrichtung rechts möglich
        if step_x != -1:  
            step_x = 1
            step_y = 0
    elif keys[pygame.K_LEFT]:        # Nur 1 Bedingung erfüllbar durch elif
        if step_x != 1:
            step_x = -1
            step_y = 0
    elif keys[pygame.K_UP]:
        if step_y !=1:
            step_x = 0
            step_y = -1
    elif keys[pygame.K_DOWN]:
        if step_y != -1:
            step_x = 0
            step_y = 1

    body_parts.append((head_column, head_row))
    
    head_column += step_x # Kopfposition in der Spalte aktualisieren
    head_row += step_y


    # Hintergrundbild zeichnen
    screen.blit(background_image, (0, 0))  # Das geladene Bild in die obere linke Ecke malen


    # Kopfposition im Raster berechnen und grünes Quadrat zeichnen
    head_x = head_column * SQUARE_SIZE
    head_y = head_row * SQUARE_SIZE
    pygame.draw.rect(screen, (24,116,205), (head_x, head_y, SQUARE_SIZE, SQUARE_SIZE))  # Kopf als grünes Quadrat

    for part in body_parts:
        part_column = part[0]
        part_row = part [1]
        part_x = part_column * SQUARE_SIZE
        part_y = part_row * SQUARE_SIZE
        pygame.draw.rect(screen, (24,116,205), head_x, head_y, SQUARE_SIZE, SQUARE_SIZE))

    # Rasterlinien zeichnen
    for i in range(SQUARE_COUNT):  # Schleife über alle Rasterlinien
        line_pos = SQUARE_SIZE * i
        pygame.draw.line(screen, (255, 255, 255), (line_pos, 0), (line_pos, WIN_SIZE), 2)  # vertikale Linie
        pygame.draw.line(screen, (255, 255, 255), (0, line_pos), (WIN_SIZE, line_pos), 2)  # horizontale Linie



    
    pygame.display.update()  # Anzeige aktualisieren

pygame.display.quit()  # Fenster schließen






























































































































































































































