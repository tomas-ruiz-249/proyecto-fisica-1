from typing import List
from renderer import *
from physics_engine import PhysicsEngine 
import time
import pygame as pg

class Simulator():
    def __init__(self):
        self.renderer = Renderer(0,0)
        self.physics = PhysicsEngine()
        self.running = True
        self.simulation_start = time.perf_counter()
        self.total_time = 0.0
        self.delta_time = 0.0
    
    def check_for_close(self):
        for event in pg.event.get():
            if event.type == pg.WINDOWCLOSE or pg.key.get_pressed()[pg.K_ESCAPE]:
                self.running = False
    
    def main_loop(self):
        # num_bodies = int(input('select the number of bodies\n'))
        num_bodies = 1
        for i in range(num_bodies):
            body = Body(velocity=Vec(0, 3), name='1', mass = 5)
            body.position.x = 3
            self.physics.bodies.append(body)

        static_body = Body(velocity=Vec(-9,0), name='2', mass=5)
        static_body.position.x = 10
        self.physics.bodies.append(static_body)

        while self.running:
            delta_start = time.perf_counter()

            a = time.perf_counter()
            self.physics.physics_process(self.delta_time)
            a = time.perf_counter() - a 
            self.renderer.render_process(self.physics.bodies)

            self.delta_time = time.perf_counter() - delta_start
            self.check_for_close()

