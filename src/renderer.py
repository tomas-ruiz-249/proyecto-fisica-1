from typing import List
from body import *
import pygame as pg

class Renderer():
    def __init__(self, width:int = 0, height:int = 0):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pg.display.set_mode((width, height), vsync=1)
    
    def draw_bodies(self, bodies: List[Body]):
        for body in bodies:
            pg.draw.circle(self.screen, "red", body.position * 0.1, body.mass * 20)
    
    def render_process(self, bodies: List[Body]):
        self.screen.fill('black')
        self.draw_bodies(bodies)
        pg.display.flip()
        