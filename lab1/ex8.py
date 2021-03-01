import turtle as t
import math

t.shape('turtle')
r = 100
x = 0


def func(n):
    t.left(180 - 90 / n)
    t.forward(2 * r * math.sin(180 / n))


for n in range(3, 11):
    for i in range(1, n+1):
        func(n)
    r = r + 50
    t.pendown()
    t.goto(x + 10, 0)
    t.penup()

input()
