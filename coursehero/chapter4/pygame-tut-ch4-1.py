#!/usr/bin/python

import sys
import pygame
from pygame.locals import *


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

    # Create some circles
    myCircle = MyCircle((100, 100), 10, red)
    myCircle2 = MyCircle((200, 200), 30, blue)
    myCircle3 = MyCircle((300, 150), 40, green, 4)
    myCircle4 = MyCircle((450, 250), 120, black, 0)
    circles = [myCircle, myCircle2, myCircle3, myCircle4]

    while True:
        # Limit the frame rate to 60 fps
        clock.tick(frameRate)

        # Handle events from the user
        handleEvents(pygame.event.get())

        # Redraw the screen as just the background color
        screen.fill(white)

        # Draw the circles to the screen
        for circle in circles:
            circle.display(screen)

        # Display everything we've drawn to the screen
        pygame.display.flip()


def initGame():
    # Initialise the pygame library
    pygame.init()

    # Set the window properties
    size = (600, 400)

    # Create the screen window in 32bit mode
    screen = pygame.display.set_mode(size)

    # Set a title on the window
    pygame.display.set_caption("First Class!")

    return screen


def main():
    # Initialise the game
    screen = initGame()

    # Start the actual core part of the game that continuously loops
    startGame(screen)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()