from typing import List
from renderer import *
from physics_engine import PhysicsEngine 
import time
import pygame as pg

class Simulator():
    def __init__(self):
        self.renderer = Renderer(800, 400)
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
        while self.running:
            delta_start = time.perf_counter()
            self.physics.physics_process(self.delta_time)
            self.renderer.render_process(self.physics.get_bodies())
            delta_end = time.perf_counter()
            self.delta_time = delta_end - delta_start

            self.total_time = time.perf_counter() - self.simulation_start
            self.check_for_close()

