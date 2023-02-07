import pygame
import time
import random
import sys

HEIGHT = 800
WEIGHT = 1000
BG_COLOR = 'black'

sc = pygame.display.set_mode((WEIGHT, HEIGHT))
sc.fill(BG_COLOR)

next_dot = None
dots = [(50, 50), (WEIGHT-50, 50), (WEIGHT // 2, HEIGHT-50)]

def dot_in_center(dot1, dot2):
    new_dot = ((dot1[0] + dot2[0]) / 2, (dot1[1] + dot2[1]) / 2)
    return new_dot


for dot in dots:
    pygame.draw.circle(sc, 'lime', dot, 5, 2)
pygame.display.update()

next_dot = dots[0]
while True:
    next_dot = dot_in_center(next_dot, random.choice(dots))
    pygame.draw.circle(sc, 'aqua', next_dot, 1, 1)
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    time.sleep(0.1)






