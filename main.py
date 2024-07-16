import pygame
import time
from random import randint
import sys

#        0 1 2 3 4 5 6 7 8
liste = [0, 0, 0, 0, 0, 0, 0, 0, 0]

level = []
turn = 1

a = 135
pygame.init()
points_x = 0
points_o = 0
P1Winscreen = pygame.image.load('Download (2).png')
P2Winscreen = pygame.image.load('P2 Wins.png')
font = pygame.font.Font('freesansbold.ttf', 100)
text = font.render('DRAW', True, 'green', 'blue')
text1score = font.render('Score P1 : ' + str(points_x), True, 'green', 'blue')
text2score = font.render('Score P2 : ' + str(points_o), True, 'green', 'blue')
textRect = text.get_rect()
textRect1 = text1score.get_rect()
textRect2 = text2score.get_rect()
stoobid = False


def check_win(liste):
    global points_x, points_o, running
    if liste[0] == liste[1] == liste[2] == 1 or liste[3] == liste[4] == liste[5] == 1 or liste[6] == liste[7] == liste[
        8] == 1 or liste[0] == liste[3] == liste[6] == 1 or liste[1] == liste[4] == liste[7] == 1 or liste[2] == liste[
        5] == liste[8] == 1 or liste[0] == liste[4] == liste[8] == 1 or liste[6] == liste[4] == liste[2] == 1:
        points_x = points_x + 1
        time.sleep(0.4)
        screen.fill('white')
        pygame.display.flip()
        screen.blit(P1Winscreen, (0, 0))
        pygame.display.flip()
        time.sleep(1)
        stoobid = True
        running = False

    if liste[0] == liste[1] == liste[2] == 2 or liste[3] == liste[4] == liste[5] == 2 or liste[6] == liste[7] == liste[
        8] == 2 or liste[0] == liste[3] == liste[6] == 2 or liste[1] == liste[4] == liste[7] == 2 or liste[2] == liste[
        5] == liste[8] == 2 or liste[0] == liste[4] == liste[8] == 2 or liste[6] == liste[4] == liste[2] == 2:
        points_o += 1
        time.sleep(0.4)
        screen.fill('white')
        screen.blit(P2Winscreen, (0, 0))
        pygame.display.flip()
        time.sleep(1)
        running = False
        pygame.display.flip()

    if liste[0] != 0 and liste[1] != 0 and liste[2] != 0 and liste[3] != 0 and liste[4] != 0 and liste[5] != 0 and \
            liste[6] != 0 and liste[7] != 0 and liste[8] != 0 and stoobid == False:
        time.sleep(0.4)
        screen.blit(text, textRect)
        pygame.display.flip()
        time.sleep(1)
        running = False


def erkennenUndErsetzen(x_pos, y_pos):
    player_value = 1
    feld = 0
    if x_pos > 697 - a:
        feld = feld + 3
    if x_pos > 995 - a:
        feld = feld + 3
    if y_pos > 333:
        feld = feld + 1
    if y_pos > 635:
        feld = feld + 1
    return feld


def ersetzen(turn, x, o, feld):
    if turn % 2 == 1 and liste[feld] == 0:
        liste[feld] = 1
        if feld == 0:
            screen.blit(x, (500 - a, 150))
        if feld == 1:
            screen.blit(x, (500 - a, 400))
        if feld == 2:
            screen.blit(x, (500 - a, 690))
        if feld == 3:
            screen.blit(x, (780 - a, 120))
        if feld == 4:
            screen.blit(x, (780 - a, 435))
        if feld == 5:
            screen.blit(x, (760 - a, 700))
        if feld == 6:
            screen.blit(x, (1040 - a, 150))
        if feld == 7:
            screen.blit(x, (1060 - a, 420))
        if feld == 8:
            screen.blit(x, (1050 - a, 690))
        pygame.display.flip()
    elif liste[feld] == 0:
        liste[feld] = 2
        if feld == 0:
            screen.blit(o, (480 - a, 110))
        if feld == 1:
            screen.blit(o, (480 - a, 400))
        if feld == 2:
            screen.blit(o, (480 - a, 690))
        if feld == 3:
            screen.blit(o, (760 - a, 120))
        if feld == 4:
            screen.blit(o, (760- a, 405))
        if feld == 5:
            screen.blit(o, (760 - a, 680))
        if feld == 6:
            screen.blit(o, (1040 - a, 115))
        if feld == 7:
            screen.blit(o, (1040 - a, 405))
        if feld == 8:
            screen.blit(o, (1050 - a, 690))
        pygame.display.flip()


modes = pygame.display.list_modes()
screen = pygame.display.set_mode()
pygame.display.toggle_fullscreen()
WIDTH, HEIGHT = screen.get_size()
pygame.mouse.set_visible(True)
backgroundColor = (255, 255, 255)  # RGB color for red
screen.fill(backgroundColor)
pygame.display.flip()
running = True
skibidi = True

points_x = 0
points_o = 0

while skibidi:
    font = pygame.font.Font('freesansbold.ttf', 50)
    text1score = font.render('Score P1 : ' + str(points_x), True, 'green', 'blue')
    text2score = font.render('Score P2 : ' + str(points_o), True, 'green', 'blue')
    textRect1 = text1score.get_rect()
    textRect2 = text2score.get_rect()

    P1Winscreen = pygame.image.load('Download (2).png')
    P2Winscreen = pygame.image.load('P2 Wins.png')
    text = font.render('DRAW', True, 'green', 'blue')
    textRect = text.get_rect()
    screen.fill('black')
    screen.fill('white')
    board = pygame.image.load('Board.png')
    x = pygame.image.load('X.png')
    o = pygame.image.load('O.png')
    running = True
    liste = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    level = []
    turn = 1

    while running:
        screen.blit(text1score, (1300 - 1200, 200 - 150))
        screen.blit(text2score, (1100, 50))
        screen.blit(board, (450 - a , 100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                level.append([mouse_x, mouse_y])
                ersetzen(turn, x, o, erkennenUndErsetzen(mouse_x, mouse_y))
                check_win(liste)
                turn += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_r]:
            running = False
            skibidi = False
    screen.fill('white')
    print(points_x)
    print(points_o)
    print(liste)
