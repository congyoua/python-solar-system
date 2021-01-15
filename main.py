from vpython import *
from math import sin, cos, radians

scene = canvas(width=1000, height=1000, center=vector(0,0,0), background=color.black)
scene.autoscale = False

sphere(pos=vector(0, 0, 0), radius=80, texture={'file': "./stars_milky_way.jpg", 'place': ['left', 'sides'], 'turn': 90}, shininess=1)

sun = sphere(pos=vector(0,0,0), radius=0.75, texture="./sun.jpg")
Lsun = label(pos=vector(0,0,0), text='Sun', xoffset=0, yoffset=0, space=30, height=16, border=4, font='sans')

mercury = sphere(pos=vector(0,1.894,0), radius=0.152, make_trail=False, trail_radius = 0.01, texture="./mercury.jpg")
Lmercury = label(pos=vector(0,1.894,0), text='Mercury', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

venus = sphere(pos=vector(0,3.6095,0), radius=0.38, make_trail=False, trail_radius = 0.01, texture="./venus.jpg")
Lvenus = label(pos=vector(0,3.6095,0), text='Venus', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

earth = sphere(pos=vector(0,5.0125,0), radius=0.4, make_trail=False, trail_radius = 0.01, texture="./earth.jpg")
Learth = label(pos=vector(0,5.0125,0), text='Earth', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

mars = sphere(pos=vector(0,7.5865,0), radius=0.212, make_trail=False, trail_radius = 0.01, texture="./mars.jpg")
Lmars = label(pos=vector(0,7.5865,0), text='Mars', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

moon = sphere(pos=vector(0,5.7625,0), radius=0.109, make_trail=False, trail_color = color.blue, trail_radius = 0.01, texture="./moon.jpg")
Lmoon = label(pos=vector(0,5.7625,0), text='Moon', xoffset=20, yoffset=0, space=30, height=16, border=4, font='sans')

scene.waitfor("textures")
scene.visible = True
scene.pause()

angle_1 = angle_2 = angle_3 = angle_4 = angle_5 = 0

scene.append_to_caption('\nNumber keys: change the camera\n')
scene.append_to_caption('                     1-Mercury 2-Venus 3-Earth 4-Mars M-Moon\n')
scene.append_to_caption('R: reset the camera\n')
scene.append_to_caption('P: Pause the demo, press any other key to resume\n\n')

def check_box(r):
    if r.checked:
        eval(r.text).visible = True
        if Lsun.visible:
            eval('L'+r.text).visible = True
    else:
        eval(r.text).clear_trail()
        eval(r.text).visible = False
        eval('L'+r.text).visible = False
checkbox(bind=check_box, text='mercury' ,checked=True)
checkbox(bind=check_box, text='venus' ,checked=True)
checkbox(bind=check_box, text='earth' ,checked=True)
checkbox(bind=check_box, text='mars' ,checked=True)
checkbox(bind=check_box, text='moon' ,checked=True)
scene.append_to_caption('\n\n')

def Label(r):
    for labels in [Lsun,Lmercury,Lvenus,Learth,Lmars,Lmoon]:
            labels.visible = True if r.checked else False
checkbox(bind = Label, text='Show Labels', checked = True)
scene.append_to_caption('\n\n')

def Trail(r):
    for planet in [mercury,venus,earth,mars]:
        planet.make_trail = True if r.checked else False
        planet.clear_trail()
checkbox(bind = Trail, text='Show Trails(without moon)')
scene.append_to_caption('\n')

def Trailmoon(r):
    moon.make_trail = True if r.checked else False
    moon.clear_trail()
checkbox(bind = Trailmoon, text='Show Moon Trail')
scene.append_to_caption('\n\n')

def CleanTrail():
    for planet in [mercury, venus, earth, mars, moon]:
        planet.clear_trail()
button( bind = CleanTrail, text='Clear Trails' )
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
    elif 'm' in keys:
        scene.camera.follow(moon)
    elif 'r' in keys:
        scene.camera.follow(sun)
    
    rate(30)

    
    mercury.pos.x = 1.935 * sin(radians(angle_1)) + 0.398
    mercury.pos.y = 1.894 * cos(radians(angle_1))
    Lmercury.pos.x = 1.935 * sin(radians(angle_1)) + 0.398
    Lmercury.pos.y = 1.894 * cos(radians(angle_1))
    angle_1 += 360/88

    
    venus.pos.x = 3.6095 * sin(radians(angle_2)) + 0.0245
    venus.pos.y = 3.6095 * cos(radians(angle_2))
    Lvenus.pos.x = 3.6095 * sin(radians(angle_2)) + 0.0245
    Lvenus.pos.y = 3.6095 * cos(radians(angle_2))
    angle_2 += 360/224.7

    
    earth.pos.x = 5.0135 * sin(radians(angle_3)) + 0.0835
    earth.pos.y = 5.0125 * cos(radians(angle_3))
    Learth.pos.x = 5.0135 * sin(radians(angle_3)) + 0.0835
    Learth.pos.y = 5.0125 * cos(radians(angle_3))
    angle_3 += 360/365.2
    
    mars.pos.x = 7.6205 * sin(radians(angle_4)) + 0.712
    mars.pos.y = 7.5865 * cos(radians(angle_4))
    Lmars.pos.x = 7.6205 * sin(radians(angle_4)) + 0.712
    Lmars.pos.y = 7.5865 * cos(radians(angle_4))
    angle_4 += 360/687

    moon.pos.x = earth.pos.x + 0.75 * sin(radians(angle_5)) + 0.05
    moon.pos.y = earth.pos.y + 0.75 * cos(radians(angle_5))
    Lmoon.pos.x = earth.pos.x + 0.75 * sin(radians(angle_5)) + 0.05
    Lmoon.pos.y = earth.pos.y + 0.75 * cos(radians(angle_5))
    angle_5 += 360/27.3
