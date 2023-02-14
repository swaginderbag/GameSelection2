import pygame
import random
import sys
import csv

x = 500
y = 500
sbreite = 50
shoehe = 15
sx = 200
sy = 450
bx = int(x / 2)
by = int(y / 2)
brad = 15
speed = 0
bxspeed = 1
byspeed = -2
leben = 3
username = ""
highscore1 = ""

pygame.init()
#Hintergrundmusik
pygame.mixer.init()
pygame.mixer.music.load("backgroundmusic.mp3")
pygame.mixer.music.play(-1)

#Fenster und Inhalt erstellen + Hintergrundbild
screen = pygame.display.set_mode([x, y])
screen.fill((0,0,0))
pygame.draw.circle(screen, (255, 255, 0), (bx, by), brad, 0)
pygame.draw.rect(screen, ("darkred"), (sx, sy, sbreite, shoehe), 0)
pygame.display.flip()
restart_button = pygame.Rect(175, 250, 150, 50)

score1 = 0
font = pygame.font.SysFont("Comic Sans MS", 14)

def add_point():
    global score1
    score1 += 1


def save_points():
    with open('users.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            score1 = int(row['score1'])

            if score1 > highscore1:
                highscore1 = score1

def sblock():
    global speed
    if sx <= 0 or sx >= x - sbreite:
        speed = 0

def ballbewegung():
    global bx, by
    bx += bxspeed
    by += byspeed


def reset():
    global byspeed, bxspeed, leben, bx, by, sx, sy, speed
    sx = 200
    sy = 450

    bx = int(x / 2)
    by = int(y / 2)

    speed = 0
    bxspeed = random.randint(-2, 2)
    if bxspeed == 0:
        bxspeed = 1
    byspeed = random.randint(-2, 2)
    if byspeed == 0:
        byspeed = 1
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255, 255, 0), (bx, by), brad, 0)
    pygame.draw.rect(screen, ("darkred"), (sx, sy, sbreite, shoehe), 0)
    pygame.display.flip()
    pygame.time.wait(1000)

def ballblock():
    global byspeed, bxspeed, leben
    if by - brad <= 0:
        byspeed *= -1
    if bx - brad <= 0:
        bxspeed *= -1
    if bx + brad >= x:
        bxspeed *= -1
    if by >= 435 and by <= 440:
        if bx >= sx - 15 and bx <= sx + sbreite + 15:
            byspeed *= -1
            add_point()

        else:
            leben -= 1
            reset()

def display_points():
    text = font.render("Punkte: " + str(score1), True, (255, 255, 255))
    screen.blit(text, (x-90, 10))

def display_leben(leben):
    font = pygame.font.SysFont("Comic Sans MS", 14)
    text = font.render("Leben: " + str(leben), True, (255, 255, 255))
    screen.blit(text, (x-90, y-30))

def check_gameover():
    global leben
    if leben <= 0:
        pygame.mixer.music.pause()
        pygame.mixer.Sound("gameover.mp3").play()
        font1 = pygame.font.SysFont("Comic Sans MS", 30)
        game_over_text = font1.render("Game Over", True, (255, 255, 255))
        screen.blit(game_over_text, (x/2, y/2))
        restart_button = pygame.Rect(x / 2 - 75, y / 2 + 50, 150, 50)
        pygame.draw.rect(screen, (255,255,255), restart_button)
        restart_text = font.render("Restart", True, (0, 0, 0))
        screen.blit(restart_text, (x / 2 - 40, y / 2 + 65))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
def reset_game():
    global byspeed, bxspeed, leben, bx, by, sx, sy, speed, score1
    sx = 200
    sy = 450

    bx = int(x / 2)
    by = int(y / 2)

    speed = 0
    bxspeed = random.randint(-2, 2)
    if bxspeed == 0:
        bxspeed = 1
    byspeed = random.randint(-2, 2)
    if byspeed == 0:
        byspeed = 1
    leben = 3
    score1 = 0
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (bx, by), brad, 0)
    pygame.draw.rect(screen, ("darkred"), (sx, sy, sbreite, shoehe), 0)
    pygame.display.flip()


def sbewegung():
    global sx
    sx += speed

background = pygame.image.load("background.gif")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: save_points(), sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -2
            elif event.key == pygame.K_RIGHT:
                speed = 2
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    display_points()
    display_leben(leben)
    sbewegung()
    sblock()
    pygame.draw.rect(screen, ("darkred"), (sx, sy, sbreite, shoehe), 0)
    ballbewegung()
    ballblock()
    check_gameover()
    pygame.draw.circle(screen, (255, 255, 0), (bx, by), brad, 0)
    pygame.display.flip()
    pygame.time.wait(5)


