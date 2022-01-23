import numpy as np
import pygame
from pygame.draw import *

def rot_ellipse(x0,y0,a,b,alpha,color):
    for x in range(int(x0-a),int(x0+a)):
        for y in range(int(y0-a),int(y0+a)):
            x1 = x-x0
            y1 = y-y0
            x2 = x1*np.cos(alpha)-y1*np.sin(alpha)
            y2 = x1*np.sin(alpha)+y1*np.cos(alpha)
            s = x2**2/a**2+y2**2/b**2
            if s <= 1:
                line(screen,color,(x,y),(x,y),1)

def window(x,y,size = 1):
    lx0 = 373*size
    lx1 = 333*size
    ly0 = 460*size
    ly1 = 420*size
    vert_w = 20*size
    horiz_w = 30*size
    rect(screen,lightblue,(x,y,lx0,ly0))
    rect(screen,blue,(x+(lx0-lx1)/2,y+(ly0-ly1)/2,lx1,ly1))
    line(screen,lightblue,(x+lx0/2,y),(x+lx0/2,y+ly0-1),int(vert_w*size))
    line(screen,lightblue,(x,y+ly0/3),(x+lx0-1,y+ly0/3),int(horiz_w*size))

def woolball(x, y, size = 1, mirror = False):
    r = 90*size
    Alpha = [[np.pi*5/6,np.pi],[np.pi*5/6,np.pi],[np.pi*5/6,np.pi],
             [-np.pi/24,np.pi/3],[-np.pi/32,np.pi*2/5],[-np.pi/32,np.pi*2/5]]
    xs,ys = -33/9*r,6/9*r
    Xlc = [-0.7*r, -0.7*r+r/7, -0.7*r+2*r/7]
    Ylc = [-1.2*r, -1.2*r+r/7, -1.2*r+2*r/7]
    Xrc = [-1.8*r,-1.8*r+r/7,-1.8*r+2*r/7]
    Yrc = [-0.6*r,-0.6*r-r/7,-0.6*r-2*r/7]
    if mirror == True:
        m = -1
        for i in Alpha:
            i[0], i[1] = np.pi-i[1], np.pi-i[0]
        for i in range(3):
            Xlc[i] = -Xlc[i] - r*3
            Xrc[i] = -Xrc[i] - r*2.3
    else:
        m = 1
    for i in range(300):
        k=i*size
        line(screen,grey,
             (x+m*(xs+k), y+(ys+2/9*r*np.sin(i/30))),
             (x+m*(xs+1+k), y+(ys+2/9*r*np.sin((i+1)/30))))
    circle(screen,grey,(x,y),r)
    circle(screen,black,(x,y),r,1)
    arc(screen,black,(x+Xlc[0],y+Ylc[0],r*3,r*3),
        Alpha[0][0],Alpha[0][1],1)
    arc(screen,black,(x+Xlc[1],y+Ylc[1],r*3,r*3),
        Alpha[1][0],Alpha[1][1],1)
    arc(screen,black,(x+Xlc[2],y+Ylc[2],r*3,r*3),
        Alpha[2][0],Alpha[2][1],1)
    arc(screen,black,(x+Xrc[0],y+Yrc[0],r*2.3,r*2.3),
        Alpha[3][0],Alpha[3][1],1)
    arc(screen,black,(x+Xrc[1],y+Yrc[1],r*2.3,r*2.3),
        Alpha[4][0],Alpha[4][1],1)
    arc(screen,black,(x+Xrc[2],y+Yrc[2],r*2.3,r*2.3),
        Alpha[5][0],Alpha[5][1],1)

