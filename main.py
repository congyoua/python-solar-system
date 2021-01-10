from vpython import *
from math import sin, cos, radians

scene = canvas(title='Solar System', width=1000, height=1000, center=vector(0,0,0), background=color.black)
scene.autoscale = False

sphere(pos=vector(0, 0, 0), radius=70, texture={'file': "https://i.imgur.com/UzMziur.jpeg", 'place': ['left', 'sides'], 'turn': 90}, shininess=1)

sun = sphere(pos=vector(0,0,0), radius=0.7, texture="https://i.imgur.com/XdRTvzj.jpg")
LSun = label(pos=vector(0,0,0), text='Sun', xoffset=0, yoffset=0, space=30, height=16, border=4, font='sans')

earth = sphere(pos=vector(0,1.0025,0), radius=0.1, make_trail=True, texture="https://i.imgur.com/nI5Qx0l.jpg")
Learth = label(pos=vector(0,1.0025,0), text='Earth', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

mars = sphere(pos=vector(0,1.5173,0), radius=0.1, make_trail=True, texture="https://i.imgur.com/Mwsa16j.jpg")
Lmars = label(pos=vector(0,1.5173,0), text='Mars', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

neptune = sphere(pos=vector(0,30.0788,0), radius=0.1, make_trail=True, texture="https://i.imgur.com/oG8fX4l.jpeg")
Lneptune = label(pos=vector(0,30.0788,0), text='Neptune', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

scene.waitfor("textures")
scene.visible = True

angle = 0

while True:
    keys = keysdown()
    if 'p' in keys:
        scene.waitfor('click keydown')
    elif '1' in keys:
        pass
    elif '3' in keys:
        scene.camera.follow(earth)
    elif 'r' in keys:
        scene.camera.follow(sun)

    rate(30)

    earth.pos.x = 1.0027 * sin(radians(angle)) + 0.0167
    earth.pos.y = 1.0025 * cos(radians(angle))
    Learth.pos.x = 1.0027 * sin(radians(angle)) + 0.0167
    Learth.pos.y = 1.0025 * cos(radians(angle))

    mars.pos.x = 1.5241 * sin(radians(angle)) + 0.1424
    mars.pos.y = 1.5173 * cos(radians(angle))
    Lmars.pos.x = 1.5241 * sin(radians(angle)) + 0.1424
    Lmars.pos.y = 1.5173 * cos(radians(angle))

    neptune.pos.x = 30.0806 * sin(radians(angle)) + 0.2587
    neptune.pos.y = 30.0788 * cos(radians(angle))
    neptune.pos.z = 7 * sin(radians(angle))
    Lneptune.pos.x = 30.0806 * sin(radians(angle)) + 0.2587
    Lneptune.pos.y = 30.0788 * cos(radians(angle))
    Lneptune.pos.z = 7 * sin(radians(angle))
    angle += 1
    if angle == 359:
        angle = 0