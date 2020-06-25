#Adam Burwood - Much of this code is taken from a tutorial and therefore is NOT my original code
#Project begun on 18-June-2020 and finished on 25-June-2020
#please note the included wav file with the tutorial was the wrong bit size, had to change it to make it work

#import the module and main game loop
#note that importing is not iterable, so they must all be seperate lines
import pygame
import time
import random
from GameCode import game_loop
from GameCode import text_objects
from GameCode import unpause
from GameCode import quitgame
from GameCode import button
from GameCode import paused
from GameCode import car
from GameCode import message_display
from GameCode import objs
from GameCode import highscore_update
from GameCode import scores_draw
from GameCode import crash
##from GameCode import collision
##from GameCode import movement


#intialise pygame
pygame.init()

#size Variables
display_width = 800
display_height = 600
car_width = 24

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

crash_sound = pygame.mixer.Sound("crash.wav")
crash_sound.set_volume(0.1)
pygame.mixer.music.load("BackgroundMusic.wav")
pygame.mixer.music.set_volume(0.1)
#MUSIC WAS FOUND AND DOWNLOADED FROM https://www.fesliyanstudios.com/royalty-free-music/downloads-c/8-bit-music/6


#Define the colours (RGB values)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)
aqua = (0,255,255)
pink = (201,65,173)
light_pink = (247,124,223)
gold = (255,215,0)
silver = (192,192,192)
black = (0,0,0)


#these need to be loaded in both files as both directly call these variables
#you could place them in a module and run it automatically, but that's a silly and annoying solution
button_active_go = pygame.image.load('GoButtonActive.png')
button_inactive_go = pygame.image.load('GoButtonInactive.png')
button_active_quit = pygame.image.load('QuitButtonActive.png')
button_inactive_quit = pygame.image.load('QuitButtonInactive.png')
button_active_help = pygame.image.load('HelpButtonActive.png')
button_inactive_help = pygame.image.load('HelpButtonInactive.png')
button_active_levels = pygame.image.load('LevelsButtonActive.png')
button_inactive_levels = pygame.image.load('LevelsButtonInactive.png')
button_active_back = pygame.image.load('BackButtonActive.png')
button_inactive_back = pygame.image.load('BackButtonInactive.png')
button_active_menu = pygame.image.load('MenuButtonActive.png')
button_inactive_menu = pygame.image.load('MenuButtonInactive.png')

