import pygame
import os
import sys
import ctypes
import time
import shelve
import winsound
from winsound import *

#from ctypes import *
#from pygame import *
#from pygame.locals import *
#from pathlib import Path
#from importlib import reload



pygame.init()
pygame.font.init() 



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


#sys.path.append('/Corona/')


counter, text = 4, '4'.rjust(3)

pygame.time.set_timer(pygame.USEREVENT, 1000)
startfont = pygame.font.SysFont('Comic Sans MS', 220)

myfont = pygame.font.SysFont('Comic Sans MS', 22)
textsurface = myfont.render('JENS SPAHN', True, WHITE)
textsurface2 = myfont.render('CHRISTIAN', True, WHITE)
start_ticks=pygame.time.get_ticks() 
bg = pygame.image.load('/Corona/images/backgrounds/bg_jens.png')
screen_width = 960
screen_height = 720
pygame.display.set_caption('Corona - summon Spahn')
win = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)




frequency = 500  
duration = 850  # Set Duration To 1000 ms == 1 second

frequency2 = 1500 
duration2 = 1110  # Set Duration To 1000 ms == 1 second




clock = pygame.time.Clock()

dt = 0
timer = 1

bubbleSound = pygame.mixer.Sound('/Corona/sounds/bubble.wav')
bloppSound = pygame.mixer.Sound('/Corona/sounds/blopp.wav')
bulletSound = pygame.mixer.Sound('/Corona/sounds/shot.wav')
hitSound = pygame.mixer.Sound('/Corona/sounds/hit.wav')
music = pygame.mixer.music.load('/Corona/sounds/music_jens.mp3')
pygame.mixer.music.play(-1)

hs = shelve.open('score.txt')
score = 0



