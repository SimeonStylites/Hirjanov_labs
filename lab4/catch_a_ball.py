import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
LX, LY = 1200, 900
screen = pygame.display.set_mode((LX, LY))
number_of_balls = 2
number_of_ovals = 2
missfine = 100
timefine = 90//FPS//number_of_balls
bonusmin = 30

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
COLORS = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, BLACK]

def new_ball():
    """
    Draw a new ball in a random place on a screen with a radius
    from r_min to r_max with a RED, GREEN or BLUE color
    Return a list with parameters of a ball and initial bonus
    """
    rmin, rmax = 11, 100
    margin = rmax
    vmin, vmax = 1,13
    bonusmin, bonusmax = 100, 300
    x = randint(margin, LX-margin)
    y = randint(margin, LY-margin)
    r = randint(10,100)
    color = COLORS[randint(0,2)]
    circle(screen, color, (x, y), r)
    vx, vy = randint(vmin,vmax), randint(vmin,vmax)
    if rmin == rmax:
        bonus0 = (bonusmax+bonusmin)//2
    else:
        bonus0 = (bonusmax-bonusmin)//(rmin-rmax)*(r-rmin)+bonusmax
    return [x,y,r,color,vx,vy,bonus0]
    
def new_oval():
    """
    Draw a new ellipse in a random place on a screen with width and height
    a=b=100 with a YELLOW, CYAN or MAGENTA color
    Return a list with parameters of an ellipse, initial and current bonus
    """
    a0, b0 = 100, 100
    a,b = a0,b0
    margin = max(a0,b0)
    vmin, vmax = 1,13
    bonus0 = 400
    bonus = bonus0
    x = randint(margin, LX-margin)
    y = randint(margin, LY-margin)
    color = COLORS[randint(3,5)]
    ellipse(screen, color, (x-a0//2, y-b0//2, a0, b0))
    vx, vy = randint(vmin,vmax), randint(vmin,vmax)
    return [x,y,a0,b0,a,b,color,vx,vy,0,bonus0,bonus]

def move_ball(ball):
    """
    Move a ball on a vx,vy. Turn a ball colliding into wall. Return
    new coordinates, radius, color of a ball and new velocities.
    Reduce a bonus for a ball
    """
    x,y,r,color,vx,vy,bonus = ball
    x += vx
    y += vy
    collide_leftright = (x > LX-r) or (x < r)
    collide_updown = (y > LY-r) or (y < r)
    if collide_leftright:
        x -= 2*vx
        vx = -vx
    if collide_updown:
        y -= 2*vy
        vy = -vy
    circle(screen, color, (x, y), r)
    if bonus > bonusmin:
        bonus -= timefine
    else:
        bonus = bonusmin
    return [x, y, r, color, vx, vy, bonus]

def move_oval(oval):
    """
    Move an oval on a vx,vy. Turn an oval colliding into wall. Chenage the shape of
    te oval. Return new coordinates, initial width and height (a0, b0),
    new width and height (a,b), color, new velocities, existing time,
    initial bonus and current bonus
    """
    x,y,a0,b0,a,b,color,vx,vy,time,bonus0,bonus = oval
    time +=1
    x += vx
    y += vy
    collide_leftright = (x > LX-max(a0,b0)) or (x < max(a0,b0))
    collide_updown = (y > LY-max(a0,b0)) or (y < max(a0,b0))
    if collide_leftright:
        x -= 2*vx
        vx = -vx
    if collide_updown:
        y -= 2*vy
        vy = -vy
    a = a0*(1+np.sin(time*np.pi/30))
    b = b0*(1-np.sin(time*np.pi/30))
    ellipse(screen, color, (x-a//2, y-b//2, a, b))
    bonus = int(bonus0*(1-np.sin(time*np.pi/15)))
    return [x, y, a0, b0, a, b, color, vx, vy, time, bonus0, bonus]

pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0
ticks = 0
balls = []
ovals = []
for ball_number in range(number_of_balls):
    balls.append(new_ball())
for oval_number in range(number_of_ovals):
    ovals.append(new_oval())
pygame.display.update()

while not finished:
    ticks += 1
    clock.tick(FPS)
    for event in pygame.event.get():
        window_closed = event.type == pygame.QUIT
        escape_pressed = \
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        if window_closed or escape_pressed:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            anyhit = False
            for i in range(number_of_balls):
                hit = (event.pos[0]-balls[i][0])**2+\
                          (event.pos[1]-balls[i][1])**2 <= balls[i][2]**2
                if hit:
                    points += balls[i][6]
                    print(points, balls[i][6])
                    balls[i] = new_ball()
                anyhit = anyhit or hit
            for i in range(number_of_ovals):
                hit = 4*(event.pos[0]-ovals[i][0])**2/ovals[i][4]**2+\
                      4*(event.pos[1]-ovals[i][1])**2/ovals[i][5]**2 <= 1
                if hit:
                    points += ovals[i][11]
                    print(points, ovals[i][11])
                    ovals[i] = new_oval()
                anyhit = anyhit or hit
            if not anyhit: 
                points -= missfine
                print(points, -missfine)
    for number in range(number_of_balls):
        balls[number] = move_ball(balls[number])
    for number in range(number_of_ovals):
        ovals[number] = move_oval(ovals[number])
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()