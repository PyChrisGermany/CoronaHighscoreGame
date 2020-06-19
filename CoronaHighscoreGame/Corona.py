import pygame
import os
import sys
import winsound
from winsound import *
#from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC


#import webbrowser





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

#url = 'https://www.paypal.me/chrismatzke90'

screen = pygame.display.set_mode((960,720))
gameIcon = pygame.image.load('/Corona/images/bullets/CV30x30.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption('Corona')
menu = True
music = pygame.mixer.music.load('/Corona/sounds/start_menu.mp3')
pygame.mixer.music.play(-1)
bg = pygame.image.load('/Corona/images/backgrounds/start.png')
#bg.set_alpha(100)
#buttonSound = pygame.mixer.Sound('sounds/click.wav')

def startGame():
    import Auswahl.py

#def paypal():
    #webbrowser.open(url)



while menu:
    font1 = pygame.font.SysFont('Comic Sans MS', 28, True)
    text1 = font1.render('BEENDEN', 1, WHITE)
    font2 = pygame.font.SysFont('Comic Sans MS', 28, True)
    text2 = font2.render('SPIELEN', 1, WHITE)
    font3 = pygame.font.SysFont('Comic Sans MS', 28, True)
    text3 = font3.render('INFO', 1, WHITE)
    
    
    screen.blit (bg, (0,0))
    
    quit_button = pygame.draw.rect(screen, RED,(410,150,150,50))
    start_button = pygame.draw.rect(screen, GREEN,(410,50,150,50))
    #donate_button = pygame.draw.rect(screen, BLUE,(410,550,150,50))


    screen.blit(text1, (418, 156))
    screen.blit(text2, (423, 56))
    #screen.blit(text3, (421, 564))

    pygame.display.flip()
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 150:
                if pygame.mouse.get_pos()[0] <= 560 and pygame.mouse.get_pos()[1] <= 200:
                    #buttonSound.play()
                    pygame.quit()
            if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 50:
                if pygame.mouse.get_pos()[0] <= 560 and pygame.mouse.get_pos()[1] <= 100:
                    #buttonSound.play()
                    startGame()
                #if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 550:
                    #if pygame.mouse.get_pos()[0] <= 560 and pygame.mouse.get_pos()[1] <= 600:
                        #information()