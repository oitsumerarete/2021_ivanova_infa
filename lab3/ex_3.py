import pygame
import pygame.draw as draw
from math import pi
from math import sin

pygame.init()

FPS = 30
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 800))

night_light = pygame.Surface((600, 800))
night_light.fill((58, 58, 58))
night_light.set_colorkey('BLACK')
night_light.set_alpha(128)

LIGHT_COLOR_WINDOW = (197, 241, 233)
DARK_COLOR_WINDOW = (25, 35, 25)
NIGHT_EYE_COLOR = 'GREEN'
LIGHT_EYE_COLOR = (60, 150, 60)
SLEEP_EYE_COLOR = (235, 130, 51)


def window(x0, y0, width, length, day):
    '''
    Функция отображает окно в заданном месте
    :param x0: координата левого верхнего угла окна по оси Х
    :param y0: координата левого верхнего угла окна по оси У
    :param width: ширина окна (ось Х)
    :param length: длина окна (ось У)
    '''
    if day == True:
        color = LIGHT_COLOR_WINDOW
    else:
        color = DARK_COLOR_WINDOW

    draw.rect(screen, (65, 56, 65), (x0, y0, width, length))
    draw.rect(screen, color, (x0 + 0.05 * width, y0 + 0.045 * length, 0.425 * width, 0.25 * length))
    draw.rect(screen, color, (x0 + 0.53 * width, y0 + 0.045 * length, 0.425 * width, 0.25 * length))
    draw.rect(screen, color, (x0 + 0.05 * width, y0 + 0.34 * length, 0.425 * width, 0.59 * length))
    draw.rect(screen, color, (x0 + 0.53 * width, y0 + 0.34 * length, 0.425 * width, 0.59 * length))


