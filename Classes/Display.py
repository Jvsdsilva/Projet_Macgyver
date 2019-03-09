# Class draw Labyrinth

import pygame
from Classes import Object
from Classes import Player
from Classes import Level
from constantes import *


# This class display the pygame
class Display(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        super().__init__()
        # Load images
        self.image_display = pygame.image.load(image_player)
        self.screen = pygame.display.set_mode((screen_side, screen_side))
        # Set file
        file = 'Labyrinth'
        # Instatiation labyrinth
        self.level = Level.Level(file)
        # Create listes
        self.list_items = []
        self.list_ennemy = []
        self.list_items = []
        self.syringe = Object.Object(syringe_object, 14*sprite_size, 0)
        # Initiation pygame
        self.init_pygame()
        # set objects
        self.init_objects()
        # Create player
        self.player1 = Player.Player(image_player, image_player, image_player,
                                     image_player, self.level)
        # Create ennemy
        self.init_ennemy()
        # Display level and objects
        self.display_level()
        self.display_objects()
        # Display ennemy
        self.blit_image(self.list_ennemy[0].image, (self.list_ennemy[0].x,
                        self.list_ennemy[0].y))

    # Generate and display level
    def display_level(self):
        self.level.generate()
        self.level.display_level(self.screen, self.list_ennemy)

    # Initiation of pygame and window
    def init_pygame(self):
        # Call this function so the Pygame library can initialize itself
        pygame.init()
        # Create the surface of (width, height), and its window.
        self.screen = pygame.display.set_mode((screen_side, screen_side))
        # Set the title of the window
        pygame.display.set_caption(screen_titre)

    # quit pygame
    def quit_pygame(self):
        pygame.quit()

    # update pygame display
    def pygame_display_flip(self):
        pygame.display.flip()

    # pygame time disply
    def pygame_display_time(self):
        pygame.time.Clock()

    # load images
    def load_image(self, image):
        return pygame.image.load(image)

    # display images
    def blit_image(self, surface, rect):
        self.screen.blit(surface, rect)

    # Display pygame rectangle
    def draw_pygame_rect(self, color, player_position):
        pygame.draw.rect(self.screen, color, player_position, 0)

    # Create player
    def display_player(self):
        player1 = Player.Player(image_player, image_player, image_player,
                                image_player, self.level)

    # Create ennemy
    def init_ennemy(self):
        ennemy = Player.Player(image_finish, image_finish, image_finish,
                               image_finish, self.level)
        self.list_ennemy.append(ennemy)

    def init_objects(self):
        # Instatiation objects
        plastic_tube = Object.Object(plastic_tube_object, 13*sprite_size, 0)
        ether = Object.Object(ether_object, 12*sprite_size, 0)
        needle = Object.Object(needle_object, 11*sprite_size, 0)

        # Add objects to list
        self.list_items.append(needle)
        self.list_items.append(ether)
        self.list_items.append(plastic_tube)

    def display_objects(self):
        # Set image object
        self.list_items[0].image = self.load_image(needle_object)
        self.list_items[1].image = self.load_image(ether_object)
        self.list_items[2].image = self.load_image(plastic_tube_object)

        # Set de position of objects
        self.list_items[0].set_item(self.player1, self.list_items, self.level)
        self.list_items[1].set_item(self.player1, self.list_items, self.level)
        self.list_items[2].set_item(self.player1, self.list_items, self.level)

        # Display objects
        self.blit_image(self.list_items[0].image, (self.list_items[0].x,
                        self.list_items[0].y))
        self.blit_image(self.list_items[1].image, (self.list_items[1].x,
                        self.list_items[1].y))
        self.blit_image(self.list_items[2].image, (self.list_items[2].x,
                        self.list_items[2].y))

    # Loop evenementiel
    def event_manager(self):
        game_over = False
        done = False
        # end loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # Move player with keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.k_right()
                if event.key == pygame.K_LEFT:
                    self.k_left()
                if event.key == pygame.K_UP:
                    self.k_up()
                if event.key == pygame.K_DOWN:
                    self.k_down()

                # Fill old player position with a black rectangle
                self.draw_pygame_rect(BLACK, (self.player1.Rect_position_old))

                # Display new player image
                self.blit_image(self.player1.image,
                                (self.player1.x, self.player1.y))
        return done

    # Move down test
    def k_down(self):
            game_over = self.player1.move_down('down', self.list_ennemy,
                                               self.screen)
            self.player1.collect_item(self.list_items, self.syringe,
                                      self.screen)

    # Move up test
    def k_up(self):
            game_over = self.player1.move_up('up', self.list_ennemy,
                                             self.screen)
            self.player1.collect_item(self.list_items, self.syringe,
                                      self.screen)

    # Move left test
    def k_left(self):
            game_over = self.player1.move_left('left', self.list_ennemy,
                                               self.screen)
            self.player1.collect_item(self.list_items, self.syringe,
                                      self.screen)

    # Move right test
    def k_right(self):
            game_over = self.player1.move_right('right', self.list_ennemy,
                                                self.screen)
            self.player1.collect_item(self.list_items, self.syringe,
                                      self.screen)