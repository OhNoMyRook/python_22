import pygame
from pygame.draw import circle, polygon, line

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill("white")   
circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (255, 0, 0), (130, 145), 28)
circle(screen, (0, 0, 0), (130, 145), 12)
circle(screen, (255, 0, 0), (260, 145), 22)
circle(screen, (0, 0, 0), (260, 145), 12)
polygon(screen, (0, 0, 0), [(130, 255), (260, 255), (260, 280), (130, 280)])
polygon(screen, (0, 0, 0), [(160, 125), (170, 110), (70, 60), (60, 75)])
polygon(screen, (0, 0, 0), [(240, 125), (230, 110), (340, 70), (350, 85)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()