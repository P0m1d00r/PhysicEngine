from .classes import WorldObject, Position
from typing import TYPE_CHECKING
from math import sqrt, radians, sin, cos
from dataclasses import dataclass

if TYPE_CHECKING:
    from .world import World

@dataclass
class Collision:
    object1: WorldObject
    object2: WorldObject
    mtvNormal: Position
    mtvDepth: float

def getRectangleCorners(obj: WorldObject):
    corners = []
    if obj.mesh.type != "rectangle":
        return corners
    for xSign in range(-1, 2, 2):
        for ySign in range(-1, 2, 2):
            corners.append(Position(obj.position.x + xSign * 1/2 * obj.mesh.width, obj.position.y + ySign * 1/2 * obj.mesh.height))

    rotatedCorners = []
    rotationRad = radians(obj.rotation)
    for corner in corners:
        x = obj.position.x + (corner.x - obj.position.x) * cos(rotationRad) - (corner.y - obj.position.y) * sin(rotationRad)
        y = obj.position.y + (corner.x - obj.position.x) * sin(rotationRad) + (corner.y - obj.position.y) * cos(rotationRad)
        rotatedCorners.append(Position(x, y))
    return rotatedCorners

def calcuateNormals(corner1: Position, corner2: Position, corner3: Position, corner4: Position):
    corners = [corner1, corner2, corner3, corner4]
    normals = []

    for i in range(3):
        corner1 = corners[0]
        corner2 = corners[(i % 3) + 1]
        corner3 = corners[((i + 1) % 3) + 1]
        corner4 = corners[((i + 2) % 3) + 1]

        vector1 = Position(corner2.x - corner1.x, corner2.y - corner1.y)
        vector2 = Position(corner3.x - corner4.x, corner3.y - corner4.y)

        D = vector1.x * vector2.y - vector1.y * vector2.x

        if abs(D) < 1e-6:
            normal = Position(-vector1.y, vector1.x)
            normals.append(normal)
    return normals

