import pygame
import math
import random
player_vehicle = pygame.image.load("monster.png")
camper = pygame.image.load("camper.png")
car = pygame.image.load("car.png")
treeimg = pygame.image.load("Pine Trees/Tree - Pine 00.png")
monstersmall = pygame.image.load("monster-small.png")
foximg = pygame.image.load("Animals/fox.png")
start_screen = True
pygame.display.set_caption("Fox-Hopper | Update 1.0")
def iscol(player1x, player2x, player1y, player2y):
    distance_eq = math.sqrt((math.pow(player1x - player2x, 2)) + (math.pow(player1y - player2y, 2)))
    if distance_eq < 125:
        return True
    else:
        return False
class player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def draw(self):
        if make_small == False:
            win.blit(player_vehicle, (self.x, self.y))
        if make_small == True:
            win.blit(monstersmall, (self.x, self.y))
            print('Changed Lane')
class tree:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def draw(self):
        win.blit(treeimg, (self.x, self.y))
class obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        win.blit(foximg, (self.x, self.y))
player = player(50, 280, 10)
tree = tree(300, 25, 3)
obstacle = obstacle(800, 400)
pygame.init()
win = pygame.display.set_mode((700, 500))


make_small = False

run = True
small = 0
smallyes = False
sc = 0
timeup = 200
while run:
    pygame.mixer.music.load('sound.wav')
    pygame.mixer.music.play(-1)
    win.fill((183, 197, 191))
    keypress = pygame.key.get_pressed()
    tree.x-=tree.speed
    obstacle.x -= 6
    if iscol(player.x,obstacle.x,player.y,obstacle.y) and make_small == False:
        sc -= 30
        obstacle.x = random.randint(6000, 8000)
    if obstacle.x <= -100:
        obstacle.x = random.randint(6000, 8000)
        sc += 30
    if tree.x <= -250:
        tree.x = 750
        timeup -= 1
    if smallyes == True:
        small += 1
        make_small = True
    if small >= 50:
        smallyes = False
        small = 0
    if smallyes == False:
        make_small = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tree.speed += 0.2
            if event.key == pygame.K_a:
                tree.speed += 0.2
                smallyes = True
    speed = int(tree.speed)
    speed_label = pygame.font.SysFont('freesansbold.tff', 25).render("Speed: " + str(speed) + " MPH", 1, (0, 0, 0))
    win.blit(speed_label, (5, 5))
    directions = pygame.font.SysFont('freesansbold.tff', 25).render("SPACE - Increase Spd / A - Change Lanes | Left: " + str(timeup)  + " | Score: " + str(sc), 1, (0, 0, 0))
    win.blit(directions, (150, 5))
    score = pygame.font.SysFont('freesansbold.tff', 25).render("Score: " + str(sc), 1,(0, 0, 0))
    win.blit(score, (5, 400))
    timeleft = pygame.font.SysFont('freesansbold.tff', 25).render("Time Left: " + str(timeup), 1,(0, 0, 0))
    win.blit(timeleft, (400, 400))
    if timeup == 0:
        gameover = pygame.font.SysFont('freesansbold.tff', 25).render("Game Over!", 1, (0, 0, 0))
        win.blit(gameover, (350, 250))
    pygame.draw.rect(win, (40, 70, 0), (0, 360, 900, 250))
    pygame.draw.rect(win, (70, 70, 70), (0, 370, 900, 250))
    tree.draw()
    obstacle.draw()
    player.draw()
    pygame.display.update()
pygame.quit()
