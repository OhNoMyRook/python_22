import pygame
import math
from pygame.draw import circle
from random import randint
pygame.init()
pygame.font.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Catch the ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    global x, y, r
    x = randint(100,1000)
    y = randint(100,800)
    r = randint(30,60)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

pygame.display.update()
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()  
stop_after = 20 * 1000 

s = 0

font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)

def points():
    draw_text(screen, "Очки : ", 60, 550, 40)  
    draw_text(screen, str(s), 60, 650, 40)

def show_go_screen():
    screen.fill(BLUE)
    draw_text(screen, "Количество очков: ", 40, 590, 400)
    draw_text(screen, str(s), 40, 750, 400)
    draw_text(screen, "Press a key to play", 30, 600, 600)
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
                    
running = True

while running:
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (math.sqrt(((event.pos[0])-x)**2 + ((event.pos[1])-y)**2)) <= r:
                s+=1
    points()    
    if (current_time - start_time) >= stop_after:
        show_go_screen()
        s = 0
        start_time = current_time 
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
