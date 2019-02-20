# Class player create

import pygame
from constantes import *


class Player(pygame.sprite.Sprite):
	#constructor 
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
		self.nb_item = 0
		#Level game
		self.level = level
		#list_ennemy = []
		#self.list = list_ennemy
	#Move player with keyboard
	def move(self, direction, liste, screen):
		list_ennemy = []
		list_ennemy = liste
		game_over = False
		finish = list_ennemy[0]
		#Move to right
		if direction == 'right':
			#Screen limit
			if self.case_x < (numbers_sprite_side - 1):
				print(finish.x)
				print(finish.y)
				game_over = self.test_ennemy_contact(list_ennemy,self.x+sprite_size,self.y, screen)
				print(game_over)
				if game_over == True:
					return True
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
				print(finish.x)
				print(finish.y)
				game_over = self.test_ennemy_contact(list_ennemy,self.x-sprite_size,self.y, screen)
				if game_over == True:
					return True
				if self.level.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.Rect_position_old.left = self.x
					self.Rect_position_old.top = self.y
					self.x = self.case_x * sprite_size
			self.image = pygame.image.load(self.left).convert_alpha()
		
		#Move Up
		if direction == 'up':
			if self.case_y > 0:
				print(finish.x)
				print(finish.y)
				game_over = self.test_ennemy_contact(list_ennemy,self.x,self.y-sprite_size, screen)
				if game_over == True:
					return True
				if self.level.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.Rect_position_old.left = self.x
					self.Rect_position_old.top = self.y
					self.y = self.case_y * sprite_size
			self.image = pygame.image.load(self.up).convert_alpha()
		
		#Move Down
		if direction == 'down':
			if self.case_y < (numbers_sprite_side - 1):
				game_over = self.test_ennemy_contact(list_ennemy,self.x,self.y+sprite_size, screen)
				if game_over == True:
					return True
				if self.level.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.Rect_position_old.left = self.x
					self.Rect_position_old.top = self.y
					self.y = self.case_y * sprite_size
			self.image = pygame.image.load(self.down).convert_alpha()
			
		return False

		
	def collect_item (self, list, syringe, screen):
		wlist = []
		wlist = list
		wall = pygame.image.load(image_wall).convert()
		
		for item in wlist:
			if item.x == self.x and item.y == self.y:
				self.nb_item += 1
				item.x = -1
				item.y = -1
				if self.nb_item == 3:
					self.nb_item += 1
					screen.blit(wall, (11*sprite_size,0))
					screen.blit(wall, (12*sprite_size,0))
					screen.blit(wall, (13*sprite_size,0))
					screen.blit(syringe.image, (syringe.x_display, syringe.y_display))
				else:
					screen.blit(item.image, (item.x_display, item.y_display))
	#class method
	def test_ennemy_contact(self, list, x, y, screen):
		list_ennemy = []
		list_ennemy = list
		finish = list_ennemy[0]
		Rect_position_ennemy = pygame.Rect(x, y, player_size, player_size)
		for ennemy in list_ennemy:
			#if list_ennemy [i].x== x and list_ennemy [i].y== y :
			if finish.x== x and finish.y== y :
				if self.nb_item == 4:
					finish.x = -1
					finish.y = -1
					pygame.draw.rect(screen,BLACK,Rect_position_ennemy,0)
					return False
				else :
					return True
			else :
				return False
	def display(self,screen):
		screen.blit(self.image, (self.x,self.y))