class player(object):
    walkRight = [pygame.image.load('/Corona/images/char_cm/R1.png'), pygame.image.load('/Corona/images/char_cm/R2.png'), pygame.image.load('/Corona/images/char_cm/R3.png'), pygame.image.load('/Corona/images/char_cm/R4.png'), pygame.image.load('/Corona/images/char_cm/R5.png'), pygame.image.load('/Corona/images/char_cm/R6.png'), pygame.image.load('/Corona/images/char_cm/R7.png'), pygame.image.load('/Corona/images/char_cm/R8.png'), pygame.image.load('/Corona/images/char_cm/R9.png'), pygame.image.load('/Corona/images/char_cm/R10.png')]#, pygame.image.load('/Corona/images/char_nb/R11.png'), pygame.image.load('/Corona/images/char_nb/R12.png'), pygame.image.load('/Corona/images/char_nb/R13.png')]
    walkLeft = [pygame.image.load('/Corona/images/char_cm/L1.png'), pygame.image.load('/Corona/images/char_cm/L2.png'), pygame.image.load('/Corona/images/char_cm/L3.png'), pygame.image.load('/Corona/images/char_cm/L4.png'), pygame.image.load('/Corona/images/char_cm/L5.png'), pygame.image.load('/Corona/images/char_cm/L6.png'), pygame.image.load('/Corona/images/char_cm/L7.png'), pygame.image.load('/Corona/images/char_cm/L8.png'), pygame.image.load('/Corona/images/char_cm/L9.png'), pygame.image.load('/Corona/images/char_cm/L10.png')]#, pygame.image.load('/Corona/images/char_nb/L11.png'), pygame.image.load('/Corona/images/char_nb/L12.png'), pygame.image.load('/Corona/images/char_nb/L13.png')]
    char = pygame.image.load('/Corona/images/char_cm/standing.png')
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.right = False
        self.left = False
        self.walkCount = 0
        self.jumpCount = 13
        self.standing = True

        self.last = pygame.time.get_ticks()
        
        self.hitbox = pygame.rect.Rect(self.x + 34, self.y + 11, 54, 222)
        self.name = pygame.rect.Rect(self.x - 5, self.y - 60, 170, 30)
        self.healthbar = pygame.rect.Rect(self.x + 10, self.y - 25, 170, 30)
        self.add3 = pygame.rect.Rect(self.x + 15, self.y - 95, 30, 30)
        self.add4 = pygame.rect.Rect(self.x + 85, self.y - 90, 30, 30)
        
        self.score = pygame.rect.Rect(250, 105, 30, 30)
        self.score_double = pygame.rect.Rect(350, 105, 30, 30)
        
        self.player_health = 50
        self.visible = True




        
    def draw(self,win):
        if self.visible and mongo.visible:
            if self.walkCount + 1 >= 30:
                    self.walkCount = 0

                
            if self.standing and mongo.visible:
                if self.left:
                    win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                    
                else:
                    win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                    
            #pygame.draw.rect(win, WHITE, self.hitbox,2)
            #pygame.draw.rect(win, (255,255,255), self.add3,2)
            #pygame.draw.rect(win, (255,255,255), self.score,2)
            #pygame.draw.rect(win, (255,255,255), self.score_double,2)
            win.blit(textsurface2, self.name)
            pygame.draw.rect (win, RED, (self.healthbar[0], self.healthbar[1] - 0, 50, 20))
            pygame.draw.rect (win, GREEN, (self.healthbar[0], self.healthbar[1] - 0, 50 - (1 * (50 - self.player_health)), 20))    
                    
            self.hitbox = pygame.rect.Rect(self.x + 34, self.y + 11, 54, 222)
            self.name = pygame.rect.Rect(self.x - 5, self.y - 60, 170, 30)
            self.healthbar = pygame.rect.Rect(self.x + 37, self.y - 25, 170, 30)
            self.add3 = pygame.rect.Rect(self.x + 15, self.y - 125, 30, 30)
            self.add4 = pygame.rect.Rect(self.x + 85, self.y - 125, 30, 30)
            
            #self.score = pygame.rect.Rect(250, 105, 30, 30)
            #self.score_double = pygame.rect.Rect(350, 105, 30, 30)
        
        
        if self.visible and mongo.visible:
            if self.walkCount + 1 >= 30:
                self.walkCount = 0
                
   
            if not self.standing and mongo.visible:
                if self.left:
                    win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                    

                else:
                    win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1           

            
    

    def hit(self):

        if mongo.enemy_health < 100:
            mongo.enemy_health += 5
            font3 = pygame.font.SysFont('Comic Sans MS', 135)
            text3 = font3.render ('+5', 1, GREEN)
            win.blit (text3, mongo.add1)
            pygame.display.update()

        if self.player_health > 0:

            self.player_health -= 5
            self.isJump = False
            self.jumpCount = 13
            #self.x = 800
            self.y = 480
            self.walkCount = 0
            
            
            font = pygame.font.SysFont('Comic Sans MS', 125)
            font2 = pygame.font.SysFont('Comic Sans MS', 68)
            text = font.render ('-5', 1, RED)
            text2 = font2.render ('-5', 1, RED)
            #font3 = pygame.font.SysFont('Comic Sans MS', 135)
            #text3 = font3.render ('+5', 1, GREEN)
            #win.blit (text3, mongo.add1)
            win.blit (text, self.hitbox)
            win.blit (text2, self.name)
            pygame.display.update()

            i = 0
            while i < 15:

                i += 1
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 16
                        pygame.quit()
        else:
            self.visible = False


                
        


class projectile(object):
    virus = pygame.image.load('/Corona/images/bullets/CV30x30.png')
    
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing
        
        
    def draw(self, win):
        win.blit(self.virus, (self.x -10, self.y - 13))


      
