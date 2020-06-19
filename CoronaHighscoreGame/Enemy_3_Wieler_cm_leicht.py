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
#from Summon_1_Jens import highscore


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
textsurface = myfont.render('LOTHAR WIELER', True, WHITE)
textsurface2 = myfont.render('CHRISTIAN', True, WHITE)

bg = pygame.image.load('/Corona/images/backgrounds/bg_lothar.png')
screen_width = 960
screen_height = 720
pygame.display.set_caption('Corona - Angela Merkel')
win = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
#mongo.draw(win)

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
music = pygame.mixer.music.load('/Corona/sounds/music_wieler.mp3')
pygame.mixer.music.play(-1)

hs = shelve.open('score.txt')
score = hs['score']
hs.close()




class player(object):
    walkRight = [pygame.image.load('/Corona/images/char_app_cm/R1.png'), pygame.image.load('/Corona/images/char_app_cm/R2.png'), pygame.image.load('/Corona/images/char_app_cm/R3.png'), pygame.image.load('/Corona/images/char_app_cm/R4.png'), pygame.image.load('/Corona/images/char_app_cm/R5.png'), pygame.image.load('/Corona/images/char_app_cm/R6.png'), pygame.image.load('/Corona/images/char_app_cm/R7.png'), pygame.image.load('/Corona/images/char_app_cm/R8.png'), pygame.image.load('/Corona/images/char_app_cm/R9.png'), pygame.image.load('/Corona/images/char_app_cm/R10.png')]
    walkLeft = [pygame.image.load('/Corona/images/char_app_cm/L1.png'), pygame.image.load('/Corona/images/char_app_cm/L2.png'), pygame.image.load('/Corona/images/char_app_cm/L3.png'), pygame.image.load('/Corona/images/char_app_cm/L4.png'), pygame.image.load('/Corona/images/char_app_cm/L5.png'), pygame.image.load('/Corona/images/char_app_cm/L6.png'), pygame.image.load('/Corona/images/char_app_cm/L7.png'), pygame.image.load('/Corona/images/char_app_cm/L8.png'), pygame.image.load('/Corona/images/char_app_cm/L9.png'), pygame.image.load('/Corona/images/char_app_cm/L10.png')]
    char = pygame.image.load ('/Corona/images/char_app_cm/standing.png')
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 13
        self.standing = True

        
        self.hitbox = pygame.rect.Rect(self.x + 34, self.y + 11, 54, 222)
        self.name = pygame.rect.Rect(self.x - 5, self.y - 60, 170, 30)
        self.healthbar = pygame.rect.Rect(self.x + 18, self.y - 25, 170, 30)
        self.add3 = pygame.rect.Rect(self.x + 15, self.y - 95, 30, 30)
        self.add4 = pygame.rect.Rect(self.x + 85, self.y - 90, 30, 30)
        
        self.score = pygame.rect.Rect(250, 105, 30, 30)
        self.score_double = pygame.rect.Rect(350, 105, 30, 30) 
        
        self.player_health = 150
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
            pygame.draw.rect (win, RED, (self.healthbar[0], self.healthbar[1] - 0, 150, 20))
            pygame.draw.rect (win, GREEN, (self.healthbar[0], self.healthbar[1] - 0, 150 - (1 * (150 - self.player_health)), 20))    
                    
            self.hitbox = pygame.rect.Rect(self.x + 34, self.y + 11, 54, 222)
            self.name = pygame.rect.Rect(self.x - 5, self.y - 60, 170, 30)
            self.healthbar = pygame.rect.Rect(self.x - 18, self.y - 25, 170, 30)
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
    
    
    
    def hit(self):
        if goblin.enemy_health < 150:
            goblin.enemy_health += 15
            font3 = pygame.font.SysFont('Comic Sans MS', 135)
            text3 = font3.render ('+15', 1, GREEN)
            win.blit (text3, goblin.add1)
            pygame.display.update()

        if self.player_health > 0:
            self.player_health -= 15
            self.isJump = False
            self.jumpCount = 13
            self.y = 480
            self.walkCount = 0
            font = pygame.font.SysFont('Comic Sans MS', 125)
            font2 = pygame.font.SysFont('Comic Sans MS', 68)
            text = font.render ('-15', 1, RED)
            text2 = font2.render ('-15', 1, RED)

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

        
    def hitVirus(self):
        if goblin.enemy_health < 150:
            goblin.enemy_health += 5
            font2 = pygame.font.SysFont('Comic Sans MS', 68)
            text2 = font2.render ('+5', 1, GREEN)
            #text2 = font2.render ('+1', 1, GREEN)
            win.blit (text2, goblin.name)
            pygame.display.update()
        if self.player_health > 0:
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
        
        
class projectile(object):
    virus = pygame.image.load('/Corona/images/bullets/CV50x50.png')
    
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 30 * facing
        
        
    def draw(self, win):
        win.blit(self.virus, (self.x -20, self.y - 13))

