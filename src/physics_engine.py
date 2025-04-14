from typing import List
from pygame import Vector2 as Vec
from body import Body
import time

class PhysicsEngine():
    def __init__(self):
        self.bodies: List[Body] = []
        self.GRAV = Vec(0, 9.81)
        for i in range(3):
            body = Body(radius=0.3, mass=1, acceleration=self.GRAV, position=Vec(0.3 ,0.3),
                        velocity=Vec(3 * i, 6 * i))
            self.bodies.append(body)
    
    def physics_process(self, time: float):
        for body in self.bodies:
            if body.position.y > 0:
                body.position.x = body.initial_pos.x + body.velocity.x * time
                body.velocity.y = body.initial_velocity.y - self.GRAV.y * time
                body.position.y = body.initial_pos.y + body.velocity.y * time - 0.5 * self.GRAV.y * time ** 2
    
    def get_bodies(self) -> List[Body]:
        return self.bodies