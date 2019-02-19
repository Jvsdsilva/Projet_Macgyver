import pygame
import random
from constantes import *
  #"""
    #This class represents the ball.
    #It derives from the "Sprite" class in Pygame.
    #"""
class Block(pygame.sprite.Sprite):


	def __init__(self, image_file):
		# Constructor. Pass in the color of the block and its size. """
		# Call the parent class (Sprite) constructor
		super().__init__()
		
		# Create an image of the block.
		# This could also be an image loaded from the disk.
		self.image = pygame.image.load(image_file).convert_alpha()
		#self.image_file = image_file
		self.x = 0
		self.y = 0
		# Fetch the rectangle object that has the dimensions of the image
		# image.
		# Update the position of this object by setting the values
		# of rect.x and rect.y
		self.rect = self.image.get_rect()
		
        
	def set_item(self, player, list, level):
		self.player = (0,0)
		wlist = []
		wlist = list
		x = random.randrange(1,15)
		y = random.randrange(1,15)
		
		for i in wlist:
			while  i.x==x or i.y == y or level.structure[y][x] == 'm' or level.structure[y][x] == 'a' or level.structure[y][x] == 'd':
				x = random.randrange(1,15)
				y = random.randrange(1,15)
		
		self.x = x * sprite_size
		self.y = y * sprite_size
		
		#self.image_file = pygame.image.load(self.image_file).convert_alpha()
        
        
