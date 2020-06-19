import pygame, sys, os, shelve
import winsound
from winsound import *
from High_Score_Module import highscore
pygame.init()

pygame.display.set_caption('Corona - Top 10 Highscores')
gameIcon = pygame.image.load('/Corona/images/bullets/CV30x30.png')
pygame.display.set_icon(gameIcon)

music = pygame.mixer.music.load('/Corona/sounds/score.mp3')
pygame.mixer.music.play(-1)

X = 960
Y = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


#pygame.display.set_mode((X, Y), pygame.NOFRAME)

bg = pygame.image.load('/Corona/images/backgrounds/no_chance.png')

font = pygame.font.SysFont('Comic Sans MS', 16)
screen = pygame.display.set_mode((X, Y))
screen.blit(bg, (200,15))
#my_score = shelve.open('score.txt')
#my_score = 111
hs = shelve.open('score.txt')
my_score = hs['score']
hs.close()

highscore(screen, 'score_file.txt', my_score)

#txt_surf = font.render('Ready to continue...', True, BLACK)
#txt_rect = txt_surf.get_rect(center=(X//2, Y//2))
#screen.blit(txt_surf, txt_rect)
pygame.display.flip()

