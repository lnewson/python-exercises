#!/usr/bin/python

import sys
import pygame
from pygame.locals import *


def quitGame():
    """
    Quits the game.
    """
    pygame.quit()
    sys.exit()


def handleEvents(events, mouseDownCallback):
    """
    Handles any user based events picked up by pygame.
    """
    for event in events:
        if event.type == pygame.QUIT:
            quitGame()
        elif event.type == MOUSEBUTTONDOWN:
            mouseDownCallback(event.pos)


def startGame(screen):
    red = Color("red")
    lineWidth = 3
    points = []

    def addPoint(pos):
        """A callback function used to add points when the mouse is clicked"""
        points.append(pos)

    while True:
        # Handle events from the user
        handleEvents(pygame.event.get(), addPoint)

        # Draw the points when we have at least two
        if len(points) > 1:
            pygame.draw.lines(screen, red, False, points, lineWidth)

        # Display everything we've drawn to the screen
        pygame.display.flip()


def initGame():
    # Initialise the pygame library
    pygame.init()

    # Set the window properties
    size = (600, 400)

    # Create the screen window in 32bit mode
    screen = pygame.display.set_mode(size, 0, 32)

    return screen


def main():
    # Initialise the game
    screen = initGame()

    # Start the actual core part of the game that continuously loops
    startGame(screen)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()