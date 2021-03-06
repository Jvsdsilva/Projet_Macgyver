# Class draw Labyrinth

import pygame
from pygame.locals import *
from constantes import *
import random


# This class represents the level of the game
class Level():
    # constructor
    def __init__(self, file):
        self.file = file
        self.structure = 0

    # Method to generate maze depending on extern file
    # Create a list of a line list
    def generate(self):
        # Open file
        with open(self.file, "r") as file:
            structure_level = []
            # read all file lines
            for line in file:
                line_level = []
                # Read all sprites(letters) in file
                for sprite in line:
                    # Unheeded "\n" at the end of the line
                    if sprite != '\n':
                        # Add to sprite line list
                        line_level.append(sprite)
                # Add line to level list
                structure_level.append(line_level)
            # Save in structure
            self.structure = structure_level

    # Display level with generate structure list
    def display_level(self, screen, list_ennemy):
        # Loading images (walls, start and finish)
        wall = pygame.image.load(IMAGE_WALL).convert()
        player = pygame.image.load(IMAGE_PLAYER).convert_alpha()
        # Read level list
        num_line = 0
        for line in self.structure:
            # Read line list
            num_case = 0
            for sprite in line:
                # Calcul reel position in pixels
                x = num_case*SPRITE_SIZE
                y = num_line*SPRITE_SIZE
                if sprite == 'm':          # m = wall
                    screen.blit(wall, (x, y))
                elif sprite == 'd':        # d = start
                    screen.blit(player, (x, y))
                elif sprite == 'a':        # a = finish
                    # Ennemy position in finish line
                    list_ennemy[0].x = x
                    list_ennemy[0].y = y
                    # list_ennemy[0].display(screen)
                num_case += 1
            num_line += 1
