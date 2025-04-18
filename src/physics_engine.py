from typing import List
from pygame import Vector2 as Vec
from body import Body
from math import atan2, pi

class PhysicsEngine():
    def __init__(self):
        self.bodies: List[Body] = []
        self.GRAV = Vec(0, 9.81)
    
    def physics_process(self, time: float):
        for body in self.bodies:
            if body.did_collide_with_floor():
                body.handle_floor_collision()

            other_bodies = [b for b in self.bodies if b != body]
            for other in other_bodies:
                if body.did_collide_with_body(other):
                    print(body.body_id + ' collided with ' + other.body_id)
                    body.handle_body_collision(other, 1)

            if not body.is_at_rest():
                body.velocity.x += body.acceleration.x * time
                body.velocity.y -= self.GRAV.y * time
                body.position.x += body.velocity.x * time
                body.position.y += body.velocity.y * time