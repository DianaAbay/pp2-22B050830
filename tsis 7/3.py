import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Red Ball")

x=400
y=350



done = False

while not done:
    clock.tick(100)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y-25>0:
                    y-=20
            if event.key == pygame.K_DOWN:
                if y+25<800:
                    y+=20
            if event.key == pygame.K_RIGHT:
                if x+25<800:
                    x+=20
            if event.key == pygame.K_LEFT:
                if x-25>0:
                    x-=20
    pygame.draw.circle(screen , (255, 0 , 0 ) , (x, y) , 25 )
    pygame.display.flip()
pygame.quit()

