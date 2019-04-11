# ********************************IMPORTS**********************************
import sys, os, random
try:
    import pygame
    from pygame.locals import *
except:
    print('PyGame not installed: https://www.pygame.org/wiki/GettingStarted')


# ********************************VARIABLES**********************************
# initialize windows/canvases
pygame.init()
pygame.display.set_caption('Karl\'s Pizza')
window = pygame.display.set_mode((1000, 500))
canvas = window.copy()
drawingSize = [200, 200]

mouse = pygame.mouse  # get mouse data
_image_library = {}  # loaded images


# ********************************CONSTANTS**********************************
# Colors (r, g, b)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
ORANGE = pygame.Color(255, 106, 0)
YELLOW = pygame.Color(255, 216, 0)
GREEN = pygame.Color(61, 206, 0)
BLUE = pygame.Color(20, 102, 255)
PURPLE = pygame.Color(109, 56, 255)
PINK = pygame.Color(255, 47, 220)
BLACK = pygame.Color(0, 0, 0)
BGCOLOR = pygame.Color(255, 212, 170)
DRAWBORDER = pygame.Color(206, 171, 138)
PIZZACRUST = pygame.Color(209, 169, 111)
SAUCE = pygame.Color(225, 0, 0)
CHEESE = pygame.Color(254, 206, 72)


# ===============================BEGIN CODE==================================
# Program:   	Lesson 7 Exercise 4 - Karl's Pizza
# Definition:   A program that allows the user to draw the pizza base and toppings, generating a great looking pizza!
# Author:  	    Karl Palmer
# History:      4/10/2019 - initial script creation


# 	Procedure:   	newgame
# 	Definition:  	initialize/reset variables for a new game to start
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def newgame():
    global r, baseDrawn, base, topping1Drawn, topping1, topping2Drawn, topping2, topping3Drawn, topping3, topping4Drawn
    global topping4, topping4Drawing, toppings, toppingSizes, toppingPoses, toppingRots, color, size
    baseDrawn = False
    base = pygame.Surface(drawingSize, pygame.SRCALPHA, 32)
    topping1Drawn = False
    topping1 = pygame.Surface(drawingSize, pygame.SRCALPHA, 32)
    topping2Drawn = False
    topping2 = pygame.Surface(drawingSize, pygame.SRCALPHA, 32)
    topping3Drawn = False
    topping3 = pygame.Surface(drawingSize, pygame.SRCALPHA, 32)
    topping4Drawn = False
    topping4 = pygame.Surface(drawingSize, pygame.SRCALPHA, 32)
    topping4Drawing = False
    color = PIZZACRUST
    size = 5

    # # # final pizza setup # # #
    toppings = [topping1, topping2, topping3, topping4, topping1, topping2, topping3, topping4, topping1, topping2,
                topping3, topping4, topping1, topping2, topping3, topping4, topping1, topping2, topping3, topping4]
                # toppings that will be generated on the final pizza

    toppingSizes = []        # [w*h...]
    toppingPoses = [[], []]  # [[x...], [y...]]
    toppingRots = []         # [deg...]

    for i in range(0, len(toppings)):
        toppingSizes.extend([random.randrange(20, 40)])       # get a random w/h
        toppingPoses[0].extend([random.randrange(415, 540)])  # get a random x position
        toppingPoses[1].extend([random.randrange(65, 215)])   # get a random y position
        toppingRots.extend([random.randrange(0, 360)])        # get a random rotation


# 	Procedure:   	get_image
# 	Definition:  	loads directed image
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        try:
            image = pygame.image.load(canonicalized_path)
        except:
            print('image: ' + canonicalized_path + ' could not be found/loaded.')
        _image_library[path] = image
    return image


# 	Procedure:   	nextbutton
# 	Definition:  	detects if mouse clicked on next button and sets current drawing to true so it will go to next one
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def nextbutton(xmin, xmax, ymin, ymax, canvas, canvasname):
    global color, size, baseDrawn, topping1Drawn, topping2Drawn, topping3Drawn, topping4Drawn
    if pygame.mouse.get_pressed()[0] and mouseX > xmin and mouseX < xmax and mouseY > ymin and mouseY < ymax:
        color = BLACK
        if canvasname == "base":
            baseDrawn = True
        elif canvasname == "topping1":
            topping1Drawn = True
        elif canvasname == "topping2":
            topping2Drawn = True
        elif canvasname == "topping3":
            topping3Drawn = True
        elif canvasname == "topping4":
            topping4Drawn = True
        pygame.time.wait(150)  # prevent from clicking the next canvas's next button


# 	Procedure:   	finishbutton
# 	Definition:  	detects if mouse clicked on finish/playagain button and run the newgame method to reset variables
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def finishbutton(xmin, xmax, ymin, ymax):
    global color, size, baseDrawn, topping1Drawn, topping2Drawn, topping3Drawn, topping4Drawn
    if pygame.mouse.get_pressed()[0] and mouseX > xmin and mouseX < xmax and mouseY > ymin and mouseY < ymax:
        newgame()


