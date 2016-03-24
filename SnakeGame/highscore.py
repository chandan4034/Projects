__author__ = 'chandan'
import pygame
import message
import color
import shelve
import data
pygame.init()
def HighScore(Display):
    back = False
    while not back:
        Display.fill(color.aquamarine)
        message.message_to_screen(Display,"High Score",color.brown,20)
        d = shelve.open("scor.txt")
        score = d['score']
        d.close()
        message.message_to_screen(Display,"High score is: " + str(score),
                                  color.black,300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        message.button(Display,"Back",color.black,340,520,120,30)
        pygame.display.update()
        # data.highScore = 26
