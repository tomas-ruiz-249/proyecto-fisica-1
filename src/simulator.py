from renderer import *
from menu import *
from physics_engine import * 
import time
import pygame as pg

class Simulator():
    def __init__(self):
        self.physics = PhysicsEngine()
        self.renderer = Renderer(self.physics.elasticity, 1000, 500)

        launch_btn = Button(self.physics.add_body, 'lanzar cuerpos')
        other_btn = Button(self.physics.change_elasticity, 'cambiar elasticidad')
        offset = self.renderer.menu_surface.get_height() * 0.1
        btn_width = self.renderer.menu_surface.get_width() * 0.8
        layout = VLayout([launch_btn, other_btn], offset, btn_width)
        self.menu = Menu([layout])

        self.running = True
        self.simulation_start = time.perf_counter()
        self.total_time = 0.0
        self.delta_time = 0.0
    
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.WINDOWCLOSE or pg.key.get_pressed()[pg.K_ESCAPE]:
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                x = pos[0] - self.renderer.VP_WIDTH
                y = pos[1]
                self.menu.check_for_click((x,y))


    def main_loop(self):
        while self.running:
            delta_start = time.perf_counter()
            self.physics.physics_process(self.delta_time)
            self.renderer.render_process(self.physics.bodies, self.menu)
            self.delta_time = time.perf_counter() - delta_start

            self.event_loop()

