_author_='chandan'

import pygame
pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('Slighter')

gameExit = False
lead_x = 300
lead_y = 300

#In looping statement space indent is important

while not gameExit:  #Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  #Take care event.key not event.type
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x +=10
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10] )    
    pygame.display.update()#If not update then changes does not affected

pygame.quit()
quit()
