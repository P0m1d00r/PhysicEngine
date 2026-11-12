from .classes import Rectangle, WorldObject, Position
from typing import TYPE_CHECKING
from math import sqrt, radians, sin, cos

if TYPE_CHECKING:
    from .world import World

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

def calclateNormals(corner1: Position, corner2: Position, corner3: Position, corner4: Position):
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

        normals.extend(calclateNormals(object1Corners[0], object1Corners[1], object1Corners[2], object1Corners[3]))
        normals.extend(calclateNormals(object2Corners[0], object2Corners[1], object2Corners[2], object2Corners[3]))

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
    elif object1.mesh.type == "rectangle" and object2.mesh.type == "circle" or object1.mesh.type == "circle" and object2.mesh.type == "rectangle":
        if object1.mesh.type == "rectangle":
            rectangle = object1
            circle = object2
        else:
            rectangle = object2
            circle = object1

        rectangleCorners = getRectangleCorners(rectangle)
        rectangleNormals = calclateNormals(rectangleCorners[0], rectangleCorners[1], rectangleCorners[2], rectangleCorners[3])

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
            return True
        return False
    elif object1.mesh.type == "circle" and object2.mesh.type == "circle":
        centersDistance = sqrt((object1.position.x - object2.position.x) ** 2 + (object1.position.y - object2.position.y) ** 2)
        if centersDistance <= object1.mesh.radius + object2.mesh.radius:
            return True
        return False
    else:
        return False


def findCollisions(world: World):
    collisions = []
    for objIndex in range(len(world.objects)):
        obj1 = world.objects[objIndex]
        for obj2Index in range(objIndex + 1, len(world.objects)):
            obj2 = world.objects[obj2Index]
            if checkColision(obj1, obj2):
                collisions.append([obj1, obj2])
    return collisions