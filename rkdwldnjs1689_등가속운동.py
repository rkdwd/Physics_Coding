from vpython import *
#Web VPython 3.2

# Creating ball
ball = sphere(radius = 0.2)

#Initial setting
ball.pos = vec(-2, 0, 0) # m
ball.v = vec(0.8, 0, 0) # m/s
ball.a = vec(0.35, 0, 0) # m/s**2
t = 0; # s
dt = 0.01; # s

attach_arrow(ball, "v", shaftwidth = 0.1, color = color.green) # arrow sign -> v
attach_arrow(ball, "a", shaftwidth = 0.05, color = color.red) # arrow sign -> a
attach_trail(ball, type = 'points', pps = 8)


while True:
    #sleep(0.2)
    rate(1/dt) # how many times in 1 second

    ball.v += ball.a*dt
    ball.pos = ball.pos + ball.v*dt
    t += dt