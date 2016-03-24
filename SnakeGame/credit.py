__author__ = 'chandan'
import pygame
import message
import color
pygame.init()
def screen(Display):
    back = False
    while not back:
        Display.fill(color.aquamarine)
        message.message_to_screen(Display,"Credits",color.brown,20)
        message.message_to_screen(Display,
                                  "This Game was made as a personal project"
                                  ,color.black,100,"small")
        message.message_to_screen(Display,"With python and pygame in march 2016"
                                  ,color.black,150,"small")
        message.message_to_screen(Display,"It is Free and any Suggestion is appereciated",
                                  color.black,200,"small")
        message.message_to_screen(Display,"Design & Programming",
                                  color.brown,300,"sfont")
        message.message_to_screen(Display,"Chandan Kumar",
                                  color.black,340,"small")
        message.message_to_screen(Display,"Sound & Music",
                                  color.brown,420,"sfont")
        message.message_to_screen(Display,"Chandan kumar",
                                  color.black,460,"small")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        message.button(Display,"Back",color.black,340,520,120,30)
        pygame.display.update()
