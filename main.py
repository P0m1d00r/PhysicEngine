from engine.world import World
from engine.classes import WorldObject, Circle, Rectangle, Position
from engine.collisions import getRectangleCorners, checkColision
from game.config import SCALE, SCREEN_HEIGHT, SCREEN_WIDTH
from game.menu import openMenu
from game.levels import levels
import pygame
import threading
import sys


jumpingCooldown = False
activateMenu = False

level = 0
world = World(gravity=9.81)
player = WorldObject(mass=1, position=Position(0.5, 1.5), mesh=Circle(radius=0.5), rotation=0, restitution=0.5, color='#bc87a5')
finish = WorldObject(mass=0, position=Position(3, 10), mesh=Rectangle(width=1, height=1), rotation=0, restitution=0.5, color='#00ff00')

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



def generateFrame(screen: pygame.Surface, world: World):
    screen.fill((53, 53, 64))
    for object in world.objects:
        drawObject(object, screen)
    pygame.display.flip()



def checkEvents(player: WorldObject):
    global jumpingCooldown
    global activateMenu

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jumpingCooldown == False:
                jumpingCooldown = True
                threading.Timer(1, resetJumpCooldown).start()
                player.addForce(0, 400)
            if event.key == pygame.K_ESCAPE:
                activateMenu = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.addForce(2, 0)
    if keys[pygame.K_a]:
        player.addForce(-2, 0)

def buildLevel(level: int):
    global world
    global player
    global finish

    player = WorldObject(mass=1, position=Position(0.5, 1.5), mesh=Circle(radius=0.5), rotation=0, restitution=0.5, color='#bc87a5')
    finish = levels[level][1]

    world.objects = []

    world.objects.extend(levels[level][0])
    world.objects.append(player)
    world.objects.append(finish)

def main():
    # config and settings
    global activateMenu
    global world
    global player
    global level

    buildLevel(0)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # event loop
    while True:
        # actions
        checkEvents(player)

        # opening menu/ frame generation
        if activateMenu:
            activateMenu = False
            openMenu(screen, player, clock)
            continue
        else:
            generateFrame(screen, world)

        # updateing objecs state
        time = clock.tick(60) / 1000
        world.update(time)

        # win condition
        if checkColision(player, finish):
            level += 1
            if level < len(levels):
                buildLevel(level)
            else:
                level = 0
                buildLevel(level)
if __name__ == "__main__":
    main()