from vpython import *
#Web VPython 3.2

rList = list() # pos list
objList = list() # obj(fireworks) list

# create objests
ground = box(pos = vec(0, -4, 0), size = vec(15, -0.01, 5))

# Data input
for i in range(0, 100):
    rList.append(vec(0, -4, 0))
    
# Data analysis
for r in rList:
    objList.append(sphere(pos = r, radius = 0.1, color = vec(random(), random(), random()), make_trail = True, retain = 30))

# Initial Condition
vi = vec(0, 5.0, 0)
a = vec(0, -3, 0)
explosion = False

for obj in objList:
    obj.v = vi
    
# Time Setting
t = 0
dt = 0.01

# Simulation Loop
while t < 12:
    rate(1/dt)
    # Explotion
    if t > 1 and explosion == False:
        print("Explosion!!!")
        for obj in objList:
            obj.v += vec(random()-0.5, random()-0.5, random()-0.5)
        explosion = True
    
    # Velocity and Position Update
    for obj in objList:
        obj.v += a*dt
        obj.pos += obj.v*dt
        # Collision Handling
        if obj.pos.y < ground.pos.y:
            obj.pos.y = ground.pos.y
            obj.v.y = -0.8 * obj.v.y
            obj.color = vec(random(), random(), random())
    t += dt










