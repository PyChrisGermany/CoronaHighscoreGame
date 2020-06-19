import pygame, sys, os
import webbrowser
pygame.init()

## COLORS ##

#            R    G    B
LIGHTGRAY = (229, 229, 229)
GRAY      = (100, 100, 100)
GREY      = (150, 150, 150)
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

url = 'https:xxx'

font = pygame.font.SysFont('Comic Sans MS', 40)
font2 = pygame.font.SysFont('Comic Sans MS', 40)
font3 = pygame.font.SysFont('Comic Sans MS', 40, True)
bg = pygame.image.load('/Corona/images/backgrounds/highscore.png')
bg.set_alpha(200)







def read_from_file_and_find_highscore(file_name):
    file = open(file_name, 'r')
    lines=file.readlines()
    file.close
       
    high_score = 0
    
    for line in lines:
        name, score = line.strip().split(',')
        score = int(score)

        if score > high_score:
            high_score = score
            high_name = name

    return high_name, high_score


def write_to_file(file_name, your_name, points):
    score_file = open(file_name, 'a')
    print (your_name+',', points, file=score_file)
    score_file.close()


def begin():
    if 'Corona' in sys.modules:  
        del sys.modules['Corona']
        import Corona.py
    else:
        import Corona.py
    
def retry():
    if 'Steuerung' in sys.modules:  
        del sys.modules['Steuerung']
    if 'Steuerung_cm' in sys.modules:  
        del sys.modules['Steuerung_cm']
    if 'Auswahl' in sys.modules:  
        del sys.modules['Auswahl']
    if 'Enemy_1_Jens' in sys.modules:  
        del sys.modules['Enemy_1_Jens']
    if 'Enemy_1_Jens_cm' in sys.modules:  
        del sys.modules['Enemy_1_Jens_cm']
    if 'Enemy_2_Drosten' in sys.modules:  
        del sys.modules['Enemy_2_Drosten']
    if 'Enemy_2_Drosten_cm' in sys.modules:  
        del sys.modules['Enemy_2_Drosten_cm']
    if 'Enemy_3_Wieler' in sys.modules:  
        del sys.modules['Enemy_3_Wieler']
    if 'Enemy_3_Wieler_cm' in sys.modules:  
        del sys.modules['Enemy_3_Wieler_cm']
    if 'Enemy_4_Angela' in sys.modules:  
        del sys.modules['Enemy_4_Angela']
    if 'Enemy_4_Angela_cm' in sys.modules:  
        del sys.modules['Enemy_4_Angela_cm']
    if 'Enemy_5_Bill' in sys.modules:  
        del sys.modules['Enemy_5_Bill']
    if 'Enemy_5_Bill_cm' in sys.modules:  
        del sys.modules['Enemy_5_Bill_cm']
    if 'highscore' in sys.modules:  
        del sys.modules['highscore']
        
    #del sys.modules['Auswahl']
    #del sys.modules['Enemy_1_Jens']
    #del sys.modules['Enemy_1_Jens_cm']
    #del sys.modules['Enemy_2_Drosten']
    #del sys.modules['Enemy_2_Drosten_cm']
    #del sys.modules['Enemy_3_Wieler']
    #del sys.modules['Enemy_3_Wieler_cm']
    #del sys.modules['Enemy_4_Angela']
    #del sys.modules['Enemy_4_Angela_cm']
    #del sys.modules['Enemy_5_Bill']
    #del sys.modules['Enemy_5_Bill_cm']
    #del sys.modules['highscore']
    
    
    
    begin()


def paypal():
    webbrowser.open(url)


