from engine.classes import WorldObject
from .config import SCALE, SCREEN_WIDTH, SCREEN_HEIGHT, MENU_SCALE
import pygame
from .menuUtils import Button, Stat, screenMiddleX, checkMenuEvents
import sys
from engine.classes import Rectangle, Circle, WorldObject, Position

pygame.font.init()

menuActions = []

global playerObj

leftMenu = False

def closeMenu():
    global leftMenu
    leftMenu = True

def closeGame():
    pygame.quit()
    sys.exit()

def restartGame():
    menuActions.append('RESTART')
    closeMenu()

def addPlayerMass():
    global playerObj
    playerObj.mass += 1

def subPlayerMass():
    global playerObj
    if playerObj.mass > 1:
        playerObj.mass -= 1

def addPlayerRestitution():
    global playerObj
    playerObj.restitution += 0.1
    playerObj.restitution = round(playerObj.restitution, 1)

def subPlayerRestitution():
    global playerObj
    if playerObj.restitution >= 0.1:
        playerObj.restitution -= 0.1
        playerObj.restitution = round(playerObj.restitution, 1)

def switchPlayerMesh():
    global playerObj
    if playerObj.mesh.type == 'rectangle':
        playerObj.mesh = Circle(radius=0.5)
    else:
        playerObj.mesh = Rectangle(width=1, height=1)

def getMass():
    global playerObj
    return playerObj.mass

def getRestitution():
    global playerObj
    return playerObj.restitution

def getPlayerMesh():
    global playerObj
    if playerObj.mesh.type == 'rectangle':
        return 'rect'
    else:
        return 'circle'

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                closeMenu()


def openGameMenu(screen: pygame.Surface, player: WorldObject, clock: pygame.time.Clock):
    global menuActions
    global leftMenu
    global playerObj
    leftMenu = False
    playerObj = player
    menuActions = []

    # [0] -> Buttons, [1] -> Stats
    MENU_LAYOUT: tuple[list[Button], list[Stat]] = (
        [
            Button('Continue', int(screenMiddleX(8)), 8, 8, 1, closeMenu),
            Button('Restart', int(screenMiddleX(8)), 10, 8, 1, restartGame),
            Button('Quit', int(screenMiddleX(8)), 12, 8, 1, closeGame)
        ],
        [
            Stat('Mass', getMass, int(screenMiddleX(3) - 5), 2, addPlayerMass, subPlayerMass),
            Stat('Restitution', getRestitution, int(screenMiddleX(3)), 2, addPlayerRestitution, subPlayerRestitution),
            Stat('Mesh', getPlayerMesh, int(screenMiddleX(3) + 5), 2, switchPlayerMesh, switchPlayerMesh),
        ]
    )

    while True:
        clock.tick(60)

        # check hover
        buttons = MENU_LAYOUT[0]
        mouseX, mouseY = pygame.mouse.get_pos()
        for buttonIndex in range(len(buttons)):
            if buttons[buttonIndex].x < mouseX < (buttons[buttonIndex].x + buttons[buttonIndex].width) and buttons[buttonIndex].y < mouseY < (buttons[buttonIndex].y + buttons[buttonIndex].height):
                buttons[buttonIndex].isHovered = True
            else:
                buttons[buttonIndex].isHovered = False
        stats = MENU_LAYOUT[1]
        for stat in stats:
            if stat.upArrowX < mouseX < (stat.upArrowX + stat.arrowWidth) and stat.upArrowY < mouseY < (stat.upArrowY + stat.arrowHeight):
                stat.upArrowIsHovered = True
            else:
                stat.upArrowIsHovered = False
            if stat.downArrowX < mouseX < (stat.downArrowX + stat.arrowWidth) and stat.downArrowY < mouseY < (stat.downArrowY + stat.arrowHeight):
                stat.downArrowIsHovered = True
            else:
                stat.downArrowIsHovered = False

        # screen etc.
        screen.fill('#353540')
        if leftMenu:
            return menuActions
        else:
            for element in MENU_LAYOUT[0]:
                element.draw(screen)
            for element in MENU_LAYOUT[1]:
                element.draw(screen)
        pygame.display.flip()

        # actions etc.
        checkMenuEvents(MENU_LAYOUT[0], MENU_LAYOUT[1])
        checkEvents()
