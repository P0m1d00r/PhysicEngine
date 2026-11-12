from dataclasses import dataclass, field
from typing import Literal

@dataclass
class Circle:
    radius: float
    type: Literal["circle"] = field(default="circle", init=False)

@dataclass
class Rectangle:
    width: float
    height: float
    type: Literal["rectangle"] = field(default="rectangle", init=False)

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
    rotation: float
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