def cat(x0, y0, length, width, day, active_in_night=True):
    '''
    :param x0: координата верхнего левого угла кошки по оХ
    :param y0: координата верхнего левого угла кошки по оУ
    :param length: длина кошки (оХ)
    :param width: ширина кошки (оУ)
    '''
    tale = pygame.Surface((length, width))  # tale
    tale.fill((195, 144, 20))
    draw.ellipse(tale, (255, 140, 51), (0, 0, 0.6 * length, 0.34 * width))
    draw.ellipse(tale, 'BLACK', (0, 0, 0.6 * length, 0.34 * width), 1)
    tale2 = pygame.transform.rotate(tale, 340)
    screen.blit(tale2, (x0 + length * 0.48, y0 + 0.11 * width))

    draw.ellipse(screen, (255, 140, 51), (x0 + 0.05 * length, y0 + 0.03 * width, 0.7 * length, 0.65 * width))  # body
    draw.ellipse(screen, 'BLACK', (x0 + 0.05 * length, y0 + 0.03 * width, 0.7 * length, 0.65 * width), 1)
    draw.circle(screen, (255, 140, 51), (x0 + 0.67 * length, y0 + 0.47 * width), 0.12 * length)  # leg circle
    draw.circle(screen, 'BLACK', (x0 + 0.67 * length, y0 + 0.47 * width), 0.12 * length, 1)
    draw.ellipse(screen, (255, 140, 51),
                 (x0 + 0.7 * length, y0 + 0.5 * width, 0.1 * length, 0.24 * length))  # leg from circle
    draw.ellipse(screen, 'black', (x0 + 0.7 * length, y0 + 0.5 * width, 0.1 * length, 0.24 * length), 1)

    draw.ellipse(screen, (255, 140, 51),
                 (x0 + 0.13 * length, y0 + 0.52 * width, 0.2 * length, 0.2 * width))  # second leg
    draw.ellipse(screen, 'black', (x0 + 0.13 * length, y0 + 0.52 * width, 0.2 * length, 0.2 * width), 1)

    draw.ellipse(screen, (255, 140, 51),
                 (x0 + 0.014 * length, y0 + 0.225 * width, 0.11 * length, 0.375 * width))  # third leg
    draw.ellipse(screen, 'black', (x0 + 0.014 * length, y0 + 0.225 * width, 0.11 * length, 0.375 * width), 1)

    draw.ellipse(screen, (255, 140, 51), (x0, y0 + 0.025 * width, 0.335 * length, 0.5 * width))  # head
    draw.ellipse(screen, 'black', (x0, y0 + 0.025 * width, 0.34 * length, 0.5 * width), 1)

    draw.polygon(screen, (255, 140, 51),
                 [(x0 + 0.22 * length, y0 + 0.075 * width), (x0 + 0.28 * length, y0 + 0.175 * width),
                  (x0 + 0.31 * length, y0)])
    draw.polygon(screen, 'black', [(x0 + 0.22 * length, y0 + 0.075 * width), (x0 + 0.28 * length, y0 + 0.175 * width),
                                   (x0 + 0.31 * length, y0)], 1)
    draw.polygon(screen, (255, 140, 51),
                 [(x0 + 0.1 * length, y0 + 0.075 * width), (x0 + 0.041 * length, y0 + 0.175 * width),
                  (x0 + 0.028 * length, y0)])
    draw.polygon(screen, 'black', [(x0 + 0.1 * length, y0 + 0.075 * width), (x0 + 0.041 * length, y0 + 0.175 * width),
                                   (x0 + 0.028 * length, y0)], 1)

    draw.polygon(screen, (243, 163, 238),
                 [(x0 + 0.24 * length, y0 + 0.075 * width), (x0 + 0.27 * length, y0 + 0.12 * width),
                  (x0 + 0.296 * length, y0 + 0.02 * width)])
    draw.polygon(screen, 'black', [(x0 + 0.24 * length, y0 + 0.075 * width), (x0 + 0.27 * length, y0 + 0.125 * width),
                                   (x0 + 0.296 * length, y0 + 0.02 * width)], 1)
    draw.polygon(screen, (243, 163, 238),
                 [(x0 + 0.084 * length, y0 + 0.075 * width), (x0 + 0.047 * length, y0 + 0.12 * width),
                  (x0 + 0.041 * length, y0 + 0.04 * width)])
    draw.polygon(screen, 'black',
                 [(x0 + 0.084 * length, y0 + 0.075 * width), (x0 + 0.047 * length, y0 + 0.14 * width),
                  (x0 + 0.041 * length, y0 + 0.04 * width)], 1)

    EYE_COLOR = LIGHT_EYE_COLOR

    if not day:
        if active_in_night:
            EYE_COLOR = NIGHT_EYE_COLOR
        else:
            EYE_COLOR = SLEEP_EYE_COLOR

    draw.ellipse(screen, EYE_COLOR, (x0 + 0.196 * length, y0 + 0.175 * width, 0.07 * length, 0.15 * width))
    draw.ellipse(screen, 'black', (x0 + 0.196 * length, y0 + 0.175 * width, 0.07 * length, 0.15 * width), 1)
    draw.ellipse(screen, EYE_COLOR, (x0 + 0.07 * length, y0 + 0.175 * width, 0.07 * length, 0.15 * width))
    draw.ellipse(screen, 'black', (x0 + 0.07 * length, y0 + 0.175 * width, 0.07 * length, 0.15 * width), 1)
    if active_in_night or day:
        draw.ellipse(screen, 'black', (x0 + 0.24 * length, y0 + 0.2 * width, 0.014 * length, 0.1 * width))
        blick = pygame.Surface((0.042 * length, 0.025 * width))
        blick.set_colorkey('BLACK')
        draw.ellipse(blick, 'white', (0, 0, 0.042 * length, 0.025 * width))
        screen.blit(pygame.transform.rotate(blick, 110), (x0 + 0.21 * length, y0 + 0.2 * width))
        draw.ellipse(screen, 'black', (x0 + 0.11 * length, y0 + 0.2 * width, 0.014 * length, 0.1 * width))
        screen.blit(pygame.transform.rotate(blick, 110), (x0 + 0.084 * length, y0 + 0.2 * width))

    draw.polygon(screen, (243, 163, 238),
                 [(x0 + 0.154 * length, y0 + 0.35 * width), (x0 + 0.18 * length, y0 + 0.35 * width),
                  (x0 + 0.166 * length, y0 + 0.39 * width)])
    draw.polygon(screen, 'black', [(x0 + 0.154 * length, y0 + 0.35 * width), (x0 + 0.18 * length, y0 + 0.35 * width),
                                   (x0 + 0.166 * length, y0 + 0.39 * width)], 1)
    draw.line(screen, 'black', [x0 + 0.166 * length, y0 + 0.39 * width], [x0 + 0.166 * length, y0 + 0.415 * width])
    draw.arc(screen, 'black', (x0 + 0.145 * length, y0 + 0.4 * width, 0.028 * length, 0.05 * width), pi, 0)
    draw.arc(screen, 'black', (x0 + 0.166 * length, y0 + 0.4 * width, 0.028 * length, 0.05 * width), pi, 0)
    draw.arc(screen, 'black', (x0 + 0.2 * length, y0 + 0.35 * width, 0.196 * length, 0.05 * width), 0, pi)
    draw.arc(screen, 'black', (x0 + 0.22 * length, y0 + 0.365 * width, 0.196 * length, 0.05 * width), 0, pi)
    draw.arc(screen, 'black', (x0 + 0.23 * length, y0 + 0.38 * width, 0.196 * length, 0.05 * width), 0, pi)
    draw.arc(screen, 'black', (x0 - 0.084 * length, y0 + 0.35 * width, 0.196 * length, 0.05 * width), 0, pi)
    draw.arc(screen, 'black', (x0 - 0.075 * length, y0 + 0.365 * width, 0.196 * length, 0.05 * width), 0, pi)
    draw.arc(screen, 'black', (x0 - 0.084 * length, y0 + 0.38 * width, 0.196 * length, 0.05 * width), 0, pi)


