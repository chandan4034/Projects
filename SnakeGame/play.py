__author__ = 'chandan'
import pygame
import constraints
import color
import message
import Intro
import random
import shelve
import time
pygame.init()
FPS = 10
clock = pygame.time.Clock()
front = pygame.image.load("Front.jpg")
apple = pygame.image.load("apple.jpg")
banana = pygame.image.load("banana.jpg")
mango = pygame.image.load("mango.png")
grapes = pygame.image.load("grapes.jpg")
blockSize = constraints.blockSize
width = constraints.display_w
height = constraints.display_h
scorefont = pygame.font.SysFont(None,25)
direction = "up"
head = pygame.image.load("snakehead1.png")
food_sound = pygame.mixer.Sound("food2.wav")
d = shelve.open("scor.txt")
hs = d['score']
d.close()
def pause(Display):
    pause = True
    message.message_to_screen(Display,"Paused",color.red,300)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                message.terminate()
            # p=message.button1(Display,"Continue",color.black,
            #                275,300,120,30)
            # q=message.button1(Display,"Quit",color.black,
            #                400,300,120,30)
            # if p == True:
            #     pause = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
        pygame.display.update()
        clock.tick(100)
def gameOver(Display):
    hs = total
    d = shelve.open("scor.txt")
    scor = d['score']
    hs = max(total,scor)
    if scor < total:
        d['score'] = total
        # print()
    d.close()
    gOver = True
    clr = color.brown
    message.message_to_screen(Display,"Game Over You Died",
                              clr,250,size = "gover")
    message.message_to_screen(Display,"Try again Y:N",
                              clr,350,size="sfont")
    message.message_to_screen(Display,"High Score is:-" + str(hs),
                              clr,450)
    score(Display)
    while gOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    gameLoop(Display)
                elif event.key == pygame.K_n:
                    Intro.mainCall()
        pygame.display.update()
def randApple(x,y):
    randomX = round((random.randrange(100,width-100-blockSize))/blockSize) * blockSize
    randomY = round((random.randrange(0,height-blockSize))/blockSize) * blockSize
    return randomX,randomY
def score(Display):
    text = scorefont.render("Score ",True,color.light_yellow)
    Display.blit(text,[25,5])
    apple_c = color.red
    banana_c = color.light_yellow
    mango_c = color.aquamarine
    grapes_c = color.grapes_c
    Display.blit(apple,[5,35])
    Display.blit(banana,[5,75])
    Display.blit(mango,[5,115])
    Display.blit(grapes,[5,155])
    text = scorefont.render(str(apple_score),True,apple_c)
    Display.blit(text,[40,40])
    text = scorefont.render(str(banana_score),True,banana_c)
    Display.blit(text,[40,80])
    text = scorefont.render(str(mango_score),True,mango_c)
    Display.blit(text,[40,120])
    text = scorefont.render(str(grapes_score),True,grapes_c)
    Display.blit(text,[40,160])
    text = scorefont.render("Total: " + str(total),True,color.blue)
    Display.blit(text,[25,195])
    mx = max(total,hs)
    text = scorefont.render("Highest:" + str(mx),True,color.light_green)
    Display.blit(text,[0,235])
def snake(Display,blocksize,snakelist):
    if direction == "left":
        shead = pygame.transform.rotate(head,90)
    if direction == "right":
        shead = pygame.transform.rotate(head,270)
    if direction == "up":
        shead = head
    if direction == "down":
        shead = pygame.transform.rotate(head,180)
    Display.blit(shead,[snakelist[-1][0],snakelist[-1][1]])
    for XnY in snakelist[:-1]:
        pygame.draw.rect(Display,color.green,[XnY[0],XnY[1],blocksize,blocksize])
def gameLoop(Display):
    gameExit = False
    snakeLen = 1
    snakeList = []
    global direction
    global apple_score
    global banana_score
    global mango_score
    global grapes_score
    global total
    total = 0
    banana_score = 0
    grapes_score = 0
    mango_score = 0
    direction = "up"
    leadX = constraints.leadX
    leadY = constraints.leadY
    leadXChange = 0
    leadYChange = 0
    apple_score = 0
    index = 0
    food_list = ["apple","banana","mango","grapes"]
    x = 100 #Setting indent from left and right side of display to 100
    y = height
    randomX,randomY = randApple(x,y)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause(Display)
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    leadXChange = -blockSize
                    leadYChange = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    leadXChange = blockSize
                    leadYChange = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    leadXChange = 0
                    leadYChange = -blockSize
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    leadXChange = 0
                    leadYChange = blockSize
        Display.fill(color.black,rect=[0,0,100,height])
        Display.fill(color.field,rect=[100,0,600,height])
        Display.fill(color.black,rect=[700,0,100,height])
        if leadX + blockSize > width - 100 or leadX < 100:
            gameOver(Display)
        elif leadY + blockSize > height or leadY < 0:
            gameOver(Display)
        leadX += leadXChange
        leadY += leadYChange
        snakeHead = []
        snakeHead.append(leadX)
        snakeHead.append(leadY)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLen:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead and snakeLen > 1:
                gameOver(Display)
        snake(Display,blockSize,snakeList)
        if food_list[index] == "apple":
            Display.blit(apple,[randomX,randomY])
        elif food_list[index] == "banana":
            Display.blit(banana,[randomX,randomY])
        elif food_list[index] == "mango":
            Display.blit(mango,[randomX,randomY])
        elif food_list[index] == "grapes":
            Display.blit(grapes,[randomX,randomY])
        score(Display)
        pygame.display.update()
        if leadX == randomX and leadY == randomY:
            if constraints.music_status == 1:
                pygame.mixer.Sound.play(food_sound)
            randomX,randomY = randApple(x,y)
            snakeLen += 1
            total += 1
            if index == 0:
                apple_score += 1
            elif index == 1:
                banana_score += 1
            elif index == 2:
                mango_score += 1
            elif index == 3:
                grapes_score += 1
            index = random.randrange(0,4)
        # message.button(Display,"Back",color.black,340,560,120,30)
        pygame.display.update()
        clock.tick(FPS)
