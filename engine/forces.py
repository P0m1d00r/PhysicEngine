from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import World

def applyGravity(world: World, time: float):
    for obj in world.objects:
        if obj.mass == 0:
            continue
        obj.currentForce.y -= world.gravity * obj.mass
def addForces(world: World):
    for obj in world.objects:
        obj.currentForce.y += obj.force.y
        obj.currentForce.x += obj.force.x
def applyAcceleration(world: World, time: float):
    for obj in world.objects:
        if obj.mass != 0:
            obj.velocity.y += (obj.currentForce.y / obj.mass) * time
            obj.velocity.x += (obj.currentForce.x / obj.mass) * time
        obj.currentForce.y = 0
        obj.currentForce.x = 0