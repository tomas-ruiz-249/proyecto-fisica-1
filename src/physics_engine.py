from typing import List
from pygame import Vector2 as Vec
import pygame as pg
from body import Body
from math import atan2, pi, sqrt

class PhysicsEngine():
    def __init__(self):
        self.bodies: List[Body] = []
        self.GRAV = Vec(0, 9.81)
        self.elasticity = 1
    
    def test_func(self):
        print('func got called')
    
    def physics_process(self, time: float):
        for body in self.bodies:
            other_bodies = [b for b in self.bodies if b != body]
            for other in other_bodies:
                if body.did_collide_with_body(other):
                    body.handle_body_collision(other, self.elasticity)

            if not body.is_at_rest():
                body.velocity.x += body.acceleration.x * time
                body.position.x += body.velocity.x * time
                body.position.y += body.velocity.y * time
                body.velocity.y -= self.GRAV.y * time
                if body.did_collide_with_floor():
                    body.handle_floor_collision()