#This part of the code is the main game loop.
#It was first seperated from the rest of the code on 21/06/2020 and finally completed on 25/06/2020
#=======================================================================================================================
#these big lines dictate scrapped sections or broken sections of code.
#they were mostly kept in case I needed them later, but mostly permanently scrapped
#as they were just a small quality of life thing more than anything, that ended up not working
#=======================================================================================================================


#it is worth noting that even though it is the same program, as it is a
#seperate file it still requires importing of modules
#for this reason I also just re-declare all constant variables and global variables here
import pygame
import time
import random

#much of this first area where many variables and constants are declared is identical to
#the other file, so check the other file for comments

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
crash_sound.set_volume(0.1)
pygame.mixer.music.load("BackgroundMusic.wav")
pygame.mixer.music.set_volume(0.1)

display_width = 800
display_height = 600

car_width = 24


black = (0,0,0)
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


gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

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
gameIcon = pygame.image.load('CarIcon.png')
roadImg = pygame.image.load('Road.png')
pygame.display.set_icon(gameIcon)
                                      
                                      
pause = False
rightPressed = False
leftPressed = False
gameExit = False
x_change = 0
animCounter = 0
highscore = 0


#highscore had issues when it wasn't pre-defined, so simply setting it as a global and grabbing it here works well
with open("Highscore.txt", mode="r", encoding="utf-8") as highscoreFile:
        for eachLine in highscoreFile:
            highscore = eachLine

#text_objects helps to format text throughout the entire project
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def return_menu():
    global pause, gameExit
    pygame.mixer.music.unpause()
    #constantly calling the functions of the games causes the game to keep having to cache and store in memory
    #where the code was up to, which is innefficent. Hence, here I have simply made the loops no longer active
    #by setting the boolean's to the opposite value
    pause = False
    gameExit = True


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def quitgame():
    #make sure to de-initialise pygame first, else it sits in memory and users get upset
    pygame.quit()
    quit()
    

#this button function is the most modularised function in the code. It works for ALL buttons in the code
#it's now quite different to the tutorial code due to me wanting image files rather than color drawing for buttons
def button(x,y,w,h,ai,ii,action=None):
    #mouse.get_pos returns 2 values in iteration, the mouse x coordinate and y coordinate, so we save it to 2 intrinsicly named variables
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #essentially the collision algorithm for the mouse
    if mouse_x >= x and mouse_x <= x+w and mouse_y >= y and mouse_y <= y+h:
        gameDisplay.blit(ai, (x,y))
        if click[0] == 1 and action != None:
            action()
    #this else sets the inactive button sprite when the mouse is not over the button
    else:
        gameDisplay.blit(ii, (x,y))


def paused():

    #the buttons in this function are the reason why pause is a global variable
    #parsing variables through buttons is a huge pain in the neck, so instead just use globals
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

        #button(x,y,w,h,ai,ii,action=None)      old code
        button(150,450,100,50,button_active_back,button_inactive_back,unpause)
        button(550,450,100,50,button_active_quit,button_inactive_quit,quitgame)
        button(350,450,100,50,button_active_menu,button_inactive_menu,return_menu)
        
        pygame.display.update()
        clock.tick(15)
        

def car(x,y):       #animation code from https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
    global animCounter
    gameDisplay.blit(carImg[int(animCounter/4)],(x,y))
    animCounter += 1
    
    if animCounter >= 20:
        animCounter = 0

    #this code works by counting the frames the car has been drawn for, and then dividing it by a set amount and
    #setting the picture displayed to that index in the list


#message_display is only used for major pieces of text, such as the title or pause screens
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    #time.sleep serves 2 purposes here. The first is to make the crash sound effect line up with the pause
    #and second reason: reduce resource usage when it really doesn't need to be high
    time.sleep(3.5)
    
#this function just gets given the current object details and draws it
def objs(objx, objy, objw, objh, color):
    pygame.draw.rect(gameDisplay, color, [objx, objy, objw, objh])


#this is the first of the functions which could not be modularised at the time to due to lack of understanding.
    #if I had my time again, I would modularise this by passing a string var with the name of the required file
    #stored, which could then be read and the function could pass back to each game rather than my approach here
    #which is to have a function per level
def highscore_update(dodged):
        
    with open("Highscore.txt", mode="r", encoding="utf-8") as highscoreFile:
        for eachLine in highscoreFile:
            highscore_in_file = eachLine
    
    if dodged > int(highscore_in_file):
        with open("Highscore.txt", mode="w", encoding="utf-8") as highscoreFile:
            highscoreFile.write('{}'.format(dodged))



#no point parsing highscore into this function seeing as it's global
def scores_draw(count):

    global highscore
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    highscoreTxt = font.render("Highscore: "+str(highscore), True, black)
    #you could modularise this in a way which allows the user to chose stuff like text colour
    
    #make sure to draw the score last so that it doesn't get overlapped
    gameDisplay.blit(text, (0,0))
    gameDisplay.blit(highscoreTxt, (0,26))



#=======================================================================================================================
#=======================================================================================================================

    #Another one of the modules that was meant to be callable by all functions that simply did not work.

