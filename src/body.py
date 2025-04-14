from pygame import Vector2 as Vec

class Body():
    def __init__(self, mass: float = 0, position: Vec = Vec(),
                 velocity: Vec = Vec(), acceleration: Vec = Vec(), radius: int = 1):
        self.radius = radius
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.initial_pos = Vec(position)
        self.initial_velocity = Vec(velocity)