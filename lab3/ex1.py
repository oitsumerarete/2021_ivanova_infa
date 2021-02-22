import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill("GREY")

circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (150, 170), 20)
circle(screen, (0, 0, 0), (150, 170), 20, 2)
circle(screen, (255, 0, 0), (230, 170), 15)
circle(screen, (0, 0, 0), (230, 170), 15, 2)
circle(screen, (0, 0, 0), (150, 170), 10)
circle(screen, (0, 0, 0), (230, 170), 6)
rect(screen, (0, 0, 0), (150, 260, 80, 10))
polygon(screen, (0,0,0), [(115,120), (120,115), (185, 175), (180, 180)])
polygon(screen, (0, 0, 0), [(190, 175), (185, 170), (260, 130), (265, 135)])




pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
