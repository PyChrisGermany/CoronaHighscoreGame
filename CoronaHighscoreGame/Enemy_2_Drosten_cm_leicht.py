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



counter, text = 4, '4'.rjust(3)

pygame.time.set_timer(pygame.USEREVENT, 1000)
startfont = pygame.font.SysFont('Comic Sans MS', 220)



myfont = pygame.font.SysFont('Comic Sans MS', 22)
textsurface = myfont.render('PROF. DR. DROSTEN', True, WHITE)
textsurface2 = myfont.render('CHRISTIAN', True, WHITE)

bg = pygame.image.load('/Corona/images/backgrounds/bg_drosten.png')
screen_width = 960
screen_height = 720

pygame.display.set_caption('Corona - Christian Drosten')
win = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)


frequency = 500  
duration = 850  # Set Duration To 1000 ms == 1 second

frequency2 = 1500 
duration2 = 1110  # Set Duration To 1000 ms == 1 second






clock = pygame.time.Clock()

bubbleSound = pygame.mixer.Sound('/Corona/sounds/bubble.wav')

damageSound = pygame.mixer.Sound('/Corona/sounds/damage.wav')
bloppSound = pygame.mixer.Sound('/Corona/sounds/blopp.wav')
bulletSound = pygame.mixer.Sound('/Corona/sounds/shot.wav')
syringeSound = pygame.mixer.Sound('/Corona/sounds/ah.wav')
hitSound = pygame.mixer.Sound('/Corona/sounds/hit.wav')
music = pygame.mixer.music.load('/Corona/sounds/music_drosten.mp3')
pygame.mixer.music.play(-1)

hs = shelve.open('score.txt')
score = hs['score']
hs.close()


