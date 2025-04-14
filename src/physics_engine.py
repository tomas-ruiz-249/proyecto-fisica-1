from typing import List
from pygame import Vector2 as Vec
from body import Body

class PhysicsEngine():
    def __init__(self):
        self.bodies = list()
        self.GRAV_ACCEL = Vec(0, -9.81)
        for i in range(10):
            body = Body(mass=10, acceleration= self.GRAV_ACCEL)
            self.bodies.append(body)
    
    def physics_process(self):
        for body in self.bodies:
            pass
    
    def get_bodies(self) -> List[Body]:
        return self.bodies