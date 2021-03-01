import turtle as t

t.shape('turtle')
t.goto(0, 0)
for i in range(1, 11):
    t.pendown()
    t.forward(20 + i*20)
    t.left(90)
    t.forward(20 + i*20)
    t.left(90)
    t.forward(20 + i * 20)
    t.left(90)
    t.forward(20 + i * 20)
    t.left(90)
    t.penup()
    t.goto(-i*10, -i*10)
input()