import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800,600))
background=pygame.image.load('tsis 7/background.jpg')
screen.blit(background,(0,0))
min=pygame.image.load('tsis 7/min.png')
sec=pygame.image.load('tsis 7/sec.png')
clock=pygame.time.Clock()

def time(t):
    return 360 - t*6

def rotate(surface, image, position, angle):
    r_im = pygame.transform.rotate(image, angle)
    r_an = r_im.get_rect(center = image.get_rect(topleft = position).center)
    screen.blit(r_im, (r_an) )
    

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    screen.blit(background,(0,0))
    t=datetime.datetime.now()
    an_min=time(t.minute)
    an_sec=time(t.second)
    rotate(screen, min, (255,150) , an_min)
    rotate(screen, sec, (255, 150), an_sec)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()