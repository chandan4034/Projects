__author__ = 'chandan'
import pygame
pygame.init()
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(blue)
Pix = pygame.PixelArray(gameDisplay)
Pix[10][10] = red
#(place,color,start,end,width)
pygame.draw.line(gameDisplay,green,(50,50),(50,70),2)
#(place,color,center,width)
pygame.draw.circle(gameDisplay,black,(100,100),60)
#(place,color,(x,y,width,height))
pygame.draw.rect(gameDisplay,red,(120,200,100,20))
#(place,color,all points tuple of tuple)
pygame.draw.polygon(gameDisplay,red,((10,10),(20,20),(15,50)))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
pygame.quit()
quit()