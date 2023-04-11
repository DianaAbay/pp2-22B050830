import pygame
import os

pygame.init()
screen = pygame.display.set_mode((300,300))
clock=pygame.time.Clock()



direction = "C:\\pp2_22B\\pp2-22B050830-1\\tsis 7\\music\\"
dir = "C:\\pp2_22B\\pp2-22B050830-1\\tsis 7\\image\\"
files=os.listdir(direction)
files1=os.listdir(dir)
current = 0
cur = 0
background=pygame.image.load('tsis 7/image/images.jpg')
screen.blit(background,(0,0))
pygame.mixer.music.load(direction + files[current])


play = pygame.K_SPACE
next = pygame.K_RIGHT
previous = pygame.K_LEFT

pygame.mixer.music.play()

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.KEYDOWN:
            if event.key == play:
                if pygame.mixer.music.get_busy:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == next:
                current = (current + 1) % len(files)
                cur = (cur + 1) % len(files1)
                pygame.mixer.music.load(direction + files[current])
                background1=pygame.image.load('tsis 7/image/im.jpg')
                screen.blit(background1,(0,0))
                pygame.mixer.music.play()

            elif event.key == previous:
                current = (current - 1) % len(files)
                cur = (cur -1) % len(files1)
                pygame.mixer.music.load(direction + files[current])
                background2=pygame.image.load('tsis 7/image/ima.jpg')
                screen.blit(background2,(0,0))
                pygame.mixer.music.play()
    pygame.display.update()
    clock.tick()