from vpython import *
#Web VPython 3.2

# Creating ball
ball = sphere(radius = 0.2)

#Initial setting
ball.pos = vec(-2, 0, 0) # m
ball.v = vector(0.8, 0, 0) # m/s
t = 0; # s
dt = 0.01; # s

attach_arrow(ball, "v", shaftwidth = 0.1, color = color.green) # arrow sign


while True:
    #sleep(0.2)
    rate(1/dt) # how many times in 1 second

    ball.pos = ball.pos + ball.v*dt
    t += dt