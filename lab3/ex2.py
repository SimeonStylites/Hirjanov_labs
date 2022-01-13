import numpy as np
import pygame
from pygame.draw import *

def rot_ellipse(x0,y0,a,b,alpha,color):
    for x in range(x0-a,y0+a):
        for y in range(x0-a,y0+a):
            x1 = x-x0
            y1 = y-y0
            x2 = x1*np.cos(alpha)-y1*np.sin(alpha)
            y2 = x1*np.sin(alpha)+y1*np.cos(alpha)
            s = x2**2/a**2+y2**2/b**2
            if s <= 1:
                line(screen,color,(x,y),(x,y))

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800,1100))

#house
rect(screen,(128,102,0),(0,0,800,1100))
rect(screen,(85,68,0),(0,0,800,500))
rect(screen,(213,255,230),(420,20,373,460))
rect(screen,(135,205,222),(440,40,333,425))
line(screen,(213,255,230),(607,20),(607,475),20)
line(screen,(213,255,230),(420,200),(790,200),30)

#wool ball
for i in range(300):
    line(screen,(153,153,153),(140+i,1050+20*np.sin(i/30)),
         (141+i,1050+20*np.sin((i+1)/30)))
circle(screen,(153,153,153),(500,970),90)
circle(screen,(0,0,0),(500,970),90,1)
arc(screen,(0,0,0),(480-15,880,250,300),np.pi*5/6,np.pi,1)
arc(screen,(0,0,0),(480+15,880+15,250,300),np.pi*5/6,np.pi,1)
arc(screen,(0,0,0),(480-40,880-15,250,300),np.pi*5/6,np.pi,1)
arc(screen,(0,0,0),(240,880,350,250),np.pi/6,np.pi/3,1)
arc(screen,(0,0,0),(325,905,250,250),np.pi/12,np.pi*2/5,1)
arc(screen,(0,0,0),(340,917,200,200),-np.pi/12,np.pi*2/5,1)

#cat body and head
rot_ellipse(700,700,200,50,-np.pi/6,(0,0,0))
rot_ellipse(700,700,199,49,-np.pi/6,(200,113,55))
ellipse(screen,(200,113,55),(120,520,530,280),0)
ellipse(screen,(0,0,0),(120,520,530,280),1)
circle(screen,(200,113,55),(575,730),85)
circle(screen,(0,0,0),(575,730),85,1)
ellipse(screen,(200,113,55),(624,745,55,140),0)
ellipse(screen,(0,0,0),(624,745,55,140),1)
ellipse(screen,(200,113,55),(155,740,120,75),0)
ellipse(screen,(0,0,0),(155,740,120,75),1)
ellipse(screen,(200,113,55),(90,650,75,120),0)
ellipse(screen,(0,0,0),(90,650,75,120),1)
circle(screen,(200,113,55),(165,642),100)
circle(screen,(0,0,0),(165,642),100,1)

#eyes
circle(screen,(136,170,0),(123,652),30)
circle(screen,(0,0,0),(123,652),30,1)
circle(screen,(136,170,0),(207,652),30)
circle(screen,(0,0,0),(207,652),30,1)
ellipse(screen,(0,0,0),(126,626,8,52))
ellipse(screen,(0,0,0),(210,626,8,52))
rot_ellipse(117,642,15,5,-np.pi*11/36,(255,255,255))
rot_ellipse(201,642,15,5,-np.pi*11/36,(255,255,255))

#ears
polygon(screen,(200,113,55),[(50,550),(75,620),(110,565),(50,550)])
polygon(screen,(0,0,0),[(50,550),(75,620),(110,565),(50,550)],1)
polygon(screen,(222,170,135),[(55,555),(76,612),(105,568),(55,555)])
polygon(screen,(0,0,0),[(55,555),(76,612),(105,568),(55,555)],1)
polygon(screen,(200,113,55),[(280,550),(255,620),(220,565),(280,550)])
polygon(screen,(0,0,0),[(280,550),(255,620),(220,565),(280,550)],1)
polygon(screen,(222,170,135),[(275,555),(254,612),(225,568),(275,555)])
polygon(screen,(0,0,0),[(275,555),(254,612),(225,568),(275,555)],1)

#nose
polygon(screen,(222,170,135),[(165,697),(155,687),(175,687),(165,697)])
polygon(screen,(0,0,0),[(165,697),(155,687),(175,687),(165,697)],2)
line(screen,(0,0,0),(165,697),(165,712),2)
arc(screen,(0,0,0),(164,698,20,20),np.pi*7/6,np.pi*10/6,2)
arc(screen,(0,0,0),(148,698,20,20),np.pi*8/6,np.pi*11/6,2)

#whiskers
arc(screen,(20,20,20),(97,689,300,300),np.pi*63/180,np.pi*63/180+np.pi/4,1)
arc(screen,(20,20,20),(92,698,300,300),np.pi*60/180,np.pi*60/180+np.pi/4,1)
arc(screen,(20,20,20),(87,710,300,300),np.pi*57/180,np.pi*57/180+np.pi/4,1)
arc(screen,(20,20,20),(-67,689,300,300),np.pi*117/180-np.pi/4,np.pi*117/180,1)
arc(screen,(20,20,20),(-62,698,300,300),np.pi*120/180-np.pi/4,np.pi*120/180,1)
arc(screen,(20,20,20),(-57,710,300,300),np.pi*123/180-np.pi/4,np.pi*123/180,1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
pygame.quit()