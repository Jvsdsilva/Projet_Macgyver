#!/usr/bin/python3
# -*- coding: Utf-8 -*
import pygame
import random
from Game import Objects
from Game import Players
from Game import Walls
from constantes import *

#Main program
def main():

	# Call this function so the Pygame library can initialize itself
	pygame.init()
	# Create the surface of (width, height), and its window.
	screen = pygame.display.set_mode((screen_side, screen_side))
	# Set the title of the window
	pygame.display.set_caption(screen_titre)
	
	# This is a font we use to draw text on the screen (size 36)
	font = pygame.font.Font(None, 36)
	# Use this boolean variable to trigger if the game is over.
	game_over = False
	
	#Set file
	file = 'Niveau'
	 # This is a list of 'sprites.' Each block in the program is
	# added to this list. The list is managed by a class called 'Group.'
	block_list = pygame.sprite.Group()
 
	# This is a list of every sprite. All blocks and the player block as well.
	all_sprites_list = pygame.sprite.Group()
	
	#Generate labyrinth
	level = Walls.Level(file)
	list_ennemy = []
	
	#Create player
	player1 = Players.Player(image_player,image_player, image_player,image_player, level)
	player2 = Players.Player(image_finish,image_finish, image_finish,image_finish, level)
	list_ennemy.append(player2)
	#Create liste of objects
	list_items = []
	
	level.generate()
	level.display_level(screen,list_ennemy)
	
	#Instatiation objects
	plastic_tube = Objects.Block(plastic_tube_object)
	ether = Objects.Block(ether_object)
	needle = Objects.Block(needle_object)
	# Add objects to list
	list_items.append(needle)
	list_items.append(ether)
	list_items.append(plastic_tube)

	# Set de position of objects
	needle.set_item(player1,list_items,level)
	ether.set_item(player1,list_items,level)
	plastic_tube.set_item(player1,list_items,level)

	# Set image object
	needle.image = pygame.image.load(needle_object)
	ether.image = pygame.image.load(ether_object)
	plastic_tube.image = pygame.image.load(plastic_tube_object)
	
	# Display objects
	screen.blit(needle.image, (needle.x, needle.y))
	screen.blit(ether.image, (ether.x, ether.y))
	screen.blit(plastic_tube.image, (plastic_tube.x, plastic_tube.y))
	
	pygame.draw.rect(screen,BLACK,player1.Rect_position_old,0)
	
	#Display new player image
	screen.blit(player1.image, (player1.x, player1.y))
	
	
	clock = pygame.time.Clock()

	done = False

	while not done:
		
		# --- Event Processing ---
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			# Move player with keyboard
			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_RIGHT:
					game_over = player1.move('right', list_ennemy)
					print(game_over)
					player1.collect_item (list_items)
				if event.key == pygame.K_LEFT:
					game_over = player1.move('left', list_ennemy)
					player1.collect_item (list_items)
					print(game_over)
				if event.key == pygame.K_UP:
					game_over = player1.move('up', list_ennemy)
					player1.collect_item (list_items)
					print(game_over)
				if event.key == pygame.K_DOWN:
					game_over = player1.move('down', list_ennemy)
					player1.collect_item (list_items)
					print(game_over)
				
				print(player1.nb_item)
				#Fill old player position with a black rectangle
				pygame.draw.rect(screen,BLACK,player1.Rect_position_old,0)
				
				#Display new player image
				screen.blit(player1.image, (player1.x, player1.y))

		all_sprites_list.update()
		# Draw all the spites
		all_sprites_list.draw(screen)
		
		pygame.display.flip()
		
		#GAME OVER
		if game_over:
			# If game over is true, draw game over
			text = font.render("Game Over", True, WHITE)
			text_rect = text.get_rect()
			text_x = screen.get_width() / 2 - text_rect.width / 2
			text_y = screen.get_height() / 2 - text_rect.height / 2
			screen.blit(text, [text_x, text_y])
		
		clock.tick(60)

	pygame.quit()


if __name__ == "__main__":
	main()
