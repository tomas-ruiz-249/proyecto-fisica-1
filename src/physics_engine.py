from typing import List
from pygame import Vector2 as Vec
import pygame as pg
from body import Body
from math import atan2, pi, sqrt
from random import randint

class EngineData():
    def __init__(self, m1, m2, Vx1, Vx2, e, wall, v1, v2):
        self.m1 = m1
        self.m2 = m2
        self.Vx1 = Vx1
        self.Vx2 = Vx2
        self.e = e
        self.wall = wall
        self.v1 = v1
        self.v2 = v2

class PhysicsEngine():
    def __init__(self):
        self.bodies: List[Body] = []
        self.GRAV = Vec(0, 9.81)
        self.elasticity = 1
        self.bounce_border = False
        self.simulation_running = True

        self.Vx1 = 13
        self.Vx2 = 7
        self.m1 = 5
        self.m2 = 5
        self.data = EngineData(self.m2, self.m2, self.Vx1, self.Vx2, self.elasticity, self.bounce_border, 0, 0)

    
    def get_data(self):
        return self.data
    
    def start_sim(self):
        self.simulation_running = True
    
    def stop_sim(self):
        self.simulation_running = False
    
    def launch_bodies(self):
        if len(self.bodies) > 1:
            self.bodies.pop(0)
            self.bodies.pop(0)
        body_1 = Body(mass=self.m1,
                        name=f'{self.m1}',
                        velocity=Vec(self.Vx1,5))
        body_2 = Body(mass=self.m2,
                        name=f'{self.m2}',
                        velocity=Vec(-self.Vx2,5))
        body_1.position.y = 2
        body_2.position.y = 2
        body_2.position.x = 10
        # self.data = EngineData(self.m1,
        #                        self.m2,
        #                        self.Vx1,
        #                        self.Vx2,
        #                        self.elasticity,
        #                        self.bounce_border,
        #                        body_1.velocity.magnitude(),
        #                        body_2.velocity.magnitude())
        self.data = EngineData(self.m1,
                               self.m2,
                               self.Vx1,
                               self.Vx2,
                               self.elasticity,
                               self.bounce_border,
                               body_1.velocity,
                               body_2.velocity)
        self.bodies.append(body_1)
        self.bodies.append(body_2)
    
    def increase_elasticity(self):
        if self.elasticity < 1:
            self.elasticity = round(self.elasticity + 0.1, 2)
        self.data.e = self.elasticity
    

    def decrease_elasticity(self):
        if self.elasticity > 0:
            self.elasticity = round(self.elasticity - 0.1, 2)
        self.data.e = self.elasticity
    
    def inc_m1(self):
        if self.simulation_running:
            return
        self.m1 += 1
        self.data.m1 = self.m1
    
    def inc_m2(self):
        if self.simulation_running:
            return
        self.m2 += 1
        self.data.m2 = self.m2
    
    def dec_m1(self):
        if self.simulation_running:
            return
        if self.m1 > 1:
            self.m1 -= 1
        self.data.m1 = self.m1
    
    def dec_m2(self):
        if self.simulation_running:
            return
        if self.m2 > 1:
            self.m2 -= 1
        self.data.m2 = self.m2
    
    def inc_v1(self):
        if self.simulation_running:
            return
        self.Vx1 += 1
        self.data.Vx1 = self.Vx1
    
    def inc_v2(self):
        if self.simulation_running:
            return
        self.Vx2 += 1
        self.data.Vx2 = self.Vx2
    
    def dec_v1(self):
        if self.simulation_running:
            return
        if self.Vx1 > 1:
            self.Vx1 -= 1
        self.data.Vx1 = self.Vx1
    
    def dec_v2(self):
        if self.simulation_running:
            return
        if self.Vx2 > 1:
            self.Vx2 -= 1
        self.data.Vx2 = self.Vx2
    
    def toggle_wall_bounce(self):
        if self.bounce_border:
            self.bounce_border = False
        else:
            self.bounce_border = True
    
    def physics_process(self, time: float):
        if self.simulation_running:
            count = 0
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
                if count == 0:
                    self.data.v1 = body.velocity
                else:
                    self.data.v2 = body.velocity
                count += 1