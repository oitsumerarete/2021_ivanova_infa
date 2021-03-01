import turtle as t

t.shape('turtle')
a = 5
while a < 1000000000000000:
    t.forward(a)
    t.left(90)
    t.forward(a + 5)
    t.left(90)
    t.forward(a + 10)
    t.left(90)
    t.forward(a + 15)
    t.left(90)
    a = a + 20
input()
