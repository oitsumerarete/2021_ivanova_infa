import turtle as t

t.shape('turtle')
i = 0.001
while i < 10000:
    dl = (0.001 + (5*i) ** 2) ** 0.5
    t.forward(dl)
    t.left(5)
    i = i + 0.001
input()