class projectile_syringe(object):
    vaccineR = pygame.image.load('/Corona/images/bullets/syringeR80x80.png')
    vaccineL = pygame.image.load('/Corona/images/bullets/syringeL80x80.png')
    
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing
        
    def draw(self, win):
        if self.facing == -1:
            win.blit(self.vaccineL, (self.x - 60, self.y - 39))
        else:
            win.blit(self.vaccineR, (self.x - 5, self.y - 39))

      
class enemy(object):
    walkRight = [pygame.image.load('/Corona/images/char_lothar/R1E.png'), pygame.image.load('/Corona/images/char_lothar/R2E.png'), pygame.image.load('/Corona/images/char_lothar/R3E.png'), pygame.image.load('/Corona/images/char_lothar/R4E.png'), pygame.image.load('/Corona/images/char_lothar/R5E.png'), pygame.image.load('/Corona/images/char_lothar/R6E.png'), pygame.image.load('/Corona/images/char_lothar/R7E.png'), pygame.image.load('/Corona/images/char_lothar/R8E.png'), pygame.image.load('/Corona/images/char_lothar/R9E.png'), pygame.image.load('/Corona/images/char_lothar/R10E.png'), pygame.image.load('/Corona/images/char_lothar/R11E.png')]
    walkLeft = [pygame.image.load('/Corona/images/char_lothar/L1E.png'), pygame.image.load('/Corona/images/char_lothar/L2E.png'), pygame.image.load('/Corona/images/char_lothar/L3E.png'), pygame.image.load('/Corona/images/char_lothar/L4E.png'), pygame.image.load('/Corona/images/char_lothar/L5E.png'), pygame.image.load('/Corona/images/char_lothar/L6E.png'), pygame.image.load('/Corona/images/char_lothar/L7E.png'), pygame.image.load('/Corona/images/char_lothar/L8E.png'), pygame.image.load('/Corona/images/char_lothar/L9E.png'), pygame.image.load('/Corona/images/char_lothar/L10E.png'), pygame.image.load('/Corona/images/char_lothar/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 20, self.y + 0, 58, 222)
        self.name = (self.x - 36, self.y - 60, 170, 30)
        self.healthbar = (self.x - 20, self.y - 25, 170, 30)
        self.add1 = (self.x + 15, self.y - 200, 30, 30)
        self.enemy_health = 150
        self.visible = True



        self.isJump = False
        self.jumpCount = 15
        

   
       
    def draw(self,win):
        self.move()
        self.move_low()
        self.shoot()
        self.jump()
        #self.jump2()
        #self.summon
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
            

            pygame.draw.rect (win, RED, (self.healthbar[0], self.healthbar[1] - 0, 150, 20))
            pygame.draw.rect (win, GREEN, (self.healthbar[0], self.healthbar[1] - 0, 150 - (1 * (150 - self.enemy_health)), 20))

            self.hitbox = (self.x + 20, self.y + 0, 58, 222)
            self.name = (self.x - 36, self.y - 60, 170, 30)
            self.healthbar = (self.x - 20, self.y - 25, 170, 30)
            self.add1 = (self.x + 15, self.y - 200, 30, 30)

            
            win.blit(textsurface, self.name)
            #pygame.draw.rect(win, WHITE, self.hitbox,2)
            #pygame.draw.rect(win, (255,255,255), self.add1,2)
            #pygame.draw.rect(win, (255,255,255), self.add2,2)
            #pygame.draw.rect(win, (255,255,255), self.name,2)
            #pygame.draw.rect(win, (255,255,255), self.healthbar,2)
       
    #def summon(self):
        #if man.visible:
            #summon.draw(win)
            #pygame.display.update()
    
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
        if self.visible and self.enemy_health < 100:
            facing = 0.2

            if len(viruses) < 3:
                viruses.append(projectile_virus(round(self.x + self.width //2), round(self.y + self.height//2), 10, (0,0,0), facing))
                bloppSound.play()
            shootLoopEnemy = 1
                    
    def jump(self):
        if self.visible and man.visible:
            if self.walkCount > 0:
                if self.jumpCount >= -15:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= (self.jumpCount ** 2) * 0.2 * neg
                    self.jumpCount -= 1

                else:
                    self.y = 495
                    self.isJump = True
                    self.jumpCount = 15
                    
    def jump2(self):
        if self.visible and man.visible and self.enemy_health < 125:
            if self.walkCount > 0:
                if self.jumpCount >= -15:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= (self.jumpCount ** 2) * 0.2 * neg
                    self.jumpCount -= 1

                else:
                    self.y = 495
                    self.isJump = True
                    self.jumpCount = 15
                
    
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
            if man.player_health < 150:
                man.player_health += 5
                font2 = pygame.font.SysFont('Comic Sans MS', 68)
                text2 = font2.render ('+5', 1, GREEN)
                win.blit (text2, man.add4)
                pygame.display.update()
            if self.enemy_health > 0:
                self.enemy_health -= 5
                font = pygame.font.SysFont('Comic Sans MS', 100)
                text = font.render ('-5', 1, RED)
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
            if man.player_health < 150:
                man.player_health += 10
                font2 = pygame.font.SysFont('Comic Sans MS', 68)
                text2 = font2.render ('+10', 1, GREEN)
                win.blit (text2, man.add3)
                pygame.display.update()
            if self.enemy_health > 0:
                self.enemy_health -= 10
                font = pygame.font.SysFont('Comic Sans MS', 125)
                text = font.render ('-10', 1, RED)
                win.blit (text, self.hitbox)
                print('hit_with_syringe')
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
                
class projectile_virus(object):
    virusEnemy = pygame.image.load('/Corona/images/bullets/CVG60x60.png')
    
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius * 3
        self.color = color
        self.facing = facing
        self.vel = 15 * facing
        
        
    def draw(self, win):
        win.blit(self.virusEnemy, (self.x, self.y - 13))

def retry():
    del sys.modules['Steuerung_cm']
    import Steuerung_cm.py
          

def startGame():
    if 'Enemy_4_Angela_cm_leicht' in sys.modules:  
        del sys.modules['Enemy_4_Angela_cm_leicht']

        import Enemy_4_Angela_cm_leicht.py
    else:
        import Enemy_4_Angela_cm_leicht.py
    
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
    #summon.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    for syringe in syringes:
        syringe.draw(win)
    for virusEnemy in viruses:
        virusEnemy.draw(win)
          
        
    if goblin.visible == False:

        win.blit(man.char, (man.x,man.y))
        man.isJump = True
        
        start_button = pygame.draw.rect(win, GREEN,(410,22,150,50))
        font_button = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button = font_button.render('WEITER', 1, WHITE)
        win.blit(text_button, (427, 28))
        
        gewinn = pygame.image.load('/Corona/images/winnings/level_3.png')
        gewinn.set_alpha(210)
        win.blit(gewinn, (50,200))
        
        gegner = pygame.image.load('/Corona/images/enemies/merkel.png')
        gegner.set_alpha(210)
        win.blit(gegner, (630,200))
        
    if goblin.visible and man.visible:
        text = font.render('Punkte: ' + str(score), 1, WHITE)
        win.blit(text, (115, 1))
    
        text2 = font2.render('LEVEL 3', 1, BLUE)
        win.blit(text2, (670, 1))

    if man.visible == False:

        game_over = pygame.image.load('/Corona/images/backgrounds/game_over.png')
        game_over.set_alpha(210)
        win.blit(game_over, (263,200))
        
        goblin.y = 495
        
        retry_button = pygame.draw.rect(win, BLUE,(150,22,150,50))
        font_button = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button = font_button.render('NOCHMAL', 1, WHITE)
        win.blit(text_button, (154, 28))
        
        quit_button = pygame.draw.rect(win, RED,(660,22,150,50))
        font_button = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button = font_button.render('BEENDEN', 1, WHITE)
        win.blit(text_button, (668, 28))
        
        endGame()
        
    if goblin.visible and man.player_health >= 150:
        font_extra2x = pygame.font.SysFont('Comic Sans MS', 68, True)
        text_extra2x = font_extra2x.render('2x', 1, GREEN)
        win.blit(text_extra2x, (10,1))
    if man.visible and goblin.visible and man.player_health < 150:
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
bullets = []
bullet = projectile
viruses = []
virusEnemy = projectile_virus
syringes = []
syringe = projectile_syringe


run = True
t = 0
menuAtivo = True


dt = 0
timer = 1
dt = clock.tick(3) / 1000

while t < 4:
    clock.tick(60)
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
                    score -= 15
                    #font_score = pygame.font.SysFont('Comic Sans MS', 68)
                    #text_score = font_score.render ('-20', 1, RED)
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
    if shootLoop3 > 20:
        shootLoop3 = 0
    if shootLoopEnemy > 0:
        shootLoopEnemy += 1
    if shootLoopEnemy > 20:
        shootLoopEnemy = 0
        
    
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
            virusEnemy.x -= virusEnemy.vel
   
        else:
            viruses.pop(viruses.index(virusEnemy))  
      
      
    for bullet in bullets:
        if goblin.visible == True:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox [3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    hitSound.play()
                    score += 5
                    #font_score = pygame.font.SysFont('Comic Sans MS', 68)
                    #text_score = font_score.render ('+5', 1, BLUE)
                    #win.blit (text_score, man.score)
                    #pygame.display.flip()
                    goblin.hitBullet()
                    bullets.pop(bullets.index(bullet))
                    if man.player_health >=150:
                        score += 5
                        #font_score2 = pygame.font.SysFont('Comic Sans MS', 125)
                        #text_score2 = font_score2.render ('+5', 1, BLUE)
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
                    score += 10
                    #font_score = pygame.font.SysFont('Comic Sans MS', 68)
                    #text_score = font_score.render ('+10', 1, BLUE)
                    #win.blit (text_score, man.score)
                    #pygame.display.flip()
                    goblin.hitSyringe()
                    syringes.pop(syringes.index(syringe))
                    if man.player_health >=150:
                        score += 10
                        #font_score2 = pygame.font.SysFont('Comic Sans MS', 125)
                        #text_score2 = font_score2.render ('+10', 1, BLUE)
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
            if len(bullets) < 4:
                bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 10, (0,0,0), facing))
                
            shootLoop = 1


        
    if keys[pygame.K_LSHIFT]and shootLoop3 == 0:
        if goblin.visible and man.visible:
            bulletSound.play()
            if man.left:
                facing = -1

            else:
                facing = 1

            if len(syringes) < 2:
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