def knit(x0, y0, r, surface):
    '''
    :param x0: центр клубочка по оХ
    :param y0: центр клубочка оУ
    :param r: радиус клубочка
    '''
    draw.circle(surface, 'grey', (x0, y0), r)
    draw.circle(surface, 'black', (x0, y0), r, 1)
    draw.arc(surface, (1, 1, 1), (x0 - 0.75 * r, y0 - 0.5 * r, 1.62 * r, 1.75 * r), 0.1 * pi, 0.55 * pi)
    draw.arc(surface, (1, 1, 1), (x0 - 0.875 * r, y0 - 0.375 * r, 1.62 * r, 1.75 * r), 0.1 * pi, 0.55 * pi)
    draw.arc(surface, (1, 1, 1), (x0 - 0.75 * r, y0 - 0.75 * r, 1.62 * r, 1.75 * r), 0.1 * pi, 0.6 * pi)
    draw.arc(surface, (1, 1, 1), (x0 - 0.375 * r, y0 - 0.375 * r, 1.5 * r, 1.62 * r), 0.7 * pi, 1.1 * pi)
    draw.arc(surface, (1, 1, 1), (x0 - 0.25 * r, y0 - 0.25 * r, 1.5 * r, 1.62 * r), 0.7 * pi, 1.1 * pi)
    draw.arc(surface, (1, 1, 1), (x0 - 0.125 * r, y0 - 0.125 * r, 1.5 * r, 1.62 * r), 0.8 * pi, 1.1 * pi)
    # d.arc(surface, 'grey', (x0 - 1.875 * r, y0 - 0.5 * r, 1.75 * r, 1.87 * r), 1.3 * pi, 1.8 * pi)
    # d.arc(surface, 'grey', (x0 - 3.225 * r, y0 + 0.9 * r, 2 * r, 1.5 * r), 0.2 * pi, 0.8 * pi)

def rollknit(counter_of_ticks, knit_speed):
    roll_knit = pygame.Surface((50, 50))
    knit(25, 25, 25, roll_knit)
    roll_knit.set_colorkey((0, 0, 0))
    screen.blit(pygame.transform.rotate(roll_knit, (-1) * counter_of_ticks * knit_speed),
                (counter_of_ticks * knit_speed, 600 - 50 * sin(counter_of_ticks / 3)))


finished = False
day = True

# background
draw.rect(screen, (128, 85, 23), (0, 0, 600, 350))
draw.rect(screen, (195, 144, 20), (0, 350, 600, 450))

knit_speed = 10
counter_of_ticks = 0

pygame.display.update()
while not finished:
    clock.tick(FPS)
    counter_of_ticks += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            day = not day
        if event.type == pygame.MOUSEBUTTONDOWN:
            rollknit(counter_of_ticks, knit_speed)
    draw.rect(screen, (128, 85, 23), (0, 0, 600, 350))
    draw.rect(screen, (195, 144, 20), (0, 350, 600, 450))
    window(20, 20, 160, 220, day)
    window(280, 20, 200, 220, day)
    cat(250, 360, 350, 200, day, active_in_night=True)
    knit(260, 515, 10, screen)
    cat(150, 550, 200, 150, day, active_in_night=False)

    rollknit(counter_of_ticks, knit_speed)

    if not day:
        screen.blit(night_light, (0, 0))
    pygame.display.update()

pygame.quit()
