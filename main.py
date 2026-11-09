from engine.world import World, WorldObject, Circle, Rectangle, Position

def main():
    world = World(gravity=9.81)
    world.addObject(WorldObject(mass=1.0, mesh=Circle(radius=1.0), position=Position(x=0, y=0)))
    world.addObject(WorldObject(mass=2.0, mesh=Rectangle(width=1.5, height=0.8), position=Position(x=3, y=0)))
    for i in range(100):
        world.update(0.01)
        state = world.readState()
        print(state)


if __name__ == "__main__":
    main()