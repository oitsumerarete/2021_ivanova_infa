import turtle as t

t.shape('turtle')
def okr(r):
    for i in range(360):
        t.forward(3.14*r/180)
        t.left(1)


def duga(r):
    for i in range (180):
        t.forward(3.14*r/180)
        t.left(1)


t.left(90)
t.begin_fill()
okr(50)
t.color('yellow')
t.end_fill()
t.penup()
t.goto(-60, 25)

t.pendown()
t.color('black')
t.begin_fill()
okr(10)
t.color('blue')
t.end_fill()
t.penup()
t.goto(-20,25)
t.pendown()

t.color('black')
t.begin_fill()
okr(10)
t.color('blue')
t.end_fill()
t.penup()
t.goto(-50,20)
t.pendown()

t.color('black')
t.width(7)
t.backward(20)

t.penup()
t.goto(-80,0)
t.pendown()
t.color('red')
t.width(10)
t.right(180)
duga(30)

input()