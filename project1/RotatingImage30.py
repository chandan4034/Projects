__author__ = 'chandan'
#Centering the text
import pygame
import random

pygame.init()
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,200,0)
ivory3 = (205,205,193)
aquamarine = (102,205,170)
yellow = (128,64,64)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slighter')

clock = pygame.time.Clock()
FPS = 8
block_size = 20
AppleThickness = 30
smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",40)
largefont = pygame.font.SysFont("comicsansms",50)

img = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple.png')
direction = "up"

def game_intro():
    intro = True
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
        message_to_screen("Welcome to Snake Game",
                          green,
                          -175,
                          "large")
        message_to_screen("The objective of game to eat the apples",
                          yellow,
                          -30,
                          "medium")
        message_to_screen("The more you eat the more you score",
                          yellow,
                          20,
                          "medium")
        message_to_screen("If you hit the boundry of self you will die",
                          yellow,
                          70,
                          "medium")
        message_to_screen("Press C to play and Q to quit",
                          aquamarine,
                          200,
                          "large")
        pygame.display.update()
        clock.tick(15)

def text_objects(text ,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    if size == "medium":
        textSurface = medfont.render(text,True,color)
    if size == "large":
        textSurface = largefont.render(text,True,color)
    return  textSurface,textSurface.get_rect()

def message_to_screen(msg,color,y_displace = 0 , size = "small"):
    textSurf , textRect = text_objects(msg,color,size)
    # screen_text = font.render(msg,True,color)
    # gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    textRect.center = (display_width / 2) , (display_height / 2) + y_displace
    gameDisplay.blit(textSurf,textRect)

def snake(block_size,snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img,180)
    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def gameLoop():
    global direction
    direction = "up"
    snakeList = []
    snakeLength = 1 #allow snake to length 10
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2;
    lead_x_change = 0
    lead_y_change = 0
    randAppleX = round(random.randrange(0,display_width - block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height - block_size))#/10.0)*10.0

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
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(ivory3)

        gameDisplay.fill(red,[randAppleX,randAppleY,AppleThickness,AppleThickness])#Apple
    
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                #print("Hello")
                gameOver = True

        snake(block_size,snakeList)
        
        pygame.display.update()
        # if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
        #     if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
        #         randAppleX = round(random.randrange(0,display_width - block_size))#/10.0)*10.0
        #         randAppleY = round(random.randrange(0,display_height - block_size))#/10.0)*10.0
        #         snakeLength += 1
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x +block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0,display_width - block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0,display_height - block_size))#/10.0)*10.0
                snakeLength += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0,display_width - block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0,display_height - block_size))#/10.0)*10.0
                snakeLength += 1

        clock.tick(FPS)
    pygame.quit()
    quit()
game_intro()
gameLoop()