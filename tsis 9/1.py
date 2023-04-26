import pygame
import random
import time

pygame.init()

# colors
black = pygame.Color(0, 0, 0)         
white = pygame.Color(255, 255, 255)   
red = pygame.Color(255, 0, 0)       
green = pygame.Color(0, 255, 0)      


height=600
width =400
screen = pygame.display.set_mode((width, height))
background = pygame.image.load('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\Background.png')
screen.blit(background, (0, 0))
pygame.mixer.music.load('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\audio.mp3')
pygame.mixer.music.play()

pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\for 1\\icon.jpg'))

clock = pygame.time.Clock()
font_small = pygame.font.SysFont("", 30)
collection = ('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\for 1\\tsis9_racing_collection.wav')

# Sprites

Player = ('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\for 1\\Player.png')
Enemy = ('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\Enemy.png')
Bronze = ('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\Bronze_Coin .jpeg')
Gold = ('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\Gold_Coin.jpeg')
Platinum = ('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\Platinum_Coin.jpeg')
Silver = ('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\Silver_Coin.jpeg')

# Points

minutes = seconds = 0
speed = 5
counter = 0
check = 6

# Player car

class Player_car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Player)
        self.image = pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    # movement of player

    def movement(self):
        pressed = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.bottom < height:
            if pressed[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.top > 0:
            if pressed[pygame.K_UP]:
                self.rect.move_ip(0, -5)


# Enemies

class Enemy(pygame.sprite.Sprite):
    # setting enemy car

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:\\pp2_22B\\pp2-22B050830-1\\tsis 9\\Enemy.png')
        self.image = pygame.transform.scale(self.image, (35, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)

    # movement

    def movement(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width-40), 0)

# Bronze Coin


class Bronze_Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Bronze)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)

    def calling_of_bronze(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, width-40), 0)

    def movement(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            self.calling_of_bronze()


# Silver Coin


class Silver_Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Silver)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)

    def calling_of_silver(self):
        self.rect.top = 0
        self.rect.center = (random.randint(35, width-35), 0)

    def movement(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > height:
            self.calling_of_silver()

# Gold Coin
class Golden_Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Gold)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)

    def calling_of_golden(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, width-40), 0)

    def movement(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > height:
            self.calling_of_golden()

# Platinum Coin
class Platinum_Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Platinum)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(25, width-25), 0)

    def calling_of_platinum(self):
        self.rect.top = 0
        self.rect.center = (random.randint(25, width-25), 0)

    def movement(self):
        self.rect.move_ip(0, 2)
        if self.rect.top > height:
            self.calling_of_platinum()

# After crush

def game_over():

    # setting end game surfacse

    boom = pygame.image.load('boom.jpeg')
    gameover = pygame.Surface(screen.get_size())
    gameover.fill((255, 0, 0))
    font = pygame.font.SysFont("", 80)
    text = font.render("GAME OVER", False, (0, 0, 0))
    crash_sound = pygame.mixer.Sound('for_crash.wav')


    # blit surfaces

    pygame.mixer.music.stop()
    crash_sound.play()
    gameover.blit(text, (25, 200))
    screen.blit(boom, (25, 150))
    pygame.display.update()
    time.sleep(2)
    screen.blit(gameover, (0, 0))
    pygame.display.update()
    time.sleep(1)


# Create sprites

P1 = Player_car()
E1 = Enemy()
E2 = Enemy()
E3 = Enemy()
E4 = Enemy()
B1 = Bronze_Coin()
B2 = Bronze_Coin()
S1 = Silver_Coin()
G1 = Golden_Coin()
Pl1 = Platinum_Coin()

# Create Groups

Sprites = pygame.sprite.Group()
Players = pygame.sprite.Group()
Enemies = pygame.sprite.Group()
Bronzes = pygame.sprite.Group()
Silvers = pygame.sprite.Group()
Golds = pygame.sprite.Group()
Platinums = pygame.sprite.Group()

# adding into groups

Sprites.add(P1)
Sprites.add(E1)
Sprites.add(B1)
Sprites.add(S1)
Players.add(P1)
Enemies.add(E1)
Bronzes.add(B1)
Silvers.add(S1)

# main loop

exit = True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    # Difficulty

    if counter >= 10 and counter <= 13:
        speed += 0.005
        Sprites.add(B2)
        Bronzes.add(B2)

    if counter >= 20 and counter <= 23:
        speed += 0.005
        Sprites.add(B2)
        Enemies.add(B2)
        Golds.add(G1)
        Sprites.add(G1)

    if counter >= 40 and counter <= 43:
        speed += 0.010
        Sprites.add(E3)
        Enemies.add(E3)
        Platinums.add(P1)
        Sprites.add(P1)

    if check*10 < counter:
        speed += 0.005
        check += 2

    if counter >= 120 and counter <= 130:
        Sprites.add(E4)
        Enemies.add(E4)
    
    # Conditions for crushing

    if pygame.sprite.spritecollideany(P1, Enemies):
        game_over()
        exit = False

    # Conditions for coins

    if pygame.sprite.spritecollideany(B1, Players):
        counter += 1
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))
        B1.calling_of_bronze()

    if pygame.sprite.spritecollideany(B2, Players):
        counter += 1
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))
        B2.calling_of_bronze()

    if pygame.sprite.spritecollideany(S1, Players):
        counter += 2
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))
        S1.calling_of_silver()

    if pygame.sprite.spritecollideany(G1, Players):
        counter += 4
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))
        G1.calling_of_golden()

    if pygame.sprite.spritecollideany(Pl1, Players):
        counter += 7
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))
        Pl1.calling_of_platinum()

    # Blitting

    screen.blit(background, (0, 0))
    scores = font_small.render("Timer: "+str(minutes)+":"+str(round(seconds)), True, (0,0,0))
    screen.blit(scores, (10, 10))

    for sprite in Sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.movement()

    text = font_small.render("Coins:"+str(counter), True, (0, 0, 0))
    screen.blit(text, (300, 10))
    seconds += 0.01
    if (seconds == 60):
        seconds = 0
        minutes += 1

    # updating

    pygame.display.update()
    clock.tick(60)