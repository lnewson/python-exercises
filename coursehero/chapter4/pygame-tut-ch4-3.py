#!/usr/bin/python

import sys
import random
import math
import pygame
from pygame.locals import *
from lib.pyeuclid import Vector2


# Define some global variables
initialVelocity = 20
screenWidth, screenHeight = (600, 400)


class MyCircle:
    def __init__(self, position, size, color=(255, 255, 255), velocity=Vector2(0, 0), width=1):
        self.position = position
        self.size = size
        self.color = color
        self.velocity = velocity
        self.width = width

    def display(self, screen):
        x, y = int(self.position.x), int(self.position.y)
        pygame.draw.circle(screen, self.color, (x, y), self.size, self.width)

    def move(self, dtime):
        self.position += self.velocity * dtime

    def changeVelocity(self, velocity):
        self.velocity = velocity


def getRandomVelocity():
    """
    Gets a random velocity value.
    """
    newAngle = random.uniform(0, math.pi * 2)
    newX = math.sin(newAngle)
    newY = math.cos(newAngle)
    newVector = Vector2(newX, newY)
    newVector.normalize()
    newVector *= initialVelocity
    return newVector


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
        velocity = getRandomVelocity()
        color = random.choice(colors)

        circle = MyCircle(Vector2(x, y), size, color, velocity)
        circles.append(circle)

    directionTick = 0.0

    while True:
        # Limit the frame rate to 60 fps
        dtime_ms = clock.tick(frameRate)
        dtime = dtime_ms / 1000.0

        # Handle events from the user
        handleEvents(pygame.event.get())

        # Calculate the direction and if its greater than 1.0 change a random circles velocity
        directionTick += dtime
        if directionTick > 1.0:
            directionTick = 0.0
            randomCircle = random.choice(circles)
            newVelocity = getRandomVelocity()
            randomCircle.changeVelocity(newVelocity)

        # Lock the screen while we draw
        screen.lock()

        # Redraw the screen as just the background color
        screen.fill(white)

        # Move and draw the circles to the screen
        for circle in circles:
            circle.move(dtime)
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
    pygame.display.set_caption("Vectors and Motion!")

    return screen


def main():
    # Initialise the game
    screen = initGame()

    # Start the actual core part of the game that continuously loops
    startGame(screen)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()