def kitty(x, y, colorkitty = 0, size = 1.0, mirror = False):
    if colorkitty == orange:
        coloreye = greeneye
        colorear = cream
        view = 1
    elif colorkitty == greykitty:
        coloreye = blueeye
        colorear = lightcream
        view = -1
    r = 100*size
    r_hip = 85/100*r
    x_hip, y_hip = 41/10*r, 88/100*r
    x_tail, y_tail = 53/10*r, 6/10*r
    a_tail, b_tail = 2*r, r/2
    alpha_tail = -np.pi/6
    xe = [-45/100*r,459/100*r,-1/10*r,-75/100*r]
    ye = [-122/100*r,103/100*r,r,8/100*r]
    rxe = [53/10*r,55/100*r,12/10*r,75/100*r]
    xeye1,yeye1 = -42/100*r,1/10*r
    xeye2,yeye2 = -xeye1,yeye1
    xpupil = [-39/100*r,45/100*r,-48/100*r,36/100*r]
    ypupil = [-16/100*r,-16/100*r,0,0]
    left_ear = [[-23/20*r,-23/25*r],[-9/10*r,-11/50*r],[-11/20*r,-77/100*r],
                [-11/10*r,-87/100*r],[-89/100*r,-3/10*r],[-6/10*r,-37/50*r]]
    nose = [[0/100*r,55/100*r],[-10/100*r,45/100*r],[10/100*r,45/100*r],
            [0/100*r,55/100*r],[0/100*r,70/100*r]]
    nosearc = [[-1/100*r,56/100*r],[-17/100*r,56/100*r]]
    dnose = 2/10*r
    noseangle = [[np.pi*7/6,np.pi*10/6],[np.pi*8/6,np.pi*11/6]]
    r_whisk = 3*r
    x_whisk = [-68/100*r,-73/100*r,-78/100*r,-232/100*r,-227/100*r,-222/100*r]
    y_whisk = [47/100*r,56/100*r,68/100*r,47/100*r,56/100*r,68/100*r]
    whisk_angle = [[np.pi*63/180,np.pi*63/180+np.pi/4],
                   [np.pi*60/180,np.pi*60/180+np.pi/4],
                   [np.pi*57/180,np.pi*57/180+np.pi/4],
                   [np.pi*117/180-np.pi/4,np.pi*117/180],
                   [np.pi*120/180-np.pi/4,np.pi*120/180],
                   [np.pi*123/180-np.pi/4,np.pi*123/180]]
    if mirror == True:
        m = -1
        for i in range(4):
            xe[i] = -xe[i]-rxe[i]
        for i in range(2):
            xpupil[i] = -xpupil[i]-7/100*r
    else:
        m = 1
    #cat body and head
    rot_ellipse(x + m*x_tail,y+y_tail,a_tail,b_tail,m*alpha_tail,black)
    rot_ellipse(x + m*x_tail,y+y_tail,a_tail-1,b_tail-1,m*alpha_tail,colorkitty)
    ellipse(screen,colorkitty,(x+xe[0],y+ye[0],rxe[0],28/10*r),0)
    ellipse(screen,black,(x+xe[0],y+ye[0],rxe[0],28/10*r),1)
    circle(screen,colorkitty,(x+m*x_hip,y+y_hip),r_hip)
    circle(screen,black,(x+m*x_hip,y+y_hip),r_hip,1)
    ellipse(screen,colorkitty,(x+xe[1],y+ye[1],rxe[1],14/10*r),0)
    ellipse(screen,black,(x+xe[1],y+ye[1],rxe[1],14/10*r),1)
    ellipse(screen,colorkitty,(x+xe[2],y+ye[2],rxe[2],75/100*r),0)
    ellipse(screen,black,(x+xe[2],y+ye[2],rxe[2],75/100*r),1)
    ellipse(screen,colorkitty,(x+xe[3],y+ye[3],rxe[3],12/10*r),0)
    ellipse(screen,black,(x+xe[3],y+ye[3],rxe[3],12/10*r),1)
    circle(screen,colorkitty,(x,y),r)
    circle(screen,black,(x,y),r,1)
    #eyes
    circle(screen,coloreye,(x+xeye1,y+yeye1),3/10*r)
    circle(screen,black,(x+xeye1,y+yeye1),3/10*r,1)
    circle(screen,coloreye,(x+xeye2,y+yeye2),3/10*r)
    circle(screen,black,(x+xeye2,y+yeye2),3/10*r,1)
    ellipse(screen,black,(x+view*xpupil[0]+0.04*r*(view-1),y+ypupil[0],
            8/100*r,52/100*r))
    ellipse(screen,black,(x+view*xpupil[1]+0.04*r*(view-1),y+ypupil[1],
            8/100*r,52/100*r))
    rot_ellipse(x+view*m*xpupil[2],y+ypupil[2],15/100*r,5/100*r,
                -view*m*np.pi*11/36,white)
    rot_ellipse(x+view*m*xpupil[3],y+ypupil[3],15/100*r,5/100*r,
                -view*m*np.pi*11/36,white) 
    #ears
    polygon(screen,colorkitty,[(x+left_ear[0][0],y+left_ear[0][1]),
                           (x+left_ear[1][0],y+left_ear[1][1]),
                           (x+left_ear[2][0],y+left_ear[2][1]),
                           (x+left_ear[0][0],y+left_ear[0][1])])
    polygon(screen,black,[(x+left_ear[0][0],y+left_ear[0][1]),
                          (x+left_ear[1][0],y+left_ear[1][1]),
                          (x+left_ear[2][0],y+left_ear[2][1]),
                          (x+left_ear[0][0],y+left_ear[0][1])],1)
    polygon(screen,colorear,[(x+left_ear[3][0],y+left_ear[3][1]),
                          (x+left_ear[4][0],y+left_ear[4][1]),
                          (x+left_ear[5][0],y+left_ear[5][1]),
                          (x+left_ear[3][0],y+left_ear[3][1])])
    polygon(screen,black,[(x+left_ear[3][0],y+left_ear[3][1]),
                          (x+left_ear[4][0],y+left_ear[4][1]),
                          (x+left_ear[5][0],y+left_ear[5][1]),
                          (x+left_ear[3][0],y+left_ear[3][1])],1)
    polygon(screen,colorkitty,[(x-left_ear[0][0],y+left_ear[0][1]),
                           (x-left_ear[1][0],y+left_ear[1][1]),
                           (x-left_ear[2][0],y+left_ear[2][1]),
                           (x-left_ear[0][0],y+left_ear[0][1])])
    polygon(screen,black,[(x-left_ear[0][0],y+left_ear[0][1]),
                          (x-left_ear[1][0],y+left_ear[1][1]),
                          (x-left_ear[2][0],y+left_ear[2][1]),
                          (x-left_ear[0][0],y+left_ear[0][1])],1)
    polygon(screen,colorear,[(x-left_ear[3][0],y+left_ear[3][1]),
                          (x-left_ear[4][0],y+left_ear[4][1]),
                          (x-left_ear[5][0],y+left_ear[5][1]),
                          (x-left_ear[3][0],y+left_ear[3][1])])
    polygon(screen,black,[(x-left_ear[3][0],y+left_ear[3][1]),
                          (x-left_ear[4][0],y+left_ear[4][1]),
                          (x-left_ear[5][0],y+left_ear[5][1]),
                          (x-left_ear[3][0],y+left_ear[3][1])],1)
    #nose
    polygon(screen,colorear,[(x+nose[0][0],y+nose[0][1]),
                          (x+nose[1][0],y+nose[1][1]),
                          (x+nose[2][0],y+nose[2][1]),
                          (x+nose[0][0],y+nose[0][1])])
    polygon(screen,black,[(x+nose[0][0],y+nose[0][1]),
                          (x+nose[1][0],y+nose[1][1]),
                          (x+nose[2][0],y+nose[2][1]),
                          (x+nose[0][0],y+nose[0][1])],2)
    line(screen,black,
         (x+nose[3][0],y+nose[3][1]),(x+nose[4][0],y+nose[4][1]),2)
    arc(screen,black,(x+nosearc[0][0],y+nosearc[0][1],dnose,dnose),
        noseangle[0][0],noseangle[0][1],2)
    arc(screen,black,(x+nosearc[1][0],y+nosearc[1][1],dnose,dnose),
        noseangle[1][0],noseangle[1][1],2)
    #whiskers
    arc(screen,darkgrey,(x+x_whisk[0],y+y_whisk[0],r_whisk,r_whisk),
        whisk_angle[0][0],whisk_angle[0][1],1)
    arc(screen,darkgrey,(x+x_whisk[1],y+y_whisk[1],r_whisk,r_whisk),
        whisk_angle[1][0],whisk_angle[1][1],1)
    arc(screen,darkgrey,(x+x_whisk[2],y+y_whisk[2],r_whisk,r_whisk),
        whisk_angle[2][0],whisk_angle[2][1],1)
    arc(screen,darkgrey,(x+x_whisk[3],y+y_whisk[3],r_whisk,r_whisk),
        whisk_angle[3][0],whisk_angle[3][1],1)
    arc(screen,darkgrey,(x+x_whisk[4],y+y_whisk[4],r_whisk,r_whisk),
        whisk_angle[4][0],whisk_angle[4][1],1)
    arc(screen,darkgrey,(x+x_whisk[5],y+y_whisk[5],r_whisk,r_whisk),
        whisk_angle[5][0],whisk_angle[5][1],1)

pygame.init()

lightblue = (213,255,230)
blue = (135,205,222)
dirty = (128,102,0)
wood = (85,68,0)
grey = (153,153,153)
greykitty = (108,93,83)
orange = (200,113,55)
cream = (222,170,135)
lightcream = (244,215,215)
greeneye = (136,170,0)
blueeye = (42,212,255)
black = (0,0,0)
white = (255,255,255)
darkgrey = (20,20,20)

FPS = 30
screen = pygame.display.set_mode((800,1100))

#house
screen.fill(dirty)
rect(screen,wood,(0,0,800,500))

for i in range(3):
    x = -200+i*350
    window(x,20,0.7)
woolball(230,570,0.3,False)
woolball(150,900,0.3,False)
woolball(360,980,1,False)
woolball(570,1050,0.3,False)
woolball(640,750,0.3,True)
woolball(500,800,0.7,True)
woolball(690,930,0.7,True)
kitty(390,580,orange,0.5,False)
kitty(500,920,orange,0.15,False)
kitty(670,1040,greykitty,0.15,False)
kitty(310,750,greykitty,0.5,True)
kitty(140,580,orange,0.15,True)
kitty(155,1040,greykitty,0.15,True)
kitty(720,800,orange,0.15,True)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
pygame.quit()