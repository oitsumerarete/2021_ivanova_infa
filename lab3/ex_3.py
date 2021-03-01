import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
pi = 3.14


def window(x0, y0, width, length):
    '''
    Функция отображает окно в заданном месте
    :param x0: координата левого верхнего угла окна по оси Х
    :param y0: координата левого верхнего угла окна по оси У
    :param width: ширина окна (ось Х)
    :param length: длина окна (ось У)
    '''
    rect(screen, (197, 241, 233), (x0, y0, width, length))
    rect(screen, (28, 224, 242), (x0 + 0.05*width, y0 + 0.045*length, 0.425*width, 0.25*length))
    rect(screen, (28, 224, 242), (x0 + 0.53 * width, y0 + 0.045 * length, 0.425*width, 0.25*length))
    rect(screen, (28, 224, 242), (x0 + 0.05 * width, y0 + 0.34 * length, 0.425*width, 0.59 * length))
    rect(screen, (28, 224, 242), (x0 + 0.53 * width, y0 + 0.34 * length, 0.425*width, 0.59*length))


def cat(x0, y0, length, width):
    '''
    :param x0: координата верхнего левого угла кошки по оХ
    :param y0: координата верхнего левого угла кошки по оУ
    :param length: длина кошки (оХ)
    :param width: ширина кошки (оУ)
    '''
    tale = pygame.Surface((length, width))  # tale
    tale.fill((195, 144, 20))
    ellipse(tale, (255, 140, 51), (0, 0, 0.6 * length, 0.34 * width))
    ellipse(tale, 'BLACK', (0, 0, 0.6 * length, 0.34 * width), 1)
    tale2 = pygame.transform.rotate(tale, 340)
    screen.blit(tale2, (x0 + length * 0.48, y0 + 0.11 * width))

    ellipse(screen, (255, 140, 51), (x0 + 0.05 * length, y0 + 0.03 * width, 0.7 * length, 0.65 * width))  # body
    ellipse(screen, 'BLACK', (x0 + 0.05 * length, y0 + 0.03 * width, 0.7 * length, 0.65 * width), 1)
    circle(screen, (255, 140, 51), (x0 + 0.67 * length, y0 + 0.47 * width), 0.12 * length)  # leg circle
    circle(screen, 'BLACK', (x0 + 0.67 * length, y0 + 0.47 * width), 0.12 * length, 1)
    ellipse(screen, (255, 140, 51),
            (x0 + 0.7 * length, y0 + 0.5 * width, 0.1 * length, 0.24 * length))  # leg from circle
    ellipse(screen, 'black', (x0 + 0.7 * length, y0 + 0.5 * width, 0.1 * length, 0.24 * length), 1)

    ellipse(screen, (255, 140, 51), (x0 + 0.13 * length, y0 + 0.52 * width, 0.2 * length, 0.2 * width))  # second leg
    ellipse(screen, 'black', (x0 + 0.13 * length, y0 + 0.52 * width, 0.2 * length, 0.2 * width), 1)

    ellipse(screen, (255, 140, 51),
            (x0 + 0.014 * length, y0 + 0.225 * width, 0.11 * length, 0.375 * width))  # third leg
    ellipse(screen, 'black', (x0 + 0.014 * length, y0 + 0.225 * width, 0.11 * length, 0.375 * width), 1)

    ellipse(screen, (255, 140, 51), (x0, y0 + 0.025 * width, 0.335 * length, 0.5 * width))  # head
    ellipse(screen, 'black', (x0, y0 + 0.025 * width, 0.34 * length, 0.5 * width), 1)

    polygon(screen, (255, 140, 51), [(x0 + 0.22 * length, y0 + 0.075 * width), (x0 + 0.28 * length, y0 + 0.175 * width),
                                     (x0 + 0.31 * length, y0)])
    polygon(screen, 'black', [(x0 + 0.22 * length, y0 + 0.075 * width), (x0 + 0.28 * length, y0 + 0.175 * width),
                                     (x0 + 0.31 * length, y0)], 1)
    polygon(screen, (255, 140, 51), [(x0 + 0.1 * length, y0 + 0.075 * width), (x0 + 0.041 * length, y0 + 0.175 * width),
                                     (x0 + 0.028 * length, y0)])
    polygon(screen, 'black', [(x0 + 0.1 * length, y0 + 0.075 * width), (x0 + 0.041 * length, y0 + 0.175 * width),
                                     (x0 + 0.028 * length, y0)], 1)

    polygon(screen, (243, 163, 238), [(x0 + 0.24*length, y0 + 0.075*width), (x0 + 0.27*length, y0 + 0.12*width), (x0 + 0.296*length, y0 + 0.02*width)])
    polygon(screen, 'black', [(x0 + 0.24 * length, y0 + 0.075 * width), (x0 + 0.27 * length, y0 + 0.125 * width),
                                     (x0 + 0.296 * length, y0 + 0.02 * width)], 1)
    polygon(screen, (243, 163, 238), [(x0 + 0.084*length, y0 + 0.075 * width), (x0 + 0.047 * length, y0 + 0.12*width), (x0 + 0.041*length, y0 + 0.04*width)])
    polygon(screen, 'black',
            [(x0 + 0.084 * length, y0 + 0.075 * width), (x0 + 0.047 * length, y0 + 0.14 * width),
             (x0 + 0.041 * length, y0 + 0.04 * width)], 1)

    ellipse(screen, (92, 240, 63), (x0 + 0.196*length, y0 + 0.175 * width, 0.07 * length, 0.15 * width))
    ellipse(screen, 'black', (x0 + 0.196 * length, y0 + 0.175 * width, 0.07 * length, 0.15 * width), 1)
    ellipse(screen, 'black', (x0 + 0.24*length, y0 + 0.2 * width, 0.014 * length, 0.1 * width))
    blick = pygame.Surface((0.042*length, 0.025*width))
    blick.set_colorkey('BLACK')
    ellipse(blick, 'white', (0, 0, 0.042*length, 0.025*width))
    blick2 = pygame.transform.rotate(blick, 110)
    screen.blit(blick2, (x0 + 0.21 * length, y0 + 0.2 * width))
    ellipse(screen, (92, 240, 63), (x0 + 0.07 * length, y0 + 0.175 * width, 0.07 * length, 0.15*width))
    ellipse(screen, 'black', (x0 + 0.07 * length, y0 + 0.175 * width, 0.07 * length, 0.15 * width), 1)
    ellipse(screen, 'black', (x0 + 0.11 * length, y0 + 0.2 * width, 0.014 * length, 0.1 * width))
    screen.blit(blick2, (x0 + 0.084 * length, y0 + 0.2 * width))

    polygon(screen, (243, 163, 238), [(x0 + 0.154 * length, y0 + 0.35 * width), (x0 + 0.18 * length, y0 + 0.35 * width), (x0 + 0.166 * length, y0 + 0.39 * width)])
    polygon(screen, 'black', [(x0 + 0.154 * length, y0 + 0.35 * width), (x0 + 0.18 * length, y0 + 0.35 * width),
                                      (x0 + 0.166 * length, y0 + 0.39 * width)], 1)
    line(screen, 'black', [x0 + 0.166 * length, y0 + 0.39 * width], [x0 + 0.166 * length, y0 + 0.415 * width])
    arc(screen, 'black', (x0 + 0.145 *length, y0 + 0.4*width, 0.028*length, 0.05*width), pi, 0)
    arc(screen, 'black', (x0 + 0.166 * length, y0 + 0.4 * width, 0.028 * length, 0.05 * width), pi, 0)
    arc(screen, 'black', (x0 + 0.2 * length, y0 + 0.35 * width, 0.196 * length, 0.05 * width), 0, pi)
    arc(screen, 'black', (x0 + 0.22 * length, y0 + 0.365 * width, 0.196 * length, 0.05 * width), 0, pi)
    arc(screen, 'black', (x0 + 0.23 * length, y0 + 0.38 * width, 0.196 * length, 0.05 * width), 0, pi)
    arc(screen, 'black', (x0 - 0.084 * length, y0 + 0.35 * width, 0.196 * length, 0.05 * width), 0, pi)
    arc(screen, 'black', (x0 - 0.075 * length, y0 + 0.365 * width, 0.196 * length, 0.05 * width), 0, pi)
    arc(screen, 'black', (x0 - 0.084 * length, y0 + 0.38 * width, 0.196 * length, 0.05 * width), 0, pi)


