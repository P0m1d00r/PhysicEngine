from engine.world import World
from engine.classes import WorldObject, Circle, Rectangle, Position
from engine.collisions import getRectangleCorners
import pygame

def drawObject(object: WorldObject, screen: pygame.Surface):
    if object.mesh.type == 'rectangle':
        corners = getRectangleCorners(object)
        corners = [corners[0], corners[2], corners[3], corners[1]]
        for i in range(len(corners)):
            corners[i].x = corners[i].x * 40
            corners[i].y = 600 - (corners[i].y * 40)
        pygame.draw.polygon(screen, object.color, [(c.x, c.y) for c in corners])
    elif object.mesh.type == 'circle':
        position = (object.position.x * 40, 600 - (object.position.y * 40))
        radius = object.mesh.radius * 40
        pygame.draw.circle(screen, object.color, position, radius)
def main():
    pygame.init()
    world = World(gravity=9.81)

    world.objects.extend([
        WorldObject(mass=0, position=Position(10, 0.5), mesh=Rectangle(width=20, height=1), rotation=0, restitution=0.5, color='#ffffff'),
        WorldObject(mass=2, position=Position(10, 2), mesh=Rectangle(width=2, height=2), rotation=0, restitution=0.5, color='#22ff22'),
        WorldObject(mass=2, position=Position(11.8, 10), mesh=Rectangle(width=2, height=2), rotation=0, restitution=0.5, color='#ff2222'),
        WorldObject(mass=1, position=Position(9.8, 10), mesh=Circle(radius=2), rotation=0, restitution=0.5, color='#ffdd22'),
        WorldObject(mass=5, position=Position(9.8, 15), mesh=Circle(radius=0.5), rotation=0, restitution=0.5, color='#eeaaee'),
        ])

    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        time = clock.tick(60) / 1000

        screen.fill((0, 0, 0))
        for object in world.objects:
            drawObject(object, screen)
        pygame.display.flip()
        world.update(time)
    pygame.quit()
if __name__ == "__main__":
    main()