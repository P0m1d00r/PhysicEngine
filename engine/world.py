from .forces import applyGravity, addForces, applyAcceleration
from .motion import applyVelocity
from .classes import WorldObject

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
    addForces(world)
    applyAcceleration(world, time)
    applyVelocity(world, time)
    return