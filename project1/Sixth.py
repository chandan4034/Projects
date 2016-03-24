_author_='chandan'

import pygame
pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,255)
green = (0,255,0)

gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('Slighter')

gameExit = False

#In looping statement space indent is important

while not gameExit:  #Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black,[400,300,50,100] )
    pygame.draw.rect(gameDisplay,red,[400,300,10,10] ) # It overlap the upper rect
    #Another way to draw using fill is comparatively faster
    gameDisplay.fill(green,rect = [200,200,50,50])

    
    pygame.display.update()#If not update then changes does not affected

pygame.quit()
quit()
