import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
LX, LY = 1200, 900
screen = pygame.display.set_mode((LX, LY))

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

def new_ball():
    """
    Draw a new ball in a random place ona screen with a radius
    from r_min to r_max with a color from COLORS except BLACK
    Return parameters of a ball
    """
    r_min, r_max = 10, 100
    margin = r_max
    x = randint(margin, LX-margin)
    y = randint(margin, LY-margin)
    r = randint(10,100)
    color = COLORS[randint(0,len(COLORS)-2)]
    circle(screen, color, (x, y), r)
    return(x,y,r,color)

def move_ball(x,y,r,color,vx,vy):
    """
    Move a ball on a vx,vy. Return new coordinates
    radius and color of a ball
    """
    circle(screen, BLACK, (x, y), r)
    x += vx
    y += vy
    circle(screen, color, (x, y), r)
    return(x, y, r, color)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0
ticks = 0
(x,y,r,color) = new_ball()
vx, vy = randint(1,10), randint(1,10)
pygame.display.update()

while not finished:
    ticks += 1
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0]-x)**2+(event.pos[1]-y)**2 <= r**2:
                points += 1
                screen.fill(BLACK)
                (x,y,r,color) = new_ball()
                vx, vy = randint(1,10), randint(1,10)
                print(points)
    (x,y,r,color) = move_ball(x,y,r,color,vx,vy)
    pygame.display.update()

pygame.quit()