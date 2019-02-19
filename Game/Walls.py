#Class draw Labyrinth

import pygame
from pygame.locals import * 
from constantes import *
import random
#Levels of the game
class Level():
	
	def __init__(self, file):
		self.file = file
		self.structure = 0
	
	# Method to generate maze depending on extern file 
	# Create a list of a line list 
	def generate(self):
		#Open file
		with open(self.file, "r") as file:
			structure_level = []
			#read all file lines
			for line in file:
				line_level = []
				#Read all sprites(letters) in file
				for sprite in line:
					#Unheeded "\n" at the end of the line
					if sprite != '\n':
						#Add to sprite line list
						line_level.append(sprite)
				#Add line to level list
				structure_level.append(line_level)
			#Save in structure
			self.structure = structure_level
	
	# Display level with generate structure list
	def display_level(self, screen):
		#Loading images (walls, start and finish)
		wall = pygame.image.load(image_wall).convert()
		player = pygame.image.load(image_player).convert_alpha()
		finish = pygame.image.load(image_finish).convert_alpha()
		
		#Read level list
		num_line = 0
		for line in self.structure:
			#Read line list
			num_case = 0
			for sprite in line:
				#Calcul reel position in pixels
				x = num_case * sprite_size
				y = num_line * sprite_size
				if sprite == 'm':		   #m = wall
					screen.blit(wall, (x,y))
				elif sprite == 'd':		   #d = start
					screen.blit(player, (x,y))
				elif sprite == 'a':		   #a = finish
					screen.blit(finish, (x,y))
					
				num_case += 1
			num_line += 1
