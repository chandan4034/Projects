__author__ = 'chandan'
#Scoring and making RandAppleGen function
import pygame
import random

pygame.init()
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,200,0)
ivory3 = (205,205,193)
aquamarine = (102,205,170)
yellow = (200,200,0)
blue = (80,20,90)
display_width = 1000
display_height = 600

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

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(aquamarine)
        message_to_screen("Paused",
                          blue,
                          -40,
                          "elarge")
        message_to_screen("Press SPACE to continue or Q to quit",
                          black,
                          40,
                          "medium")
        pygame.display.update()
        clock.tick(8)

def score(score):
    text = scorefont.render("Score:-"+str(score),True,black);
    gameDisplay.blit(text,[0,0])

def randAppleGen():
    randAppleX = round(random.randrange(0,display_width - AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height - AppleThickness))#/10.0)*10.0
    return randAppleX,randAppleY

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
        # message_to_screen("Press C to play SPACE to pause or Q to quit",
        #                   aquamarine,
        #                   200,
        #                   "medium")
        #Adding button for play and quit
        pygame.draw.rect(gameDisplay,green,(250,500,100,50))
        pygame.draw.rect(gameDisplay,yellow,(450,500,100,50))
        pygame.draw.rect(gameDisplay,red,(650,500,100,50))
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

def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15
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
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_SPACE:
                    pause()

        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
game_intro()
gameLoop()