##def obj_end(dodged,obj_starty,obj_startx,obj_height,obj_width,obj_speed,display_height):
##    
##    if obj_starty > display_height:
##            obj_starty = 0 - obj_height
##            obj_startx = random.randrange(0, display_width)
##            dodged += 1
##            
##            if obj_speed < 12:
##                obj_speed += 1
##                
##            if obj_width < 200:
##                obj_width += (dodged *1.2)

#=======================================================================================================================
#=======================================================================================================================

def crash():
    global x_change
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('You Crashed')

    #we need to reset x_change else the car will keep moving after crashing with the speed it had prior
    x_change = 0
    game_loop()
    #constantly just calling the function again is bad practise, but for small projects like this its okay


#=======================================================================================================================    
#=======================================================================================================================

    #similar idea to the module above and below. Just wanted to modularise a section of code to be reused,
    #maybe with more work they all would have worked, but I spent too long on them for no result. So they
    #were scrapped

##def collision(x,y,dodged,display_width,display_height,car_width,obj_starty,obj_startx,obj_height,obj_width,obj_speed):
##    #collision with side of screen
##    if x > display_width - car_width or x < 0:
##        highscore_update(dodged)
##        crash()
##
##    #checks for collision with the object
##    if y < obj_starty + obj_height and y > obj_starty:
##        if x > obj_startx and x < obj_startx + obj_width:
##            highscore_update(dodged)
##            crash()
##        elif x + car_width > obj_startx and x + car_width < obj_startx+obj_width:
##            highscore_update(dodged)
##            crash()
#=======================================================================================================================
#=======================================================================================================================    

    #this function was supposed to be the modularised movement function. The idea was to save heaps of lines of code
    #as well as just generally making the code easier to follow by having all the levels call this function
    #which would also allow for easy variation of acceleration and max speed
    
##def movement(x_change,acceleration,max_speed,x):
##
##    global leftPressed, rightPressed
##    
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            quit()
##            
##        elif event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                leftPressed = True
##            if event.key == pygame.K_RIGHT:
##                rightPressed = True
##            if event.key == pygame.K_p:
##                pause = True
##                paused()
##
##        #check if arrow is released and set var to false
##        elif event.type == pygame.KEYUP:
##            if event.key == pygame.K_LEFT:
##                leftPressed = False
##            if event.key == pygame.K_RIGHT:
##                rightPressed = False
##            
##    #acceleration and deceleration system
##    if leftPressed == True and rightPressed == True:
##        print("Both Pressed")
##        if x_change > 0:
##            if (x_change - acceleration) > 0:
##                x_change = x_change - acceleration
##            else:
##                x_change = 0
##
##        elif x_change < 0:
##            if (x_change + acceleration) < 0:
##                x_change = x_change + acceleration
##            else:
##                x_change = 0
##            
##
##    elif leftPressed == True:
##        print("Left Pressed")
##        x_change = x_change - acceleration
##        if x_change < (-1*max_speed):
##            x_change = -1*max_speed
##
##    elif rightPressed == True:
##        print("Right Pressed")
##        x_change += acceleration
##        if x_change > max_speed:
##            x_change = max_speed
##
##    elif x_change != 0:
##        if x_change < 0:
##            if (x_change + acceleration) < 0: 
##                x_change = max_speed + acceleration
##            else:
##                x_change = 0
##
##        elif x_change > 0:
##            if (x_change - acceleration) > 0:
##                x_change = max_speed - acceleration
##            else:
##                x_change = 0
##
##        else:
##            print("nothing")
##            x_change = 0
##                
##    x += x_change
    
#=======================================================================================================================
#=======================================================================================================================

    
def game_loop():

    #please note that this function has a few sections commented out as they were attempts at modularising
    #that piece of code. Those modules can be seen above (commented out)
    #they were kept as a form of documentation

    global pause, x_change, highscore, leftPressed, rightPressed, gameExit
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
    #originally acceleration and deceleration where the same variable, but having them seperate basicly allows control over the "grip" the level puts on the vehicle
    acceleration = 0.4
    deceleration = 0.4
    max_speed = 9

    #retrives highscore from file so it can be drawn later
    with open("Highscore.txt", mode="r", encoding="utf-8") as highscoreFile:
        for eachLine in highscoreFile:
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
                    paused()

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
        gameDisplay.blit(roadImg,(0,0))

        #obj defines block.
        objs(obj_startx, obj_starty, obj_width, obj_height, blue)
        obj_starty += obj_speed
        car(x,y)
        scores_draw(dodged)

##        collision(x,y,dodged,display_width,display_height,car_width,obj_starty,obj_startx,obj_height,obj_width,obj_speed)
##        obj_end(dodged,obj_starty,obj_startx,obj_height,obj_width,obj_speed,display_height)

        #collision with side of screen
        if x > display_width - car_width or x < 0:
            highscore_update(dodged)
            crash()

        #checks for collision with the object
        if y < obj_starty + obj_height and y > obj_starty:
            if x > obj_startx and x < obj_startx + obj_width:
                highscore_update(dodged)
                crash()
            elif x + car_width > obj_startx and x + car_width < obj_startx+obj_width:
                highscore_update(dodged)
                crash()

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


