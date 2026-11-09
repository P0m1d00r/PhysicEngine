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
class Force:
    x: float
    y: float

@dataclass
class Velocity:
    x: float
    y: float

WorldObjectType = Rectangle | Circle

@dataclass
class WorldObject:
    mass: float
    mesh: WorldObjectType
    position: Position
    force: Force = field(default_factory=lambda: Force(0,0))
    currentForce: Force = field(default_factory=lambda: Force(0,0))
    velocity: Velocity = field(default_factory=lambda: Velocity(0,0))

    def addConstantForce(self, x: float, y: float):
        self.force.x += x
        self.force.y += y

    def addForce(self, x: float, y: float):
        self.currentForce.x += x
        self.currentForce.y += y

    def addVelocity(self, x: float, y: float):
        self.velocity.x += x
        self.velocity.y += y
