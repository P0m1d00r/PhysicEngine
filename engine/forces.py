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
        obj.currentAngularForce += obj.angularForce

def applyAcceleration(world: World, time: float):
    for obj in world.objects:
        if obj.mass != 0:
            obj.velocity.y += (obj.currentForce.y / obj.mass) * time
            obj.velocity.x += (obj.currentForce.x / obj.mass) * time
        obj.currentForce.y = 0
        obj.currentForce.x = 0

def applyAngularAcceleration(world: World, time: float):
    for obj in world.objects:
        if obj.mesh.type == 'circle':
            interia = 0.5 * obj.mass * obj.mesh.radius**2
        elif obj.mesh.type == 'rectangle':
            interia = obj.mass * (obj.mesh.width**2 + obj.mesh.height**2) / 12
        else:
            interia = 0
        if interia != 0:
            obj.angularVelocity += (obj.currentAngularForce / interia) * time
        obj.currentAngularForce = 0