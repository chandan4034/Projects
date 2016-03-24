__author__ = 'chandan'
#lec-49 to 52
import pygame
import random
import time

pygame.init()
white = (255,255,255)
red = (200,0,0)
light_red = (255,0,0)
black = (0,0,0)
green = (34,177,76)
light_green = (0,255,0)
ivory3 = (205,205,193)
aquamarine = (102,205,170)
yellow = (200,200,0)
light_yellow = (255,255,0)
blue = (80,20,90)
display_width = 800
display_height = 600
ground_height = 35
# img = pygame.image.load('snakehead.png')
# appleimg = pygame.image.load('apple.png')

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')
#icon = pygame.image.load('apple.png')
#pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 8
block_size = 20
AppleThickness = 30
smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",40)
largefont = pygame.font.SysFont("jokerman",50)
scorefont = pygame.font.SysFont("comicsansms",25)
elargefont = pygame.font.SysFont("comicsansms",80)

tankWidth = 40
tankHeight = 20
turrentWidth = 5
wheelWidth = 5
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)),(buttony+(buttonheight/2)))
    gameDisplay.blit(textSurf,textRect)
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(aquamarine)
        message_to_screen("Paused",
                          blue,
                          -40,
                          "elarge")
        message_to_screen("Press c to continue or Q to quit",
                          black,
                          40,
                          "medium")
        pygame.display.update()
        clock.tick(8)
def score(score):
    text = scorefont.render("Score:-"+str(score),True,black);
    gameDisplay.blit(text,[0,0])
def barrier(xlocation,randomHeight,barrier_width):
    pygame.draw.rect(gameDisplay,black,[xlocation,display_height-randomHeight,barrier_width,randomHeight])
    #print(xlocation,randomHeight)

def game_intro():  #Start Screen
    intro = True
    gameDisplay.fill(blue)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        message_to_screen("Welcome to Tanks",
                          green,
                          -175,
                          "large")
        message_to_screen("The objective is to shoot and destroy",
                          yellow,
                          -30,
                          "medium")
        message_to_screen("the enemy before they destroy you",
                          yellow,
                          20,
                          "medium")
        message_to_screen("The more you destroy the harder you get",
                          yellow,
                          70,
                          "medium")
        #Adding Button
        button("Play",150,500,100,50,green,light_green,action = "play")
        button("Controls",350,500,100,50,yellow,light_yellow,action = "controls")
        button("Quit",550,500,100,50,red,light_red,action = "quit")
        #End of adding button
        pygame.display.update()
        clock.tick(15)