def knit(x0, y0, r):
    '''
    :param x0: центр клубочка по оХ
    :param y0: центр клубочка оУ
    :param r: радиус клубочка
    '''
    circle(screen, 'grey', (x0, y0), r)
    circle(screen, 'black', (x0, y0), r, 1)
    arc(screen, 'black', (x0 - 0.75*r, y0 - 0.5*r, 1.62*r, 1.75*r), 0.1*pi, 0.55*pi)
    arc(screen, 'black', (x0 - 0.875 * r, y0 - 0.375 * r, 1.62 * r, 1.75 * r), 0.1 * pi, 0.55 * pi)
    arc(screen, 'black', (x0 - 0.75 * r, y0 - 0.75 * r, 1.62 * r, 1.75 * r), 0.1 * pi, 0.6 * pi)
    arc(screen, 'black', (x0 - 0.375 * r, y0 - 0.375 * r, 1.5 * r, 1.62 * r), 0.7 * pi, 1.1 * pi)
    arc(screen, 'black', (x0 - 0.25 * r, y0 - 0.25 * r, 1.5 * r, 1.62 * r), 0.7 * pi, 1.1 * pi)
    arc(screen, 'black', (x0 - 0.125 * r, y0 - 0.125 * r, 1.5 * r, 1.62 * r), 0.8 * pi, 1.1 * pi)
    arc(screen, 'grey', (x0 - 1.875 * r, y0 - 0.5 * r, 1.75 * r, 1.87 * r), 1.3 * pi, 1.8 * pi)
    arc(screen, 'grey', (x0 - 3.225 * r, y0 + 0.9 * r, 2 * r, 1.5 * r), 0.2 * pi, 0.8 * pi)


# background
rect(screen, (128, 85, 23), (0, 0, 600, 350))
rect(screen, (195, 144, 20), (0, 350, 600, 450))
# everything else
window(20, 20, 160, 220)
window(280, 20, 200, 220)
cat(250, 360, 350, 200)
knit(400, 640, 25)


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