def show_top10(screen, file_name):

    bx = 960  # x-size of box
    by = 720  # y-size of box
    #pygame.display.set_mode((bx, by), pygame.NOFRAME)
    file = open(file_name, 'r')
    lines=file.readlines()
    
    

       
    all_score = []
    
    for line in lines:
        sep = line.index(',')
        name = line[:sep]
        score = int(line[sep+1:-1])
        all_score.append((score, name))
    file.close
    all_score.sort(reverse=True)  # sort from largest to smallest
    best = all_score[:10]  # top 10 values

    # make the presentation box
    box = pygame.surface.Surface((bx, by)) 
    box.blit(bg, (0,0))

    txt_surf = font3.render(' TOP 10 - SCHWER ', True, RED, GREEN)  # headline
    txt_rect = txt_surf.get_rect(center=(bx//2, 30))
    box.blit(txt_surf, txt_rect)


    # write the top-10 
    for i, entry in enumerate(best):
        txt_surf = font.render(entry[1] + ' - ' + str(entry[0]), True, GREEN)
        txt_rect = txt_surf.get_rect(center=(bx//2, 50*i+120))
        box.blit(txt_surf, txt_rect)

    
 

    
    while True:  # wait for user to acknowledge and return
        screen.blit(box, (0, 0))
        font1x = pygame.font.SysFont('Comic Sans MS', 28, True)
        text1x = font1x.render('SPIELEN', 1, WHITE)
        font2x = pygame.font.SysFont('Comic Sans MS', 28, True)
        text2x = font2x.render('BEENDEN', 1, WHITE)
        font3x = pygame.font.SysFont('Comic Sans MS', 28, True)
        text3x = font3x.render('SPENDEN', 1, WHITE)
        
        
        retry_button = pygame.draw.rect(screen, GREEN,(150,640,150,50))
        font_button = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button = font_button.render('NOCHMAL', 1, WHITE)
        screen.blit(text_button, (153, 646))

        
        
        donate_button = pygame.draw.rect(screen, BLUE,(410,640,150,50))
        font_button2 = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button2 = font_button2.render('SPENDEN', 1, WHITE)
        screen.blit(text_button2, (417, 646))
        
        
        quit_button = pygame.draw.rect(screen, RED,(660,640,150,50))
        font_button3 = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button3 = font_button3.render('BEENDEN', 1, WHITE)
        screen.blit(text_button3, (667, 646))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 640:
                    if pygame.mouse.get_pos()[0] <= 300 and pygame.mouse.get_pos()[1] <= 690:
                        retry()
                if pygame.mouse.get_pos()[0] >= 660 and pygame.mouse.get_pos()[1] >= 640:
                    if pygame.mouse.get_pos()[0] <= 810 and pygame.mouse.get_pos()[1] <= 690:
                        pygame.quit()
                if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 640:
                    if pygame.mouse.get_pos()[0] <= 560 and pygame.mouse.get_pos()[1] <= 690:
                        paypal()
 
    

def enterbox(screen, txt):

    def blink(screen):
        for color in [BLUE, RED, GREEN]:
            pygame.draw.circle(box, color, (872, int(by*0.25)), 30, 0)
            pygame.draw.circle(box, color, (85, int(by*0.25)), 30, 0)
            pygame.draw.rect(box, color, (50, int(by*0.17),855, 10), 0)
            pygame.draw.rect(box, color, (50, int(by*0.32),855, 10), 0)
            screen.blit(box, (0, by//2))
            
       
            pygame.display.flip()
            pygame.time.wait(50)

    def show_name(screen, name):
        pygame.draw.rect(box, WHITE, (190, 150, bx//1.7, 57), 0)
        txt_surf = font.render(name, True, BLACK)
        txt_rect = txt_surf.get_rect(center=(bx//2, int(by*0.25)))
        box.blit(txt_surf, txt_rect)
        screen.blit(box, (0, by//2))
        #screen.blit(box, (0, 0)
        pygame.display.flip()
        
    bx = 960
    by = 720

    # make box
    box = pygame.surface.Surface((bx, by))
    box.fill(GREY)

    txt_surf = font.render(txt, True, BLACK)
    txt_rect = txt_surf.get_rect(center=(bx//2, int(by*0.1)))
    box.blit(txt_surf, txt_rect)

    name = ''
    show_name(screen, name)
    


    # the input-loop
    while True: 
        weiter_button = pygame.draw.rect(box, BLUE,(410,260,150,50))
        font_button = pygame.font.SysFont('Comic Sans MS', 28, True)
        text_button = font_button.render('WEITER', 1, WHITE)
        box.blit(text_button, (426, 265))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 640:
                    if pygame.mouse.get_pos()[0] <= 560 and pygame.mouse.get_pos()[1] <= 690:
                        if len(name) >= 1:
                            return name
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                inkey = event.key
                if inkey in [13, 271]:  # enter/return key
                    if len(name) >= 1:
                        return name
                elif inkey == 8:  # backspace key
                    name = name[:-1]
                elif inkey <= 300:
                    name = name[:10]
                    #if pygame.key.get_mods() & pygame.KMOD_SHIFT and 122 >= inkey >= 97:
                    if pygame.key.get_mods() and 122 >= inkey >= 97:
                        inkey -= 32  # handles CAPITAL input
                    name += chr(inkey)
                    

            

        if name == '':
            blink(screen)
        show_name(screen, name)
        
    
        



def highscore(screen, file_name, your_points):
    high_name, high_score = read_from_file_and_find_highscore(file_name)

    if your_points > high_score:
        your_name = enterbox(screen, 'Neuer Rekord! - Wie ist dein Name?')
    
    elif your_points == high_score:
        your_name = enterbox(screen, 'Sehr gut! - Wie ist dein Name?')
    
    elif your_points < high_score:
        your_name = enterbox(screen, 'Nicht Schlecht! - Wie ist dein Name?')

    if your_name == None or len(your_name) == 0:
        return  # do not update the file unless a name is given

    write_to_file(file_name, your_name, your_points)
    show_top10(screen, file_name)
    return





