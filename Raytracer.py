import pygame as pg
from pygame.locals import *
from rt import Raytracer
from figures import *
from materials import *
from lights import *

width = 720
height = 720

pg.init()

screen = pg.display.set_mode((width, height), pg.DOUBLEBUF | pg.HWACCEL | pg.HWSURFACE)
screen.set_alpha(None)

raytracer = Raytracer(screen=screen)
raytracer.envMap = pg.image.load("mapa.jpeg")

red = Material(diffuse=(1, 0, 0), specular=2, matType=OPAQUE)
trans = Material(diffuse=(0.5, 0.5, 0.5), specular=64, ks=2.7, ior=2.3, matType=TRANSPARENT)
ref=Material(diffuse=(0.9, 0.9, 0.9), specular=64, ks=2.7, ior=2.3, matType=REFLECTIVE)


raytracer.scene.append(Triangle(material=red, v0=(1,1,-5), v1=(3,1,-5), v2=(2,1,3)))
raytracer.scene.append(Triangle(material=trans, v0=(-1,1,-5), v1=(-3,1,-5), v2=(-2,1,3)))
raytracer.scene.append(Triangle(material=trans, v0=(1,-1,-5), v1=(3,-1,-5), v2=(2,-1,3)))





#Lights
raytracer.lights.append(AmbientLight(0.9))


isRunning = True
while(isRunning):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                isRunning = False
            elif event.key == pg.K_s:
                pg.image.save(screen, "image.bmp")
    raytracer.rtClear()
    raytracer.rtRender()
    pg.display.flip()



pg.quit()