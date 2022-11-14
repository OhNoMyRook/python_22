import math
from random import choice
from os import path

import pygame
from random import randint

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

start_time = pygame.time.get_ticks()  
stop_after = 30 * 1000 

font_name = pygame.font.match_font('arial')
pygame.init()
pygame.font.init()
pygame.display.set_caption("Gunshot")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load(path.join('background.png')).convert()
background_rect = background.get_rect()
pygame.display.update()

score = 0

def theme():
    '''Добавляет фон'''
    screen.fill(BLACK)
    screen.blit(background, background_rect)

def draw_text(surf, text, size, x, y):
    '''Пишет желаемый текст размера size на экране в (x,y)'''
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect) 

def points():
    '''Отображает очки'''
    draw_text(screen, "Очки : ", 60, 400, 25)  
    draw_text(screen, str(score), 60, 480, 25)   

def show_go_screen():
    '''Начальный экран, экран по окончании одной игровой сессии с опцией возобновления игры с отображением итоговых очков'''
    theme()
    draw_text(screen, "Количество очков: ", 40, 400, 300)
    draw_text(screen, str(score), 40, 560, 300)
    draw_text(screen, "Press any key to play", 30, 400, 350)
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

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self, dt):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g = 2
        self.vy-= g*dt
        self.x += self.vx * dt
        self.y -= self.vy * dt
        if self.x >= 790 or self.x <= 10:
            self.vx = self.vx * (-1)
        if self.y <= 10:
            self.vy = self.vy * (-1)

    def draw(self):
        '''Рисует снаряд'''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5 <= self.r + obj.r:
            return True
        else:
            return False

class Gun:
    def __init__(self, screen):
        '''Конструктор класса Gun
        
        Args:
        screen - экран отрисовки'''
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 40
        self.y = 450
        self.r = 5

    def fire2_start(self, event):
        '''Не понимаю, что делает'''
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        '''Рисует пушку на экране'''
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x, self.y),(self.x + 40, self.y),(self.x + 40, self.y + 10),(self.x, self.y + 10)]
            )

    def power_up(self):
        '''Меняет цвет с серого на черный при подготовке к выстрелу'''
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = BLACK
        else:
            self.color = GREY

class Target:
    def __init__(self, screen):
        '''Конструктор класса Target
        
        Args:
        screen - экран отрисовки'''
        self.screen = screen
        self.points = 0
        self.live = 1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(500,750)
        self.y = randint(100,350)
        self.r = randint(2,50)
        self.color = RED
        self.vx = randint(1,10)
        self.vy = randint(1,10)

    def move(self, dt):
        '''Задает движение мишеням (на мишени не действует сила тяжести)'''
        self.x+=self.vx * dt
        self.y+=self.vy * dt
        if self.x >= 800 - self.r or self.x <= self.r:
            self.vx = self.vx * (-1)
        if self.y >= 600 - self.r or self.y <= self.r:
            self.vy = self.vy * (-1)

    def draw(self):
        '''Отрисовка мишени'''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)

bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target_kind = Target(screen)
target_angry = Target(screen)

running = True
game_over = True

while running:
    theme()
    points()
    gun.draw()
    target_kind.draw()
    target_kind.move(0.5)
    target_angry.draw()
    target_angry.move(0.5)
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        if (current_time - start_time) >= stop_after:
            game_over = True
    if game_over:    
        show_go_screen()
        game_over = False
        score = 0
        start_time = current_time
    for b in balls:
        b.move(0.5)
        if b.hittest(target_kind) and target_kind.live:
            score+=1
            target_kind.new_target()
        if b.hittest(target_angry) and target_angry.live:
            score+=1
            target_angry.new_target()
    gun.power_up()

pygame.quit()
