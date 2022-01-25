import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
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
    """
    r_min, r_max = 10, 100
    margin = r_max
    x = randint(margin, LX-margin)
    y = randint(margin, LY-margin)
    r = randint(10,100)
    color = COLORS[randint(0,len(COLORS)-2)]
    circle(screen, color, (x, y), r)
    return (x,y,r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0]-x)**2+(event.pos[1]-y)**2 <= r**2:
                points +=1
                print(points)
    
    (x,y,r) = new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()