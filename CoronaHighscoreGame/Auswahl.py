import pygame
import os
import sys



## COLORS ##

#            R    G    B
LIGHTGRAY = (229, 229, 229)
GRAY      = (100, 100, 100)
NAVYBLUE  = ( 60,  60, 100)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
LIGHTRED  = (255,   77,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
YELLOW    = (255, 255,   0)
ORANGE    = (255, 128,   0)
PURPLE    = (255,   0, 255)
CYAN      = (  0, 255, 255)
BLACK     = (  0,   0,   0)
NEARBLACK = ( 19,  15,  48)
LIGHTBLUE   = (33, 202, 255)

pygame.init()

screen = pygame.display.set_mode((960,720))
#screen = pygame.display.set_mode((960,720), pygame.NOFRAME)
gameIcon = pygame.image.load('/Corona/images/bullets/CV30x30.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption('Corona - Auswahl')
menu = True

#bg = pygame.image.load('images/backgrounds/steuerung.png')

christian = pygame.image.load('/Corona/images/enemies/christian.png')
christian.set_alpha(220)

niklas = pygame.image.load('/Corona/images/enemies/niklas.png')
niklas.set_alpha(220)

chars = pygame.image.load('/Corona/images/enemies/auswahl.png')
chars.set_alpha(30)


def startGame_cm():
    import Steuerung_cm.py

def startGame():
    import Steuerung.py

while menu:
    font1 = pygame.font.SysFont('Comic Sans MS', 63, True)
    text1 = font1.render('Wähle deinen Corona Helden!', 1, WHITE)


    
    screen.fill (BLACK,(0, 0, screen.get_width(), screen.get_height()))
    

    
    screen.blit(christian, (615,160))
    screen.blit(niklas, (150,160))
    screen.blit(chars, (1, 400))
    screen.blit(text1, (33, 20))

    pygame.display.flip()
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 140:
                if pygame.mouse.get_pos()[0] <= 330 and pygame.mouse.get_pos()[1] <= 360:
                    startGame()

            if pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[1] >= 140:
                if pygame.mouse.get_pos()[0] <= 750 and pygame.mouse.get_pos()[1] <= 360:
                    startGame_cm()