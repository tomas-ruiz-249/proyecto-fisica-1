from typing import List
from renderer import *
from input_handler import *
from physics_engine import PhysicsEngine 
import time
import pygame as pg
import pygame_menu as pg_menu

class Simulator():
    def __init__(self):
        self.physics = PhysicsEngine()
        self.renderer = Renderer(1000, 500)
        self.input = InputHandler(self.renderer.menu_surface, self.physics)
        self.running = True
        self.simulation_start = time.perf_counter()
        self.total_time = 0.0
        self.delta_time = 0.0
    
    def check_for_close(self):
        for event in pg.event.get():
            if event.type == pg.WINDOWCLOSE or pg.key.get_pressed()[pg.K_ESCAPE]:
                self.running = False
    
    def main_loop(self):
        num_bodies = 1
        for i in range(num_bodies):
            body = Body(velocity=Vec(12, 5), name=f'{i+1}', mass=10)
            body.position.x = 0
            self.physics.bodies.append(body)

        static_body = Body(velocity=Vec(-12,5), name='2', mass=10)
        static_body.position.x = 10
        self.physics.bodies.append(static_body)

        while self.running:
            delta_start = time.perf_counter()
            self.physics.physics_process(self.delta_time)
            self.renderer.render_process(self.physics.bodies, self.input.menu)
            self.delta_time = time.perf_counter() - delta_start

            self.check_for_close()

