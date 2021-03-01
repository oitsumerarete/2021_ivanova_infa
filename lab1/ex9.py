import turtle as t

t.shape('turtle')
def eight():
    for i in range(360):
        t.forward(1)
        t.left(1)
    for i in range(360):
        t.right(1)
        t.forward(1)

for i in range (3):
    eight()
    t.left(60)
input()