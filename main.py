from vpython import *
from math import sin, cos, radians

scene = canvas(title='Solar System', width=1000, height=1000, center=vector(0,0,0), background=color.black)
scene.autoscale = False

sphere(pos=vector(0, 0, 0), radius=70, texture={'file': "./stars_milky_way.jpg", 'place': ['left', 'sides'], 'turn': 90}, shininess=1)

sun = sphere(pos=vector(0,0,0), radius=0.25, texture="./sun.jpg")
LSun = label(pos=vector(0,0,0), text='Sun', xoffset=0, yoffset=0, space=30, height=16, border=4, font='sans')

mercury = sphere(pos=vector(0,0.3788,0), radius=0.038, make_trail=True, texture="./mercury.jpg")
Lmercury = label(pos=vector(0,0.3788,0), text='Mercury', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

venus = sphere(pos=vector(0,0.7219,0), radius=0.095, make_trail=True, texture="./venus.jpg")
Lvenus = label(pos=vector(0,0.7219,0), text='Venus', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

earth = sphere(pos=vector(0,1.0025,0), radius=0.1, make_trail=True, texture="./earth.jpg")
Learth = label(pos=vector(0,1.0025,0), text='Earth', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

mars = sphere(pos=vector(0,1.5173,0), radius=0.053, make_trail=True, texture="./mars.jpg")
Lmars = label(pos=vector(0,1.5173,0), text='Mars', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

scene.waitfor("textures")
scene.visible = True

angle_1 = angle_2 = angle_3 = angle_4 = 0

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

    angle_1 += 360/88
    mercury.pos.x = 0.387 * sin(radians(angle_1)) + 0.0796
    mercury.pos.y = 0.3788 * cos(radians(angle_1))
    #mercury.pos.z = 7 * sin(radians(angle_1))
    Lmercury.pos.x = 0.387 * sin(radians(angle_1)) + 0.0796
    Lmercury.pos.y = 0.3788 * cos(radians(angle_1))
    #Lmercury.pos.z = 7 * sin(radians(angle_1))

    angle_2 += 360/224.7
    venus.pos.x = 0.7219 * sin(radians(angle_2)) + 0.0049
    venus.pos.y = 0.7219 * cos(radians(angle_2))
    #venus.pos.z = 3.4 * sin(radians(angle_2))
    Lvenus.pos.x = 0.7219 * sin(radians(angle_2)) + 0.0049
    Lvenus.pos.y = 0.7219 * cos(radians(angle_2))
    #Lvenus.pos.z = 3.4 * sin(radians(angle_2))

    angle_3 += 360/365.2
    earth.pos.x = 1.0027 * sin(radians(angle_3)) + 0.0167
    earth.pos.y = 1.0025 * cos(radians(angle_3))
    Learth.pos.x = 1.0027 * sin(radians(angle_3)) + 0.0167
    Learth.pos.y = 1.0025 * cos(radians(angle_3))

    angle_4 += 360/687
    mars.pos.x = 1.5241 * sin(radians(angle_4)) + 0.1424
    mars.pos.y = 1.5173 * cos(radians(angle_4))
    #mars.pos.z = 1.9 * sin(radians(angle_4))
    Lmars.pos.x = 1.5241 * sin(radians(angle_4)) + 0.1424
    Lmars.pos.y = 1.5173 * cos(radians(angle_4))
    #Lmars.pos.z = 1.9 * sin(radians(angle_4))

