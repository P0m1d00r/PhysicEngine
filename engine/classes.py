from dataclasses import dataclass, field

@dataclass
class Circle:
    radius: float

@dataclass
class Rectangle:
    width: float
    height: float

@dataclass
class Position:
    x: float
    y: float

@dataclass
class Velocity:
    x: float
    y: float

@dataclass
class Acceleration:
    x: float
    y: float

WorldObjectType = Rectangle | Circle

@dataclass
class WorldObject:
    mass: float
    mesh: WorldObjectType
    position: Position
    velocity: Velocity = field(default_factory=lambda: Velocity(0,0))
    acceleration: Acceleration = field(default_factory=lambda: Acceleration(0,0))

    def addVelocity(self, x: float, y: float):
        self.velocity.x += x
        self.velocity.y -= y

    def addAcceleration(self, x: float, y: float):
        self.acceleration.x += x
        self.acceleration.y += y
