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
    contactPoint: Position | None = None

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
        object1Normals = calcuateNormals(object1Corners[0], object1Corners[1], object1Corners[2], object1Corners[3])
        object2Normals = calcuateNormals(object2Corners[0], object2Corners[1], object2Corners[2], object2Corners[3])
        normals.extend(object1Normals)
        normals.extend(object2Normals)

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

        for i in range(len(object1Normals)):
            length = sqrt(object1Normals[i].x**2 + object1Normals[i].y**2)
            object1Normals[i].x = object1Normals[i].x / length
            object1Normals[i].y = object1Normals[i].y / length

        object1CornersInObject1Local = []
        for corner in object1Corners:
            localCornerX = corner.x * object1Normals[0].x + corner.y * object1Normals[0].y
            localCornerY = corner.x * object1Normals[1].x + corner.y * object1Normals[1].y
            object1CornersInObject1Local.append(Position(localCornerX, localCornerY))

        object2CornersInObject1Local = []
        for corner in object2Corners:
            localCornerX = corner.x * object1Normals[0].x + corner.y * object1Normals[0].y
            localCornerY = corner.x * object1Normals[1].x + corner.y * object1Normals[1].y
            object2CornersInObject1Local.append(Position(localCornerX, localCornerY))

        object1LocalMinX = min(object1CornersInObject1Local[0].x,object1CornersInObject1Local[1].x,object1CornersInObject1Local[2].x,object1CornersInObject1Local[3].x)
        object1LocalMaxX = max(object1CornersInObject1Local[0].x,object1CornersInObject1Local[1].x,object1CornersInObject1Local[2].x,object1CornersInObject1Local[3].x)
        object1LocalMinY = min(object1CornersInObject1Local[0].y,object1CornersInObject1Local[1].y,object1CornersInObject1Local[2].y,object1CornersInObject1Local[3].y)
        object1LocalMaxY = max(object1CornersInObject1Local[0].y,object1CornersInObject1Local[1].y,object1CornersInObject1Local[2].y,object1CornersInObject1Local[3].y)

        object2CornersInsideObject1 = []
        for i in range(len(object2CornersInObject1Local)):
            if object1LocalMinX <= object2CornersInObject1Local[i].x <= object1LocalMaxX and object1LocalMinY <= object2CornersInObject1Local[i].y <= object1LocalMaxY:
                object2CornersInsideObject1.append(object2Corners[i])

        # =======================================================================================

        for i in range(len(object2Normals)):
            length = sqrt(object2Normals[i].x**2 + object2Normals[i].y**2)
            object2Normals[i].x = object2Normals[i].x / length
            object2Normals[i].y = object2Normals[i].y / length

        object2CornersInObject2Local = []
        for corner in object2Corners:
            localCornerX = corner.x * object2Normals[0].x + corner.y * object2Normals[0].y
            localCornerY = corner.x * object2Normals[1].x + corner.y * object2Normals[1].y
            object2CornersInObject2Local.append(Position(localCornerX, localCornerY))

        object1CornersInObject2Local = []
        for corner in object1Corners:
            localCornerX = corner.x * object2Normals[0].x + corner.y * object2Normals[0].y
            localCornerY = corner.x * object2Normals[1].x + corner.y * object2Normals[1].y
            object1CornersInObject2Local.append(Position(localCornerX, localCornerY))

        object2LocalMinX = min(object2CornersInObject2Local[0].x,object2CornersInObject2Local[1].x,object2CornersInObject2Local[2].x,object2CornersInObject2Local[3].x)
        object2LocalMaxX = max(object2CornersInObject2Local[0].x,object2CornersInObject2Local[1].x,object2CornersInObject2Local[2].x,object2CornersInObject2Local[3].x)
        object2LocalMinY = min(object2CornersInObject2Local[0].y,object2CornersInObject2Local[1].y,object2CornersInObject2Local[2].y,object2CornersInObject2Local[3].y)
        object2LocalMaxY = max(object2CornersInObject2Local[0].y,object2CornersInObject2Local[1].y,object2CornersInObject2Local[2].y,object2CornersInObject2Local[3].y)

        object1CornersInsideObject2 = []
        for i in range(len(object1CornersInObject2Local)):
            if object2LocalMinX <= object1CornersInObject2Local[i].x <= object2LocalMaxX and object2LocalMinY <= object1CornersInObject2Local[i].y <= object2LocalMaxY:
                object1CornersInsideObject2.append(object1Corners[i])

        allCornersInside = []
        allCornersInside.extend(object1CornersInsideObject2)
        allCornersInside.extend(object2CornersInsideObject1)

        if len(allCornersInside) > 0:
            allCornersInsideXSum = 0
            allCornersInsideYSum = 0
            for corner in allCornersInside:
                allCornersInsideXSum += corner.x
                allCornersInsideYSum += corner.y
            collision.contactPoint = Position(allCornersInsideXSum / len(allCornersInside), allCornersInsideYSum / len(allCornersInside))
        else:
            collision.contactPoint = Position((object1.position.x + object2.position.x) / 2, (object1.position.y + object2.position.y) / 2)

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

            closestPoint: Position = Position(closestRectanglePoint.x * rectangleNormals[0].x + closestRectanglePoint.y * rectangleNormals[1].x, closestRectanglePoint.x * rectangleNormals[0].y + closestRectanglePoint.y * rectangleNormals[1].y)
            collision.contactPoint = closestPoint

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
            overlapStart = max(-object1.mesh.radius, centersDistance - object2.mesh.radius)
            overlapEnd = min(object1.mesh.radius, centersDistance + object2.mesh.radius)
            overlapMiddle = (overlapStart + overlapEnd) / 2
            collision.contactPoint = Position(object1.position.x + collision.mtvNormal.x * overlapMiddle, object1.position.y + collision.mtvNormal.y * overlapMiddle)
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
        if collision.object1.mass == 0:
            invObject1Mass = 0
            invObject1Interia = 0
        else:
            invObject1Mass = 1 / collision.object1.mass
            if collision.object1.mesh.type == 'circle':
                invObject1Interia = 1 / (0.5 * collision.object1.mass * collision.object1.mesh.radius ** 2)
            elif collision.object1.mesh.type == 'rectangle':
                invObject1Interia = 1 / (collision.object1.mass * (collision.object1.mesh.width ** 2 + collision.object1.mesh.height ** 2) / 12)

        if collision.object2.mass == 0:
            invObject2Mass = 0
            invObject2Interia = 0
        else:
            invObject2Mass = 1 / collision.object2.mass
            if collision.object2.mesh.type == 'circle':
                invObject2Interia = 1 / (0.5 * collision.object2.mass * collision.object2.mesh.radius ** 2)
            elif collision.object2.mesh.type == 'rectangle':
                invObject2Interia = 1 / (collision.object2.mass * (
                            collision.object2.mesh.width ** 2 + collision.object2.mesh.height ** 2) / 12)

        object1Angle = Position(collision.contactPoint.x - collision.object1.position.x, collision.contactPoint.y - collision.object1.position.y)
        object2Angle = Position(collision.contactPoint.x - collision.object2.position.x, collision.contactPoint.y - collision.object2.position.y)


        angle1CrossNormal = object1Angle.x * collision.mtvNormal.y - object1Angle.y * collision.mtvNormal.x
        angle2CrossNormal = object2Angle.x * collision.mtvNormal.y - object2Angle.y * collision.mtvNormal.x

        invMassSum: float = invObject1Mass + invObject2Mass
        if invMassSum == 0:
            continue
        collision.object1.position.x -= collision.mtvNormal.x * collision.mtvDepth * invObject1Mass / invMassSum
        collision.object1.position.y -= collision.mtvNormal.y * collision.mtvDepth * invObject1Mass / invMassSum
        collision.object2.position.x += collision.mtvNormal.x * collision.mtvDepth * invObject2Mass / invMassSum
        collision.object2.position.y += collision.mtvNormal.y * collision.mtvDepth * invObject2Mass / invMassSum
        vRel: Position = Position(
            (collision.object2.velocity.x - collision.object2.angularVelocity * object2Angle.y) - (collision.object1.velocity.x - collision.object1.angularVelocity * object1Angle.y),
            (collision.object2.velocity.y + collision.object2.angularVelocity * object2Angle.x) - (collision.object1.velocity.y + collision.object1.angularVelocity * object1Angle.x)
        )
        vNor = vRel.x * collision.mtvNormal.x + vRel.y * collision.mtvNormal.y
        if vNor <= 0:
            vNorRestitution = 0 if abs(vNor) < 0.5 else vNor * -1 * min(collision.object1.restitution, collision.object2.restitution)
            j = (vNorRestitution - vNor) / (invObject1Mass + invObject2Mass + angle1CrossNormal**2 * invObject1Interia + angle2CrossNormal**2 * invObject2Interia)
            j1 = j * invObject1Mass
            j2 = j * invObject2Mass
            collision.object1.velocity.x -= collision.mtvNormal.x * j1
            collision.object1.velocity.y -= collision.mtvNormal.y * j1
            collision.object2.velocity.x += collision.mtvNormal.x * j2
            collision.object2.velocity.y += collision.mtvNormal.y * j2
            collision.object1.angularVelocity -= angle1CrossNormal * j * invObject1Interia
            collision.object2.angularVelocity += angle2CrossNormal * j * invObject2Interia

        if collision.object1 not in collidingObjects:
            collidingObjects.append(collision.object1)
        if collision.object2 not in collidingObjects:
            collidingObjects.append(collision.object2)

    for i in range(3):
        collisions = findCollisions(collidingObjects)
        for collision in collisions:
            if collision.object1.mass == 0:
                invObject1Mass = 0
                invObject1Interia = 0
            else:
                invObject1Mass = 1 / collision.object1.mass
                if collision.object1.mesh.type == 'circle':
                    invObject1Interia = 1 / (0.5 * collision.object1.mass * collision.object1.mesh.radius ** 2)
                elif collision.object1.mesh.type == 'rectangle':
                    invObject1Interia = 1 / (collision.object1.mass * (
                                collision.object1.mesh.width ** 2 + collision.object1.mesh.height ** 2) / 12)

            if collision.object2.mass == 0:
                invObject2Mass = 0
                invObject2Interia = 0
            else:
                invObject2Mass = 1 / collision.object2.mass
                if collision.object2.mesh.type == 'circle':
                    invObject2Interia = 1 / (0.5 * collision.object2.mass * collision.object2.mesh.radius ** 2)
                elif collision.object2.mesh.type == 'rectangle':
                    invObject2Interia = 1 / (collision.object2.mass * (
                            collision.object2.mesh.width ** 2 + collision.object2.mesh.height ** 2) / 12)

            object1Angle = Position(collision.contactPoint.x - collision.object1.position.x,
                                    collision.contactPoint.y - collision.object1.position.y)
            object2Angle = Position(collision.contactPoint.x - collision.object2.position.x,
                                    collision.contactPoint.y - collision.object2.position.y)

            angle1CrossNormal = object1Angle.x * collision.mtvNormal.y - object1Angle.y * collision.mtvNormal.x
            angle2CrossNormal = object2Angle.x * collision.mtvNormal.y - object2Angle.y * collision.mtvNormal.x

            invMassSum: float = invObject1Mass + invObject2Mass
            if invMassSum == 0:
                continue
            collision.object1.position.x -= collision.mtvNormal.x * collision.mtvDepth * invObject1Mass / invMassSum
            collision.object1.position.y -= collision.mtvNormal.y * collision.mtvDepth * invObject1Mass / invMassSum
            collision.object2.position.x += collision.mtvNormal.x * collision.mtvDepth * invObject2Mass / invMassSum
            collision.object2.position.y += collision.mtvNormal.y * collision.mtvDepth * invObject2Mass / invMassSum
            vRel: Position = Position(
                (collision.object2.velocity.x - collision.object2.angularVelocity * object2Angle.y) - (
                            collision.object1.velocity.x - collision.object1.angularVelocity * object1Angle.y),
                (collision.object2.velocity.y + collision.object2.angularVelocity * object2Angle.x) - (
                            collision.object1.velocity.y + collision.object1.angularVelocity * object1Angle.x)
            )
            vNor = vRel.x * collision.mtvNormal.x + vRel.y * collision.mtvNormal.y
            if vNor <= 0:
                vNorRestitution = 0 if abs(vNor) < 0.5 else vNor * -1 * min(collision.object1.restitution, collision.object2.restitution)
                j = (vNorRestitution - vNor) / (invObject1Mass + invObject2Mass + (angle1CrossNormal ** 2) * invObject1Interia + (angle2CrossNormal ** 2) * invObject2Interia)
                j1 = j * invObject1Mass
                j2 = j * invObject2Mass
                collision.object1.velocity.x -= collision.mtvNormal.x * j1
                collision.object1.velocity.y -= collision.mtvNormal.y * j1
                collision.object2.velocity.x += collision.mtvNormal.x * j2
                collision.object2.velocity.y += collision.mtvNormal.y * j2
                collision.object1.angularVelocity -= angle1CrossNormal * j * invObject1Interia
                collision.object2.angularVelocity += angle2CrossNormal * j * invObject2Interia

            if collision.object1 not in collidingObjects:
                collidingObjects.append(collision.object1)
            if collision.object2 not in collidingObjects:
                collidingObjects.append(collision.object2)
