from .classes import Rectangle, WorldObject, Position
from typing import TYPE_CHECKING
from math import sqrt

if TYPE_CHECKING:
    from .world import World

def getRectangleCorners(obj: WorldObject):
    corners = []
    if obj.mesh.type != "rectangle":
        return corners
    for xSign in range(-1, 2, 2):
        for ySign in range(-1, 2, 2):
            corners.append(Position(obj.position.x + xSign * 1/2 * obj.mesh.width, obj.position.y + ySign * 1/2 * obj.mesh.height))
    return corners

def checkColision(object1: WorldObject, object2: WorldObject):
    if object1.mesh.type == "rectangle" and object2.mesh.type == "rectangle":
        object1Corners = getRectangleCorners(object1)
        object2Corners = getRectangleCorners(object2)
        normals = []

        for i in range(3):
            corner1 = object1Corners[0]
            corner2 = object1Corners[(i%3)+1]
            corner3 = object1Corners[((i+1)%3)+1]
            corner4 = object1Corners[((i+2)%3)+1]

            vector1 = Position(corner2.x - corner1.x, corner2.y - corner1.y)
            vector2 = Position(corner3.x - corner4.x, corner3.y - corner4.y)

            D = vector1.x*vector2.y - vector1.y*vector2.x

            if abs(D) < 1e-6:
                normal = Position(-vector1.y, vector1.x)
                normals.append(normal)

        for i in range(3):
            corner1 = object2Corners[0]
            corner2 = object2Corners[(i%3)+1]
            corner3 = object2Corners[((i+1)%3)+1]
            corner4 = object2Corners[((i+2)%3)+1]

            vector1 = Position(corner2.x - corner1.x, corner2.y - corner1.y)
            vector2 = Position(corner3.x - corner4.x, corner3.y - corner4.y)

            D = vector1.x*vector2.y - vector1.y*vector2.x

            if abs(D) < 1e-6:
                normal = Position(-vector1.y, vector1.x)
                normals.append(normal)

        for normal in normals:
            projectionCornersPositions1 = []
            projectionCornersPositions2 = []
            normalLen = sqrt(normal.x**2 + normal.y**2)
            for corner in object1Corners:
                dotProduct = normal.x*corner.x + normal.y*corner.y
                projectionPosition = dotProduct / normalLen
                projectionCornersPositions1.append(projectionPosition)
            for corner in object2Corners:
                dotProduct = normal.x*corner.x + normal.y*corner.y
                projectionPosition = dotProduct / normalLen
                projectionCornersPositions2.append(projectionPosition)
            projectionCornersPositions1.sort()
            projectionCornersPositions2.sort()
            min1, max1 = projectionCornersPositions1[0], projectionCornersPositions1[-1]
            min2, max2 = projectionCornersPositions2[0], projectionCornersPositions2[-1]
            if max1 < min2 or max2 < min1:
                return False
        return True
    # TODO: ADD COLLISION FOR OTHER TYPES


def findCollisions(world: World):
    collisions = []
    for objIndex in range(len(world.objects)):
        obj1 = world.objects[objIndex]
        for obj2Index in range(objIndex + 1, len(world.objects)):
            obj2 = world.objects[obj2Index]
            if checkColision(obj1, obj2):
                collisions.append([obj1, obj2])
    return collisions