# 	Procedure:   	colorbutton
# 	Definition:  	detects if mouse clicked on color button and sets the current drawing color to specified color
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def colorbutton(xmin, xmax, ymin, ymax, newcolor):
    global color
    if pygame.mouse.get_pressed()[0] and mouseX > xmin and mouseX < xmax and mouseY > ymin and mouseY < ymax:
        color = newcolor


# 	Procedure:   	sizebutton
# 	Definition:  	detects if mouse clicked on size button and sets the current drawing size to specified size
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def sizebutton(xmin, xmax, ymin, ymax, newsize):
    global size
    if pygame.mouse.get_pressed()[0] and mouseX > xmin and mouseX < xmax and mouseY > ymin and mouseY < ymax:
        size = newsize


# 	Procedure:   	drawingevent
# 	Definition:  	draws a circle at the current mouse position with the current size/color on the specified surface
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def drawingevent(canvas):
    global width, height, size
    pygame.draw.circle(canvas, color, [pygame.mouse.get_pos()[0] - 400, pygame.mouse.get_pos()[1] - 50], size)


# 	Procedure:   	basedrawcolors
# 	Definition:  	draws the buttons for changing colors on the base screen
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def basedrawcolors():
    pygame.draw.rect(window, PIZZACRUST, (462.5, 255, 25, 25))
    colorbutton(462.5, 487.5, 255, 280, PIZZACRUST)
    pygame.draw.rect(window, SAUCE, (487.5, 255, 25, 25))
    colorbutton(487.5, 512.5, 255, 280, SAUCE)
    pygame.draw.rect(window, CHEESE, (512.5, 255, 25, 25))
    colorbutton(512.5, 537.5, 255, 280, CHEESE)
    if color == PIZZACRUST:
        pygame.draw.rect(window, BLACK, (462.5, 283, 25, 3))
    elif color == SAUCE:
        pygame.draw.rect(window, BLACK, (487.5, 283, 25, 3))
    elif color == CHEESE:
        pygame.draw.rect(window, BLACK, (512.5, 283, 25, 3))


# 	Procedure:   	toppingdrawcolors
# 	Definition:  	draws the buttons for changing colors on the topping screens
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def toppingdrawcolors():
    pygame.draw.rect(window, BLACK, (400, 255, 25, 25))
    colorbutton(400, 425, 255, 280, BLACK)
    pygame.draw.rect(window, RED, (425, 255, 25, 25))
    colorbutton(425, 450, 255, 280, RED)
    pygame.draw.rect(window, ORANGE, (450, 255, 25, 25))
    colorbutton(450, 475, 255, 280, ORANGE)
    pygame.draw.rect(window, YELLOW, (475, 255, 25, 25))
    colorbutton(475, 500, 255, 280, YELLOW)
    pygame.draw.rect(window, GREEN, (500, 255, 25, 25))
    colorbutton(500, 525, 255, 280, GREEN)
    pygame.draw.rect(window, BLUE, (525, 255, 25, 25))
    colorbutton(525, 550, 255, 280, BLUE)
    pygame.draw.rect(window, PURPLE, (550, 255, 25, 25))
    colorbutton(550, 575, 255, 280, PURPLE)
    pygame.draw.rect(window, PINK, (575, 255, 25, 25))
    colorbutton(575, 600, 255, 280, PINK)
    if color == BLACK:
        pygame.draw.rect(window, BLACK, (400, 283, 25, 3))
    elif color == RED:
        pygame.draw.rect(window, BLACK, (425, 283, 25, 3))
    elif color == ORANGE:
        pygame.draw.rect(window, BLACK, (450, 283, 25, 3))
    elif color == YELLOW:
        pygame.draw.rect(window, BLACK, (475, 283, 25, 3))
    elif color == GREEN:
        pygame.draw.rect(window, BLACK, (500, 283, 25, 3))
    elif color == BLUE:
        pygame.draw.rect(window, BLACK, (525, 283, 25, 3))
    elif color == PURPLE:
        pygame.draw.rect(window, BLACK, (550, 283, 25, 3))
    elif color == PINK:
        pygame.draw.rect(window, BLACK, (575, 283, 25, 3))


# 	Procedure:   	draw_sizebuttons
# 	Definition:  	draws the buttons for changing drawing size for base and topping screens
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def draw_sizebuttons():
    window.blit(get_image('images/size2.jpg'), (400, 20))
    window.blit(get_image('images/size4.jpg'), (443.75, 20))
    window.blit(get_image('images/size6.jpg'), (487.5, 20))
    window.blit(get_image('images/size8.jpg'), (531.25, 20))
    window.blit(get_image('images/size10.jpg'), (575, 20))
    sizebutton(400, 425, 20, 45, 2)
    sizebutton(443.75, 468.75, 20, 45, 5)
    sizebutton(487.5, 512.5, 20, 45, 10)
    sizebutton(531.25, 556.25, 20, 45, 15)
    sizebutton(575, 600, 20, 45, 20)
    if size == 2:
        pygame.draw.rect(window, BLACK, (400, 14, 25, 3))
    elif size == 5:
        pygame.draw.rect(window, BLACK, (443.75, 14, 25, 3))
    elif size == 10:
        pygame.draw.rect(window, BLACK, (487.5, 14, 25, 3))
    elif size == 15:
        pygame.draw.rect(window, BLACK, (531.25, 14, 25, 3))
    elif size == 20:
        pygame.draw.rect(window, BLACK, (575, 14, 25, 3))


