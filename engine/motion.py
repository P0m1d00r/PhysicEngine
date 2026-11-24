from typing import TYPE_CHECKING
from math import degrees

if TYPE_CHECKING:
    from .world import World

def applyVelocity(world: World, time: float):
    for obj in world.objects:
        obj.position.x += obj.velocity.x * time
        obj.position.y += obj.velocity.y * time

def applyAngularVelocity(world: World, time: float):
    for obj in world.objects:
        obj.rotation += degrees(obj.angularVelocity * time)