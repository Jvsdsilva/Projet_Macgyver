# Class player create

import pygame
from constantes import *


class Player(pygame.sprite.Sprite):
	#constructur 
	def __init__(self, right, left, up, down, level):
		#Sprites of the player
		self.image = pygame.image.load(right).convert_alpha()
		self.right = right
		self.left = left
		self.up = up
		self.down = down
		#Position of the player in steps and pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		self.Rect_position_old = pygame.Rect(self.x, self.y, player_size, player_size)
		#Default direction
		self.direction = self.right
		
		#Level game
		self.level = level
	
	#Move player with keyboard
	def move(self, direction):
		
		#Move to right
		if direction == 'right':
			#Screen limit
			if self.case_x < (numbers_sprite_side - 1):
				#Verication if not walls 
				if self.level.structure[self.case_y][self.case_x+1] != 'm':
					#Move one step
					self.case_x += 1
					#Save old position
					self.Rect_position_old.left = self.x
					self.Rect_position_old.top = self.y
					#Calcul of the reel position in pixel
					self.x = self.case_x * sprite_size
			#Image of the player
			self.image = pygame.image.load(self.right).convert_alpha()
		
		#Move to Left
		if direction == 'left':
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.Rect_position_old.left = self.x
					self.Rect_position_old.top = self.y
					self.x = self.case_x * sprite_size
			self.image = pygame.image.load(self.left).convert_alpha()
		
		#Move Up
		if direction == 'up':
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.Rect_position_old.left = self.x
					self.Rect_position_old.top = self.y
					self.y = self.case_y * sprite_size
			self.image = pygame.image.load(self.up).convert_alpha()
		
		#Move Down
		if direction == 'down':
			if self.case_y < (numbers_sprite_side - 1):
				if self.level.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.Rect_position_old.left = self.x
					self.Rect_position_old.top = self.y
					self.y = self.case_y * sprite_size
			self.image = pygame.image.load(self.down).convert_alpha()
		
		print(direction)
		print(self.Rect_position_old.left)
		print(self.Rect_position_old.top)
		