# 	Procedure:   	drawbg
# 	Definition:  	draws the GUI that appears on all screens
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def drawbg(title, button, progress):
    window.fill(BGCOLOR)
    pygame.draw.rect(window, DRAWBORDER, (397, 47, 206, 206))
    pygame.draw.rect(window, WHITE, (400, 50, 200, 200))
    window.blit(get_image('images/Logo.png'), (75, 40))
    window.blit(get_image(title), (690, 80))
    window.blit(get_image(progress), (675, 185))
    window.blit(get_image(button), (384, 335))


# 	Procedure:   	rungame
# 	Definition:  	runs a game frame
# 	Author:  		Karl Palmer
# 	History:        4/10/2019 - Initial Function Creation
def rungame():
    # get mouse x and y positions
    global mouseX, mouseY
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    # drawing the pizza base (crust, sauce, cheese)
    if baseDrawn == False:
        drawbg('images/Title_PizzBase.png', 'images/Done.jpg', 'images/progress_1.png')
        basedrawcolors()
        draw_sizebuttons()
        if pygame.mouse.get_pressed()[0] and mouseX > 400 and mouseX < 600 and mouseY > 50 and mouseY < 250:
            drawingevent(base)
        nextbutton(384, 616, 335, 430, base, 'base')
        window.blit(base, [400, 50])

    # drawing the first pizza topping
    elif not topping1Drawn:
        drawbg('images/Title_Topp1.png', 'images/Done.jpg', 'images/progress_2.png')
        draw_sizebuttons()
        toppingdrawcolors()
        if pygame.mouse.get_pressed()[0] and mouseX > 400 and mouseX < 600 and mouseY > 50 and mouseY < 250:
            drawingevent(topping1)
        nextbutton(384, 616, 335, 430, topping1, 'topping1')
        window.blit(topping1, [400, 50])

    # drawing the second pizza topping
    elif not topping2Drawn:
        drawbg('images/Title_Topp2.png', 'images/Done.jpg', 'images/progress_3.png')
        draw_sizebuttons()
        toppingdrawcolors()
        draw_sizebuttons()
        if pygame.mouse.get_pressed()[0] and mouseX > 400 and mouseX < 600 and mouseY > 50 and mouseY < 250:
            drawingevent(topping2)
        nextbutton(384, 616, 335, 430, topping2, 'topping2')
        window.blit(topping2, [400, 50])

    # drawing the third pizza topping
    elif not topping3Drawn:
        drawbg('images/Title_Topp3.png', 'images/Done.jpg', 'images/progress_4.png')
        draw_sizebuttons()
        toppingdrawcolors()
        draw_sizebuttons()
        if pygame.mouse.get_pressed()[0] and mouseX > 400 and mouseX < 600 and mouseY > 50 and mouseY < 250:
            drawingevent(topping3)
        nextbutton(384, 616, 335, 430, topping3, 'topping3')
        window.blit(topping3, [400, 50])

    # drawing the fourth pizza topping
    elif not topping4Drawn:
        drawbg('images/Title_Topp4.png', 'images/Done.jpg', 'images/progress_5.png')
        draw_sizebuttons()
        toppingdrawcolors()
        if pygame.mouse.get_pressed()[0] and mouseX > 400 and mouseX < 600 and mouseY > 50 and mouseY < 250:
            drawingevent(topping4)
        nextbutton(384, 616, 335, 430, topping4, 'topping4')
        window.blit(topping4, [400, 50])

    # displaying the created pizza
    else:
        drawbg('images/Title_Congrats.png', 'images/PlayAgain.jpg', 'images/progress_6.png')
        finishbutton(384, 616, 335, 430)

        window.blit(base, [400, 50])       # draw pizza base
        for i in range(0, len(toppings)):  # draw pizza toppings in random locations, size, and rotation
            modifiedtopping = pygame.transform.rotate(
                pygame.transform.scale(toppings[i], (toppingSizes[i], toppingSizes[i])), toppingRots[i])
            window.blit(modifiedtopping, (toppingPoses[0][i], toppingPoses[1][i]))


newgame()  # setup the first game

try:  # running game loop
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:       # check for quit even
            break                    # leave the game loop
        else:
            rungame()                # run logic for game frame
            pygame.display.update()  # update screen

finally:  # exit/quit game
    print('\nClosing Karl\'s Pizza...')
    pygame.quit()
    sys.exit()
# =================================END CODE==================================
