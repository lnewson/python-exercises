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


def handleEvents(events):
    """
    Handles any user based events picked up by pygame.
    """
    for event in events:
        if event.type == pygame.QUIT:
            quitGame()


def drawRect(screen, color, pos, size):
    """
    Draws a Rectangle to the screen, using the specified RGB colour, position and size.
    """
    screen.lock()
    pygame.draw.rect(screen, color, Rect(pos, size))
    screen.unlock()


def drawPolygon(screen, color, points):
    """
    Draws a Polygon to the screen, using the specified RGB colour and list of points.
    """
    screen.lock()
    pygame.draw.polygon(screen, color, points)
    screen.unlock()


def drawCircle(screen, color, pos, radius):
    """
    Draws a Circle with a certain radius to the screen, at the specified position..
    """
    screen.lock()
    pygame.draw.circle(screen, color, pos, radius)
    screen.unlock()


def drawEllipse(screen, color, pos, size):
    """
    Draws an Ellipse with certain bounds to the screen, for the specified colour.
    """
    screen.lock()
    pygame.draw.ellipse(screen, color, Rect(pos, size))
    screen.unlock()


def drawLine(screen, color, pos1, pos2, width=0):
    """
    Draws an Ellipse with certain bounds to the screen, for the specified colour.
    """
    screen.lock()
    pygame.draw.line(screen, color, pos1, pos2)
    screen.unlock()


def startGame(screen):
    # Declare some initial color variables
    aqua = Color("aquamarine")
    yellow = Color("yellow")
    blue = Color("blue")
    green = Color("green")
    random = (200, 155, 64)

    # Declare the shape variables
    rectSize = (150, 125)
    rectPos = (590 - rectSize[0], 390 - rectSize[1])
    polygonPoints = [(20, 120), (140, 140), (110, 30)]
    circleRadius = 50
    circlePos = (300, 200)
    ellipsePos = (440, 10)
    ellipseSize = (150, 90)
    linePos1 = (0, 400)
    linePos2 = (600, 0)
    lineWidth = 4

    while True:
        # Handle events from the user
        handleEvents(pygame.event.get())

        # Draw a rectangle in the bottom right corner (this is done before the image, so the image is in front of the rect)
        drawRect(screen, aqua, rectPos, rectSize)

        # Draw a polygon in the upper left somewhere
        drawPolygon(screen, yellow, polygonPoints)

        # Draw a circle in the middle of the screen
        drawCircle(screen, blue, circlePos, circleRadius)

        # Draw an ellipse in the upper right of the screen
        drawEllipse(screen, green, ellipsePos, ellipseSize)

        # Draw a line from bottom left to top right
        drawLine(screen, random, linePos1, linePos2, lineWidth)

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