import pygame
import random
from pygame.locals import *

run=True
xmax=600
ymax=600
food=True
foodpos=[0,0]
score=0
collision = False
score = 0
path="up"
count=0
reset = False

again=Rect(xmax//2 - 80 ,ymax//2,160,40)

bodyout=(0, 128, 0)
bodyin=(128, 204, 255)

cell=15
snake=[[xmax//2,ymax//2]]
snake.append([xmax//2,ymax//2 + cell])
snake.append([xmax//2,ymax//2 + cell*2])
snake.append([xmax//2,ymax//2 + cell*3])
snake.append([xmax//2,ymax//2 + cell*4])

pygame.init() 
font=pygame.font.SysFont(None,30)                                                       #initialized pygames
screen=pygame.display.set_mode((xmax,ymax))                                             #display created
pygame.display.set_caption('Snake')

def outscore():                                                                         #score displayer
    out = ' Score : ' + str(score)
    image=font.render(out,True,(255,0,0))
    screen.blit(image,(0,0))

def collision_detection(collision):                                                     #collision detector
    for item in snake[1:]:
        if item == snake[0]:
            return True
    if snake[0][0] < 0 or snake[0][0] > xmax :
        return True
    elif snake[0][1] < 0 or snake[0][1] > ymax:
        return True
    return False

def game_over():                                                                        #game over message 
    pygame.draw.rect(screen,(90,180,0),(xmax//2-80,ymax//2-60,160,40))
    txt="Game Over!"
    image=font.render(txt,True,(255,0,0))
    screen.blit(image,(xmax//2-55,ymax//2-50))

    txt="Play again"                                                                     #play again message
    image=font.render(txt,True,(255,0,0))
    pygame.draw.rect(screen,(95,190,10),again)
    screen.blit(image,(xmax//2-50,ymax//2+10))

while run:
    screen.fill((89,179,0))
    outscore()

    for events in pygame.event.get():                                                   # event checker
        if events.type ==  pygame.QUIT:
            run =False
        elif events.type == KEYDOWN :
            if events.key == pygame.K_UP and path != 'down' or events.key == pygame.K_w and path != 'down' :
                path = 'up'
            if events.key == pygame.K_DOWN and path != 'up' or events.key == pygame.K_s and path != 'up':
                path = 'down'
            if events.key == pygame.K_LEFT and path != 'right' or events.key == pygame.K_a and path != 'right':
                path = 'left'
            if events.key == pygame.K_RIGHT and path != 'left' or events.key == pygame.K_d and path != 'left':
                path= 'right'
            if events.key == pygame.K_RETURN and collision == True:
                reset=True
        elif events.type == MOUSEBUTTONUP or reset == True:
            pos=pygame.mouse.get_pos()
            if again.collidepoint(pos) or reset == True:                                # reseting game variables
                score=0
                collision = False
                score = 0
                path="up"
                snake=[[xmax//2,ymax//2]]
                snake.append([xmax//2,ymax//2 + cell])
                snake.append([xmax//2,ymax//2 + cell*2])
                snake.append([xmax//2,ymax//2 + cell*3])
                snake.append([xmax//2,ymax//2 + cell*4])
                reset = False

    

    while food== True:                                                                  #food genrator
        food=False
        foodpos[0] = cell * random.randint(0,xmax // cell -2)
        foodpos[1] = cell * random.randint(0,ymax // cell -2)
        if foodpos in snake :
            food=True

    pygame.draw.rect(screen,(230, 92, 0),(foodpos[0],foodpos[1],cell,cell))            #food drawer


    if snake[0] == foodpos:                                                             #checks if dood has been eaten 
        score +=1
        food = True
        extend = list(snake[-1])                                                        #extend the snake based on its path
        if path =='up':
            extend[1] +=cell
        if path =='down':
            extend[1] -= cell
        if path =='left':
            extend[0] += cell
        if path =='right':
            extend[0] -= cell
        snake.append(extend)

    collision=collision_detection(collision)                                            #checks for collision
    if collision ==False:                                                               
        if count > 180:                     #increase value to decrease snake's speed   #snake mover
            count=0
            snake= snake[-1:] +snake[:-1]
            if path =='up':
                snake[0][0]= snake[1][0]
                snake[0][1]= snake[1][1] - cell
            if path =='down':
                snake[0][0]= snake[1][0]
                snake[0][1]= snake[1][1] + cell
            if path =='left':
                snake[0][0]= snake[1][0] - cell
                snake[0][1]= snake[1][1] 
            if path =='right':
                snake[0][0]= snake[1][0] + cell
                snake[0][1]= snake[1][1] 

    if collision == True:
        game_over()                                                                    #game over message
            
            
    head =0                                                                            #snake renderer
    for x in snake:
        if head == 0:
            pygame.draw.rect(screen,bodyout,(x[0],x[1],cell,cell))
            pygame.draw.rect(screen,(255,0,0),(x[0]+1,x[1]+1,cell-3,cell-3))
            head=1
        else:
            pygame.draw.rect(screen,bodyout,(x[0],x[1],cell,cell))
            pygame.draw.rect(screen,bodyin,(x[0]+1,x[1]+1,cell-3,cell-3))




    pygame.display.update()
    count+=1

pygame.quit()



