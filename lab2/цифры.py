import turtle as t

t.shape('turtle')


def one():
    t.penup()
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()
    t.left(45)
    t.forward(14)
    t.right(135)
    t.forward(20)
    t.left(90)



def four():
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.backward(20)
    t.right(90)
    t.penup()
    t.goto(0,0)
    t.pendown()


def seven():
    t.forward(10)
    t.right(135)
    t.forward(14)
    t.left(45)
    t.forward(10)
    t.left(90)
    t.penup()
    t.goto(0,0)
    t.pendown()


def zero():
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.right(90)


one()
t.penup()
t.goto(15,0)
t.pendown()
four()
t.penup()
t.goto(30,0)
t.pendown()
one()
t.penup()
t.goto(45,0)
t.pendown()
seven()
t.penup()
t.goto(60,0)
t.pendown()
zero()
t.penup()
t.goto(75,0)
t.pendown()
zero()

