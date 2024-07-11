import pygame
import time
from random import randint
import sys
#        0 1 2 3 4 5 6 7 8
liste = [0,0,0,0,0,0,0,0,0]

level = []
turn = 1

pygame.init()
points_x = 0
points_o = 0   
P1Winscreen = pygame.image.load('TicTacToi\Download (2).png')
P2Winscreen = pygame.image.load('TicTacToi\P2 Wins.png')
font = pygame.font.Font('freesansbold.ttf', 100)
text = font.render('DRAW', True, 'green', 'blue')
text1score = font.render('Score P1 : ' + str(points_x), True, 'green', 'blue')
text2score = font.render('Score P2 : ' + str(points_o), True, 'green', 'blue')
textRect = text.get_rect()
textRect1 = text1score.get_rect()
textRect2 = text2score.get_rect()


def check_win(liste):
    global points_x, points_o, running
    if liste[0] == liste[1] == liste[2] == 1 or liste[3] == liste[4] == liste[5] == 1 or liste[6] == liste[7] == liste[8] == 1 or liste[0] == liste[3] == liste[6] == 1 or liste[1] == liste[4] == liste[7] == 1 or liste[2] == liste[5] == liste[8] == 1 or liste[0] == liste[4] == liste[8] == 1 or liste[6] == liste[4] == liste[2] == 1:
        # Assuming 'screen' is your Pygame display surface:
        points_x = points_x +1
        screen.fill('white')  # Fill the screen with black color
        pygame.display.flip()
        screen.blit(P1Winscreen, (0,0))
        pygame.display.flip()
        # Don't forget to update the display after filling:

    if liste[0] == liste[1] == liste[2] == 2 or liste[3] == liste[4] == liste[5] == 2 or liste[6] == liste[7] == liste[8] == 2 or liste[0] == liste[3] == liste[6] == 2 or liste[1] == liste[4] == liste[7] == 2 or liste[2] == liste[5] == liste[8] == 2 or liste[0] == liste[4] == liste[8] == 2 or liste[6] == liste[4] == liste[2] == 2:
        points_o += 1
        screen.fill('white')
        pygame.display.flip()
        screen.blit(P2Winscreen, (0,0))
        pygame.display.flip()
    if liste[0] != 0 and liste[1] != 0 and liste[2] != 0 and liste[3] != 0 and liste[4] != 0 and liste[5] != 0 and liste[6] != 0 and liste[7] != 0 and liste[8] != 0:
        screen.blit(text, textRect)
        
        
    

        

def erkennenUndErsetzen(x_pos, y_pos):
    player_value =  1
    feld = 0
    if x_pos > 697:
        feld = feld + 3
    if x_pos > 995:
        feld = feld + 3
    if y_pos > 333:
        feld = feld + 1
    if y_pos > 635:
        feld= feld + 1
    return feld
    
def ersetzen(turn, x, o, feld):
    if turn % 2 ==  1 and liste[feld] == 0:
        liste[feld] = 1
        if feld == 0:
            screen.blit(x, (500, 150))
        if feld == 1:
            screen.blit(x, (500, 400))
        if feld == 2:
            screen.blit(x, (500, 690))
        if feld == 3:
            screen.blit(x, (780, 120))
        if feld == 4:
            screen.blit(x, (780, 435))
        if feld == 5:
            screen.blit(x, (760, 700))
        if feld == 6:
            screen.blit(x, (1040, 150))
        if feld == 7:
            screen.blit(x, (1060, 420))
        if feld == 8:
            screen.blit(x, (1050, 690))
    elif liste[feld] == 0:
        liste[feld] =  2
        if feld == 0:
            screen.blit(o, (480, 150))
        if feld == 1:
            screen.blit(o, (480,400))
        if feld == 2:
            screen.blit(o, (480, 690))
        if feld == 3:
            screen.blit(o, (760, 120))
        if feld == 4:
            screen.blit(o, (760, 405))
        if feld == 5:
            screen.blit(o, (760, 680))
        if feld == 6:
            screen.blit(o, (1040, 115))
        if feld == 7:
            screen.blit(o, (1040, 405))
        if feld == 8:
            screen.blit(o, (1050, 690))


    
modes = pygame.display.list_modes()
WIDTH, HEIGHT = modes[0]
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(True)
backgroundColor = (255, 255, 255) # RGB color for red
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

    P1Winscreen = pygame.image.load('TicTacToi\Download (2).png')
    P2Winscreen = pygame.image.load('TicTacToi\P2 Wins.png')
    text = font.render('DRAW', True, 'green', 'blue')
    textRect = text.get_rect()
    screen.fill('black')
    screen.fill('white')
    board = pygame.image.load('TicTacToi\Board.png')
    x = pygame.image.load('TicTacToi\X.png')
    o = pygame.image.load('TicTacToi\O.png')
    running = True
    liste = [0,0,0,0,0,0,0,0,0]

    level = []
    turn = 1

    while running:
        pygame.font.Font
        screen.blit(text1score, (1300,200))
        screen.blit(text2score, (100, 200))
        screen.blit(board, (450, 100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                level.append([mouse_x,mouse_y])
                ersetzen(turn,x,o,erkennenUndErsetzen(mouse_x, mouse_y))
                check_win(liste)
                turn = turn + 1
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