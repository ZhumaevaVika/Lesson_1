import pygame
from pygame.draw import line, circle, rect
from random import randint
pygame.init()

FPS = 150
POINT = 50
K_COMBO = 0.01
frame_count = 0
score = 0
accuracy = 0.0
combo = 0
combo_break = 1
misses = 0
draw_miss = 0
target_count = 0
pos_x_prev = 0
pos_y_prev = 0
is_gameover = 0
pos_x = 0
pos_y = 0
Balls = []

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


def draws_miss(pos_x, pos_y):
    """ Render misses in display """
    global pos_x_prev, pos_y_prev
    line(screen, BLACK, (pos_x_prev - 10, pos_y_prev - 10), (pos_x_prev + 10, pos_y_prev + 10), 10)
    line(screen, BLACK, (pos_x_prev + 10, pos_y_prev - 10), (pos_x_prev - 10, pos_y_prev + 10), 10)
    line(screen, RED, (pos_x-10, pos_y-10), (pos_x+10, pos_y+10), 10)
    line(screen, RED, (pos_x + 10, pos_y - 10), (pos_x - 10, pos_y + 10), 10)
    pos_x_prev = pos_x
    pos_y_prev = pos_y
def update_screen(balls, pos_x=0, pos_y=0):
    """ Render balls in display """
    screen.fill(BLACK)
    for ball in balls:
        circle(screen, ball[3], (ball[0], ball[1]), ball[2])
        circle(screen, tuple(0.5 * i for i in ball[3]), (ball[0], ball[1]), ball[2]/ 1.25)
        circle(screen, tuple(0.33 * i for i in ball[3]), (ball[0], ball[1]), ball[2] / 2)
    if draw_miss == 1:
        draws_miss(pos_x, pos_y)
def text_update(score=0, accuracy=0.0, combo=0):
    """ Render text in display """
    global is_gameover
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
    if is_gameover == 1:
        font = pygame.font.Font('freesansbold.ttf', 128)
        death = 'YOU DIED'
        text = font.render(death, True, RED)
        screen.blit(text, (275, 310))
        image = pygame.image.load("YouDied1.png").convert()
        image = pygame.transform.scale(image, (580, 280))
        screen.blit(image, (280, 475))


def weigh_point(combo):
    """ Counting points """
    return int(POINT * (1 + K_COMBO * combo))
def weigh_accuracy(score, target_count, misses):
    """ Counting accuracy """
    accuracy = int(score * 10000 / (target_count * POINT * 4 * (1 + K_COMBO))) / 100
    if accuracy > 100:
        accuracy = float(100 - (100 * misses // target_count))
    return accuracy


def new_ball():
    """ Creates a new ball """
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
    Balls.append([x, y, r, color, speed_x, speed_y, is_move])
def move_ball(balls):
    """ Moves a ball """
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
    """ Process button click """
    pass


def game_over(balls):
    """ Checks the end of the game """
    global is_gameover, finished
    if len(balls) > 4:
        screen.fill(BLACK)
        finished = True
        is_gameover = 1


def save_score(score):
    """ Saving score """
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
    frame_count += 1
    update_screen(Balls, pos_x, pos_y)
    text_update(score, accuracy, combo)
    move_ball(Balls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(0)
            target_count += 1
            pos_x, pos_y = event.pos
            for ball in Balls:
                if (pos_x-ball[0])**2+(pos_y-ball[1])**2 < ball[2]**2:
                    combo_break = 0
                    Balls.remove(ball)
                    combo += 1
                    draw_miss = 0
                    score += weigh_point(combo)
                    if (pos_x-ball[0])**2+(pos_y-ball[1])**2 < (ball[2]/1.25)**2:
                        score += weigh_point(combo)
                        if (pos_x-ball[0])**2 + (pos_y-ball[1])**2 < (ball[2]/2)**2:
                            score += 2*weigh_point(combo)
            if combo_break == 1:
                misses += 1
                combo = 0
                draw_miss = 1
            combo_break = 1
            accuracy = weigh_accuracy(score, target_count, misses)
    if frame_count % 60 == 0:
        frame_count = 0
        new_ball()
    game_over(Balls)
    pygame.display.update()

text_update(score, accuracy, combo)
save_score(score)
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()
pygame.quit()
