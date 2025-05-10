from renderer import *
from menu import *
from physics_engine import * 
import time
import pygame as pg

class Simulator():
    def __init__(self):
        self.physics = PhysicsEngine()
        self.renderer = Renderer(self.physics.elasticity)

        launch = Button(self.physics.launch_bodies, 'reiniciar simulacion')
        start_sim = Button(self.physics.start_sim, 'start')
        stop_sim = Button(self.physics.stop_sim, 'stop')
        increase_elasticity = Button(self.physics.increase_elasticity, 'elasticidad(+)')
        decrease_elasticity = Button(self.physics.decrease_elasticity, 'elasticidad(-)')
        inc_m1 = Button(self.physics.inc_m1, 'masa 1(+)')
        inc_m2 = Button(self.physics.inc_m2, 'masa 2(+)')
        dec_m1 = Button(self.physics.dec_m1, 'masa 1(-)')
        dec_m2 = Button(self.physics.dec_m2, 'masa 2(-)')
        inc_v1 = Button(self.physics.inc_v1, 'Vx1(+)')
        inc_v2 = Button(self.physics.inc_v2, 'Vx2(+)')
        dec_v1 = Button(self.physics.dec_v1, 'Vx1(-)')
        dec_v2 = Button(self.physics.dec_v2, 'Vx2(-)')
        wall_bounce = Button(self.physics.toggle_wall_bounce, 'colision con pared')
        row_1 = Layout([launch])
        row_2 = Layout([start_sim, stop_sim])
        row_3 = Layout([increase_elasticity, decrease_elasticity])
        row_4 = Layout([inc_m1, dec_m1])
        row_5 = Layout([inc_m2, dec_m2])
        row_6 = Layout([inc_v1, dec_v1])
        row_7 = Layout([inc_v2, dec_v2])
        row_8 = Layout([wall_bounce])
        self.menu = Menu([row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8], menuHeight=self.renderer.menu_surface.get_height(), menuWidth=self.renderer.menu_surface.get_width())

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
        self.physics.launch_bodies()
        while self.running:
            delta_start = time.perf_counter()
            self.physics.physics_process(self.delta_time)
            self.renderer.render_process(self.physics.bodies, self.menu, self.physics.get_data())
            self.delta_time = time.perf_counter() - delta_start

            self.event_loop()