class player(object):
    walkRight = [pygame.image.load('/Corona/images/char_mask_cm/R1.png'), pygame.image.load('/Corona/images/char_mask_cm/R2.png'), pygame.image.load('/Corona/images/char_mask_cm/R3.png'), pygame.image.load('/Corona/images/char_mask_cm/R4.png'), pygame.image.load('/Corona/images/char_mask_cm/R5.png'), pygame.image.load('/Corona/images/char_mask_cm/R6.png'), pygame.image.load('/Corona/images/char_mask_cm/R7.png'), pygame.image.load('/Corona/images/char_mask_cm/R8.png'), pygame.image.load('/Corona/images/char_mask_cm/R9.png'), pygame.image.load('/Corona/images/char_mask_cm/R10.png')]
    walkLeft = [pygame.image.load('/Corona/images/char_mask_cm/L1.png'), pygame.image.load('/Corona/images/char_mask_cm/L2.png'), pygame.image.load('/Corona/images/char_mask_cm/L3.png'), pygame.image.load('/Corona/images/char_mask_cm/L4.png'), pygame.image.load('/Corona/images/char_mask_cm/L5.png'), pygame.image.load('/Corona/images/char_mask_cm/L6.png'), pygame.image.load('/Corona/images/char_mask_cm/L7.png'), pygame.image.load('/Corona/images/char_mask_cm/L8.png'), pygame.image.load('/Corona/images/char_mask_cm/L9.png'), pygame.image.load('/Corona/images/char_mask_cm/L10.png')]
    char = pygame.image.load ('/Corona/images/char_mask_cm/standing.png')
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 12
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 13
        self.standing = True

        
        self.hitbox = pygame.rect.Rect(self.x + 34, self.y + 11, 54, 222)
        self.name = pygame.rect.Rect(self.x - 5, self.y - 60, 170, 30)
        self.healthbar = pygame.rect.Rect(self.x + 10, self.y - 25, 170, 30)
        self.add3 = pygame.rect.Rect(self.x + 15, self.y - 95, 30, 30)
        self.add4 = pygame.rect.Rect(self.x + 85, self.y - 90, 30, 30)
        
        self.score = pygame.rect.Rect(250, 105, 30, 30)
        self.score_double = pygame.rect.Rect(350, 105, 30, 30)
        
        self.player_health = 100
        self.visible = True



        
    def draw(self,win):

        if self.visible and goblin.visible:
            if self.walkCount + 1 >= 30:
                    self.walkCount = 0

                
            if self.standing and goblin.visible:
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
            pygame.draw.rect (win, RED, (self.healthbar[0], self.healthbar[1] - 0, 100, 20))
            pygame.draw.rect (win, GREEN, (self.healthbar[0], self.healthbar[1] - 0, 100 - (1 * (100 - self.player_health)), 20))    
                    
            self.hitbox = pygame.rect.Rect(self.x + 34, self.y + 11, 54, 222)
            self.name = pygame.rect.Rect(self.x - 5, self.y - 60, 170, 30)
            self.healthbar = pygame.rect.Rect(self.x + 10, self.y - 25, 170, 30)
            self.add3 = pygame.rect.Rect(self.x + 15, self.y - 125, 30, 30)
            self.add4 = pygame.rect.Rect(self.x + 85, self.y - 125, 30, 30)
            
            #self.score = pygame.rect.Rect(250, 105, 30, 30)
            #self.score_double = pygame.rect.Rect(350, 105, 30, 30)
        
        if self.visible and goblin.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
                
   
            if not self.standing and goblin.visible:
                if self.left:
                    win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                    

                else:
                    win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1

                

    
    def winner(self):
        win.blit(self.char, (self.x,self.y))
        self.isJump = True
    
    
    
    def hitVirus(self):
        if goblin.visible and goblin.enemy_health < 100:
            goblin.enemy_health += 5
            font2 = pygame.font.SysFont('Comic Sans MS', 68)
            text2 = font2.render ('5', 1, GREEN)
            win.blit (text2, goblin.name)
            pygame.display.update()
        if goblin.visible and self.player_health > 0:
            self.player_health -= 5
            font = pygame.font.SysFont('Comic Sans MS', 100)
            text = font.render ('-5', 1, RED)
            win.blit (text, self.hitbox)
            print('ouch')
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
    
    def hit(self):
        if goblin.enemy_health < 100:
            goblin.enemy_health += 10
            font3 = pygame.font.SysFont('Comic Sans MS', 135)
            text3 = font3.render ('+10', 1, GREEN)
            win.blit (text3, goblin.add1)
            pygame.display.update()


        if self.player_health > 0:
            self.player_health -= 10
            self.isJump = False
            self.jumpCount = 13
            self.y = 480
            self.walkCount = 0
            font = pygame.font.SysFont('Comic Sans MS', 125)
            font2 = pygame.font.SysFont('Comic Sans MS', 68)
            text = font.render ('-10', 1, RED)
            text2 = font2.render ('-10', 1, RED)

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
    bullet = pygame.image.load('/Corona/images/bullets/CV40x40.png')
    
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing
        
        
    def draw(self, win):
        win.blit(self.bullet, (self.x -10, self.y - 13))

        
class projectile_syringe(object):
    vaccineR = pygame.image.load('/Corona/images/bullets/syringeR80x80.png')
    vaccineL = pygame.image.load('/Corona/images/bullets/syringeL80x80.png')
    
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 7 * facing
        
    def draw(self, win):
        if self.facing == -1:
            win.blit(self.vaccineL, (self.x - 70, self.y - 39 ))
        else:
            win.blit(self.vaccineR, (self.x + 10, self.y - 39))



      
class enemy(object):
    walkRight = [pygame.image.load('/Corona/images/char_chris/R1E.png'), pygame.image.load('/Corona/images/char_chris/R2E.png'), pygame.image.load('/Corona/images/char_chris/R3E.png'), pygame.image.load('/Corona/images/char_chris/R4E.png'), pygame.image.load('/Corona/images/char_chris/R5E.png'), pygame.image.load('/Corona/images/char_chris/R6E.png'), pygame.image.load('/Corona/images/char_chris/R7E.png'), pygame.image.load('/Corona/images/char_chris/R8E.png'), pygame.image.load('/Corona/images/char_chris/R9E.png'), pygame.image.load('/Corona/images/char_chris/R10E.png'), pygame.image.load('/Corona/images/char_chris/R11E.png')]
    walkLeft = [pygame.image.load('/Corona/images/char_chris/L1E.png'), pygame.image.load('/Corona/images/char_chris/L2E.png'), pygame.image.load('/Corona/images/char_chris/L3E.png'), pygame.image.load('/Corona/images/char_chris/L4E.png'), pygame.image.load('/Corona/images/char_chris/L5E.png'), pygame.image.load('/Corona/images/char_chris/L6E.png'), pygame.image.load('/Corona/images/char_chris/L7E.png'), pygame.image.load('/Corona/images/char_chris/L8E.png'), pygame.image.load('/Corona/images/char_chris/L9E.png'), pygame.image.load('/Corona/images/char_chris/L10E.png'), pygame.image.load('/Corona/images/char_chris/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]

        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x + 20, self.y + 0, 58, 222)
        self.name = (self.x - 45, self.y - 60, 170, 30)
        self.healthbar = (self.x + 5, self.y - 25, 170, 30)
        self.add1 = (self.x + 15, self.y - 200, 30, 30)
        self.enemy_health = 100
        self.visible = True
        self.damageBullet = -2
        self.DamageHit = 10
        self.isJump = False
        self.jumpCount = 15
        self.left = False
        self.right = False

        

   
       
    def draw(self,win):
        self.move()
        self.move_low()
        self.move_superlow()
        self.shoot()
        self.shoot2()
        if self.visible:

            if self.walkCount + 1 >= 33:
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
            self.name = (self.x - 45, self.y - 60, 170, 30)
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
        if man.visible and self.enemy_health < 50:
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
                    
    def shoot(self):
        if self.visible and man.visible:
            facing = 0.3

            if len(viruses) < 2:
                viruses.append(projectile_virus(round(self.x + self.width //2), round(self.y + self.height//2), 10, (0,0,0), facing))
                bloppSound.play()
            shootLoopEnemy = 1
            
    def shoot2(self):
        if self.visible and man.visible and self.enemy_health < 50:
            facing = 0.7

            if len(viruses) < 3:
                viruses.append(projectile_virus2(round(self.x + self.width //2), round(self.y + self.height//2), 10, (0,0,0), facing))
                bloppSound.play()
            shootLoopEnemy2 = 1
            

                    
    
    def winner(self):

        if self.walkCount > 0:
            if self.jumpCount >= -15:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.2 * neg
                self.jumpCount -= 1

            else:
                self.isJump = True
                self.jumpCount = 15
        
 
    def hitBullet(self):
        if man.visible:
            if man.player_health < 100:
                man.player_health += 3
                font2 = pygame.font.SysFont('Comic Sans MS', 68)
                text2 = font2.render ('+3', 1, GREEN)
                win.blit (text2, man.add4)
                pygame.display.update()
            if self.enemy_health > 0:
                self.enemy_health -= 3
                font = pygame.font.SysFont('Comic Sans MS', 100)
                text = font.render ('-3', 1, RED)
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
                
    def hitSyringe(self):
        if man.visible:
            if man.player_health < 100:
                man.player_health += 5
                font2 = pygame.font.SysFont('Comic Sans MS', 68)
                text2 = font2.render ('+5', 1, GREEN)
                win.blit (text2, man.add3)
                pygame.display.update()
            if self.enemy_health > 0:
                self.enemy_health -= 5
                font = pygame.font.SysFont('Comic Sans MS', 125)
                text = font.render ('-5', 1, RED)
                win.blit (text, self.hitbox)
                print('hit_with_syringe')
                pygame.display.update()
                i = 0
                while i < 4:
                    pygame.time.delay(3)
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 5
                            pygame.quit()
            else:
                self.visible = False

                
                
class projectile_virus(object):
    virusEnemy = pygame.image.load('/Corona/images/bullets/CV20x20.png')
    
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius 
        self.color = color
        self.facing = facing
        self.vel = 15 * facing
  
    def draw(self, win):
        win.blit(self.virusEnemy, (self.x, self.y - 13))
        
class projectile_virus2(object):
    virusEnemy2 = pygame.image.load('/Corona/images/bullets/CVG40x40.png')
    
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius * 2
        self.color = color
        self.facing = facing
        self.vel = 15 * facing
  
    def draw(self, win):
        win.blit(self.virusEnemy2, (self.x, self.y - 13))
     
def retry():
    del sys.modules['Steuerung_cm']
    import Steuerung_cm.py
            

def startGame():
    if 'Enemy_3_Wieler_cm_leicht' in sys.modules:  
        del sys.modules['Enemy_3_Wieler_cm_leicht']

        import Enemy_3_Wieler_cm_leicht.py
    else:
        import Enemy_3_Wieler_cm_leicht.py

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
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    for syringe in syringes:
        syringe.draw(win)
    for virusEnemy in viruses:
        virusEnemy.draw(win)
    for virusEnemy2 in viruses2:
        virusEnemy2.draw(win)
        
    if goblin.visible == False:
       
        win.blit(man.char, (man.x,man.y))
        man.isJump = True
        
        start_button = pygame.draw.rect(win, GREEN,(410,22,150,50))
        font_button = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button = font_button.render('WEITER', 1, WHITE)
        win.blit(text_button, (427, 28))
        
        gewinn = pygame.image.load('/Corona/images/winnings/level_2.png')
        gewinn.set_alpha(210)
        win.blit(gewinn, (50,200))
        
        gegner = pygame.image.load('/Corona/images/enemies/wieler.png')
        gegner.set_alpha(210)
        win.blit(gegner, (630,200))
        
    if goblin.visible and man.visible:
        text = font.render('Punkte: ' + str(score), 1, WHITE)
        win.blit(text, (115, 1))
    
        text2 = font2.render('LEVEL 2', 1, BLUE)
        win.blit(text2, (670, 1))
        

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
       
       
    if goblin.visible and man.player_health >= 100:
        font_extra2x = pygame.font.SysFont('Comic Sans MS', 68, True)
        text_extra2x = font_extra2x.render('2x', 1, GREEN, BLACK)
        win.blit(text_extra2x, (10,1))
        
    if man.visible and goblin.visible and man.player_health < 100:
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
goblin = enemy(10, 495, 111, 222, 820)
shootLoop = 0
shootLoop2 = 0
shootLoop3 = 0
shootLoopEnemy = 0
shootLoopEnemy2 = 0
bullets = []
bullet = projectile
viruses = []
virusEnemy = projectile_virus
viruses2 = []
virusEnemy2 = projectile_virus2
syringes = []
syringe = projectile_syringe

run = True
t = 0
menuAtivo = True

dt = 0
timer = 1
dt = clock.tick(3) / 1000

while t < 4:
    win.blit(bg,(0,0))
    counter -= 1
    t += 1
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

    if goblin.visible == True and man.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                timer -= dt
                print('Time elapsed is', dt, 'seconds')
                if timer <= 0:
                    bubbleSound.play()
                    score -= 10
                    #font_score = pygame.font.SysFont('Comic Sans MS', 68)
                    #text_score = font_score.render ('-10', 1, RED)
                    #win.blit (text_score, man.score)
                    #pygame.display.flip()
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
    if shootLoopEnemy > 0:
        shootLoopEnemy += 1
    if shootLoopEnemy > 15:
        shootLoopEnemy = 0
    if shootLoopEnemy2 > 0:
        shootLoopEnemy2 += 1
    if shootLoopEnemy2 > 15:
        shootLoopEnemy2 = 0
        
        
        
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 25:
                if pygame.mouse.get_pos()[0] <= 560 and pygame.mouse.get_pos()[1] <= 75:
                    startGame()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    
    
    for virusEnemy in viruses:
        if man.visible == True and goblin.visible == True:
            if virusEnemy.y - virusEnemy.radius < man.hitbox[1] + man.hitbox [3] and virusEnemy.y + virusEnemy.radius > man.hitbox[1]:
                if virusEnemy.x + virusEnemy.radius > man.hitbox[0] and virusEnemy.x - virusEnemy.radius < man.hitbox[0] + man.hitbox[2]:
                    damageSound.play()
                    #font_score = pygame.font.SysFont('Comic Sans MS', 68)
                    #text_score = font_score.render ('-5', 1, RED)
                    #win.blit (text_score, man.score)
                    man.hitVirus()
                    #pygame.display.flip()
                    score -= 5
                    viruses.pop(viruses.index(virusEnemy))
    
        if virusEnemy.x < screen_width and virusEnemy.x > 0:
            virusEnemy.x += virusEnemy.vel
   
        else:
            viruses.pop(viruses.index(virusEnemy))
            
            
    for virusEnemy2 in viruses2:
        if man.visible == True and goblin.visible == True:
            if virusEnemy2.y - virusEnemy2.radius < man.hitbox[1] + man.hitbox [3] and virusEnemy2.y + virusEnemy2.radius > man.hitbox[1]:
                if virusEnemy2.x + virusEnemy2.radius > man.hitbox[0] and virusEnemy2.x - virusEnemy2.radius < man.hitbox[0] + man.hitbox[2]:
                    damageSound.play()
                    #font_score = pygame.font.SysFont('Comic Sans MS', 68)
                    #text_score = font_score.render ('-5', 1, RED)
                    #win.blit (text_score, man.score)
                    man.hitVirus()
                    #pygame.display.flip()
                    score -= 5
                    viruses2.pop(viruses2.index(virusEnemy2))
    
        if virusEnemy2.x < screen_width and virusEnemy2.x > 0:
            virusEnemy2.x -= virusEnemy2.vel
   
        else:
            viruses2.pop(viruses2.index(virusEnemy2))

    
    for bullet in bullets:
        if goblin.visible == True:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox [3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    hitSound.play()
                    score += 3
                    #font_score = pygame.font.SysFont('Comic Sans MS', 68)
                    #text_score = font_score.render ('+3', 1, BLUE)
                    #win.blit (text_score, man.score)
                    #pygame.display.flip()
                    goblin.hitBullet()
                    bullets.pop(bullets.index(bullet))
                    if man.player_health >=100:
                        score += 3
                        #font_score2 = pygame.font.SysFont('Comic Sans MS', 125)
                        #text_score2 = font_score2.render ('+3', 1, BLUE)
                        #win.blit (text_score2, man.score_double)
                        #pygame.display.flip()
    
        if bullet.x < screen_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    for syringe in syringes:
        if goblin.visible == True:
            if syringe.y - syringe.radius < goblin.hitbox[1] + goblin.hitbox [3] and syringe.y + syringe.radius > goblin.hitbox[1]:
                if syringe.x + syringe.radius > goblin.hitbox[0] and syringe.x - syringe.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    syringeSound.play()
                    score += 5
                    #font_score = pygame.font.SysFont('Comic Sans MS', 68)
                    #text_score = font_score.render ('+5', 1, BLUE)
                    #win.blit (text_score, man.score)
                    #pygame.display.flip()
                    goblin.hitSyringe()
                    syringes.pop(syringes.index(syringe))
                    if man.player_health >=100:
                        score += 5
                        #font_score2 = pygame.font.SysFont('Comic Sans MS', 125)
                        #text_score2 = font_score2.render ('+5', 1, BLUE)
                        #win.blit (text_score2, man.score_double)
                        #pygame.display.flip()
            
        if syringe.x < screen_width and syringe.x > 0:
            syringe.x += syringe.vel
        else:
            syringes.pop(syringes.index(syringe))


       
    previous_key = pygame.key.get_pressed()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LCTRL] and shootLoop == 0:
        if goblin.visible and man.visible:
            bulletSound.play()
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 3:
                bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 10, (0,0,0), facing))
                
            shootLoop = 1
            
            
        
    if keys[pygame.K_LSHIFT] and shootLoop3 == 0:
        if goblin.visible and man.visible:
            bulletSound.play()
            if man.left:
                facing = -1

            else:
                facing = 1

            if len(syringes) < 1:
                syringes.append(projectile_syringe(round(man.x + man.width //2), round(man.y + man.height//2), 1, (0,0,0), facing))
                
            shootLoop3 = 1

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
                man.right = True
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