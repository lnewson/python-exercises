#!/usr/bin/python

import sys
import random
import pygame
from pygame.locals import *


# Define some global variables
screenWidth, screenHeight = (600, 400)


class MyCircle:
    def __init__(self, (x, y), size, color=(255, 255, 255), width=1):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.width = width

    def display(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.width)


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


def startGame(screen):
    # Create the clock to control the frame rate
    clock = pygame.time.Clock()
    frameRate = 60

    # Define some colors
    black = Color("black")
    white = Color("white")
    red = Color("red")
    green = Color("green")
    blue = Color("blue")
    colors = [black, red, green, blue]

    # Create some circles
    numCircles = 10
    circles = []
    for n in range(numCircles):
        size = random.randint(10, 20)
        x = random.randint(size, screenWidth - size)
        y = random.randint(size, screenHeight - size)
        color = random.choice(colors)
        circles.append(MyCircle((x, y), size, color))

    while True:
        # Limit the frame rate to 60 fps
        clock.tick(frameRate)

        # Handle events from the user
        handleEvents(pygame.event.get())

        # Lock the screen while we draw
        screen.lock()

        # Redraw the screen as just the background color
        screen.fill(white)

        # Draw the circles to the screen
        for circle in circles:
            circle.display(screen)

        # Unlock the screen now that we are finished
        screen.unlock()

        # Display everything we've drawn to the screen
        pygame.display.flip()


def initGame():
    # Initialise the pygame library
    pygame.init()

    # Set the window properties
    size = screenWidth, screenHeight

    # Create the screen window
    screen = pygame.display.set_mode(size)

    # Set a title on the window
    pygame.display.set_caption("Randomness and Order!")

    return screen


def main():
    # Initialise the game
    screen = initGame()

    # Start the actual core part of the game that continuously loops
    startGame(screen)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()