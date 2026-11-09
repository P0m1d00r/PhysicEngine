from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import World

def applyGravity(world: World, time: float):
    for obj in world.objects:
        if obj.mass == 0:
            continue
        obj.velocity.y -= world.gravity * time
def applyAcceleration(world: World, time: float):
    for obj in world.objects:
        obj.velocity.y += obj.acceleration.y * time
        obj.velocity.x += obj.acceleration.x * time