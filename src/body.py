from pygame import Vector2 as Vec

class Body():
    def __init__(self, mass: float = 0, position: Vec = Vec(),
                 velocity: Vec = Vec(), acceleration: Vec = Vec()):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration