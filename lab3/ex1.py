import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen,(200,200,200),(0,0,400,400))
circle(screen,(255,255,0),(200,200),100)
circle(screen,(0,0,0),(200,200),100,1)

circle(screen,(255,0,0),(160,175),20)
circle(screen,(0,0,0),(160,175),20,1)
circle(screen,(0,0,0),(160,175),8)
circle(screen,(255,0,0),(240,175),15)
circle(screen,(0,0,0),(240,175),15,1)
circle(screen,(0,0,0),(240,175),8)

line(screen,(0,0,0),(150,255),(250,255),20)
line(screen,(0,0,0),(110,110),(190,170),12)
line(screen,(0,0,0),(290,130),(210,167),10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
