import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
LX, LY = 1200, 900
screen = pygame.display.set_mode((LX, LY))
number_of_balls = 2
missfine = 100
timefine = 90//FPS//number_of_balls
bonusmin = 30

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
    Draw a new ball in a random place on a screen with a radius
    from r_min to r_max with a color from COLORS except BLACK
    Return parameters of a ball and initial bonus
    """
    r_min, r_max = 10, 100
    margin = r_max
    vmin, vmax = 1,15
    bonus0 = 300
    x = randint(margin, LX-margin)
    y = randint(margin, LY-margin)
    r = randint(10,100)
    color = COLORS[randint(0,len(COLORS)-2)]
    circle(screen, color, (x, y), r)
    vx, vy = randint(vmin,vmax), randint(vmin,vmax)
    return [x,y,r,color,vx,vy,bonus0]

def move_ball(ball):
    """
    Move a ball on a vx,vy. Turn a ball colliding into wall. Return
    new coordinates, radius, color of a ball and new velocities.
    Reduce a bonus for a ball
    """
    x,y,r,color,vx,vy,bonus = ball
    circle(screen, BLACK, (x, y), r)
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

pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0
ticks = 0
balls = []
for ball_number in range(number_of_balls):
    balls.append(new_ball())
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
                    screen.fill(BLACK)
                    balls[i] = new_ball()
                anyhit = anyhit or hit
            if not anyhit: 
                points -= missfine
                print(points, -missfine)
                screen.fill(BLACK)
    for number in range(number_of_balls):
        balls[number] = move_ball(balls[number])
    pygame.display.update()

pygame.quit()