carImg = [pygame.image.load('racer.png'), pygame.image.load('racer2.png'), pygame.image.load('racer3.png'), pygame.image.load('racer4.png'), pygame.image.load('racer5.png')]
stormImg = [pygame.image.load('DesertStorm.png'), pygame.image.load('DesertStorm2.png'), pygame.image.load('DesertStorm3.png')]
boatImg = [pygame.image.load('boat.png'), pygame.image.load('boat2.png'), pygame.image.load('boat3.png')]
gameIcon = pygame.image.load('CarIcon.png')
roadImg = pygame.image.load('Road.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption('A Wild Ride')
kangImg = pygame.image.load('Kangaroo.png')


#these are the images only needed by this file
button_active_desert = pygame.image.load('DesertButtonActive.png')
button_inactive_desert = pygame.image.load('DesertButtonInactive.png')
button_active_snow = pygame.image.load('SnowButtonActive.png')
button_inactive_snow = pygame.image.load('SnowButtonInactive.png')
button_active_ocean = pygame.image.load('OceanButtonActive.png')
button_inactive_ocean = pygame.image.load('OceanButtonInactive.png')
button_active_country = pygame.image.load('CountryButtonActive.png')
button_inactive_country = pygame.image.load('CountryButtonInactive.png')

oceanImg = pygame.image.load('OceanBackground.png')
countryImg = pygame.image.load('CountryBackground.png')
snowImg = pygame.image.load('SnowBackground.png')
desertImg = pygame.image.load('DesertBackground.png')


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.mixer.music.set_volume(0.1)
clock = pygame.time.Clock()

pause = False
rightPressed = False
leftPressed = False
gameExit = False
x_change = 0
animCounter = 0
animCounterStorm = 0
highscore = 0
    

def return_menu_mainFile():
    global pause, gameExit, x_change
    pygame.mixer.music.unpause()
    pause = False
    gameExit = True
    #if you don't reset x_change the next game you load has its speed carried over
    x_change = 0


def game_help():
    
    help_ = True

    while help_:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(pink)


        #purely using division/multiplication in the positioning is really annoying
        #but python didn't work when I used addition so I used this instead
        #basicly treat it as a ratio to get the position right

        #python string formatting didn't seem to work at all when I tired it alongside the text surface
        #and blit in pygame, so I just decided to declare each of them seperately and then
        #blit them each seperately
        smallText_one = pygame.font.Font('freesansbold.ttf',23)
        helpText_one_one = ("Begin by hitting the 'GO!'")
        helpText_one_two = ("Button on the menu! This will")
        helpText_one_three = ("get you into the game trying")
        helpText_one_four = ("for a high score!")
        helpText_one_five = ("Be careful to dodge the")
        helpText_one_six = ("objects that come your way!")
        helpText_one_seven = ("Press the 'Levels' button to")
        helpText_one_eight = ("go the the levels menu!")
        
        TextSurf, TextRect = text_objects(helpText_one_one, smallText_one)
        TextRect.center = (((display_width/8)*2), (display_height/16))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_one_two, smallText_one)
        TextRect.center = (((display_width/8)*2), (display_height/16)*2)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_one_three, smallText_one)
        TextRect.center = (((display_width/8)*2), (display_height/16)*3)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_one_four, smallText_one)
        TextRect.center = (((display_width/8)*2), (display_height/16)*4)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_one_five, smallText_one)
        TextRect.center = (((display_width/8)*2), (display_height/16)*5)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_one_six, smallText_one)
        TextRect.center = (((display_width/8)*2), (display_height/16)*6)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_one_seven, smallText_one)
        TextRect.center = (((display_width/8)*2), (display_height/16)*7)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_one_eight, smallText_one)
        TextRect.center = (((display_width/8)*2), (display_height/16)*8)
        gameDisplay.blit(TextSurf, TextRect)

        smallText_two = pygame.font.Font('freesansbold.ttf',23)

        helpText_two_one = ("Use the left and right arrow")
        helpText_two_two = ("keys to move the car!")
        helpText_two_three = ("To pause at any time,")
        helpText_two_four = ("press 'p'!")
        helpText_two_five = ("In the levels menu, you will")
        helpText_two_six = ("find a bunch of bonus levels")
        helpText_two_seven = ("with special features!")
        helpText_two_eight = ("Don't forget, have fun!")
        
        TextSurf, TextRect = text_objects(helpText_two_one, smallText_two)
        TextRect.center = (((display_width/8)*6), (display_height/16))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_two_two, smallText_two)
        TextRect.center = (((display_width/8)*6), (display_height/16)*2)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_two_three, smallText_two)
        TextRect.center = (((display_width/8)*6), (display_height/16)*3)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_two_four, smallText_two)
        TextRect.center = (((display_width/8)*6), (display_height/16)*4)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_two_five, smallText_two)
        TextRect.center = (((display_width/8)*6), (display_height/16)*5)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_two_six, smallText_two)
        TextRect.center = (((display_width/8)*6), (display_height/16)*6)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_two_seven, smallText_two)
        TextRect.center = (((display_width/8)*6), (display_height/16)*7)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(helpText_two_eight, smallText_two)
        TextRect.center = (((display_width/8)*6), (display_height/16)*8)
        gameDisplay.blit(TextSurf, TextRect)
        
        
        button(100,450,100,50,button_active_back,button_inactive_back,game_intro)
        button(600,450,100,50,button_active_quit,button_inactive_quit,quitgame)
        
        pygame.display.update()
        clock.tick(15)


