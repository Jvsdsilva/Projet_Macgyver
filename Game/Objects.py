import pygame
import random
from constantes import *


  #"""
    #This class represents the ball.
    #It derives from the "Sprite" class in Pygame.
    #"""
class Block(pygame.sprite.Sprite):
  

    def __init__(self, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        self.image = pygame.Surface([width, height])
        self.x = 0
        self.y = 0
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        

    def display_list(self):
        image_list = [needle_object, plastic_tube_object, ether_object]
        
        self.list = random.shuffle(image_list)
        
        return image_list
    
        

