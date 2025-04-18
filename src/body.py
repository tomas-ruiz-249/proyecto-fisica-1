from pygame import Vector2 as Vec
from math import sqrt, atan2, pi, sin, cos

class Body():
    def __init__(self,
                 mass: float = 1,
                 position: Vec = None,
                 velocity: Vec = None,
                 acceleration: Vec = None,
                 name: str = None):

        self.mass = mass
        self.radius = mass * 0.3
        self.body_id = name

        if position == None:
            self.position = Vec(0, self.radius) 
        else:
            self.position = position

        if velocity == None:
            self.velocity = Vec(0,0) 
        else:
            self.velocity = velocity

        if acceleration == None:
            self.acceleration = Vec(0,0) 
        else:
            self.acceleration = acceleration


    def is_at_rest(self) -> bool:
        return self.radius == self.position.y and self.velocity.magnitude() < 0.1

    def did_collide_with_body(self, b: "Body") -> bool:
        dist = sqrt((self.position.x - b.position.x)**2 + (self.position.y - b.position.y)**2)
        return dist <= self.radius + b.radius
    
    def handle_body_collision(self, b: "Body", elasticity: float):
        #if intersecting, put one circle outside the other
        ideal_dist = self.radius + b.radius
        real_dist = sqrt((self.position.x - b.position.x)**2 + (self.position.y - b.position.y)**2)
        offset = ideal_dist - real_dist
        angle = atan2(self.position.x - b.position.x, self.position.y - b.position.y)
        offset_x = offset * sin(angle)
        offset_y = offset * cos(angle)
        self.position.x += offset_x
        self.position.y += offset_y

        #change circle velocity
        new_vel = ((2*b.mass*b.velocity.magnitude())+(self.mass - b.mass) * self.velocity.magnitude())/(self.mass + b.mass)
        new_vel *= elasticity
        new_angle = atan2(self.velocity.y, self.velocity.x) + pi
        self.velocity.x = new_vel * cos(new_angle)
        self.velocity.y = new_vel * sin(new_angle)
    
    def did_collide_with_floor(self) -> bool:
        return self.radius >= self.position.y and self.velocity.y < 0
    
    def handle_floor_collision(self):
        self.position.y = self.radius 
        if abs(self.velocity.y) < 0.1:
            self.velocity.y = 0
        else:
            self.velocity.y *= -0.3