def storm(x,y):       #animation code from https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
    global animCounterStorm
    gameDisplay.blit(stormImg[int(animCounterStorm/3)],(x,y))
    animCounterStorm += 1
    
    if animCounterStorm >= 9:
        animCounterStorm = 0


def unpause_desert():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused_desert():

    global pause
    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause_desert()
        
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        #button(x,y,w,h,ai,ii,action=None)
        button(150,450,100,50,button_active_back,button_inactive_back,unpause)
        button(550,450,100,50,button_active_quit,button_inactive_quit,quitgame)
        button(350,450,100,50,button_active_menu,button_inactive_menu,return_menu_mainFile)
        
        pygame.display.update()
        clock.tick(15)


def crash_desert():
    
    global x_change
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('You Crashed')
    
    #we need to reset x_change else the car will keep moving after crashing with the speed it had prior
    x_change = 0
    game_desert()


def desert_highscore_update(dodged):
    
    with open("HighscoreDesert.txt", mode="r", encoding="utf-8") as highscoreFileDesert:
        for eachLine in highscoreFileDesert:
            highscore_in_fileDesert = eachLine
    
    if dodged > int(highscore_in_fileDesert):
        with open("HighscoreDesert.txt", mode="w", encoding="utf-8") as highscoreFileDesert:
            highscoreFileDesert.write('{}'.format(dodged))


def desert_scores_draw(count):

    global highscore
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    highscoreTxt = font.render("Highscore: "+str(highscore), True, black)
    
    #make sure to draw the score last so that it doesn't get overlapped
    gameDisplay.blit(text, (0,0))
    gameDisplay.blit(highscoreTxt, (0,26))



def game_desert():
    global pause, x_change, highscore, leftPressed, rightPressed, gameExit
    highscore = 0
    pygame.mixer.music.play(-1)  #positive counts the music will run that many times, -1 is indefinately
    x = (display_width * 0.45)
    y = (display_height * 0.8)


    #adjusting start y changes how long it will take to see the object
    obj_startx = random.randrange(0, display_width)
    obj_starty = -600
    obj_speed = 3
    obj_width = 100
    obj_height = 100

    dodged = 0
    acceleration = 0.4
    deceleration = 0.4
    max_speed = 9

    #retrives highscore from file so it can be drawn later
    with open("HighscoreDesert.txt", mode="r", encoding="utf-8") as highscoreFileDesert:
        for eachLine in highscoreFileDesert:
            highscore = eachLine

    gameExit = False
    

# THIS IS THE EVENT HANDLER
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #a section of this next bit of code was modified after being ripped from https://gamedev.stackexchange.com/questions/54841/rpg-movement-holding-down-button
            #check if arrow is pressed and set var to true
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftPressed = True
                if event.key == pygame.K_RIGHT:
                    rightPressed = True
                if event.key == pygame.K_p:
                    pause = True
                    paused_desert()

            #check if arrow is released and set var to false
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftPressed = False
                if event.key == pygame.K_RIGHT:
                    rightPressed = False
            
        #acceleration and deceleration system
        if leftPressed == True and rightPressed == True:
            if x_change > 0:
                if (x_change - deceleration) > 0:
                    x_change -= deceleration
                else:
                    x_change = 0

            elif x_change < 0:
                if (x_change + deceleration) < 0:
                    x_change += deceleration
                else:
                    x_change = 0

        elif leftPressed == True:
            x_change -= acceleration
            if x_change < (-1*max_speed):
                x_change = (-1*max_speed)

        elif rightPressed == True:
            x_change += acceleration
            if x_change > max_speed:
                x_change = max_speed

        elif x_change != 0:
            #failsafe, ensures they don't stay on when they shouldn't be
            leftPressed = False
            rightPressed = False
            if x_change < 0:
                if (x_change + deceleration) < 0: 
                    x_change += deceleration
                else:
                    x_change = 0

            elif x_change > 0:
                if (x_change - deceleration) > 0:
                    x_change -= deceleration
                else:
                    x_change = 0

            else:
                x_change = 0
                
        x += x_change

        #just to give that small satisfaction of watching the highscore rise as you play
        if dodged > int(highscore):
             highscore = dodged
            

        #changes colour of entire window (overwrites previously drawn objs)
        #gameDisplay.fill(white)
        gameDisplay.blit(desertImg,(0,0))

        #obj defines block.
        objs(obj_startx, obj_starty, obj_width, obj_height, gold)
        obj_starty += obj_speed
        car(x,y)
        storm(0,0)
        desert_scores_draw(dodged)

