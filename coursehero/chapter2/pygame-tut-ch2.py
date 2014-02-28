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
        elif event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q):
            quitGame()
        elif event.type == MOUSEBUTTONDOWN:
            sounds["laser"].play()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            pygame.image.save(screen, "screenshot.png")


def resizeImage(image, height, width):
    """
    Returns a resized image to the specified size in pixels
    """
    return pygame.transform.scale(image, (height, width))


def startGame(screen, sounds, images):
    # Create the clock to control the frame rate
    clock = pygame.time.Clock()

    # Declare some initial variables
    x = y = r = 0
    colorMod = 1
    frameRate = 60

    while True:
        # Limit the frame rate to 60 fps
        clock.tick(frameRate)

        # Handle events from the user
        handleEvents(screen, pygame.event.get(), sounds)

        # Redraw the screen with just the background color
        screen.fill((r, 0, 0))

        # Get the mouse position
        mx, my = pygame.mouse.get_pos()

        # Place the image on the screen
        screen.blit(images["penguin1"], (mx - 50, my - 50))
        screen.blit(images["penguin2"], (x, y))

        # Display everything we've drawn to the screen
        pygame.display.flip()
        x += 1
        y += 1

        # Make the background change colour rapidly
        if r >= 255:
            colorMod = -1
        elif r <= 0:
            colorMod = 1
        r += 1 * colorMod


def initGame():
    # Initialise the pygame library
    pygame.init()

    # Load the sound file and play it
    startSound = pygame.mixer.Sound("sounds/jet-start-02.wav")
    laserSound = pygame.mixer.Sound("sounds/Laser-Blasts.wav")
    sounds = {
        "start": startSound,
        "laser": laserSound
    }

    # Set the window properties
    size = (600, 400)

    # Create the screen window in 32bit mode
    screen = pygame.display.set_mode(size)

    # Load the penguin image
    penguinImg = pygame.image.load("images/penguin.png")
    penguinImg2 = resizeImage(penguinImg, 100, 100)
    penguinImg = resizeImage(penguinImg, 100, 100)
    images = {
        "penguin1": penguinImg,
        "penguin2": penguinImg2
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