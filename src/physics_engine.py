from typing import List
from pygame import Vector2 as Vec
from body import Body
import time

class PhysicsEngine():
    def __init__(self):
        self.bodies: List[Body] = []
        self.GRAV = Vec(0, 9.81)
        for i in range(1):
            body = Body(radius=0.3, mass=1, acceleration=self.GRAV, position=Vec(0.3 ,0.4),
                        velocity=Vec(1, 4))
            self.bodies.append(body)
    
    def physics_process(self, time: float):
        for body in self.bodies:
            body.position.x += body.velocity.x * time
            if not body.did_collide_with_floor() and body.velocity.magnitude() > 0:
                body.velocity.y += -self.GRAV.y * time
                body.position.y += body.velocity.y * time - 0.5 * self.GRAV.y * time ** 2
            elif body.did_collide_with_floor():
                body.handle_floor_collision()
    
    def get_bodies(self) -> List[Body]:
        return self.bodies