##        collision(x,y,dodged,display_width,display_height,car_width,obj_starty,obj_startx,obj_height,obj_width,obj_speed)
##        obj_end(dodged,obj_starty,obj_startx,obj_height,obj_width,obj_speed,display_height)

        #collision with side of screen
        if x > display_width - car_width or x < 0:
            desert_highscore_update(dodged)
            desert_crash()

        #checks for collision with the object
        if y < obj_starty + obj_height and y > obj_starty:
            if x > obj_startx and x < obj_startx + obj_width:
                desert_highscore_update(dodged)
                crash_desert()
            elif x + car_width > obj_startx and x + car_width < obj_startx+obj_width:
                desert_highscore_update(dodged)
                crash_desert()

        if obj_starty > display_height:
            obj_starty = 0 - obj_height
            obj_startx = random.randrange(0, display_width)
            dodged += 1
            
            if obj_speed < 14:
                obj_speed += 1
                
            if (obj_width + dodged*1.2) < 240:
                obj_width += (dodged *1.2)
                
            else:
                obj_width = 240
            
        
    #   only updates changes if given a paramater, however with no paramater
    #   it will still update the whole panel. .flip also exists but is
    #   apparently useless
        pygame.display.update()

        #actually sets the framerate
        clock.tick(60)


def unpause_snow():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused_snow():

    global pause
    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
        
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        #button(x,y,w,h,ai,ii,action=None)
        button(150,450,100,50,button_active_back,button_inactive_back,unpause_snow)
        button(550,450,100,50,button_active_quit,button_inactive_quit,quitgame)
        button(350,450,100,50,button_active_menu,button_inactive_menu,return_menu_mainFile)
        
        pygame.display.update()
        clock.tick(15)


def crash_snow():
    
    global x_change
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('You Crashed')
    
    #we need to reset x_change else the car will keep moving after crashing with the speed it had prior
    x_change = 0
    game_snow()


def snow_highscore_update(dodged):
    
    with open("HighscoreSnow.txt", mode="r", encoding="utf-8") as highscoreFileSnow:
        for eachLine in highscoreFileSnow:
            highscore_in_fileSnow = eachLine
    
    if dodged > int(highscore_in_fileSnow):
        with open("HighscoreSnow.txt", mode="w", encoding="utf-8") as highscoreFileSnow:
            highscoreFileSnow.write('{}'.format(dodged))


def snow_scores_draw(count):

    global highscore
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    highscoreTxt = font.render("Highscore: "+str(highscore), True, black)
    
    #make sure to draw the score last so that it doesn't get overlapped
    gameDisplay.blit(text, (0,0))
    gameDisplay.blit(highscoreTxt, (0,26))



