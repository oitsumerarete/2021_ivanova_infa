import pygame
import pygame.draw as draw
from math import pi
from math import sin

pygame.init()

FPS = 30
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 800))  # основной экран


night_light = pygame.Surface((600, 800))  # поверхность для ночного затемнения
night_light.fill((58, 58, 58))
night_light.set_colorkey('BLACK')
night_light.set_alpha(128)


LIGHT_COLOR_WINDOW = (197, 241, 233)  # основные цвета
DARK_COLOR_WINDOW = (25, 35, 25)
NIGHT_EYE_COLOR = 'GREEN'
LIGHT_EYE_COLOR = (60, 150, 60)
SLEEP_EYE_COLOR = (235, 130, 51)


knit_speed = 10  # скорость и время движения прягыющего клубка
counter_of_knit_ticks = 0

finished = False  # закончился ли просмотр
day = True  # день или недень (ночь)


def window(x0, y0, width, length, day_):
    """
    Функция отображает окно (домовое) в заданном месте
    :param x0: координата левого верхнего угла окна по оси Х
    :param y0: координата левого верхнего угла окна по оси У
    :param width: ширина окна (ось Х)
    :param length: длина окна (ось У)
    :param day_: день или недень
    """

    if day_:
        color = LIGHT_COLOR_WINDOW
    else:
        color = DARK_COLOR_WINDOW

    draw.rect(screen, (65, 56, 65), (x0, y0, width, length))
    draw.rect(screen, color, (x0 + 0.05 * width, y0 + 0.045 * length, 0.425 * width, 0.25 * length))
    draw.rect(screen, color, (x0 + 0.53 * width, y0 + 0.045 * length, 0.425 * width, 0.25 * length))
    draw.rect(screen, color, (x0 + 0.05 * width, y0 + 0.34 * length, 0.425 * width, 0.59 * length))
    draw.rect(screen, color, (x0 + 0.53 * width, y0 + 0.34 * length, 0.425 * width, 0.59 * length))


def cat(x0, y0, length, width, day_, how_long_is_night, how_long_is_day, active_in_night=True):
    """
    Рисует целого кота
    :param x0: координата верхнего левого угла кошки по оХ
    :param y0: координата верхнего левого угла кошки по оУ
    :param length: длина кошки (оХ)
    :param width: ширина кошки (оУ)
    :param day_: ширина кошки (оУ)
    :param active_in_night: активени ли кот ночью (если нет, то заснёт через 2 секунды,впрочем это можно контролировать)
    :param how_long_is_night: количество ночи в тиках (30 = 1 секунда)
    :param how_long_is_day: количество дня в тиках (30 = 1 секунда)
    """

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

    # рисуем динамическую мордочку с помощью функции
    draw_cat_face(x0, y0, length, width, day_, how_long_is_night, how_long_is_day, active_in_night)


def draw_cat_face(x0, y0, length, width, day_, how_long_is_night, how_long_is_day, active_in_night):
    """
    Рисует коту лицо
    В функцию передаются параметры кота (функции cat в соответсвующие поля)
    :param x0: координата верхнего левого угла кошки по оХ
    :param y0: координата верхнего левого угла кошки по оУ
    :param length: длина кошки (оХ)
    :param width: ширина кошки (оУ)
    :param day_: ширина кошки (оУ)
    :param active_in_night: активени ли кот ночью (если нет, то заснёт через 2 секунды,впрочем это можно контролировать)
    :param how_long_is_night: количество ночи в тиках (30 = 1 секунда)
    :param how_long_is_day: количество дня в тиках (30 = 1 секунда)
    """

    draw_cat_ears(x0, y0, length, width)
    draw_cat_eye(x0, y0, length, width, day_, how_long_is_night, how_long_is_day, active_in_night)
    draw_cat_mouth(x0, y0, length, width)


