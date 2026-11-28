from .config import MENU_SCALE, SCALE, SCREEN_WIDTH
from collections.abc import Callable
import pygame

FONT_BUTTON = pygame.font.SysFont('Arial', int(36 * MENU_SCALE / SCALE))
FONT_STAT = pygame.font.SysFont('Arial', int(18 * MENU_SCALE / SCALE))

def screenMiddleX(width: int):
    return (SCREEN_WIDTH / 2 / MENU_SCALE) - (width / 2)

class Button:
    def __init__(self, text: str, x: int, y: int, width: int, height: int, action: Callable[[], None]):
        self.text = text
        self.x = x * MENU_SCALE
        self.y = y * MENU_SCALE
        self.width = width * MENU_SCALE
        self.height = height * MENU_SCALE
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
        self.x = x * MENU_SCALE
        self.y = y * MENU_SCALE
        self.height = 1.5 * MENU_SCALE
        self.width = 3 * MENU_SCALE
        self.arrowHeight = 0.5 * MENU_SCALE
        self.arrowWidth = 0.5 * MENU_SCALE
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

def checkMenuEvents(buttons: list[Button], stats: list[Stat]): # TODO: USE TUPLE TYPE
    for event in pygame.event.get():
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