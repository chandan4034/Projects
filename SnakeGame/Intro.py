__author__ = 'chandan'
import pygame
import message
import color
import constraints
import shelve
pygame.init()
# welcome_screen = pygame.mixer.Sound("button-17.wav") #welcome screen
pygame.mixer.music.load("credit.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
def mainCall():
    # pygame.mixer.Sound.play(welcome_screen)
    icon = pygame.image.load('snake.png')
    front = pygame.image.load("Front.jpg")
    intro_snake = pygame.image.load("introsnake.png")
    gameDisplay = pygame.display.set_mode((constraints.display_w,
                                           constraints.display_h))
    pygame.display.set_caption('Snake Game')
    pygame.display.set_icon(icon)
    button_w = 120
    button_h = 30
    pygame.display.update()
    def gameLoop():
        gameDisplay.blit(front,[0,0])
        gameDisplay.blit(intro_snake,[240,28])
        MainLoop = True
        while MainLoop:
            message.message_to_screen(gameDisplay,
                                      "Welcome to Snake Game",
                                      color.brown,15)
            message.button(gameDisplay,"Play",color.black,340,340,button_w,button_h)
            message.button(gameDisplay,"High Score",color.black,340,375,button_w,button_h)
            message.button(gameDisplay,"Music off",color.black,340,410,button_w,button_h)
            message.button(gameDisplay,"Music on",color.black,340,445,button_w,button_h)
            message.button(gameDisplay,"Instruction",color.black,340,480,button_w,button_h)
            message.button(gameDisplay,"Credits",color.black,340,515,button_w,button_h)
            message.button(gameDisplay,"Quit",color.black,340,550,button_w,button_h)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()
        pygame.quit()
        quit()
    gameLoop()