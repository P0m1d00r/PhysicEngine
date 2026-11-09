from dataclasses import dataclass, field
from .forces import applyGravity, applyAcceleration
from .motion import applyVelocity

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

class World:
    def __init__(self, gravity):
        self.gravity = gravity
        self.objects = []
    def addObject(self, worldObject: WorldObject):
        self.objects.append(worldObject)
    def update(self, time: float):
        updateWorld(self, time)
    def readState(self):
        return self.objects

def updateWorld(world: World, time: float):
    applyGravity(world, time)
    applyAcceleration(world, time)
    applyVelocity(world, time)
    return