def draw_cat_ears(x0, y0, length, width):
    """
    Рисует коту ушки в зависимости от переданных значений параметров
    В функцию передаются параметры кота (функции cat в соответсвующие поля)
    :param x0: координата верхнего левого угла кошки по оХ
    :param y0: координата верхнего левого угла кошки по оУ
    :param length: длина кошки (оХ)
    :param width: ширина кошки (оУ)
    """
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


def draw_cat_eye(x0, y0, length, width, day_, how_long_is_night, how_long_is_day, active_in_night):
    """
    Рисует коту глазки в зависимости от переданных значений параметров
    В функцию передаются параметры кота (функции cat в соответсвующие поля)
    :param x0: координата верхнего левого угла кошки по оХ
    :param y0: координата верхнего левого угла кошки по оУ
    :param length: длина кошки (оХ)
    :param width: ширина кошки (оУ)
    :param day_: ширина кошки (оУ)
    :param active_in_night: активени ли кот ночью (если нет, то заснёт через 2 секунды,впрочем это можно контролировать)
    :param how_long_is_night: количество ночи в тиках (30 = 1 секунда)
    :param how_long_is_day: количество дня в тиках (30 = 1 секунда)
    """
    eye_color = LIGHT_EYE_COLOR  # переменная содержит в себе нужный цвет глаз
    if not day_:
        if active_in_night:
            eye_color = NIGHT_EYE_COLOR
        else:
            if how_long_is_night > 60:
                eye_color = SLEEP_EYE_COLOR
            else:
                eye_color = NIGHT_EYE_COLOR
    if day_:
        if not active_in_night and how_long_is_day < 30:
            eye_color = SLEEP_EYE_COLOR
        else:
            eye_color = LIGHT_EYE_COLOR
    # общий контур глаз
    draw.ellipse(screen, eye_color, (x0 + 0.196 * length, y0 + 0.175 * width, 0.07 * length, 0.15 * width))
    draw.ellipse(screen, 'black', (x0 + 0.196 * length, y0 + 0.175 * width, 0.07 * length, 0.15 * width), 1)
    draw.ellipse(screen, eye_color, (x0 + 0.07 * length, y0 + 0.175 * width, 0.07 * length, 0.15 * width))
    draw.ellipse(screen, 'black', (x0 + 0.07 * length, y0 + 0.175 * width, 0.07 * length, 0.15 * width), 1)
    # зрачок и блики
    if ((active_in_night or day or how_long_is_night < 59) and how_long_is_day > 30) or active_in_night:
        draw.ellipse(screen, 'black', (x0 + 0.24 * length, y0 + 0.2 * width, 0.014 * length, 0.1 * width))
        white_el_in_eye = pygame.Surface((0.042 * length, 0.025 * width))
        white_el_in_eye.set_colorkey('BLACK')
        draw.ellipse(white_el_in_eye, 'white', (0, 0, 0.042 * length, 0.025 * width))
        screen.blit(pygame.transform.rotate(white_el_in_eye, 110), (x0 + 0.21 * length, y0 + 0.2 * width))
        draw.ellipse(screen, 'black', (x0 + 0.11 * length, y0 + 0.2 * width, 0.014 * length, 0.1 * width))
        screen.blit(pygame.transform.rotate(white_el_in_eye, 110), (x0 + 0.084 * length, y0 + 0.2 * width))


