import turtle as t
t.shape('circle')
t.goto(0,0)
x = y = 0.01
vx = 10
vy = 40
ay = -10
dt = 0.1
t.speed = 30
while vx>0:
    if y > 0:
        x += vx*dt
        y += vy*dt + ay*dt**2/2
        vy += ay*dt
    elif y <= 0:
        y = 0.1
        vy = -0.8*vy
        vx = 0.8*vx
    t.goto(x,y)
