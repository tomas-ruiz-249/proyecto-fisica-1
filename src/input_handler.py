from physics_engine import *
import pygame_menu as pg_menu
import pygame as pg

class InputHandler():
    def __init__(self, surface: pg.Surface, physics: PhysicsEngine):
        self.surface = surface
        self.menu = pg_menu.Menu('Simulador de colisiones',self.surface.get_width(), self.surface.get_height(),
                                 theme=pg_menu.themes.THEME_BLUE,
                                 surface=self.surface,
                                 position=(0,0),
                                 enabled=True,
                                 verbose=True)
        self.menu.add.button('test', physics.test_func)
        self.menu.add.clock()

    