class summon(object):
    walkRight = [pygame.image.load('/Corona/images/char_jens/R1E.png'), pygame.image.load('/Corona/images/char_jens/R2E.png'), pygame.image.load('/Corona/images/char_jens/R3E.png'), pygame.image.load('/Corona/images/char_jens/R4E.png'), pygame.image.load('/Corona/images/char_jens/R5E.png'), pygame.image.load('/Corona/images/char_jens/R6E.png'), pygame.image.load('/Corona/images/char_jens/R7E.png'), pygame.image.load('/Corona/images/char_jens/R8E.png'), pygame.image.load('/Corona/images/char_jens/R9E.png'), pygame.image.load('/Corona/images/char_jens/R10E.png'), pygame.image.load('/Corona/images/char_jens/R11E.png')]
    walkLeft = [pygame.image.load('/Corona/images/char_jens/L1E.png'), pygame.image.load('/Corona/images/char_jens/L2E.png'), pygame.image.load('/Corona/images/char_jens/L3E.png'), pygame.image.load('/Corona/images/char_jens/L4E.png'), pygame.image.load('/Corona/images/char_jens/L5E.png'), pygame.image.load('/Corona/images/char_jens/L6E.png'), pygame.image.load('/Corona/images/char_jens/L7E.png'), pygame.image.load('/Corona/images/char_jens/L8E.png'), pygame.image.load('/Corona/images/char_jens/L9E.png'), pygame.image.load('/Corona/images/char_jens/L10E.png'), pygame.image.load('/Corona/images/char_jens/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 7
        self.hitbox = (self.x + 20, self.y + 0, 58, 222)
        self.name = (self.x - 15, self.y - 60, 170, 30)
        self.healthbar = (self.x + 5, self.y - 25, 170, 30)
        self.add1 = (self.x + 15, self.y - 200, 30, 30)
        self.add2 = (self.x + 85, self.y - 90, 30, 30)
        self.enemy_health = 100
        self.visible = True

        

   
       
    def draw(self,win):
        self.move()
        self.move_low()
        self.move_superlow()
        if self.visible:

            if self.walkCount + 1 >= 33: #27
                self.walkCount = 0
            else:
                self.hitbox = (self.x + 60, self.y + 0, 58, 142)

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            

            pygame.draw.rect (win, RED, (self.healthbar[0], self.healthbar[1] - 0, 100, 20))
            pygame.draw.rect (win, GREEN, (self.healthbar[0], self.healthbar[1] - 0, 100 - (1 * (100 - self.enemy_health)), 20))
            self.hitbox = (self.x + 20, self.y + 0, 58, 222)
            self.name = (self.x - 15, self.y - 60, 170, 30)
            self.healthbar = (self.x + 5, self.y - 25, 170, 30)
            self.add1 = (self.x + 15, self.y - 200, 30, 30)
            
            win.blit(textsurface, self.name)
            #pygame.draw.rect(win, WHITE, self.hitbox,2)
            #pygame.draw.rect(win, (255,255,255), self.add1,2)
            #pygame.draw.rect(win, (255,255,255), self.add2,2)
            #pygame.draw.rect(win, (255,255,255), self.name,2)
            #pygame.draw.rect(win, (255,255,255), self.healthbar,2)
       

    
    def move(self):
        if man.visible:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
                    
                    
    def move_low(self):
        if man.visible and self.enemy_health < 25:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel * 0.5
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel * 0.5
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
                    
    def move_superlow(self):
        if man.visible and self.enemy_health < 75:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel #* 0.5
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel #* 0.5
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0    
                    

                    
    
    def winner(self):

        if self.walkCount > 0:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.2 * neg
                self.jumpCount -= 1

            else:
                self.isJump = True
                self.jumpCount = 10
 
     
    def hitBullet(self):
        if man.visible:
            if man.player_health < 50:
                man.player_health += 2
                font2 = pygame.font.SysFont('Comic Sans MS', 68)
                text2 = font2.render ('+2', 1, GREEN)
                win.blit (text2, man.add4)
                pygame.display.update()
            if self.enemy_health > 0:
                self.enemy_health -= 2
                font = pygame.font.SysFont('Comic Sans MS', 100)
                text = font.render ('-2', 1, RED)
                win.blit (text, self.hitbox)
                print('hit_with_virus')
                pygame.display.update()
                
                i = 0
                while i < 4:

                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 5
                            pygame.quit()
            else:
                self.visible = False

def retry():
    del sys.modules['Steuerung_cm']
    import Steuerung_cm.py

    
        
def startGame():
    if 'Enemy_2_Drosten_cm' in sys.modules:  
        del sys.modules['Enemy_2_Drosten_cm']

        import Enemy_2_Drosten_cm.py
    else:
        import Enemy_2_Drosten_cm.py

    
def endGame():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 25:
                    if pygame.mouse.get_pos()[0] <= 300 and pygame.mouse.get_pos()[1] <= 75:
                        retry()
                if pygame.mouse.get_pos()[0] >= 660 and pygame.mouse.get_pos()[1] >= 25:
                    if pygame.mouse.get_pos()[0] <= 810 and pygame.mouse.get_pos()[1] <= 75:
                        pygame.quit()



    

def redrawGameWindow():
    win.blit(bg, (0,0))
    win.fill(BLACK, (0, 0, win.get_width(), win.get_height()// 8))

    hs = shelve.open('score.txt') 
    hs['score'] = score


    man.draw(win)
    mongo.draw(win)
    for bullet in bullets:
        bullet.draw(win)
        
    if mongo.visible and man.visible:
        text = font.render('Punkte: ' + str(score), 1, WHITE)
        win.blit(text, (115, 1))
        text2 = font2.render('LEVEL 1', 1, BLUE)
        win.blit(text2, (670, 1))
        
        
    if mongo.visible == False:
        win.blit(man.char, (man.x,man.y))
        man.isJump = True
        
        start_button = pygame.draw.rect(win, GREEN,(410,22,150,50))
        font_button = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button = font_button.render('WEITER', 1, WHITE)
        win.blit(text_button, (427, 28))
        
        gewinn = pygame.image.load('/Corona/images/winnings/level_1.png')
        gewinn.set_alpha(210)
        win.blit(gewinn, (50,200))
        
        gegner = pygame.image.load('/Corona/images/enemies/drosten.png')
        gegner.set_alpha(210)
        win.blit(gegner, (630,200))
             
        
    if man.visible == False:
        game_over = pygame.image.load('/Corona/images/backgrounds/game_over.png')
        game_over.set_alpha(210)
        win.blit(game_over, (263,200))
        
        retry_button = pygame.draw.rect(win, BLUE,(150,22,150,50))
        font_button = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button = font_button.render('NOCHMAL', 1, WHITE)
        win.blit(text_button, (154, 28))
        
        quit_button = pygame.draw.rect(win, RED,(660,22,150,50))
        font_button = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button = font_button.render('BEENDEN', 1, WHITE)
        win.blit(text_button, (668, 28))
        
        
        endGame()
        
    if mongo.visible and man.player_health >= 50:
        font_extra2x = pygame.font.SysFont('Comic Sans MS', 68, True)
        text_extra2x = font_extra2x.render('2x', 1, GREEN)
        win.blit(text_extra2x, (10,1))
  
    if man.visible and mongo.visible and man.player_health < 50:
        font_extra = pygame.font.SysFont('Comic Sans MS', 68, True)
        text_extra = font_extra.render('1x', 1, GRAY)
        win.blit(text_extra, (10,1))

        
    pygame.display.update()
            

#mainloop
font = pygame.font.SysFont('Comic Sans MS', 68)
font2 = pygame.font.SysFont('Comic Sans MS', 68)
font3 = pygame.font.SysFont('Comic Sans MS', 40, True)
font4 = pygame.font.SysFont('Comic Sans MS', 22, True)

man = player(800, 480, 128, 240)
mongo = summon(10, 495, 111, 222, 820)
shootLoop = 0
shootLoop2 = 0
shootLoop3 = 0
bullets = []
bullet = projectile


run = True
t = 0
menuAtivo = True

dt = 0
timer = 1
dt = clock.tick(3) / 1000

while t < 4:

    counter -= 1
    t += 1
    #bga.set_alpha(100)
    win.blit(bg,(0,0))
    pygame.display.update()
    if counter >= 1:
        text = str(counter).rjust(3)
        win.blit(startfont.render(text, True, RED), (265, 170))
        pygame.display.update()
        winsound.Beep(frequency, duration)
    else:
        los = pygame.image.load('/Corona/images/backgrounds/los.png')
        los.set_alpha(250)
        win.blit(los, (135, 140))
        pygame.display.update()
        winsound.Beep(frequency2, duration2)

        




while run and t > 0:
    

    clock.tick(60)
    

    if mongo.visible == True and man.visible == True:
  
        if man.hitbox[1] < mongo.hitbox[1] + mongo.hitbox[3] and man.hitbox[1] + man.hitbox[3] > mongo.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > mongo.hitbox[0] and man.hitbox[0] < mongo.hitbox[0] + mongo.hitbox[2]:
                timer -= dt
                print('Time elapsed is', dt, 'seconds')
                if timer <= 0:
                    bubbleSound.play()
                    score -= 5
                    #font_score = pygame.font.SysFont('Comic Sans MS', 68)
                    #text_score = font_score.render ('-5', 1, RED)
                    #win.blit (text_score, man.score)
                    man.hit()
                    timer += 1
                   

    
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 10:
        shootLoop = 0
    if shootLoop2 > 0:
        shootLoop2 += 1
    if shootLoop2 > 30:
        shootLoop2 = 0
    if shootLoop3 > 0:
        shootLoop3 += 1
    if shootLoop3 > 30:
        shootLoop3 = 0
        
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 25:
                if pygame.mouse.get_pos()[0] <= 560 and pygame.mouse.get_pos()[1] <= 75:
                    startGame()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

      
    for bullet in bullets:
        if mongo.visible == True:
            if bullet.y - bullet.radius < mongo.hitbox[1] + mongo.hitbox [3] and bullet.y + bullet.radius > mongo.hitbox[1]:
                if bullet.x + bullet.radius > mongo.hitbox[0] and bullet.x - bullet.radius < mongo.hitbox[0] + mongo.hitbox[2]:
                    hitSound.play()
                    score += 2
                    #font_score = pygame.font.SysFont('Comic Sans MS', 68)
                    #text_score = font_score.render ('+2', 1, BLUE)
                    #win.blit (text_score, man.score)
                    #pygame.display.flip()
                    mongo.hitBullet()
                    bullets.pop(bullets.index(bullet))
                    if man.player_health >=50:
                        score += 2
                        #font_score2 = pygame.font.SysFont('Comic Sans MS', 125)
                        #text_score2 = font_score2.render ('+2', 1, BLUE)
                        #win.blit (text_score2, man.score_double)
                        #pygame.display.flip()

    
        if bullet.x < screen_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


       
    previous_key = pygame.key.get_pressed()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LCTRL] and shootLoop == 0:
        if mongo.visible and man.visible:
            bulletSound.play()
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 3:
                bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 10, (0,0,0), facing))
                
            shootLoop = 1

#Arrowkeys
   
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.hitbox.move_ip(-1 *(man.vel), 0)
        man.add3.move_ip(-1 *(man.vel), 0)
        man.add4.move_ip(-1 *(man.vel), 0)
        man.healthbar.move_ip(-1 *(man.vel), 0)
        man.name.move_ip(-1 *(man.vel), 0)
        
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False


    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel:
        man.hitbox.move_ip(1 *(man.vel), 0)
        man.add3.move_ip(1 *(man.vel), 0)
        man.add4.move_ip(1 *(man.vel), 0)
        man.healthbar.move_ip(1 *(man.vel), 0)
        man.name.move_ip(1 *(man.vel), 0)

        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False

        

    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump): 
        if keys[pygame.K_UP]:

            man.isJump = True
            man.walkCount = 0

            if man.isJump == True:
                man.right = False

   
            else:
                man.left = True

    else:
        if man.jumpCount >= -13:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.3 * neg
            man.jumpCount -= 1

        else:
            man.isJump = False
            man.jumpCount = 13


#exit           
    if keys[pygame.K_ESCAPE]:
        print('Game Shuting Down!')
        done = True
        pygame.event.pump() # process event queue
        pygame.quit()
    
    redrawGameWindow()
    

pygame.quit()