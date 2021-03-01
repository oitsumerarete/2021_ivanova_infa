import turtle as t

t.shape('turtle')
n = int(input())
for i in range(n):
    t.forward(50)
    t.stamp()
    t.backward(50)
    t.right(360/n)
input()