def game_snow():
    
    global pause, x_change, highscore, leftPressed, rightPressed, gameExit
    #have to reset the highscore to make sure it's not carried over from a different game
    highscore = 0
    
    pygame.mixer.music.play(-1)  #positive counts the music will run that many times, -1 is indefinately
    x = (display_width * 0.45)
    y = (display_height * 0.8)


    #adjusting start y changes how long it will take to see the object
    obj_startx = random.randrange(0, display_width)
    obj_starty = -600
    obj_speed = 3
    obj_width = 100
    obj_height = 100

    dodged = 0
    acceleration = 0.6
    deceleration = 0.05
    max_speed = 10

    #retrives highscore from file so it can be drawn later
    with open("HighscoreSnow.txt", mode="r", encoding="utf-8") as highscoreFileSnow:
        for eachLine in highscoreFileSnow:
            highscore = eachLine

    gameExit = False
    

# THIS IS THE EVENT HANDLER
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #a section of this next bit of code was modified after being ripped from https://gamedev.stackexchange.com/questions/54841/rpg-movement-holding-down-button
            #check if arrow is pressed and set var to true
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftPressed = True
                if event.key == pygame.K_RIGHT:
                    rightPressed = True
                if event.key == pygame.K_p:
                    pause = True
                    paused_snow()

            #check if arrow is released and set var to false
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftPressed = False
                if event.key == pygame.K_RIGHT:
                    rightPressed = False
            
        #acceleration and deceleration system
        if leftPressed == True and rightPressed == True:
            if x_change > 0:
                if (x_change - deceleration) > 0:
                    x_change -= deceleration
                else:
                    x_change = 0

            elif x_change < 0:
                if (x_change + deceleration) < 0:
                    x_change += deceleration
                else:
                    x_change = 0

        elif leftPressed == True:
            x_change -= acceleration
            if x_change < (-1*max_speed):
                x_change = (-1*max_speed)

        elif rightPressed == True:
            x_change += acceleration
            if x_change > max_speed:
                x_change = max_speed

        elif x_change != 0:
            #failsafe, ensures they don't stay on when they shouldn't be
            leftPressed = False
            rightPressed = False
            if x_change < 0:
                if (x_change + deceleration) < 0: 
                    x_change += deceleration
                else:
                    x_change = 0

            elif x_change > 0:
                if (x_change - deceleration) > 0:
                    x_change -= deceleration
                else:
                    x_change = 0

            else:
                x_change = 0
                
        x += x_change

        #just to give that small satisfaction of watching the highscore rise as you play
        if dodged > int(highscore):
             highscore = dodged
            

        #changes colour of entire window (overwrites previously drawn objs)
        #gameDisplay.fill(white)
        gameDisplay.blit(snowImg,(0,0))

        #obj defines block.
        objs(obj_startx, obj_starty, obj_width, obj_height, blue)
        obj_starty += obj_speed
        car(x,y)
        snow_scores_draw(dodged)

##        collision(x,y,dodged,display_width,display_height,car_width,obj_starty,obj_startx,obj_height,obj_width,obj_speed)
##        obj_end(dodged,obj_starty,obj_startx,obj_height,obj_width,obj_speed,display_height)

        #collision with side of screen
        if x > display_width - car_width or x < 0:
            snow_highscore_update(dodged)
            crash_snow()

        #checks for collision with the object
        if y < obj_starty + obj_height and y > obj_starty:
            if x > obj_startx and x < obj_startx + obj_width:
                snow_highscore_update(dodged)
                crash_snow()
            elif x + car_width > obj_startx and x + car_width < obj_startx+obj_width:
                snow_highscore_update(dodged)
                crash_snow()

        if obj_starty > display_height:
            obj_starty = 0 - obj_height
            obj_startx = random.randrange(0, display_width)
            dodged += 1
            
            if obj_speed < 14:
                obj_speed += 1
                
            if (obj_width + dodged*1.2) < 240:
                obj_width += (dodged *1.2)
                
            else:
                obj_width = 240
            
        
    #   only updates changes if given a paramater, however with no paramater
    #   it will still update the whole panel. .flip also exists but is
    #   apparently useless
        pygame.display.update()

        #actually sets the framerate
        clock.tick(60)


