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


def handleEvents(screen, events, sounds):
    """
    Handles any user based events picked up by pygame.
    """
    for event in events:
        if event.type == pygame.QUIT:
            quitGame()


def startGame(screen, sounds, images):
    # Declare some initial variables
    x = y = r = 0
    colorMod = 1

    while True:
        # Handle events from the user
        handleEvents(screen, pygame.event.get(), sounds)

        # Redraw the screen as just the background color
        screen.fill((r, 0, 0))

        # Place the image on the screen
        screen.blit(images["penguin"], (200, 200))
        screen.blit(images["penguin"], (x, y))

        # Display everything we've drawn to the screen
        pygame.display.flip()
        x += 1
        y += 1

        # Make the background change colour rapidly
        if r >= 255:
            colorMod = -1
            sounds["start"].play()
        elif r <= 0:
            colorMod = 1
        r += 1 * colorMod


def initGame():
    # Initialise the pygame library
    pygame.init()

    # Load the sound file
    startSound = pygame.mixer.Sound("sounds/jet-start-02.wav")
    sounds = {
        "start": startSound,
    }

    # Set the window properties
    size = (600, 400)

    # Create the screen window
    screen = pygame.display.set_mode(size)

    # Load the penguin image
    penguinImg = pygame.image.load("images/penguin.png")
    images = {
        "penguin": penguinImg,
    }

    return screen, sounds, images


def main():
    # Initialise the game
    screen, sounds, images = initGame()

    # Play the startup sound
    sounds["start"].play()

    # Start the actual core part of the game that continuously loops
    startGame(screen, sounds, images)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()