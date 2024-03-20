from vpython import *
#Web VPython 3.2

# create ball
ball = sphere(radius = 0.2)
ground = box(pos = vec(0, -4, 0), size = vec(15, -0.01, 5))

# initial setting
ball.pos = vec(-2, 0, 0) # m
ball.v = vec(1, 1, 0) # m/s
ball. a = vec(0, -0.35, 0) # m/s**2 : y axis to 0.35m
t = 0 # s
dt = 0.01 # s

attach_trail(ball, type = 'points', pps = 8)

# Motion graph
motion_graph = graph(title = 'position_time', xtitle = 't', ytitle = 'y')
g_bally = gcurve()

motion_graph2 = graph(title = 'velocity_time', xtitle = 't', ytitle = 'y')
g_ballvy = gcurve()

gcurve(color = color.green)


# while loop
while ball.pos.y > ground.pos.y :
    rate(1/dt)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    t += dt
    g_bally.plot(pos = (t, ball.pos.y))
    g_ballvy.plot(pos = (t, ball.v.y))
    
