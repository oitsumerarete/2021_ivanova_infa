import turtle as t

t.shape('turtle')
def big():
    for i in range(180):
        t.forward(1)
        t.right(1)
def small():
    for i in range(180):
        t.forward(0.3)
        t.right(1)

t.left(90)
while True:
    big()
    small()

