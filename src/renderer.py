from typing import List
from body import *
import pygame as pg

class Renderer():
    def __init__(self, width:int = 0, height:int = 0):
        self.WIDTH = width
        self.HEIGHT = height
        self.METER = width / 10
        self.screen = pg.display.set_mode((width, height), vsync=1)
        self.ground_height = self.HEIGHT * 0.25
    
    def flip_y(self, y: float):
        return self.HEIGHT - y
    
    def draw_bodies(self, bodies: List[Body]):
        for body in bodies:
            x = body.position.x * self.METER
            y = self.flip_y(body.position.y * self.METER + self.ground_height)
            pg.draw.circle(self.screen, "chocolate2", (x,y), body.radius * self.METER)

            arrow_x = x + (body.velocity.x * self.METER)
            arrow_y = y - (body.velocity.y * self.METER)

            pg.draw.line(self.screen, 'blue', (x,y), (arrow_x, arrow_y), 3)
    
    def draw_background(self):
        self.screen.fill('aquamarine3')
        new_y = self.flip_y(self.ground_height)
        ground_rect = pg.Rect(0, new_y, self.WIDTH, self.HEIGHT)
        pg.draw.rect(self.screen, 'black', ground_rect)
    
    def render_process(self, bodies: List[Body]):
        self.screen.fill('black')
        self.draw_background()
        self.draw_bodies(bodies)
        pg.display.flip()
        