def text_objects(text ,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    if size == "medium":
        textSurface = medfont.render(text,True,color)
    if size == "large":
        textSurface = largefont.render(text,True,color)
    if size == "elarge":
        textSurface = elargefont.render(text,True,color)
    return  textSurface,textSurface.get_rect()

def message_to_screen(msg,color,y_displace = 0 , size = "small"):
    textSurf , textRect = text_objects(msg,color,size)
    textRect.center = (display_width / 2) , (display_height / 2) + y_displace
    gameDisplay.blit(textSurf,textRect)
def game_controls():
    gcont = True
    gameDisplay.fill(blue)
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        message_to_screen("Controls",
                          green,
                          -175,
                          "large")
        message_to_screen("Fire: Spacebar",
                          yellow,
                          -30,
                          "medium")
        message_to_screen("Move Turrent: up and down arrow key",
                          yellow,
                          20,
                          "medium")
        message_to_screen("Move Tanks: Left and Right arrow key",
                          yellow,
                          70,
                          "medium")
        #Adding Button
        button("Play",150,500,100,50,green,light_green,action = "play")
        button("Main",350,500,100,50,yellow,light_yellow,action = "main")
        button("Quit",550,500,100,50,red,light_red,action = "quit")
        #End of adding button
        pygame.display.update()
        clock.tick(FPS)
def button(text, x, y, width, height, inactive_color,active_color,action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+width >= cur[0] >= x and y+height >= cur[1] >= y:
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "play":
                gameLoop()
            if action == "controls":
                game_controls()
            if action == "quit":
                pygame.quit()
                quit()
            if action == "main":
                game_intro()
    else:
        pygame.draw.rect(gameDisplay,inactive_color,(x,y,width,height))
    text_to_button(text,black,x,y,width,height)
def tank(x,y,turPos):
    x = int(x)
    y = int(y)
    possibleTurrets = [(x-27,y-2),
                       (x-26,y-5),
                       (x-25,y-8),
                       (x-23,y-12),
                       (x-20,y-14),
                       (x-18,y-15),
                       (x-15,y-17),
                       (x-13,y-19),
                       (x-11,y-21),]
    pygame.draw.circle(gameDisplay,black,(x,y),int(tankHeight/2))
    pygame.draw.rect(gameDisplay,black,(x-tankHeight,y,tankWidth,tankHeight))

    pygame.draw.line(gameDisplay,black,(x,y),possibleTurrets[turPos],turrentWidth)
    startX = 15
    for i in range(1,8):
        pygame.draw.circle(gameDisplay,black,(x-startX,y+20),wheelWidth)
        startX -= 5
    return possibleTurrets[turPos]
def enemy_tank(x,y,turPos):
    x = int(x)
    y = int(y)
    possibleTurrets = [(x+27,y-2),
                       (x+26,y-5),
                       (x+25,y-8),
                       (x+23,y-12),
                       (x+20,y-14),
                       (x+18,y-15),
                       (x+15,y-17),
                       (x+13,y-19),
                       (x+11,y-21),]
    pygame.draw.circle(gameDisplay,black,(x,y),int(tankHeight/2))
    pygame.draw.rect(gameDisplay,black,(x-tankHeight,y,tankWidth,tankHeight))

    #pygame.draw.line(gameDisplay,black,(x,y),possibleTurrets[turPos],turrentWidth)
    #For enemy tank lets fix the turret position for now
    pygame.draw.line(gameDisplay,black,(x,y),possibleTurrets[8],turrentWidth)

    startX = 15
    for i in range(1,8):
        pygame.draw.circle(gameDisplay,black,(x-startX,y+20),wheelWidth)
        startX -= 5
    return possibleTurrets[turPos]
def explosion(x,y,size = 50):
    explode = True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        startPoint = x,y
        magnitude = 1
        colorChoices = [red,light_red,yellow,light_yellow]
        while magnitude < size:
            exploding_bit_x = x + random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y + random.randrange(-1*magnitude,magnitude)
            pygame.draw.circle(gameDisplay,colorChoices[random.randrange(0,4)],
                               (exploding_bit_x,exploding_bit_y),
                               random.randrange(0,5))
            pygame.display.update()
            clock.tick(100)
            magnitude += 1
        explode = False
def fireShell(xy,tankx,tanky,turPos,gun_power,xlocation,barrier_width,randomHeight,
              Tank="player"):
    fire = True
    startingShell = list(xy)
    #print("FIRE!",startingShell)
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #print(startingShell[0],startingShell[1])#Debugging purpose
        pygame.draw.circle(gameDisplay,green,(startingShell[0],startingShell[1]),5)
        #Just making an arc by adjusting quadratic equation
        if Tank == "enemy":
            startingShell[0] += (12 - turPos) * 2
        else:
            startingShell[0] -= (12 - turPos) * 2
        startingShell[1] += int((((startingShell[0]-xy[0])*(0.015/(gun_power/50)))**2) - turPos+turPos/(12-turPos))
        if startingShell[1] > display_height - ground_height:
            print("Last shell: ",startingShell[0],startingShell[1])
            hit_x = int(startingShell[0]*((display_height-ground_height)/startingShell[1]))
            hit_y = int(display_height-ground_height)
            print("Impact: ",hit_x,hit_y)
            explosion(hit_x,hit_y)
            fire = False
        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] > xlocation
        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] > display_height - randomHeight
        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell: ",startingShell[0],startingShell[1])
            hit_x = int(startingShell[0])
            hit_y = int(startingShell[1])
            print("Impact: ",hit_x,hit_y)
            explosion(hit_x,hit_y)
            fire = False
        pygame.display.update()
        clock.tick(100)
def power(level):
    text = smallfont.render("Power: "+str(level)+"%",True,blue)
    gameDisplay.blit(text,[display_width/2,0])

def gameLoop():
    gameExit = False
    gameOver = False
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0
    barrier_width = 50
    power_change = 0
    fire_power = 50
    xlocation = (display_width/2) + random.randint(-0.2*display_width,0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)
    FPS = 20
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(aquamarine)
            message_to_screen("Game Over",
                              red,
                              -40,
                              size = "large")

            message_to_screen("Press c to play again or q to quit",
                              black,
                              20,
                              size = "medium")

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove -= 5
                elif event.key == pygame.K_RIGHT:
                    tankMove += 5
                elif event.key == pygame.K_UP:
                    changeTur += 1
                elif event.key == pygame.K_DOWN:
                    changeTur -=1
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_SPACE:
                    #fireShell(gun,mainTankX,mainTankY,currentTurPos)
                    fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,
                              xlocation,barrier_width,randomHeight)
                    fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,
                              xlocation,barrier_width,randomHeight,Tank="enemy")
                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0
        mainTankX += tankMove
        currentTurPos += changeTur
        if currentTurPos < 0:
            currentTurPos = 0
        elif currentTurPos > 8:
            currentTurPos = 8

        if mainTankX - (tankWidth/2) < xlocation + barrier_width:
            mainTankX += 5  #so that it can't move because firstly we are
                            #adding -5 so here +5
        gameDisplay.fill(white)
        gun=tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX,enemyTankY,currentTurPos)
        fire_power += power_change
        power(fire_power)
        barrier(xlocation,randomHeight,barrier_width)
        #Drawing ground
        gameDisplay.fill(green,rect=[0,display_height-ground_height,
                                     display_width,ground_height])
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
game_intro()
gameLoop()