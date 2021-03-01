import turtle as t
import math

t.shape('turtle')
def star(a, n):
    r = a/(2*math.sin(math.pi/n))
    t.left(180/n+90)
    for i in range(n):
        t.forward(a)
        t.left(180-180/n)
    t.right(180-180/n)

star(100,11)
