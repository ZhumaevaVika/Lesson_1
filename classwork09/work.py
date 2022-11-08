import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 120
SCORE = 0
POINT = 50
COMBO = 0
K_COMBO = 0.01
COMBO_BREAK = 0
MISSES = 0
TARGET_COUNT = 0
ACCURACY = 0.0
POS_X_PREV = 0
POS_Y_PREV = 0
FRAME_COUNT = 0
IS_GAMEOVER = 0
BALLS = []

screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def text_update(SCORE=0, ACCURACY=0.0, COMBO=0):
    global IS_GAMEOVER
    font = pygame.font.Font('freesansbold.ttf', 32)
    rect(screen, BLACK, (860, 50, 350, 100))
    rect(screen, BLACK, (30, 775, 200, 50))
    SCORE = 'SCORE  ' + str(SCORE)
    text = font.render(SCORE, True, WHITE)
    screen.blit(text, (930, 50))
    ACCURACY = 'ACCURACY  ' + str(ACCURACY) + ' %'
    text = font.render(ACCURACY, True, WHITE)
    screen.blit(text, (860, 100))
    COMBO = 'COMBO  ' + str(COMBO)
    text = font.render(COMBO, True, WHITE)
    screen.blit(text, (30, 775))
    if IS_GAMEOVER == 1:
        font = pygame.font.Font('freesansbold.ttf', 128)
        DEATH = 'YOU DIED'
        text = font.render(DEATH, True, RED)
        screen.blit(text, (275, 310))

def weigh_point(POINT, COMBO):
    return int(POINT * (1 + K_COMBO * COMBO))

def new_ball():
    global x, y, r, color
    x = randint(100, 800)
    y = randint(100, 650)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    circle(screen, tuple(0.5*i for i in color), (x, y), r/1.25)
    circle(screen, tuple(0.33*i for i in color), (x, y), r/2)
    BALLS.append([x, y, r])

def mov_ball():
    global x, y, r, color
    dx = 100
    dy = 100
    # по идее тут должен быть бесконечный цикл, но тогда программа дальше работать не будет
    delete_ball(x, y, r)
    BALLS.remove([x, y, r])
    x += dx
    y += dy
    if (x > 1200-r) or (x < r):
        dx *= -1
    if (y > 900-r) or (y < r):
        dy *= -1
    circle(screen, color, (x, y), r)
    circle(screen, tuple(0.5 * i for i in color), (x, y), r / 1.25)
    circle(screen, tuple(0.33 * i for i in color), (x, y), r / 2)
    BALLS.append([x, y, r])

def delete_ball(x, y, r):
    circle(screen, BLACK, (x, y), r)

def click(event):
    pass

def draw_miss(pos_x, pos_y):
    global POS_X_PREV, POS_Y_PREV
    line(screen, BLACK, (POS_X_PREV - 10, POS_Y_PREV - 10), (POS_X_PREV + 10, POS_Y_PREV + 10), 10)
    line(screen, BLACK, (POS_X_PREV + 10, POS_Y_PREV - 10), (POS_X_PREV - 10, POS_Y_PREV + 10), 10)
    line(screen, RED, (pos_x-10, pos_y-10), (pos_x+10, pos_y+10), 10)
    line(screen, RED, (pos_x + 10, pos_y - 10), (pos_x - 10, pos_y + 10), 10)
    POS_X_PREV = pos_x
    POS_Y_PREV = pos_y

def gameover(BALLS):
    global IS_GAMEOVER, finished
    if len(BALLS)>4:
        screen.fill(BLACK)
        finished = True
        IS_GAMEOVER = 1

pygame.display.update()
clock = pygame.time.Clock()
finished = False
text_update()

while not finished:
    clock.tick(FPS)
    FRAME_COUNT += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(0)
            TARGET_COUNT += 1
            pos_x, pos_y = event.pos
            for ball in BALLS:
                if ((pos_x-ball[0])**2+(pos_y-ball[1])**2<ball[2]**2):
                    COMBO_BREAK = 1
                    delete_ball(ball[0], ball[1], ball[2])
                    BALLS.remove(ball)
                    COMBO += 1
                    SCORE += weigh_point(POINT, COMBO)
                    if ((pos_x-ball[0])**2+(pos_y-ball[1])**2<(ball[2]/1.25)**2):
                        SCORE += weigh_point(POINT, COMBO)
                        if ((pos_x-ball[0])**2 + (pos_y-ball[1])**2 < (ball[2]/2)**2):
                            SCORE += 2*weigh_point(POINT, COMBO)
            if COMBO_BREAK == 0:
                MISSES += 1
                COMBO = 0
                draw_miss(pos_x, pos_y)
            COMBO_BREAK = 0
            ACCURACY = int(SCORE*10000/(TARGET_COUNT*POINT*4*(1+K_COMBO)))/100
            if ACCURACY>100:
                ACCURACY = 100 - (MISSES//TARGET_COUNT)*100
            text_update(SCORE, ACCURACY, COMBO)
    if FRAME_COUNT%60 == 0:
        FRAME_COUNT = 0
        new_ball()
        mov_ball()
    gameover(BALLS)
    print(BALLS)
    pygame.display.update()

text_update(SCORE, ACCURACY, COMBO)
if IS_GAMEOVER == 1:
    image = pygame.image.load("YouDied1.png").convert()
    image = pygame.transform.scale(image, (580, 280))
    screen.blit(image, (280, 475))
    finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()
pygame.quit()