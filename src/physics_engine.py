from typing import List
from pygame import Vector2 as Vec
import pygame as pg
from body import Body
from math import atan2, pi, sqrt
from random import randint

class PhysicsEngine():
    def __init__(self):
        self.bodies: List[Body] = []
        self.GRAV = Vec(0, 9.81)
        self.elasticity = 1
        self.bounce_border = True
    
    def add_body(self):
        vel_1 = randint(5,15)
        vel_2 = randint(5,8)
        # vel_2 = vel_1
        mass_1 = randint(1,20)
        mass_2 = mass_1
        # mass_2 = randint(1,20)
        if len(self.bodies) > 1:
            self.bodies.pop(0)
            self.bodies.pop(0)
        body_1 = Body(mass=mass_1,
                        name=f'{mass_1}',
                        velocity=Vec(vel_1,5))
        body_2 = Body(mass=mass_1,
                        name=f'{mass_2}',
                        velocity=Vec(-vel_2,5))
        body_1.position.y = 1
        body_2.position.y = 1
        body_2.position.x = 10
        self.bodies.append(body_1)
        self.bodies.append(body_2)
    
    def physics_process(self, time: float):
        print(self.elasticity)
        for body in self.bodies:
            other_bodies = [b for b in self.bodies if b != body]
            for other in other_bodies:
                if body.did_collide_with_body(other):
                    body.handle_body_collision(other, self.elasticity)

            if not body.is_at_rest():
                body.velocity.x += body.acceleration.x * time
                body.position.x += body.velocity.x * time
                body.velocity.y -= self.GRAV.y * time
                body.position.y += body.velocity.y * time
                if body.did_collide_with_floor():
                    body.handle_floor_collision()
                if self.bounce_border:
                    if body.velocity.x < 0 and body.position.x <= body.radius:
                        body.position.x = body.radius + 0.01
                        body.velocity.x *= -0.3
                    if body.velocity.x > 0 and body.position.x >= 10 - body.radius:
                        body.position.x = 10 - body.radius + 0.01
                        body.velocity.x *= -0.3