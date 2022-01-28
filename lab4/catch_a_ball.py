import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
LX, LY = 1200, 900
screen = pygame.display.set_mode((LX, LY))
bonus0 = 300
missfine = 100
timefine = 90//FPS

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
    vmin, vmax = 1,15
    x = randint(margin, LX-margin)
    y = randint(margin, LY-margin)
    r = randint(10,100)
    color = COLORS[randint(0,len(COLORS)-2)]
    circle(screen, color, (x, y), r)
    vx, vy = randint(vmin,vmax), randint(vmin,vmax)
    return(x,y,r,color,vx,vy)

def move_ball(x,y,r,color,vx,vy):
    """
    Move a ball on a vx,vy. Turn a ball colliding into wall. Return new coordinates
    radius, color of a ball and new velocities.
    """
    circle(screen, BLACK, (x, y), r)
    x += vx
    y += vy
    A = (x > LX-r) or (x < r)
    B = (y > LY-r) or (y < r)
    if A:
        x -= 2*vx
        vx = -vx
    if B:
        y -= 2*vy
        vy = -vy
    circle(screen, color, (x, y), r)
    return(x, y, r, color, vx, vy)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0
ticks = 0
(x,y,r,color,vx,vy) = new_ball()
bonus = bonus0
pygame.display.update()

while not finished:
    ticks += 1
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0]-x)**2+(event.pos[1]-y)**2 <= r**2:
                points += bonus
                print(points, bonus)
                screen.fill(BLACK)
                (x,y,r,color,vx,vy) = new_ball()
                bonus = bonus0
            else:
                points -= missfine
                print(points, -missfine)
                screen.fill(BLACK)
                (x,y,r,color,vx,vy) = new_ball()
                bonus = bonus0
    (x, y, r, color, vx, vy) = move_ball(x,y,r,color,vx,vy)
    pygame.display.update()
    bonus -= timefine

pygame.quit()