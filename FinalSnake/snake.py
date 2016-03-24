import pygame
import shelve
import random
pygame.init()
clock = pygame.time.Clock()
#Colour
blue = (0,0,165)
green = (0,150,50)
black = (0,0,0)
brown = (136,0,21)
red = (165,0,0)
white = (175,175,175)
ivory3 = (205,205,193)
aquamarine = (102,205,170)
field = (70,115,75)
light_white = (255,255,255)
light_white = (255,255,255)
light_red = (255,255,255)
light_yellow = (255,255,0)
light_blue = (0,0,255)
light_green = (0,255,0)
grapes_c = (153,217,122)
#Colour
inactive_c = white
active_c = red
FPSPlay = 10
display_w = 800
display_h = 600
blockSize = 25
FPS = 30
FPSButton = 100
leadX = display_w/2
leadY = display_h/2
music_status = 1
button_status = 1
high_score = 0

apple_c = red
banana_c = light_yellow
mango_c = aquamarine
#Music,Photo and font
pygame.mixer.music.load("credit.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

front = pygame.image.load("Front.jpg")
apple = pygame.image.load("apple.jpg")
banana = pygame.image.load("banana.jpg")
mango = pygame.image.load("mango.png")
grapes = pygame.image.load("grapes.jpg")
head = pygame.image.load("snakehead1.png")
food_sound = pygame.mixer.Sound("food2.wav")

largefont = pygame.font.SysFont("comicsansms",35,bold=5)
smallfont = pygame.font.SysFont("comicsansms",20)
button_sound = pygame.mixer.Sound("button.wav")
goverfont = pygame.font.SysFont("Jokerman",50)
scorefont = pygame.font.SysFont(None,25)
font = pygame.font.SysFont(None,30)
#Music,photo and font end

d = shelve.open("scor.txt")
# d['score'] = 0
hs = d['score']
d.close()

width = display_w
height = display_h

direction = "up"  #Initial Direction

def pause(Display):
    pause = True
    message_to_screen(Display,"Paused",red,300)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
        pygame.display.update()
        clock.tick(100)
def gameOver(Display):
    d = shelve.open("scor.txt")
    scor = d['score']
    hs = max(total,scor)
    if scor < total:
        d['score'] = total
    d.close()
    gOver = True
    clr = brown
    message_to_screen(Display,"Game Over You Died",
                              clr,250,size = "gover")
    message_to_screen(Display,"Try again Y:N",
                              clr,350,size="sfont")
    message_to_screen(Display,"High Score is:-" + str(hs),
                              clr,450)
    score(Display)
    while gOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    playLoop(Display)
                elif event.key == pygame.K_n:
                    mainCall()
        pygame.display.update()
def randApple(x,y):
    randomX = round((random.randrange(100,width-100-blockSize))/blockSize) * blockSize
    randomY = round((random.randrange(0,height-blockSize))/blockSize) * blockSize
    return randomX,randomY
def score(Display):
    text = scorefont.render("Score ",True,light_yellow)
    Display.blit(text,[25,5])
    Display.blit(apple,[5,35])
    Display.blit(banana,[5,75])
    Display.blit(mango,[5,115])
    Display.blit(grapes,[5,155])
    text = scorefont.render(str(apple_score),True,apple_c)
    Display.blit(text,[40,40])
    text = scorefont.render(str(banana_score),True,banana_c)
    Display.blit(text,[40,80])
    text = scorefont.render(str(mango_score),True,mango_c)
    Display.blit(text,[40,120])
    text = scorefont.render(str(grapes_score),True,grapes_c)
    Display.blit(text,[40,160])
    text = scorefont.render("Total: " + str(total),True,blue)
    Display.blit(text,[25,195])
    mx = max(total,hs)
    text = scorefont.render("Highest:" + str(mx),True,light_green)
    Display.blit(text,[0,235])
def snake(Display,blocksize,snakelist):
    if direction == "left":
        shead = pygame.transform.rotate(head,90)
    if direction == "right":
        shead = pygame.transform.rotate(head,270)
    if direction == "up":
        shead = head
    if direction == "down":
        shead = pygame.transform.rotate(head,180)
    Display.blit(shead,[snakelist[-1][0],snakelist[-1][1]])
    for XnY in snakelist[:-1]:
        pygame.draw.rect(Display,green,[XnY[0],XnY[1],blocksize,blocksize])
def playLoop(Display):
    global hs
    d = shelve.open("scor.txt")
    hs = d['score']
    d.close()
    gameExit = False
    snakeLen = 1
    snakeList = []
    global direction
    global apple_score
    global banana_score
    global mango_score
    global grapes_score
    global total
    total = 0
    banana_score = 0
    grapes_score = 0
    mango_score = 0
    direction = "up"
    leadX = width/2
    leadY = height/2
    leadXChange = 0
    leadYChange = 0
    apple_score = 0
    index = 0
    food_list = ["apple","banana","mango","grapes"]
    x = 100 #Setting indent from left and right side of display to 100
    y = height
    randomX,randomY = randApple(x,y)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause(Display)
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    leadXChange = -blockSize
                    leadYChange = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    leadXChange = blockSize
                    leadYChange = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    leadXChange = 0
                    leadYChange = -blockSize
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    leadXChange = 0
                    leadYChange = blockSize
        Display.fill(black,rect=[0,0,100,height])
        Display.fill(field,rect=[100,0,600,height])
        Display.fill(black,rect=[700,0,100,height])
        if leadX + blockSize > width - 100 or leadX < 100:
            gameOver(Display)
        elif leadY + blockSize > height or leadY < 0:
            gameOver(Display)
        leadX += leadXChange
        leadY += leadYChange
        snakeHead = []
        snakeHead.append(leadX)
        snakeHead.append(leadY)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLen:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead and snakeLen > 1:
                gameOver(Display)
        snake(Display,blockSize,snakeList)
        if food_list[index] == "apple":
            Display.blit(apple,[randomX,randomY])
        elif food_list[index] == "banana":
            Display.blit(banana,[randomX,randomY])
        elif food_list[index] == "mango":
            Display.blit(mango,[randomX,randomY])
        elif food_list[index] == "grapes":
            Display.blit(grapes,[randomX,randomY])
        score(Display)
        pygame.display.update()
        if leadX == randomX and leadY == randomY:
            if music_status == 1:
                pygame.mixer.Sound.play(food_sound)
            randomX,randomY = randApple(x,y)
            snakeLen += 1
            total += 1
            if index == 0:
                apple_score += 1
            elif index == 1:
                banana_score += 1
            elif index == 2:
                mango_score += 1
            elif index == 3:
                grapes_score += 1
            index = random.randrange(0,4)
        # button(Display,"Back",black,340,560,120,30)
        pygame.display.update()
        clock.tick(FPSPlay)

def HighScore(Display):
    back = False
    while not back:
        Display.fill(aquamarine)
        message_to_screen(Display,"High Score",brown,20)
        d = shelve.open("scor.txt")
        score = d['score']
        d.close()
        message_to_screen(Display,"High score is: " + str(score),
                                  black,300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(Display,"Back",black,340,520,120,30)
        pygame.display.update()
def credit(Display):
    back = False
    while not back:
        Display.fill(aquamarine)
        message_to_screen(Display,"Credits",brown,20)
        message_to_screen(Display,
                                  "This Game was made as a personal project"
                                  ,black,100,"small")
        message_to_screen(Display,"With python and pygame in march 2016"
                                  ,black,150,"small")
        message_to_screen(Display,"It is Free and any Suggestion is appereciated",
                                  black,200,"small")
        message_to_screen(Display,"Design & Programming",
                                  brown,300,"sfont")
        message_to_screen(Display,"Chandan Kumar",
                                  black,340,"small")
        message_to_screen(Display,"Sound & Music",
                                  brown,420,"sfont")
        message_to_screen(Display,"Chandan kumar",
                                  black,460,"small")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(Display,"Back",black,340,520,120,30)
        pygame.display.update()
def instruction(Display):
    back = False
    while not back:
        Display.fill(aquamarine)
        message_to_screen(Display,"Instructions",brown,20)
        message_to_screen(Display,
                                  "The Objective of the Game is to eat food and grow"
                                  ,black,90,"small")
        message_to_screen(Display,"There are four types of food",black,
                                  130,"small")
        message_to_screen(Display,"Pressing reverse key also lead to die",black,
                                  170,"small")
        message_to_screen(Display,"The more you eat more you grow"
                                  ,black,210,"small")
        message_to_screen(Display,"Hitting the boundry of own lead to Die",
                                  black,250,"small")
        message_to_screen(Display,"Move left,right arrow key",
                                  black,290,"small")
        message_to_screen(Display,"Move Up,Down arrow key",
                                  black,330,"small")
        message_to_screen(Display,"Space to pause",
                                  black,370,"sfont")
        message_to_screen(Display,"Red apple: 1 Points",
                                  black,410,"small")
        message_to_screen(Display,"Black apple: 2 Points",
                                  black,450,"small")
        message_to_screen(Display,"Press C to clear the highScore",
                                  brown,490)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    d = shelve.open("scor.txt")
                    d['score'] = 0
                    d.close()
                    message_to_screen(Display,"Cleared",red,
                                              530,"small")
        button(Display,"Back",black,340,540,120,30)
        pygame.display.update()
def terminate():
    pygame.quit()
    quit()
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
    textRect.center = (display_w/2),(height)
    Display.blit(textSurf,textRect)
def button(Display,text,background_colour,xloc,yloc,width,height):
    global music_status
    global button_status
    pygame.draw.rect(Display,background_colour,[xloc,yloc,width,height])
    colour = inactive_c
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    clr = green
    if xloc + width >= cur[0] > xloc and yloc + height >= cur[1] >= yloc:
        clr = white
        colour = active_c
        pygame.draw.line(Display,clr,(xloc,yloc),(xloc+width,yloc),3)
        pygame.draw.line(Display,clr,(xloc,yloc),(xloc,yloc+height),3)
        pygame.draw.line(Display,clr,(xloc+width,yloc),(xloc+width,yloc+height),3)
        pygame.draw.line(Display,clr,(xloc,yloc+height),(xloc+width,yloc+height),3)
        textSurf,textRect = text_objects(text,colour,"sfont") #Simple Font
        textRect.center = ((xloc + width/2),(yloc + height/2))
        Display.blit(textSurf,textRect)
        if click[0] == 1:
            if button_status == 1:
                pygame.mixer.Sound.play(button_sound)
            if text == "Quit":
                terminate()
            elif text == "Play":
                playLoop(Display)
            elif text == "High Score":
                HighScore(Display)
            elif text == "Instruction":
                instruction(Display)
            elif text == "Credits":
                credit(Display)
            elif text == "Back":
                mainCall()
            elif text == "Continue":
                playLoop(Display)
            elif text == "Music off":
                music_status = 0
                button_status = 0
                pygame.mixer.music.stop()
                # pass
            elif text == "Music on":
                music_status = 1
                button_status = 1
                pygame.mixer.music.play(-1)
                # pass

    else:
        pygame.draw.line(Display,clr,(xloc,yloc),(xloc+width,yloc),3)
        pygame.draw.line(Display,clr,(xloc,yloc),(xloc,yloc+height),3)
        pygame.draw.line(Display,clr,(xloc+width,yloc),(xloc+width,yloc+height),3)
        pygame.draw.line(Display,clr,(xloc,yloc+height),(xloc+width,yloc+height),3)
        textSurf,textRect = text_objects(text,colour,"sfont") #Simple Font
        textRect.center = ((xloc + width/2),(yloc + height/2))
        Display.blit(textSurf,textRect)
        pygame.display.update()
    clock.tick(FPSButton)
def mainCall():
    # pygame.mixer.Sound.play(welcome_screen)
    icon = pygame.image.load('snake.png')
    front = pygame.image.load("Front.jpg")
    intro_snake = pygame.image.load("introsnake.png")
    gameDisplay = pygame.display.set_mode((display_w,
                                           display_h))
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
            message_to_screen(gameDisplay,
                                      "Welcome to Snake Game",
                                      brown,15)
            button(gameDisplay,"Play",black,340,340,button_w,button_h)
            button(gameDisplay,"High Score",black,340,375,button_w,button_h)
            button(gameDisplay,"Music off",black,340,410,button_w,button_h)
            button(gameDisplay,"Music on",black,340,445,button_w,button_h)
            button(gameDisplay,"Instruction",black,340,480,button_w,button_h)
            button(gameDisplay,"Credits",black,340,515,button_w,button_h)
            button(gameDisplay,"Quit",black,340,550,button_w,button_h)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()
        pygame.quit()
        quit()
    gameLoop()
mainCall()