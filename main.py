from engine.world import World
from engine.classes import WorldObject, Circle, Rectangle, Position
from engine.collisions import getRectangleCorners

def main():
    world = World(gravity=9.81)

    circle1 = WorldObject(mass=1.0, mesh=Circle(radius=1.0), position=Position(x=0, y=0))
    rectangle1 = WorldObject(mass=2.0, mesh=Rectangle(width=1.5, height=0.8), position=Position(x=3, y=0))
    world.addObject(circle1)
    world.addObject(rectangle1)

    print(getRectangleCorners(circle1))
    print(getRectangleCorners(rectangle1))


if __name__ == "__main__":
    main()