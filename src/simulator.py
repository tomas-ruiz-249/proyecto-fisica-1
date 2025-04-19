from typing import List
from renderer import *
from physics_engine import PhysicsEngine 
import time
import pygame as pg

class Simulator():
    def __init__(self):
        self.physics = PhysicsEngine()
        self.renderer = Renderer(self.physics.elasticity, 1000, 500)
        self.running = True
        self.simulation_start = time.perf_counter()
        self.total_time = 0.0
        self.delta_time = 0.0
    
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.WINDOWCLOSE or pg.key.get_pressed()[pg.K_ESCAPE]:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.physics.add_body()
                if event.key == pg.K_UP:
                    if self.physics.elasticity + 0.1 <= 1:
                        self.physics.elasticity += 0.1
                        self.physics.elasticity = round(self.physics.elasticity, 1)
                elif event.key == pg.K_DOWN:
                    if self.physics.elasticity - 0.1 >= 0:
                        self.physics.elasticity -= 0.1
                        self.physics.elasticity = round(self.physics.elasticity, 1)

    def main_loop(self):
        while self.running:
            delta_start = time.perf_counter()
            self.physics.physics_process(self.delta_time)
            self.renderer.render_process(self.physics.bodies)
            self.delta_time = time.perf_counter() - delta_start

            self.event_loop()

