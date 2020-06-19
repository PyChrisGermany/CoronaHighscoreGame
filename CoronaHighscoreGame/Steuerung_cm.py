import pygame
import os
import sys
#import importlib
#from importlib import reload
#importlib.reload(sys.modules['Steuerung'])


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
pygame.display.set_caption('Corona - Steuerung')
menu = True

bg = pygame.image.load('/Corona/images/backgrounds/steuerung.png')

#del sys.modules['Steuerung']

def startGame_cm_leicht():
    if 'Enemy_1_Jens_cm_leicht' in sys.modules:  
        del sys.modules['Enemy_1_Jens_cm_leicht']

        import Enemy_1_Jens_cm_leicht.py
    else:
        import Enemy_1_Jens_cm_leicht.py

def startGame_cm():
    if 'Enemy_1_Jens_cm' in sys.modules:  
        del sys.modules['Enemy_1_Jens_cm']

        import Enemy_1_Jens_cm.py
    else:
        import Enemy_1_Jens_cm.py



while menu:
    font1 = pygame.font.SysFont('Comic Sans MS', 28, True)
    text1 = font1.render('SCHWER', 1, WHITE)
    font2 = pygame.font.SysFont('Comic Sans MS', 28, True)
    text2 = font2.render('LEICHT', 1, WHITE)
    #font3 = pygame.font.SysFont('Comic Sans MS', 28, True)
    #text3 = font3.render('SCHWER', 1, RED)
    
    screen.blit (bg, (0,0))
    
    start_button = pygame.draw.rect(screen, RED,(410,20,150,50))
    #hard_button = pygame.draw.rect(screen, BLUE,(410,100,150,50),1)
    quit_button = pygame.draw.rect(screen, GREEN,(410,100,150,50))

    screen.blit(text1, (423, 26))
    screen.blit(text2, (433, 106))
    #screen.blit(text3, (424, 115))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 30:
                if pygame.mouse.get_pos()[0] <= 560 and pygame.mouse.get_pos()[1] <= 80:
                    startGame_cm()
            if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 110:
                if pygame.mouse.get_pos()[0] <= 560 and pygame.mouse.get_pos()[1] <= 160:
                    startGame_cm_leicht()
            #if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 110:
                #if pygame.mouse.get_pos()[0] <= 560 and pygame.mouse.get_pos()[1] <= 160:
                    #pygame.quit()