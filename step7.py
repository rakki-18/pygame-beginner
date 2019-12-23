
# importing necessary files
import pygame
import time
import random

# initiating pygame
pygame.init()

# setting display window parameters
disp_width = 800
disp_height = 600

# making a display window
gameDisp = pygame.display.set_mode((disp_width,disp_height))

# setting title
pygame.display.set_caption("Fast and Furious!")

# defining colors
black = (0,0,0)
white = (255,255,255)

# clock of the game
clock = pygame.time.Clock()

# variable definition
crashed = False

# defining car
carImg = pygame.image.load('redcar.png')
car_height = 100
car_width = 50
x_change = 0

# placement of car
def car(x,y):
    gameDisp.blit(carImg,(x,y))

# initial coordinates of the car
x = disp_width * 0.5
y = disp_height * 0.8


# defining obstacles (boxes)
box_w = 100
box_h = 100
box_y = -600
box_x = random.randrange(0,disp_width-box_w)
box_s = 7

# scoring
score = 0

# draw obstacles
def box(box_w,box_h,box_x,box_y,color):
    pygame.draw.rect(gameDisp,color,[box_x,box_y,box_w,box_h])


# crash message
def crash():
    disp_message("You Crashed")

# defining text objects
def text_objects(text,font):
    text_surf = font.render(text,True,black)
    return text_surf,text_surf.get_rect()

# dislaying message
def disp_message(text):
    large_text = pygame.font.SysFont('arial',120)
    text_surf,text_rect = text_objects(text,large_text)
    text_rect.center = (disp_width/2,disp_height/2)
    gameDisp.blit(text_surf,text_rect)
    pygame.display.update()
    time.sleep(2)

# displaying score
def disp_score(score):
    font = pygame.font.SysFont('arial',25)
    text = font.render("Score: "+str(score),True,black)
    gameDisp.blit(text,(0,0))

# gameloop
while not crashed:

    # choose an event
    for event in pygame.event.get():

        # if window is closed
        if event.type == pygame.QUIT:
            crashed = True

        # checking key event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5

            if event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            x_change = 0


    # filling the display with white color
    gameDisp.fill(white)

    # change coorinates of car
    x += x_change

    # place obstacles
    box(box_w,box_h,box_x,box_y,black)
    box_y += box_s

    # place car
    car(x,y)

    # setting boundaries
    if x < 0 or x + car_width > disp_width:
        crash()
        crashed = True

    # obstacles after obstacles
    if box_y > disp_height:
        box_x = random.randrange(0,disp_width-box_w)
        box_y = -box_h
        score += 1
        ##########################
        # make the game more interesting
        box_s += 1
        ##########################

    # car hits the boxes
    if y < box_y + box_h and y + car_height > box_y:
        if x < box_x + box_w and x + car_width > box_x:
            crash()
            crashed = True

    # display score
    disp_score(score)

    # after any change, you have to update the game window for visual change
    pygame.display.update()

    # setting the FPS of the game
    clock.tick(60)

# stopping pygame
pygame.quit()

# quitting application
quit()
