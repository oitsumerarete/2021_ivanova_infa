import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))

pi = 3.14


# background
def background(x0, y0, width, length):
    rect(screen, (128, 85, 23), (x0, y0, width, length))
    rect(screen, (195, 144, 20), (x0, length, width, length+100))


rect(screen, (128, 85, 23), (0, 0, 400, 250))
rect(screen, (195, 144, 20), (0, 250, 400, 350))


# windows
def bigwindow(x0, y0, width, length):
    rect(screen, (197, 241, 233), (x0, y0, width, length))


rect(screen, (197, 241, 233), (220, 20, 160, 220))


def lilwindows(x0, y0, width, length):
    rect(screen, (28, 224, 242), (x0, y0, width, length))
    rect(screen, (28, 224, 242), (x0 + 85, y0, width, length))
    rect(screen, (28, 224, 242), (x0, y0 + 65, width, length + 75))
    rect(screen, (28, 224, 242), (x0 + 85, y0 + 65, width, length + 75))


rect(screen, (28, 224, 242), (228, 30, 68, 55))
rect(screen, (28, 224, 242), (305, 30, 68, 55))
rect(screen, (28, 224, 242), (228, 95, 68, 130))
rect(screen, (28, 224, 242), (305, 95, 68, 130))


def cat(x0, y0, tale, x1, y1, color, width, length):
    tale = pygame.Surface((x1,y1))
    tale.fill(color)
    ellipse(tale, color, (0, 0, 0.8*width, 0.5*length))
    ellipse(tale, 'BLACK', (0, 0, 0.8*width, 0.5*length))
    tale2 = pygame.transform.rotate(tale, 340)
    screen.blit(tale2, (x0+width*0.7, y0+0.5*length))
    ellipse(screen, color, x0+0.2*width, y0+0.3*length)
    ellipse(screen, 'BLACK', x0+0.2*width, y0+0.3*width)
    circle(screen, color, (x0 + 0.6*width, y0+0.7*length), 0.2*length)
    circle(screen, 'BLACK', (x0 + 0.6 * width, y0 + 0.7 * length), 0.2 * length)
    ellipse(screen, color, (x0 + 0.7*width, y0 + 0.8*length, )

tale = pygame.Surface((200, 140))
tale.fill((195, 144, 20))

# tale
ellipse(tale, (255, 140, 51), (0, 0, 200, 60))
ellipse(tale, (0, 0, 0), (0, 0, 200, 60), 1)
tale2 = pygame.transform.rotate(tale, 340)
screen.blit(tale2, (220, 310))

# body
ellipse(screen, (255, 140, 51), (70, 300, 250, 130))
ellipse(screen, (0, 0, 0), (70, 300, 250, 130), 1)

# legcircle
circle(screen, (255, 140, 51), (290, 405), 45)
circle(screen, (0, 0, 0), (290, 405), 45, 1)

# lapa1
ellipse(screen, (255, 140, 51), (313, 415, 35, 80))
ellipse(screen, (0, 0, 0), (313, 415, 35, 80), 1)

# lapa2
ellipse(screen, (255, 140, 51), (95, 400, 75, 40))
ellipse(screen, (0, 0, 0), (95, 400, 75, 40), 1)

# lapa3
ellipse(screen, (255, 140, 51), (55, 340, 40, 75))
ellipse(screen, (0, 0, 0), (55, 340, 40, 75), 1)

# head
ellipse(screen, (255, 140, 51), (50, 300, 120, 100))
ellipse(screen, (0, 0, 0), (50, 300, 120, 100), 1)

# ears
polygon(screen, (255, 140, 51), [(130, 310), (150, 330), (160, 295)])
polygon(screen, (0, 0, 0), [(130, 310), (150, 330), (160, 295)], 1)
polygon(screen, (243, 163, 238), [(138, 310), (147, 320), (156, 299)])
polygon(screen, (0, 0, 0), [(138, 310), (147, 320), (156, 299)], 1)
polygon(screen, (255, 140, 51), [(85, 310), (65, 330), (60, 295)])
polygon(screen, (0, 0, 0), [(85, 310), (65, 330), (60, 295)], 1)
polygon(screen, (243, 163, 238), [(80, 310), (67, 323), (65, 303)])
polygon(screen, (0, 0, 0), [(80, 310), (67, 323), (65, 303)], 1)

# eyes
ellipse(screen, (92, 240, 63), (120, 330, 25, 30))
ellipse(screen, (0, 0, 0), (120, 330, 25, 30), 1)
ellipse(screen, (0, 0, 0), (135, 335, 5, 20))
blick = pygame.Surface((15, 5))
blick.fill((92, 240, 63))
ellipse(blick, (255, 255, 255), (0, 0, 15, 5))
blick2 = pygame.transform.rotate(blick, 110)
# def glare(x0, y0):
#   screen.blit(blick2, (x0,y0))
# glare(125, 335)
# glare(75, 335)

screen.blit(blick2, (125, 335))

ellipse(screen, (92, 240, 63), (75, 330, 25, 30))
ellipse(screen, (0, 0, 0), (75, 330, 25, 30), 1)
ellipse(screen, (0, 0, 0), (90, 335, 5, 20))
screen.blit(blick2, (80, 335))

# nose
polygon(screen, (243, 163, 238), [(105, 365), (115, 365), (110, 373)])
polygon(screen, (0, 0, 0), [(105, 365), (115, 365), (110, 373)], 1)
line(screen, (0, 0, 0), [110, 373], [110, 378])
arc(screen, (0, 0, 0), (100, 375, 10, 10), pi, 2 * pi)
arc(screen, (0, 0, 0), (110, 375, 10, 10), pi, 2 * pi)
arc(screen, (0, 0, 0), (130, 365, 70, 10), 0, pi)
arc(screen, (0, 0, 0), (133, 368, 70, 10), 0, pi)
arc(screen, (0, 0, 0), (130, 371, 70, 10), 0, pi)
arc(screen, (0, 0, 0), (20, 365, 70, 10), 0, pi)
arc(screen, (0, 0, 0), (23, 368, 70, 10), 0, pi)
arc(screen, (0, 0, 0), (20, 371, 70, 10), 0, pi)

# knit
circle(screen, 'GREY', (260, 515), 40)
circle(screen, 'BLACK', (260, 515), 40, 1)
arc(screen, 'BLACK', (230, 495, 65, 70), 0.1*pi, 0.55*pi)
arc(screen, 'BLACK', (225, 500, 65, 70), 0.1*pi, 0.55*pi)
arc(screen, 'BLACK', (230, 485, 65, 70), 0.1*pi, 0.6*pi)
arc(screen, 'BlACK', (245, 500, 60, 65), 0.7*pi, 1.1*pi)
arc(screen, 'BlACK', (250, 505, 60, 65), 0.7*pi, 1.1*pi)
arc(screen, 'BlACK', (255, 510, 60, 65), 0.8*pi, 1.1*pi)
arc(screen, 'GREY', (185, 490, 70, 75), 1.3*pi, 1.8*pi)
arc(screen, 'GREY', (135, 550, 80, 60), 0.3*pi, 0.8*pi)

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
