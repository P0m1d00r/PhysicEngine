from engine.classes import WorldObject
from .config import SCALE, SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
from collections.abc import Callable
import sys
from engine.classes import Rectangle, Circle, WorldObject, Position

pygame.font.init()
FONT_BUTTON = pygame.font.SysFont('Arial', 36)
FONT_STAT = pygame.font.SysFont('Arial', 18)
menuActions = []

global playerObj

class Button:
    def __init__(self, text: str, x: int, y: int, width: int, height: int, action: Callable[[], None]):
        self.text = text
        self.x = x * SCALE
        self.y = y * SCALE
        self.width = width * SCALE
        self.height = height * SCALE
        self.isHovered = False
        self.color = '#918d8d'
        self.action = action

    def draw(self, screen: pygame.Surface):
        if self.isHovered:
            pygame.draw.rect(screen, self.color, (self.x + 5, self.y - 5, self.width, self.height))

            pygame.draw.rect(screen, '#e39347', (self.x, self.y, self.width, self.height))
            label = FONT_BUTTON.render(self.text, True, (255, 255, 255))
            labelRect = label.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
            screen.blit(label, labelRect)
        else:
            pygame.draw.rect(screen, '#e39347', (self.x + 5, self.y - 5, self.width, self.height))

            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            label = FONT_BUTTON.render(self.text, True, (255, 255, 255))
            labelRect = label.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
            screen.blit(label, labelRect)

class Stat:
    def __init__(self, text: str, getValue: Callable[[], None], x: int, y: int, upArrowAction: Callable[[], None], downArrowAction: Callable[[], None]):
        self.text = text
        self.getValue = getValue
        self.x = x * SCALE
        self.y = y * SCALE
        self.height = 1.5 * SCALE
        self.width = 3 * SCALE
        self.arrowHeight = 0.5 * SCALE
        self.arrowWidth = 0.5 * SCALE
        self.upArrowX = self.x + self.width * 1.1
        self.upArrowY = self.y
        self.downArrowX = self.x + self.width * 1.1
        self.downArrowY = self.y + self.height - self.arrowHeight
        self.upArrowAction = upArrowAction
        self.downArrowAction = downArrowAction
        self.upArrowIsHovered = False
        self.downArrowIsHovered = False

    def draw(self, screen: pygame.Surface):
        value = str(self.getValue())
        pygame.draw.rect(screen, '#555565', (self.x, self.y, self.width, self.height))
        label = FONT_BUTTON.render(value, True, '#ffffff')
        labelRect = label.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(label, labelRect)

        pygame.draw.rect(screen, '#e39347', (self.x, self.y + self.height, self.width, self.height / 2))
        label = FONT_STAT.render(self.text, True, '#ffffff')
        labelRect = label.get_rect(center=(self.x + self.width / 2, (self.y + self.height) + self.height / 4))
        screen.blit(label, labelRect)

        upArrowColor = '#e39347' if self.upArrowIsHovered else '#555565'
        downArrowColor = '#e39347' if self.downArrowIsHovered else '#555565'

        pygame.draw.polygon(screen, upArrowColor, [
            (self.upArrowX + self.arrowWidth / 2, self.upArrowY),
            (self.upArrowX, self.upArrowY + self.arrowHeight),
            (self.upArrowX + self.arrowWidth, self.upArrowY + self.arrowHeight),
        ])
        pygame.draw.polygon(screen, downArrowColor, [
            (self.downArrowX, self.downArrowY),
            (self.downArrowX + self.arrowWidth, self.downArrowY),
            (self.downArrowX + self.arrowWidth / 2, self.downArrowY + self.arrowHeight),
        ])

def screenMiddleX(width: int):
    return (SCREEN_WIDTH / 2 / SCALE) - (width / 2)

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
    if playerObj.restitution > 0.1:
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

def checkEvents(buttons: list[Button], stats: list[Stat]):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                closeMenu()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                mouseX, mouseY = event.pos
                for button in buttons:
                    if button.x < mouseX < (button.x + button.width) and button.y < mouseY < (button.y + button.height):
                        button.action()
                for stat in stats:
                    if stat.upArrowX < mouseX < (stat.upArrowX + stat.arrowWidth ) and stat.upArrowY < mouseY < (stat.upArrowY + stat.arrowHeight):
                        stat.upArrowAction()
                    if stat.downArrowX < mouseX < (stat.downArrowX + stat.arrowWidth ) and stat.downArrowY < mouseY < (stat.downArrowY + stat.arrowHeight):
                        stat.downArrowAction()



def openMenu(screen: pygame.Surface, player: WorldObject, clock: pygame.time.Clock):
    global menuActions
    global leftMenu
    global playerObj
    leftMenu = False
    playerObj = player
    menuActions = []

    # [0] -> Buttons, [1] -> Stats
    MENU_LAYOUT = [
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
    ]

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
        checkEvents(MENU_LAYOUT[0], MENU_LAYOUT[1])
