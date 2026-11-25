from engine.world import World
from engine.classes import WorldObject, Circle, Rectangle, Position
from engine.collisions import getRectangleCorners
import pygame
import time
import threading

SCALE = 40
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
jumpingCooldown = False

def drawObject(object: WorldObject, screen: pygame.Surface):
    if object.mesh.type == 'rectangle':
        corners = getRectangleCorners(object)
        corners = [corners[0], corners[2], corners[3], corners[1]]
        for i in range(len(corners)):
            corners[i].x = corners[i].x * SCALE
            corners[i].y = SCREEN_HEIGHT - (corners[i].y * SCALE)
        pygame.draw.polygon(screen, object.color, [(c.x, c.y) for c in corners])
    elif object.mesh.type == 'circle':
        position = (object.position.x * SCALE, SCREEN_HEIGHT - (object.position.y * SCALE))
        radius = object.mesh.radius * SCALE
        pygame.draw.circle(screen, object.color, position, radius)

def resetJumpCooldown():
    global jumpingCooldown
    jumpingCooldown = False

def main():
    pygame.init()
    world = World(gravity=9.81)
    global jumpingCooldown
    player = WorldObject(mass=1, position=Position(2, 1.5), mesh=Circle(radius=0.5), rotation=0, restitution=0.5, color='#eeaaee')
    world.objects.extend([
        WorldObject(mass=0, position=Position(10, 0.5), mesh=Rectangle(width=20, height=1), rotation=0, restitution=0.5, color='#ffffff'),
        player
        ])

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jumpingCooldown == False:
                    jumpingCooldown = True
                    threading.Timer(1, resetJumpCooldown).start()
                    player.addForce(0, 400 )

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player.addForce(2,0)
        if keys[pygame.K_a]:
            player.addForce(-2,0)


        time = clock.tick(60) / 1000

        screen.fill((0, 0, 0))
        for object in world.objects:
            drawObject(object, screen)
        pygame.display.flip()
        world.update(time)
if __name__ == "__main__":
    main()