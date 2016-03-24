__author__ = 'chandan'
import pygame
import message
import color
import shelve
pygame.init()
def instruction(Display):
    back = False
    while not back:
        Display.fill(color.aquamarine)
        message.message_to_screen(Display,"Instructions",color.brown,20)
        message.message_to_screen(Display,
                                  "The Objective of the Game is to eat food and grow"
                                  ,color.black,90,"small")
        message.message_to_screen(Display,"There are four types of food",color.black,
                                  130,"small")
        message.message_to_screen(Display,"Pressing reverse key also lead to die",color.black,
                                  170,"small")
        message.message_to_screen(Display,"The more you eat more you grow"
                                  ,color.black,210,"small")
        message.message_to_screen(Display,"Hitting the boundry of own lead to Die",
                                  color.black,250,"small")
        message.message_to_screen(Display,"Move left,right arrow key",
                                  color.black,290,"small")
        message.message_to_screen(Display,"Move Up,Down arrow key",
                                  color.black,330,"small")
        message.message_to_screen(Display,"Space to pause",
                                  color.black,370,"sfont")
        message.message_to_screen(Display,"Red apple: 1 Points",
                                  color.black,410,"small")
        message.message_to_screen(Display,"Black apple: 2 Points",
                                  color.black,450,"small")
        message.message_to_screen(Display,"Press C to clear the highScore",
                                  color.brown,490)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    d = shelve.open("scor.txt")
                    d['score'] = 0
                    d.close()
                    message.message_to_screen(Display,"Cleared",color.red,
                                              530,"small")
        message.button(Display,"Back",color.black,340,540,120,30)
        pygame.display.update()