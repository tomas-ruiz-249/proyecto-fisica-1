from typing import List
from body import *
from math import e
import pygame_menu as pg_menu
import pygame as pg

class Renderer():
    def __init__(self, width:int = 0, height:int = 0 ):
        self.screen = pg.display.set_mode((width, height), vsync=1)
        self.WINDOW_WIDTH = self.screen.get_width()
        self.WINDOW_HEIGHT = self.screen.get_height()
        self.viewport = pg.Surface((self.WINDOW_WIDTH * 0.6 , self.WINDOW_HEIGHT ))
        self.VP_WIDTH = self.viewport.get_width()
        self.VP_HEIGHT = self.viewport.get_height()
        self.METER = self.VP_WIDTH / 10
        self.ground_height = self.VP_HEIGHT * 0.1

        self.menu_surface = pg.Surface((self.WINDOW_WIDTH - self.VP_WIDTH, self.WINDOW_HEIGHT))
    
    def get_menu_surface(self):
        return self.menu_surface
    
    def flip_y(self, y: float):
        return self.VP_HEIGHT - y
    
    def draw_bodies(self, bodies: List[Body]):
        for body in bodies:
            x = body.position.x * self.METER
            y = self.flip_y(body.position.y * self.METER + self.ground_height)
            hue = pg.math.clamp(self.mass_to_hue(body.mass), 0, 270)
            body_color = pg.Color(0,0,0)
            body_color.hsva = (hue, 50, 100, 100)
            pg.draw.circle(self.viewport, body_color, (x,y), body.radius * self.METER)

            font_size = int(body.radius * self.METER * 2)
            font = pg.font.Font(None, font_size)
            text_surface = font.render(body.name, True, (0,0,0))
            text_rect = text_surface.get_rect(center=(x,y))
            self.viewport.blit(text_surface, text_rect)
    
    def draw_background(self):
        self.viewport.fill('aquamarine3')
        new_y = self.flip_y(self.ground_height)
        ground_rect = pg.Rect(0, new_y, self.VP_WIDTH, self.VP_HEIGHT)
        pg.draw.rect(self.viewport, 'grey', ground_rect)
    
    def draw_menu(self, menu: pg_menu.Menu):
        menu.mainloop(self.menu_surface)
    
    def render_process(self, bodies: List[Body], menu: pg_menu.Menu):
        #draw simulation
        self.screen.fill('white')
        self.draw_background()
        self.draw_bodies(bodies)
        self.draw_menu(menu)
        self.screen.blit(self.viewport, (0,0))
        self.screen.blit(self.menu_surface, (self.VP_WIDTH,0))
        pg.display.update()
    
    def mass_to_hue(self, n: float):
        max_hue = 270
        middle_mass = 10
        step = 3
        return max_hue/(1+e**((middle_mass-n)/step)) 
        