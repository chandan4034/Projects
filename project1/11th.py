#8-10
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
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()
#In looping statement space indent is important

while not gameExit:  #Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            #here we can use elif because no need of all if statement
            if event.key == pygame.K_LEFT:  #Take care event.key not event.type
                lead_x_change = -10
                lead_y_change =0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0
            
    lead_x += lead_x_change   #very fast so maintaining frames/sec
    lead_y += lead_y_change
    
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,25,25] )    
    pygame.display.update()#If not update then changes does not affected
    clock.tick(10) #It will be after update make sure 8 is the frames/sec
    
pygame.quit()
quit()
