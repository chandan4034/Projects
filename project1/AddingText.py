__author__ = 'chandan'
import time

import pygame

pygame.init()
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
ivory3 = (205,205,193)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slighter')

gameExit = False
lead_x = display_width/2
lead_y = display_height/2;
lead_x_change = 0
lead_y_change = 0
clock = pygame.time.Clock()
FPS = 10
block_size = 25;

font = pygame.font.SysFont(None,25)

def message_to_string(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0

    if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
        gameExit = True

    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(ivory3)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])
    pygame.display.update()
    clock.tick(FPS)

message_to_string("Game Over",red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()