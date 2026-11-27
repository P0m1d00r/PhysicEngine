from .forces import applyGravity, addForces, applyAcceleration, applyAngularAcceleration
from .motion import applyVelocity, applyAngularVelocity
from .classes import WorldObject
from .collisions import resolveCollisions

class World:
    def __init__(self, gravity):
        self.gravity = gravity
        self.objects: list[WorldObject] = []
    def addObject(self, worldObject: WorldObject):
        self.objects.append(worldObject)
    def update(self, time: float):
        updateWorld(self, time)
    def readState(self):
        return self.objects

def updateWorld(world: World, time: float):
    applyGravity(world, time)
    addForces(world)
    applyAcceleration(world, time)
    applyAngularAcceleration(world, time)
    applyVelocity(world, time)
    applyAngularVelocity(world, time)
    resolveCollisions(world)

    return