def draw_cat_mouth(x0, y0, length, width):
    """
    В функцию передаются параметры кота (функции cat в соответсвующие поля) и она рисует мордочку и усы
    :param x0: координата верхнего левого угла кошки по оХ
    :param y0: координата верхнего левого угла кошки по оУ
    :param length: длина кошки (оХ)
    :param width: ширина кошки (оУ)
    """
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
    """
    Функция отрисовки клубо44ка
    :param x0: центр клубочка по оХ
    :param y0: центр клубочка оУ
    :param r: радиус клубочка
    :param surface: вспомогательная поверхность для отрисовки клубка
    """

    draw.circle(surface, 'grey', (x0, y0), r)
    draw.circle(surface, (0, 0, 1), (x0, y0), r, 1)
    draw.arc(surface, (1, 1, 1), (x0 - 0.75 * r, y0 - 0.5 * r, 1.62 * r, 1.75 * r), 0.1 * pi, 0.55 * pi)
    draw.arc(surface, (1, 1, 1), (x0 - 0.875 * r, y0 - 0.375 * r, 1.62 * r, 1.75 * r), 0.1 * pi, 0.55 * pi)
    draw.arc(surface, (1, 1, 1), (x0 - 0.75 * r, y0 - 0.75 * r, 1.62 * r, 1.75 * r), 0.1 * pi, 0.6 * pi)
    draw.arc(surface, (1, 1, 1), (x0 - 0.375 * r, y0 - 0.375 * r, 1.5 * r, 1.62 * r), 0.7 * pi, 1.1 * pi)
    draw.arc(surface, (1, 1, 1), (x0 - 0.25 * r, y0 - 0.25 * r, 1.5 * r, 1.62 * r), 0.7 * pi, 1.1 * pi)
    draw.arc(surface, (1, 1, 1), (x0 - 0.125 * r, y0 - 0.125 * r, 1.5 * r, 1.62 * r), 0.8 * pi, 1.1 * pi)
    draw.arc(surface, 'grey', (x0 - 1.875 * r, y0 - 0.5 * r, 1.75 * r, 1.87 * r), 1.3 * pi, 1.8 * pi)
    draw.arc(surface, 'grey', (x0 - 3.225 * r, y0 + 0.9 * r, 2 * r, 1.5 * r), 0.2 * pi, 0.8 * pi)


def roll_knit(counter_of_ticks, knit_speed_):
    """
    Функция отрисовки прыгающего клубка
    :param counter_of_ticks: количество тиков, прошедших с момента запуска (30 тиков - 1 секунда)
    :param knit_speed_: скорость клубка
    """

    roll_knit_ = pygame.Surface((50, 50))  # поверхность, на которой рисуется клубок
    knit(25, 25, 25, roll_knit_)
    roll_knit_.set_colorkey((0, 0, 0))
    screen.blit(pygame.transform.rotate(roll_knit_, (-1) * counter_of_ticks * knit_speed_),
                (counter_of_ticks * knit_speed_, 600 - 50 * sin(counter_of_ticks / 3)))


# background
draw.rect(screen, (128, 85, 23), (0, 0, 600, 350))
draw.rect(screen, (195, 144, 20), (0, 350, 600, 450))


counter_of_night_ticks = 0
counter_of_day_ticks = 0
if not day:
    counter_of_night_ticks = 61
if day:
    counter_of_day_ticks = 61
pygame.display.update()

# основной цикл отрисовки

while not finished:
    clock.tick(FPS)
    counter_of_knit_ticks += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            day = not day
            if day:
                counter_of_night_ticks = 0
                counter_of_day_ticks = 0
        if (event.type == pygame.MOUSEBUTTONDOWN) and (counter_of_knit_ticks > 60):
            counter_of_knit_ticks = 0
    if not day:
        counter_of_night_ticks += 1
    if day:
        counter_of_day_ticks += 1
    draw.rect(screen, (128, 85, 23), (0, 0, 600, 350))
    draw.rect(screen, (195, 144, 20), (0, 350, 600, 450))
    window(20, 20, 160, 220, day)
    window(280, 20, 200, 220, day)
    cat(250, 360, 350, 200, day, counter_of_night_ticks, counter_of_day_ticks, active_in_night=True)
    knit(260, 515, 20, screen)
    cat(150, 550, 200, 150, day, counter_of_night_ticks, counter_of_day_ticks, active_in_night=False)

    roll_knit(counter_of_knit_ticks, knit_speed)

    if not day:
        screen.blit(night_light, (0, 0))
    pygame.display.update()

pygame.quit()