def unpause_country():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused_country():

    global pause
    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
        
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        #button(x,y,w,h,ai,ii,action=None)
        button(150,450,100,50,button_active_back,button_inactive_back,unpause_country)
        button(550,450,100,50,button_active_quit,button_inactive_quit,quitgame)
        button(350,450,100,50,button_active_menu,button_inactive_menu,return_menu_mainFile)
        
        pygame.display.update()
        clock.tick(15)


def crash_country():
    
    global x_change
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('You Crashed')
    
    #we need to reset x_change else the car will keep moving after crashing with the speed it had prior
    x_change = 0
    game_country()


def country_highscore_update(dodged):
    
    with open("HighscoreCountry.txt", mode="r", encoding="utf-8") as highscoreFileCountry:
        for eachLine in highscoreFileCountry:
            highscore_in_fileCountry = eachLine
    
    if dodged > int(highscore_in_fileCountry):
        with open("HighscoreCountry.txt", mode="w", encoding="utf-8") as highscoreFileCountry:
            highscoreFileCountry.write('{}'.format(dodged))


def country_scores_draw(count):

    global highscore
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    highscoreTxt = font.render("Highscore: "+str(highscore), True, black)
    
    #make sure to draw the score last so that it doesn't get overlapped
    gameDisplay.blit(text, (0,0))
    gameDisplay.blit(highscoreTxt, (0,26))


def objs_country(objx, objy, objw, objh, obj_count, objx_speed, color):

    #basicly checks if the object has gone off screen yet before allowing a different random number to generate
    #this is important, else the direction of the animal will change too often
    #this random thing essentially every time the object is spawned randomly decides which direction
    #it will start moving in

    #original algorithm
##    if obj_count == 0:
##        randNum = random.randint(1,2)
##    if randNum == 1:
##        objx_speed = 3
##    elif randNum == 0:
##        objx_speed = -3
##    obj_count = 1

    if obj_count == 0:
        randNum = random.randint(1,2)

    if randNum == 1:
        objx_speed = objx_speed * (-1)
        obj_count = 1
        
    gameDisplay.blit(kangImg, (objx,objy))
##    pygame.draw.rect(gameDisplay, color, [objx, objy, objw, objh])
    return objx
    return objx_speed


def game_country():
    
    global pause, x_change, highscore, leftPressed, rightPressed, gameExit
    highscore = 0
    pygame.mixer.music.play(-1)  #positive counts the music will run that many times, -1 is indefinately
    x = (display_width * 0.45)
    y = (display_height * 0.8)


    #adjusting start y changes how long it will take to see the object
    obj_startx = random.randrange(100, (display_width-100))
    obj_starty = -600
    obj_speed = 3
    obj_width = 78
    obj_height = 85
    obj_count = 0
    objx_speed = 6

    dodged = 0
    acceleration = 0.4
    deceleration = 0.4
    max_speed = 9

    #retrives highscore from file so it can be drawn later
    with open("HighscoreCountry.txt", mode="r", encoding="utf-8") as highscoreFileCountry:
        for eachLine in highscoreFileCountry:
            highscore = eachLine

    gameExit = False
    

