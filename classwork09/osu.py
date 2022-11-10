import pygame
from pygame.draw import line, circle, rect
from random import randint
pygame.init()

FPS = 150
FRAME_COUNT = 0
SCORE = 0
ACCURACY = 0.0
POINT = 50
COMBO = 0
K_COMBO = 0.01
COMBO_BREAK = 1
MISSES = 0
DRAW_MISS = 0
TARGET_COUNT = 0
POS_X_PREV = 0
POS_Y_PREV = 0
IS_GAMEOVER = 0
pos_x = 0
pos_y = 0
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


def draw_miss(pos_x, pos_y):
    global POS_X_PREV, POS_Y_PREV
    line(screen, BLACK, (POS_X_PREV - 10, POS_Y_PREV - 10), (POS_X_PREV + 10, POS_Y_PREV + 10), 10)
    line(screen, BLACK, (POS_X_PREV + 10, POS_Y_PREV - 10), (POS_X_PREV - 10, POS_Y_PREV + 10), 10)
    line(screen, RED, (pos_x-10, pos_y-10), (pos_x+10, pos_y+10), 10)
    line(screen, RED, (pos_x + 10, pos_y - 10), (pos_x - 10, pos_y + 10), 10)
    POS_X_PREV = pos_x
    POS_Y_PREV = pos_y
def update_screen(balls, pos_x=0, pos_y=0):
    screen.fill(BLACK)
    for ball in balls:
        circle(screen, ball[3], (ball[0], ball[1]), ball[2])
        circle(screen, tuple(0.5 * i for i in ball[3]), (ball[0], ball[1]), ball[2]/ 1.25)
        circle(screen, tuple(0.33 * i for i in ball[3]), (ball[0], ball[1]), ball[2] / 2)
    if DRAW_MISS == 1:
        draw_miss(pos_x, pos_y)
def text_update(score=0, accuracy=0.0, combo=0):
    global IS_GAMEOVER
    font = pygame.font.Font('freesansbold.ttf', 32)
    rect(screen, BLACK, (860, 50, 350, 100))
    rect(screen, BLACK, (30, 775, 200, 50))
    score = 'SCORE  ' + str(score)
    text = font.render(score, True, WHITE)
    screen.blit(text, (930, 50))
    accuracy = 'ACCURACY  ' + str(accuracy) + ' %'
    text = font.render(accuracy, True, WHITE)
    screen.blit(text, (860, 100))
    combo = 'COMBO  ' + str(combo)
    text = font.render(combo, True, WHITE)
    screen.blit(text, (30, 775))
    if IS_GAMEOVER == 1:
        font = pygame.font.Font('freesansbold.ttf', 128)
        death = 'YOU DIED'
        text = font.render(death, True, RED)
        screen.blit(text, (275, 310))
        image = pygame.image.load("YouDied1.png").convert()
        image = pygame.transform.scale(image, (580, 280))
        screen.blit(image, (280, 475))


def weigh_point(combo):
    return int(POINT * (1 + K_COMBO * combo))
def weigh_accuracy(score, target_count, misses):
    accuracy = int(score * 10000 / (target_count * POINT * 4 * (1 + K_COMBO))) / 100
    if accuracy > 100:
        accuracy = float(100 - (100 * misses // target_count))
    return accuracy


def new_ball():
    x = randint(100, 800)
    y = randint(100, 650)
    r = randint(30, 50)
    speed_x = randint(-100, 100)/100
    speed_y = randint(-100, 100)/100
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    circle(screen, tuple(0.5*i for i in color), (x, y), r/1.25)
    circle(screen, tuple(0.33*i for i in color), (x, y), r/2)
    is_move = randint(0, 2)
    BALLS.append([x, y, r, color, speed_x, speed_y, is_move])
def move_ball(balls):
    for ball in balls:
        if ball[6]:
            ball[0] += ball[4]
            ball[0] = int(ball[0]*100)/100
            ball[1] += ball[5]
            ball[1] = int(ball[1]*100) / 100
            if ball[2] > ball[0] or ball[0] > 1200 - ball[2]:
                ball[4] *= -1
            if ball[2] > ball[1] or ball[1] > 900 - ball[2]:
                ball[5] *= -1


def click(event):
    pass


def game_over(balls):
    global IS_GAMEOVER, finished
    if len(balls) > 4:
        screen.fill(BLACK)
        finished = True
        IS_GAMEOVER = 1


def save_score(score):
    with open("score.txt", "r") as f:
        scor = f.readlines()
        scor = list(map(lambda x: int(x.rstrip()), scor))
    scor.append(score)
    scor.sort()
    scor = scor[::-1]
    with open("score.txt", "w") as f:
        f.writelines(str(x) + '\n' for x in scor)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    FRAME_COUNT += 1
    update_screen(BALLS, pos_x, pos_y)
    text_update(SCORE, ACCURACY, COMBO)
    move_ball(BALLS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(0)
            TARGET_COUNT += 1
            pos_x, pos_y = event.pos
            for ball in BALLS:
                if (pos_x-ball[0])**2+(pos_y-ball[1])**2 < ball[2]**2:
                    COMBO_BREAK = 0
                    BALLS.remove(ball)
                    COMBO += 1
                    DRAW_MISS = 0
                    SCORE += weigh_point(COMBO)
                    if (pos_x-ball[0])**2+(pos_y-ball[1])**2 < (ball[2]/1.25)**2:
                        SCORE += weigh_point(COMBO)
                        if (pos_x-ball[0])**2 + (pos_y-ball[1])**2 < (ball[2]/2)**2:
                            SCORE += 2*weigh_point(COMBO)
            if COMBO_BREAK == 1:
                MISSES += 1
                COMBO = 0
                DRAW_MISS = 1
            COMBO_BREAK = 1
            ACCURACY = weigh_accuracy(SCORE, TARGET_COUNT, MISSES)
    if FRAME_COUNT % 60 == 0:
        FRAME_COUNT = 0
        new_ball()
    game_over(BALLS)
    pygame.display.update()

text_update(SCORE, ACCURACY, COMBO)
save_score(SCORE)
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()
pygame.quit()
