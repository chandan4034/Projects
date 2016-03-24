__author__ = 'chandan'
import pygame
import constraints
import color
import credit
import Intro
import highscore
import instruction
import play
import shelve
pygame.init()
clock = pygame.time.Clock()
inactive_c = color.white
active_c = color.red
FPS = 100
def terminate():
    pygame.quit()
    quit()
font = pygame.font.SysFont(None,30)
largefont = pygame.font.SysFont("comicsansms",35,bold=5)
smallfont = pygame.font.SysFont("comicsansms",20)
button_sound = pygame.mixer.Sound("button.wav")
goverfont = pygame.font.SysFont("Jokerman",50)
def text_objects(msg,colour,size = "small"):
    if size == "large":
        textSurface = largefont.render(msg,True,colour)
    elif size == "sfont":
        textSurface = font.render(msg,True,colour)
    elif size == "small":
        textSurface = font.render(msg,True,colour)
    elif size == "gover":
        textSurface = goverfont.render(msg,True,colour)
    return textSurface,textSurface.get_rect()
def message_to_screen(Display,msg,colour,height,size = "large"):
    textSurf,textRect = text_objects(msg,colour,size)
    textRect.center = (constraints.display_w/2),(height)
    Display.blit(textSurf,textRect)
def newFunction(Display):
    Display.fill(color.white)
    pygame.display.update()
def button(Display,text,background_colour,xloc,yloc,width,height):
    pygame.draw.rect(Display,background_colour,[xloc,yloc,width,height])
    colour = inactive_c
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    clr = color.green
    if xloc + width >= cur[0] > xloc and yloc + height >= cur[1] >= yloc:
        clr = color.white
        colour = active_c
        pygame.draw.line(Display,clr,(xloc,yloc),(xloc+width,yloc),3)
        pygame.draw.line(Display,clr,(xloc,yloc),(xloc,yloc+height),3)
        pygame.draw.line(Display,clr,(xloc+width,yloc),(xloc+width,yloc+height),3)
        pygame.draw.line(Display,clr,(xloc,yloc+height),(xloc+width,yloc+height),3)
        textSurf,textRect = text_objects(text,colour,"sfont") #Simple Font
        textRect.center = ((xloc + width/2),(yloc + height/2))
        Display.blit(textSurf,textRect)
        if click[0] == 1:
            if constraints.button_status == 1:
                pygame.mixer.Sound.play(button_sound)
            if text == "Quit":
                terminate()
            elif text == "Play":
                play.gameLoop(Display)
            elif text == "High Score":
                highscore.HighScore(Display)
            elif text == "Instruction":
                instruction.instruction(Display)
            elif text == "Credits":
                credit.screen(Display)
            elif text == "Back":
                Intro.mainCall()
            elif text == "Continue":
                play.gameLoop(Display)
            elif text == "Music off":
                constraints.music_status = 0
                constraints.button_status = 0
                pygame.mixer.music.stop()
            elif text == "Music on":
                constraints.music_status = 1
                constraints.button_status = 1
                pygame.mixer.music.play(-1)

    else:
        pygame.draw.line(Display,clr,(xloc,yloc),(xloc+width,yloc),3)
        pygame.draw.line(Display,clr,(xloc,yloc),(xloc,yloc+height),3)
        pygame.draw.line(Display,clr,(xloc+width,yloc),(xloc+width,yloc+height),3)
        pygame.draw.line(Display,clr,(xloc,yloc+height),(xloc+width,yloc+height),3)
        textSurf,textRect = text_objects(text,colour,"sfont") #Simple Font
        textRect.center = ((xloc + width/2),(yloc + height/2))
        Display.blit(textSurf,textRect)
        pygame.display.update()
    clock.tick(FPS)
# def button1(Display,text,background_colour,xloc,yloc,width,height,action="Inactive"):
#     pygame.draw.rect(Display,background_colour,[xloc,yloc,width,height])
#     colour = inactive_c
#     cur = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     clr = color.green
#     if xloc + width >= cur[0] > xloc and yloc + height >= cur[1] >= yloc:
#         clr = color.white
#         colour = active_c
#         pygame.draw.line(Display,clr,(xloc,yloc),(xloc+width,yloc),3)
#         pygame.draw.line(Display,clr,(xloc,yloc),(xloc,yloc+height),3)
#         pygame.draw.line(Display,clr,(xloc+width,yloc),(xloc+width,yloc+height),3)
#         pygame.draw.line(Display,clr,(xloc,yloc+height),(xloc+width,yloc+height),3)
#         textSurf,textRect = text_objects(text,colour,"sfont") #Simple Font
#         textRect.center = ((xloc + width/2),(yloc + height/2))
#         Display.blit(textSurf,textRect)
#         if click[0] == 1:
#             if text == "Quit":
#                 terminate()
#             elif text == "Continue":
#                 return True
#             elif text == "Retry":
#                 return True
#         pygame.display.update()
#     else:
#         pygame.draw.line(Display,clr,(xloc,yloc),(xloc+width,yloc),3)
#         pygame.draw.line(Display,clr,(xloc,yloc),(xloc,yloc+height),3)
#         pygame.draw.line(Display,clr,(xloc+width,yloc),(xloc+width,yloc+height),3)
#         pygame.draw.line(Display,clr,(xloc,yloc+height),(xloc+width,yloc+height),3)
#         textSurf,textRect = text_objects(text,colour,"sfont") #Simple Font
#         textRect.center = ((xloc + width/2),(yloc + height/2))
#         Display.blit(textSurf,textRect)
#         pygame.display.update()
#     return False
#     clock.tick(FPS)
#
