import pygame
import random
import numpy as np
from pygame.draw import *
pygame.init()

FPS = 30
LX, LY = 1200, 900
screen = pygame.display.set_mode((LX, LY))
number_of_balls = 2
number_of_ovals = 2
missfine = 100
timefine = 90/FPS/number_of_balls

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
BALL_COLORS = [RED, GREEN, BLUE]
OVAL_COLORS = [YELLOW, MAGENTA, CYAN]


class Ball:
    def __init__(self):
        """
        Draw a new ball in a random place on a screen with a radius
        from r_min to r_max with a RED, GREEN or BLUE color
        Return a list with parameters of a ball and initial bonus:
        x,y - coordinates of the center
        """
        rmin, rmax = 11, 100
        margin = rmax
        vmin, vmax = 1,13
        bonusmin, bonusmax = 100, 300
        self.x = random.randint(margin, LX-margin)
        self.y = random.randint(margin, LY-margin)
        self.r = random.randint(10,100)
        self.color = random.choice(BALL_COLORS)
        self.vx, self.vy = random.randint(vmin,vmax), random.randint(vmin,vmax)
        if rmin == rmax:
            self.bonus = (bonusmax+bonusmin)//2
        else:
            self.bonus = (bonusmax-bonusmin)//(rmin-rmax)*(self.r-rmin) + \
                bonusmax
        circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """
        Move a ball on a vx,vy. Turn a ball colliding into wall. Return
        new coordinates, radius, color of a ball and new velocities.
        Reduce a bonus for a ball
        """
        self.x += self.vx
        self.y += self.vy
        collide_leftright = (self.x > LX-self.r) or (self.x < self.r)
        collide_updown = (self.y > LY-self.r) or (self.y < self.r)
        if collide_leftright:
            self.x -= 2*self.vx
            self.vx = -self.vx
        if collide_updown:
            self.y -= 2*self.vy
            self.vy = -self.vy
        circle(screen, self.color, (self.x, self.y), self.r)
        bonusmin = 50
        if self.bonus > bonusmin:
            self.bonus -= timefine
        else:
            self.bonus = bonusmin
    
    def hit(self, mouse_x, mouse_y):
        return (mouse_x-self.x)**2+(mouse_y-self.y)**2 <= self.r**2

class Oval:
    def __init__(self):
        """
        Draw a new ellipse in a random place on a screen with width and height
        a=b=100 with a YELLOW, CYAN or MAGENTA color
        Return a list with parameters of an ellipse, initial and current bonus:
        x,y - coordinates of the center
        """
        self.time = 0
        self.a0, self.b0 = 99, 99
        self.a, self.b = self.a0, self.b0
        margin = max(self.a0,self.b0)
        vmin, vmax = 1,13
        self.bonus0 = 400
        self.bonus = self.bonus0
        self.x = random.randint(margin, LX-margin)
        self.y = random.randint(margin, LY-margin)
        self.color = random.choice(OVAL_COLORS)
        self.vx, self.vy = random.randint(vmin,vmax), random.randint(vmin,vmax)
        ellipse(screen, self.color,
                (self.x-self.a0//2, self.y-self.b0//2, self.a0, self.b0))

    def move(self):
        """
        Moves an oval on a vx,vy. Turn an oval colliding into wall. Changes
        the shape of the oval. Returns new coordinates, initial width and
        height (a0, b0), new width and height (a,b), color, new velocities,
        existing time, initial bonus and current bonus
        """
        self.time +=1
        self.x += self.vx
        self.y += self.vy
        collide_leftright = (self.x > LX-max(self.a0,self.b0)) or \
            (self.x < max(self.a0,self.b0))
        collide_updown = (self.y > LY-max(self.a0,self.b0)) or \
            (self.y < max(self.a0,self.b0))
        if collide_leftright:
            self.x -= 2*self.vx
            self.vx = -self.vx
        if collide_updown:
            self.y -= 2*self.vy
            self.vy = -self.vy
        self.a = self.a0*(1+np.sin(self.time*np.pi/30))+1
        self.b = self.b0*(1-np.sin(self.time*np.pi/30))+1
        ellipse(screen, self.color,
                (self.x-self.a//2, self.y-self.b//2, self.a, self.b))
        self.bonus = int(self.bonus0*(1-np.sin(self.time*np.pi/15)))
    
    def hit(self, mouse_x, mouse_y):
        return 4*(mouse_x-self.x)**2/self.a**2 + \
                    4*(mouse_y-self.y)**2/self.b**2 <= 1

def save_score(points):
    """
    Saves your score in Catch_a_ball_stat.txt
    Print your place and name of the file with statistics
    """
    name = input('Enter your name\n')
    #copy the results from file to the list "results"
    input_stat = open(r'catch_a_ball_stat.txt','r')
    results = input_stat.readlines()
    input_stat.close()
    #save a new list with new results
    new_results, place = change_results(results,name,points)
    #write new results to the file
    output_stat = open(r'catch_a_ball_stat.txt', 'w')
    output_stat.write(''.join(new_results))
    output_stat.close()
    print('Your place is '+str(place))
    print('See the results in Catch_a_ball_stat.txt')
    
def change_results(results,name,points):
    """
    Returns a list of strings with a new element with player's
    points (place points name) and player's place
    results - list of strings with previous results
    name - player's name
    points - player's final points
    """
    #for the first entry in file special instructions
    if results == []:
        results.append('1 '+str(points)+' '+name)
        return results, 1
    #finding player position
    position = 0
    for result in results:
        if points <= int(result.split()[1]):
            position +=1
    #add a new result in the end or in the middle
    if position == len(results):
        results.insert(position, 
                       '\n'+str(position+1)+' '+str(points)+' '+name)
    else:
        results.insert(position,
                       str(position+1)+' '+str(points)+' '+name+'\n')
        #changing the places for the rest of the list
        for i in range(position+1,len(results)-1):
            results[i] = \
                str(i+1)+' '+results[i].split()[1]+' '+\
                results[i].split()[2]+'\n'
        results[-1] = str(len(results))+' '+\
                      results[len(results)-1].split()[1]+' '+\
                      results[len(results)-1].split()[2]
    #return a list of new results and player's place
    return results, position+1
    
clock = pygame.time.Clock()
finished = False
points = 0
#Creating objects
balls = [Ball(),Ball()]
ovals = [Oval(),Oval()]
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        window_closed = event.type == pygame.QUIT
        escape_pressed = \
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        if window_closed or escape_pressed:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            anyhit = False
            for ball in balls:
                if ball.hit(event.pos[0],event.pos[1]):
                    points += int(ball.bonus)
                    print(points, int(ball.bonus))
                    balls.remove(ball)
                    balls.append(Ball())
                anyhit = anyhit or ball.hit(event.pos[0],event.pos[1])
            for oval in ovals:
                if oval.hit(event.pos[0],event.pos[1]):
                    points += oval.bonus
                    print(points, oval.bonus)
                    ovals.remove(oval)
                    ovals.append(Oval())
                anyhit = anyhit or oval.hit(event.pos[0],event.pos[1])
            if not anyhit: 
                points -= missfine
                print(points, -missfine)
    #Moving objects
    for ball in balls:
        ball.move()
    for oval in ovals:
        oval.move()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

save_score(points)
