import pygame
import sys
from .menuUtils import Button, Stat, screenMiddleX

openSettings = False
openGameSelector = False
quitGame = False


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

def drawMenu(screen: pygame.Surface, menuLayout: tuple[list[Button], list[Stat]]):
    for button in menuLayout[0]:
        button.draw(screen)
    for stat in menuLayout[1]:
        stat.draw(screen)
    # TODO: MOVE TO UTILS


def mainMenu(screen: pygame.Surface, clock: pygame.time.Clock):
    global openSettings
    global openGameSelector
    global quitGame

    MAIN_LAYOUT: tuple[list[Button], list[Stat]] = (
        [],
        []
    )

    while True:
        time = clock.tick(60)
        if quitGame:
            pygame.quit()
            sys.exit()
        elif openSettings:
            openSettings = False
            settingsMenu(screen, clock)
        elif openGameSelector:
            openGameSelector = False
            gameSelectorMenu(screen, clock)

        screen.fill((0,0,0))
        drawMenu(screen, MAIN_LAYOUT)
        pygame.display.flip()
        #TODO: ADD BUTTON CHECKS


def settingsMenu(screen: pygame.Surface, clock: pygame.time.Clock):
    return

def gameSelectorMenu(screen: pygame.Surface, clock: pygame.time.Clock):
    return