# THIS IS THE EVENT HANDLER
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftPressed = True
                if event.key == pygame.K_RIGHT:
                    rightPressed = True
                if event.key == pygame.K_p:
                    pause = True
                    paused_country()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftPressed = False
                if event.key == pygame.K_RIGHT:
                    rightPressed = False
            
        if leftPressed == True and rightPressed == True:
            if x_change > 0:
                if (x_change - deceleration) > 0:
                    x_change -= deceleration
                else:
                    x_change = 0

            elif x_change < 0:
                if (x_change + deceleration) < 0:
                    x_change += deceleration
                else:
                    x_change = 0

        elif leftPressed == True:
            x_change -= acceleration
            if x_change < (-1*max_speed):
                x_change = (-1*max_speed)

        elif rightPressed == True:
            x_change += acceleration
            if x_change > max_speed:
                x_change = max_speed

        elif x_change != 0:
            leftPressed = False
            rightPressed = False
            if x_change < 0:
                if (x_change + deceleration) < 0: 
                    x_change += deceleration
                else:
                    x_change = 0

            elif x_change > 0:
                if (x_change - deceleration) > 0:
                    x_change -= deceleration
                else:
                    x_change = 0

            else:
                x_change = 0
                
        x += x_change

        if dodged > int(highscore):
             highscore = dodged

        gameDisplay.blit(countryImg,(0,0))
        
        objs_country(obj_startx, obj_starty, obj_width, obj_height,obj_count, objx_speed, blue)
        obj_starty += obj_speed
        obj_startx += objx_speed
        car(x,y)
        country_scores_draw(dodged)

        if x > display_width - car_width or x < 0:
            country_highscore_update(dodged)
            crash_country()

        if y < obj_starty + obj_height and y > obj_starty:
            if x > obj_startx and x < obj_startx + obj_width:
                country_highscore_update(dodged)
                crash_country()
            elif x + car_width > obj_startx and x + car_width < obj_startx+obj_width:
                country_highscore_update(dodged)
                crash_country()

        if obj_starty > display_height:
            obj_starty = 0 - obj_height
            obj_startx = random.randrange(100, (display_width-100))
            dodged += 1
            obj_count = 0
            
            if obj_speed < 14:
                obj_speed += 1


                #commented out this code as I don't want the the object to get larger than the image
##            if (obj_width + dodged*1.2) < 240:
##                obj_width += (dodged *1.2)
##                
##            else:
##                obj_width = 240

        #this next check is exclusive to this level, as it checks for the animal "screen wall bounce"
        #(ensures that the objects come back the other direction if they hit the edge of the screen)
        #values deliberately larger than just the edge to avoid a weird look

        if obj_startx <= 25 or obj_startx >= (display_width - 25):
            #simply multiplying by -1 inverts positive/negative value
            #aka changes direction
            objx_speed = objx_speed*(-1)

            
        pygame.display.update()

        clock.tick(60)
        

def boat(x,y):       #animation code from https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
    global animCounter
    gameDisplay.blit(boatImg[int(animCounter/3)],(x,y))
    animCounter += 1
    
    if animCounter >= 9:
        animCounter = 0


def unpause_ocean():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def ocean_paused():

    global pause
    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
        
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        #button(x,y,w,h,ai,ii,action=None)
        button(150,450,100,50,button_active_back,button_inactive_back,unpause_ocean)
        button(550,450,100,50,button_active_quit,button_inactive_quit,quitgame)
        button(350,450,100,50,button_active_menu,button_inactive_menu,return_menu_mainFile)
        
        pygame.display.update()
        clock.tick(15)


def crash_ocean():
    global x_change
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('You Crashed')
    
    #we need to reset x_change else the car will keep moving after crashing with the speed it had prior
    x_change = 0
    game_ocean()


def scores_draw_ocean(count):

    global highscore
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    highscoreTxt = font.render("Highscore: "+str(highscore), True, black)
    
    #make sure to draw the score last so that it doesn't get overlapped
    gameDisplay.blit(text, (0,0))
    gameDisplay.blit(highscoreTxt, (0,26))


def ocean_highscore_update(dodged):
    
    with open("HighscoreOcean.txt", mode="r", encoding="utf-8") as highscoreFileOcean:
        for eachLine in highscoreFileOcean:
            highscore_in_Oceanfile = eachLine
    
    if dodged > int(highscore_in_Oceanfile):
        with open("HighscoreOcean.txt", mode="w", encoding="utf-8") as highscoreFileOcean:
            highscoreFileOcean.write('{}'.format(dodged))

            

