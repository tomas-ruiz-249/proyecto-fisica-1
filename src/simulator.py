from typing import List
from renderer import *
from physics_engine import PhysicsEngine 
import pygame as pg

class Simulator():
    def __init__(self):
        self.renderer = Renderer(800, 400)
        self.physics = PhysicsEngine()
        self.running = True
    
    def check_for_close(self):
        for event in pg.event.get():
            if event.type == pg.WINDOWCLOSE or pg.key.get_pressed()[pg.K_ESCAPE]:
                self.running = False
    
    def main_loop(self):
        while self.running:
            self.physics.physics_process()
            self.renderer.render_process(self.physics.get_bodies())
            self.check_for_close()

