import pygame
import math
from pygame.draw import circle
from random import randint
from os import path

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH = 1200
HEIGTH = 900
r_min = 40
r_max = 100
FPS = 2
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Catch the ball")
clock = pygame.time.Clock()

background = pygame.image.load(path.join('background.png')).convert()
background_rect = background.get_rect()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

pygame.display.update()
start_time = pygame.time.get_ticks()  
stop_after = 20 * 1000 

s = 0

font_name = pygame.font.match_font('arial')

def new_ball_1():
    global x, y, r
    x = randint(r_max,WIDTH - r_max)
    y = randint(r_max,HEIGTH - r_max)
    r = randint(r_min,r_max)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def new_ball_2():
    global x_1, y_1, r_1
    x_1 = randint(r_max,WIDTH - r_max)
    y_1 = randint(r_max,HEIGTH - r_max)
    r_1 = randint(r_min,r_max)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x_1, y_1), r_1)

def new_ball_3():
    global x_2, y_2, r_2
    x_2 = randint(r_max,WIDTH - r_max)
    y_2 = randint(r_max,HEIGTH - r_max)
    r_2 = randint(r_min,r_max)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x_2, y_2), r_2)

def bomb():
    global x_0, y_0, r_0
    x_0 = randint(r_max,WIDTH - r_max)
    y_0 = randint(r_max,HEIGTH - r_max)
    r_0 = randint(r_min,r_max)
    circle(screen, BLACK, (x_0, y_0), r_0)

def some_balls():
    new_ball_1()
    new_ball_2()
    new_ball_3()

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)

def points():
    draw_text(screen, "Очки : ", 60, 550, 40)  
    draw_text(screen, str(s), 60, 650, 40)

def show_go_screen():
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    draw_text(screen, "Количество очков: ", 40, 590, 400)
    draw_text(screen, str(s), 40, 750, 400)
    draw_text(screen, "Press any key to play", 30, 600, 600)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
                pygame.display.flip()
                screen.fill(BLACK)
                screen.blit(background, background_rect)
                    
running = True
game_over = True

while running:
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (math.sqrt(((event.pos[0])-x)**2 + ((event.pos[1])-y)**2)) <= r or (math.sqrt(((event.pos[0])-x_1)**2 + ((event.pos[1])-y_1)**2)) <= r_1 or (math.sqrt(((event.pos[0])-x_2)**2 + ((event.pos[1])-y_2)**2)) <= r_2:
                s+=1
            elif (math.sqrt(((event.pos[0])-x_0)**2 + ((event.pos[1])-y_0)**2)) <= r_0:
                s=s-3
    points()    
    if (current_time - start_time) >= stop_after:
        game_over = True
    if game_over:    
        show_go_screen()
        game_over = False
        s = 0
        start_time = current_time 
    some_balls()
    bomb()
    pygame.display.update()
    screen.fill(BLACK)
    screen.blit(background, background_rect)
