from vpython import *
from math import sin, cos, radians, tan, sqrt

scene = canvas(title='Solar System', width=1000, height=1000, center=vector(0,0,0), background=color.black)
scene.autoscale = False

sphere(pos=vector(0, 0, 0), radius=70, texture={'file': "./stars_milky_way.jpg", 'place': ['left', 'sides'], 'turn': 90}, shininess=1)

sun = sphere(pos=vector(0,0,0), radius=0.25, texture="./sun.jpg")
LSun = label(pos=vector(0,0,0), text='Sun', xoffset=0, yoffset=0, space=30, height=16, border=4, font='sans', visible = False)

mercury = sphere(pos=vector(0,0.3788,0), radius=0.038, make_trail=True, texture="./mercury.jpg")
Lmercury = label(pos=vector(0,0.3788,0), text='Mercury', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans', visible = False)

venus = sphere(pos=vector(0,0.7219,0), radius=0.095, make_trail=True, texture="./venus.jpg")
Lvenus = label(pos=vector(0,0.7219,0), text='Venus', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans', visible = False)

earth = sphere(pos=vector(0,1.0025,0), radius=0.1, make_trail=True, texture="./earth.jpg")
Learth = label(pos=vector(0,1.0025,0), text='Earth', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans', visible = False)

mars = sphere(pos=vector(0,1.5173,0), radius=0.053, make_trail=True, texture="./mars.jpg")
Lmars = label(pos=vector(0,1.5173,0), text='Mars', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans', visible = False)

scene.waitfor("textures")
scene.visible = True
scene.pause()

angle_1 = angle_2 = angle_3 = angle_4 = 0

def Trail():
    for labels in [mercury,venus,earth,mars]:
        labels.make_trail = not labels.make_trail
button( bind = Trail, text='Hide/Show Trails' )
scene.append_to_caption('\n')

def Label():
    for labels in [LSun,Lmercury,Lvenus,Learth,Lmars]:
        labels.visible = not labels.visible
button( bind = Label, text='Hide/Show Labels' )
scene.append_to_caption('\n\n')


while True:
    keys = keysdown()
    if 'p' in keys:
        scene.waitfor('click keydown')
    elif '1' in keys:
        scene.camera.follow(mercury)
    elif '2' in keys:
        scene.camera.follow(venus)
    elif '3' in keys:
        scene.camera.follow(earth)
    elif '4' in keys:
        scene.camera.follow(mars)
    elif 'r' in keys:
        scene.camera.follow(sun)
    
    rate(30)

    
    mercury.pos.x = 0.387 * sin(radians(angle_1)) + 0.0796
    mercury.pos.y = 0.3788 * cos(radians(angle_1))
    Lmercury.pos.x = 0.387 * sin(radians(angle_1)) + 0.0796
    Lmercury.pos.y = 0.3788 * cos(radians(angle_1))
    angle_1 += 360/88

    
    venus.pos.x = 0.7219 * sin(radians(angle_2)) + 0.0049
    venus.pos.y = 0.7219 * cos(radians(angle_2))
    Lvenus.pos.x = 0.7219 * sin(radians(angle_2)) + 0.0049
    Lvenus.pos.y = 0.7219 * cos(radians(angle_2))
    angle_2 += 360/224.7

    
    earth.pos.x = 1.0027 * sin(radians(angle_3)) + 0.0167
    earth.pos.y = 1.0025 * cos(radians(angle_3))
    Learth.pos.x = 1.0027 * sin(radians(angle_3)) + 0.0167
    Learth.pos.y = 1.0025 * cos(radians(angle_3))
    angle_3 += 360/365.2
    
    mars.pos.x = 1.5241 * sin(radians(angle_4)) + 0.1424
    mars.pos.y = 1.5173 * cos(radians(angle_4))
    Lmars.pos.x = 1.5241 * sin(radians(angle_4)) + 0.1424
    Lmars.pos.y = 1.5173 * cos(radians(angle_4))
    angle_4 += 360/687