def game_ocean():
    global pause, x_change, highscore, leftPressed, rightPressed, gameExit
    highscore = 0
    pygame.mixer.music.play(-1)  #positive counts the music will run that many times, -1 is indefinately
    x = (display_width * 0.45)
    y = (display_height * 0.8)


    #adjusting start y changes how long it will take to see the object
    obj_startx = random.randrange(0, display_width)
    obj_starty = -350
    obj_speed = 3
    obj_width = 100
    obj_height = 250

    dodged = 0

    #retrives highscore from file so it can be drawn later
    with open("HighscoreOcean.txt", mode="r", encoding="utf-8") as highscoreFileOcean:
        for eachLine in highscoreFileOcean:
            highscore = eachLine

    gameExit = False
    

# THIS IS THE EVENT HANDLER
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftPressed = True
                if event.key == pygame.K_RIGHT:
                    rightPressed = True
                if event.key == pygame.K_p:
                    pause = True
                    ocean_paused()

            #check if arrow is released and set var to false
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftPressed = False
                if event.key == pygame.K_RIGHT:
                    rightPressed = False

            if leftPressed == True and rightPressed == True:
                x_change = 0
                
            elif leftPressed == True:
                x_change = -8
                
            elif rightPressed == True:
                x_change = 8
                
            else:
                x_change = 0
            
                
        x += x_change

        #just to give that small satisfaction of watching the highscore rise as you play
        if dodged > int(highscore):
             highscore = dodged
            

        #changes colour of entire window (overwrites previously drawn objs)
        #gameDisplay.fill(white)
        gameDisplay.blit(oceanImg,(0,0))

        #obj defines block.
        objs(obj_startx, obj_starty, obj_width, obj_height, blue)
        obj_starty += obj_speed
        boat(x,y)
        scores_draw_ocean(dodged)

        #collision with side of screen
        if x > display_width - car_width or x < 0:
            ocean_highscore_update(dodged)
            crash_ocean()

        #checks for collision with the object
        if y < obj_starty + obj_height and y > obj_starty:
            if x > obj_startx and x < obj_startx + obj_width:
                ocean_highscore_update(dodged)
                crash_ocean()
            elif x + car_width > obj_startx and x + car_width < obj_startx+obj_width:
                ocean_highscore_update(dodged)
                crash_ocean()

        if obj_starty > display_height:
            obj_starty = 0 - obj_height
            obj_startx = random.randrange(0, display_width)
            dodged += 1
            
            if obj_speed < 17:
                obj_speed += 1
                
            if (obj_width + dodged*1.2) < 270:
                obj_width += (dodged *1.2)
                
            else:
                obj_width = 270
            
        
    #   only updates changes if given a paramater, however with no paramater
    #   it will still update the whole panel. .flip also exists but is
    #   apparently useless
        pygame.display.update()

        #actually sets the framerate
        clock.tick(60)


def game_levels():
    
    levels = True

    while levels:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(silver)

        #buttons row 1
        button(100,50,100,50,button_active_desert,button_inactive_desert,game_desert)
        button(350,50,100,50,button_active_back,button_inactive_back,game_intro)
        button(600,50,100,50,button_active_snow,button_inactive_snow,game_snow)

        #buttons row 2
        button(100,350,100,50,button_active_country,button_inactive_country,game_country)
        button(600,350,100,50,button_active_ocean,button_inactive_ocean,game_ocean)
        
        pygame.display.update()
        clock.tick(15)


def game_intro():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("A Wild Ride", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        #buttons row 1
        button(150,400,100,50,button_active_go,button_inactive_go,game_loop)
        button(550,400,100,50,button_active_quit,button_inactive_quit,quitgame)

        #buttons row 2
        button(150,500,100,50,button_active_levels,button_inactive_levels,game_levels)
        button(550,500,100,50,button_active_help,button_inactive_help,game_help)
        
        pygame.display.update()
        clock.tick(15)



game_intro()

#de-initialises pygame
pygame.quit()
quit()
