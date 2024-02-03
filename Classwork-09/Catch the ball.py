import pygame
import math
from pygame.draw import circle
from random import randint
from os import path

pygame.init()
pygame.font.init()

WIDTH = 1200
HEIGTH = 900
r_min = 40
r_max = 100
FPS = 15
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

score = 0

font_name = pygame.font.match_font('arial')

def theme():
    '''Добавляет фон'''
    screen.fill(BLACK)
    screen.blit(background, background_rect)

class Ball:
    def __init__(self):
        '''Конструктор класса Ball'''
        self.screen = screen
        self.x = randint(r_max,WIDTH - r_max)
        self.y = randint(r_max,HEIGTH - r_max)
        self.r = randint(r_min,r_max)
        self.Vx = randint(0, 3)
        self.Vy = randint(0, 3)
        self.color = COLORS[randint(0,5)]
    
    def draw(self):
        '''Рисует цели-шарики'''
        circle(self.screen, self.color, (self.x, self.y), self.r)

    def move(self, dt):
        '''Задает движение целей-шариков'''
        self.x+=self.Vx * dt
        self.y+=self.Vy * dt
        if self.y <= self.r or self.y >= HEIGTH - self.r:
            self.Vy = (-1)*self.Vy
        if self.x <= self.r or self.x >= WIDTH - self.r:
            self.Vx = (-1)*self.Vx
        
    def hit_and_return_score(self, event_pos, balls):
        '''Определяет попадание, заменяет пораженную цель новой, добавляет балл'''
        x_pos, y_pos = event_pos
        if math.sqrt((x_pos-self.x)**2 + (y_pos-self.y)**2) <= self.r:
            balls.remove(self)
            new_ball = Ball()
            balls.append(new_ball)
            return 1
        return 0
            
balls = []

for i in range (3):
    new_ball = Ball()
    balls.append(new_ball)

class Bomb:
    def __init__(self):
        '''Конструктор класса Bomb'''
        self.screen = screen
        self.x = randint(r_max,WIDTH - r_max)
        self.y = randint(r_max,HEIGTH - r_max)
        self.r = randint(r_min,r_max)
        self.Vx = randint(0, 3)
        self.Vy = randint(0, 3)
        self.color = BLACK
    
    def draw(self):
        '''Рисует цель-бомбу'''
        circle(self.screen, self.color, (self.x, self.y), self.r)

    def move(self, dt):
        '''Задает движение бомбы'''
        self.x+=self.Vx * dt
        self.y+=self.Vy * dt
        if self.y <= self.r or self.y >= HEIGTH - self.r:
            self.Vy = (-1)*self.Vy
        if self.x <= self.r or self.x >= WIDTH - self.r:
            self.Vx = (-1)*self.Vx

    def boom_and_return_score(self, event_pos, bombs):
        '''Определяет попадание по бомбе, заменяет пораженную бомбу новой, снимает 3 балла'''
        x_pos, y_pos = event_pos
        if math.sqrt((x_pos-self.x)**2 + (y_pos-self.y)**2) <= self.r:
            bombs.remove(self)
            new_bomb = Bomb()
            bombs.append(new_bomb)
            return -3
        return 0
            
bombs = []

new_bomb = Bomb()
bombs.append(new_bomb)

def draw_text(surf, text, size, x, y):
    '''Пишет желаемый текст размера size на экране в (x,y)'''
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)

def points():
    '''Отображает очки'''
    draw_text(screen, "Очки : ", 60, 550, 40)  
    draw_text(screen, str(score), 60, 650, 40)

def show_go_screen():
    '''Начальный экран, экран по окончании одной игровой сессии с опцией возобновления игры с отображением итоговых очков'''
    theme()
    draw_text(screen, "Количество очков: ", 40, 590, 400)
    draw_text(screen, str(score), 40, 750, 400)
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
                theme()
                    
running = True
game_over = True

while running:
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                for ball in balls:
                    score+=ball.hit_and_return_score(event.pos, balls)
                for bomb in bombs:
                    score+=bomb.boom_and_return_score(event.pos, bombs)                
    points() 
    if (current_time - start_time) >= stop_after:
        game_over = True
    if game_over:    
        show_go_screen()
        game_over = False
        score = 0
        start_time = current_time 
    for ball in balls:
        ball.draw()
        ball.move(FPS)
    for bomb in bombs:
        bomb.draw()
        bomb.move(FPS)
    pygame.display.update()
    theme()
    