def checkColision(object1: WorldObject, object2: WorldObject):
    if object1.mesh.type == "rectangle" and object2.mesh.type == "rectangle":
        object1Corners = getRectangleCorners(object1)
        object2Corners = getRectangleCorners(object2)
        normals = []

        normals.extend(calcuateNormals(object1Corners[0], object1Corners[1], object1Corners[2], object1Corners[3]))
        normals.extend(calcuateNormals(object2Corners[0], object2Corners[1], object2Corners[2], object2Corners[3]))

        collision = Collision(object1, object2, Position(0,0), float('inf'))

        for normal in normals:
            projectionCornersPositions1: list[float] = []
            projectionCornersPositions2: list[float] = []
            normalLen = sqrt(normal.x**2 + normal.y**2)
            for corner in object1Corners:
                dotProduct: float = normal.x*corner.x + normal.y*corner.y
                projectionPosition: float = dotProduct / normalLen
                projectionCornersPositions1.append(projectionPosition)
            for corner in object2Corners:
                dotProduct: float = normal.x*corner.x + normal.y*corner.y
                projectionPosition: float = dotProduct / normalLen
                projectionCornersPositions2.append(projectionPosition)
            projectionCornersPositions1.sort()
            projectionCornersPositions2.sort()
            min1, max1 = projectionCornersPositions1[0], projectionCornersPositions1[-1]
            min2, max2 = projectionCornersPositions2[0], projectionCornersPositions2[-1]
            if max1 < min2 or max2 < min1:
                return False
            else:
                depth = min(abs(max1 - min2), abs(max2 - min1))
                if depth < collision.mtvDepth:
                    collision.mtvDepth = depth
                    centersVector = Position(object2.position.x - object1.position.x, object2.position.y - object1.position.y)
                    if (centersVector.x * normal.x) + (centersVector.y * normal.y) < 0:
                        collision.mtvNormal = Position(-1 * normal.x / normalLen, -1 * normal.y / normalLen)
                    else:
                        collision.mtvNormal = Position(normal.x / normalLen, normal.y / normalLen)

        return collision

    elif object1.mesh.type == "rectangle" and object2.mesh.type == "circle" or object1.mesh.type == "circle" and object2.mesh.type == "rectangle":
        if object1.mesh.type == "rectangle":
            rectangle = object1
            circle = object2
        else:
            rectangle = object2
            circle = object1

        collision = Collision(object1, object2, Position(0, 0), float('inf'))

        rectangleCorners = getRectangleCorners(rectangle)
        rectangleNormals = calcuateNormals(rectangleCorners[0], rectangleCorners[1], rectangleCorners[2], rectangleCorners[3])

        rectangleCornerX = []
        rectangleCornerY = []

        for corner in rectangleCorners:
            rectangleCornerX.append(
                (rectangleNormals[0].x * corner.x + rectangleNormals[0].y * corner.y) / sqrt(rectangleNormals[0].x**2 + rectangleNormals[0].y**2)
            )
            rectangleCornerY.append(
                (rectangleNormals[1].x * corner.x + rectangleNormals[1].y * corner.y) / sqrt(rectangleNormals[1].x**2 + rectangleNormals[1].y**2)
            )
        circleX = (rectangleNormals[0].x * circle.position.x + rectangleNormals[0].y * circle.position.y) / sqrt(rectangleNormals[0].x**2 + rectangleNormals[0].y**2)
        circleY = (rectangleNormals[1].x * circle.position.x + rectangleNormals[1].y * circle.position.y) / sqrt(rectangleNormals[1].x**2 + rectangleNormals[1].y**2)

        circlePosition = Position(circleX, circleY)

        minRectangleX = min(rectangleCornerX)
        maxRectangleX = max(rectangleCornerX)
        minRectangleY = min(rectangleCornerY)
        maxRectangleY = max(rectangleCornerY)

        closestRectanglePoint = Position(max(minRectangleX, min(maxRectangleX, circleX)), max(minRectangleY, min(maxRectangleY, circleY)))

        closestPointDistance = sqrt((closestRectanglePoint.x - circlePosition.x) ** 2 + (closestRectanglePoint.y - circlePosition.y) ** 2)
        if closestPointDistance <= circle.mesh.radius:
            if closestPointDistance == 0:

                depth: float = abs(circleY - maxRectangleY)
                localNormal = Position(0,1)

                if abs(circleY - minRectangleY) < depth:
                    depth = abs(circleY - minRectangleY)
                    localNormal = Position(0,-1)
                if abs(circleX - maxRectangleX) < depth:
                    depth = abs(circleX - maxRectangleX)
                    localNormal = Position(1,0)
                if abs(circleX - minRectangleX) < depth:
                    depth = abs(circleX - minRectangleX)
                    localNormal = Position(-1,0)
                depth += circle.mesh.radius
            else:
                localNormal = Position(circleX - closestRectanglePoint.x, circleY - closestRectanglePoint.y)
                localNormal = Position(localNormal.x / closestPointDistance, localNormal.y / closestPointDistance)
                depth: float = circle.mesh.radius - closestPointDistance

            collision.mtvDepth = depth
            rectangleNormals[0] = Position(rectangleNormals[0].x / sqrt(rectangleNormals[0].x**2 + rectangleNormals[0].y**2), rectangleNormals[0].y / sqrt(rectangleNormals[0].x**2 + rectangleNormals[0].y**2))
            rectangleNormals[1] = Position(rectangleNormals[1].x / sqrt(rectangleNormals[1].x**2 + rectangleNormals[1].y**2), rectangleNormals[1].y / sqrt(rectangleNormals[1].x**2 + rectangleNormals[1].y**2))

            normalX = (localNormal.x * rectangleNormals[0].x + localNormal.y * rectangleNormals[1].x)
            normalY = (localNormal.x * rectangleNormals[0].y + localNormal.y * rectangleNormals[1].y)
            normal = Position(normalX, normalY)

            centersVector = Position(object2.position.x - object1.position.x, object2.position.y - object1.position.y)
            if (centersVector.x * normal.x) + (centersVector.y * normal.y) < 0:
                collision.mtvNormal = Position(-1 * normal.x, -1 * normal.y)
            else:
                collision.mtvNormal = Position(normal.x, normal.y)

            return collision

        return False

    elif object1.mesh.type == "circle" and object2.mesh.type == "circle":
        collision = Collision(object1, object2, Position(0,0), float('inf'))
        centersDistance = sqrt((object1.position.x - object2.position.x) ** 2 + (object1.position.y - object2.position.y) ** 2)
        if centersDistance <= object1.mesh.radius + object2.mesh.radius:
            collision.mtvDepth = abs(centersDistance - object1.mesh.radius - object2.mesh.radius)
            if centersDistance == 0:
                collision.mtvNormal = Position(1, 0)
            else:
                normal = Position(object2.position.x - object1.position.x, object2.position.y - object1.position.y)
                collision.mtvNormal = Position(normal.x / centersDistance, normal.y / centersDistance)
            return collision
        return False
    else:
        return False


def findCollisions(world: list[WorldObject]):
    collisions = []
    for objIndex in range(len(world)):
        obj1 = world[objIndex]
        for obj2Index in range(objIndex + 1, len(world)):
            obj2 = world[obj2Index]
            collision = checkColision(obj1, obj2)
            if collision:
                collisions.append(collision)
    return collisions

def resolveCollisions(world: World):
    collisions = findCollisions(world.objects)
    collidingObjects = []
    for collision in collisions:
        massSum: float = collision.object1.mass + collision.object2.mass
        collision.object1.position.x -= collision.mtvNormal.x * collision.mtvDepth * collision.object2.mass / massSum
        collision.object1.position.y -= collision.mtvNormal.y * collision.mtvDepth * collision.object2.mass / massSum
        collision.object2.position.x += collision.mtvNormal.x * collision.mtvDepth * collision.object1.mass / massSum
        collision.object2.position.y += collision.mtvNormal.y * collision.mtvDepth * collision.object1.mass / massSum

        if collision.object1 not in collidingObjects:
            collidingObjects.append(collision.object1)
        if collision.object2 not in collidingObjects:
            collidingObjects.append(collision.object2)

    for i in range(3):
        collisions = findCollisions(collidingObjects)
        for collision in collisions:
            massSum: float = collision.object1.mass + collision.object2.mass
            collision.object1.position.x -= collision.mtvNormal.x * collision.mtvDepth * collision.object2.mass / massSum
            collision.object1.position.y -= collision.mtvNormal.y * collision.mtvDepth * collision.object2.mass / massSum
            collision.object2.position.x += collision.mtvNormal.x * collision.mtvDepth * collision.object1.mass / massSum
            collision.object2.position.y += collision.mtvNormal.y * collision.mtvDepth * collision.object1.mass / massSum

