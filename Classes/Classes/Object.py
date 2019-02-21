import pygame
import random
from constantes import *


    #This class represents the objects that player have to collect.
class Object(pygame.sprite.Sprite):

    # Constructor.
    def __init__(self, image_file,x_display,y_display):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Create an image of the object.
        self.image = pygame.image.load(image_file).convert_alpha()
        #cordinates of object
        self.x = 0
        self.y = 0
        #coordinates to display object in wall
        self.x_display = x_display
        self.y_display = y_display
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    #Set of random objects
    def set_item(self, player, list, level):
        self.player = (0,0)
        wlist = []
        wlist = list
        x = random.randrange(1,15)
        y = random.randrange(1,15)
        #Obstacles verification to random objects
        for object in wlist:
            while  object.x == x or object.y == y or level.structure[y][x] == 'm' or level.structure[y][x] == 'a' or level.structure[y][x] == 'd':
                #random in screen
                x = random.randrange(1,15)
                y = random.randrange(1,15)
        #Position of random objects
        self.x = x * sprite_size
        self.y = y * sprite_size

