import turtle as t
import math

t.shape('turtle')
def fig(n,a):
    t.penup()
    t.goto(0,0)
    r = a/(2*math.sin(math.pi/n))
    t.goto(r,0)
    t.left(180-90*(n-2)/n)
    t.pendown()
    for i in range(n):
        t.forward(a)
        t.left(180 - (n-2)*180/n)
    t.right(180 - (n-2)*90/n)

a = 15
for i in range(3,11):
    fig(i,a)
    a = a+20
