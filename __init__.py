#!/usr/bin/python3
# -*- coding: Utf-8 -*
import pygame
import random

from Classes import Object
from Classes import Player
from Classes import Level
from constantes import *

#Main program
def main():

    # Call this function so the Pygame library can initialize itself
    pygame.init()
    # Create the surface of (width, height), and its window.
    screen = pygame.display.set_mode((screen_side, screen_side))
    # Set the title of the window
    pygame.display.set_caption(screen_titre)
    
    #Set file
    file = 'Niveau2'
    
    #Generate labyrinth
    level = Level.Level(file)
    list_ennemy = []
    
    #Create player
    player1 = Player.Player(image_player,image_player, image_player,
                            image_player, level)
    player2 = Player.Player(image_finish,image_finish, image_finish,
                            image_finish, level)
    list_ennemy.append(player2)
    #Create liste of objects
    list_items = []
    
    level.generate()
    level.display_level(screen,list_ennemy)
    
    #Instatiation objects
    plastic_tube = Object.Object(plastic_tube_object,13*sprite_size,0)
    ether = Object.Object(ether_object,12*sprite_size,0)
    needle = Object.Object(needle_object,11*sprite_size,0)
    syringe = Object.Object(syringe_object,14*sprite_size,0)
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
                    game_over = player1.move('right', list_ennemy, screen)
                    player1.collect_item (list_items, syringe, screen)
                if event.key == pygame.K_LEFT:
                    game_over = player1.move('left', list_ennemy, screen)
                    player1.collect_item (list_items, syringe, screen)
                if event.key == pygame.K_UP:
                    game_over = player1.move('up', list_ennemy, screen)
                    player1.collect_item (list_items, syringe, screen)
                if event.key == pygame.K_DOWN:
                    game_over = player1.move('down', list_ennemy, screen)
                    player1.collect_item (list_items, syringe, screen)

                #Fill old player position with a black rectangle
                pygame.draw.rect(screen,BLACK,player1.Rect_position_old,0)
                
                #Display new player image
                screen.blit(player1.image, (player1.x, player1.y))
        
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
