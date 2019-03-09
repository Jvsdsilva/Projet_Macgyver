# Class player create

import pygame
from constantes import *
from Classes import Display


# This class represents the palyer of the game
class Player(pygame.sprite.Sprite):
    # constructor
    def __init__(self, right, left, up, down, level):
        # Sprites of the player
        self.image = pygame.image.load(right).convert_alpha()
        self.right = right
        self.left = left
        self.up = up
        self.down = down
        # Position of the player in steps and pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.Rect_position_old = pygame.Rect(self.x, self.y, player_size,
                                             player_size)
        # Default direction
        self.direction = self.right
        self.nb_item = 0
        # Level game
        self.level = level

    # Move player with keyboard
    # Move to right
    def move_right(self, direction, list_ennemy, screen):
        game_over = False
        finish = list_ennemy[0]

        if direction == 'right':
            # Screen limit
            if self.case_x < (numbers_sprite_side - 1):
                game_over = self.contact_test_ennemy(list_ennemy,
                                                     self.x+sprite_size,
                                                     self.y, screen)
                if game_over:
                    return True
                # Verification if not walls
                if self.level.structure[self.case_y][self.case_x+1] != 'm':
                    # Move one step
                    self.case_x += 1
                    # Save old position
                    self.Rect_position_old.left = self.x
                    self.Rect_position_old.top = self.y
                    # Calcul of the reel position in pixel
                    self.x = self.case_x * sprite_size
            # Image of the player
            self.image = pygame.image.load(self.right).convert_alpha()

    # Move to Left
    def move_left(self, direction, list_ennemy, screen):
        game_over = False
        finish = list_ennemy[0]

        if direction == 'left':
            if self.case_x > 0:
                game_over = self.contact_test_ennemy(list_ennemy,
                                                     self.x-sprite_size,
                                                     self.y, screen)
                if game_over:
                    return True
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.Rect_position_old.left = self.x
                    self.Rect_position_old.top = self.y
                    self.x = self.case_x * sprite_size
            self.image = pygame.image.load(self.left).convert_alpha()

    # Move Up
    def move_up(self, direction, list_ennemy, screen):
        game_over = False
        finish = list_ennemy[0]

        if direction == 'up':
            if self.case_y > 0:
                game_over = self.contact_test_ennemy(list_ennemy, self.x,
                                                     self.y-sprite_size,
                                                     screen)
                if game_over:
                    return True
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.Rect_position_old.left = self.x
                    self.Rect_position_old.top = self.y
                    self.y = self.case_y * sprite_size
            self.image = pygame.image.load(self.up).convert_alpha()

    # Move Down
    def move_down(self, direction, list_ennemy, screen):
        game_over = False
        finish = list_ennemy[0]

        if direction == 'down':
            if self.case_y < (numbers_sprite_side - 1):
                game_over = self.contact_test_ennemy(list_ennemy, self.x,
                                                     self.y+sprite_size,
                                                     screen)
                if game_over:
                    return True
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.Rect_position_old.left = self.x
                    self.Rect_position_old.top = self.y
                    self.y = self.case_y * sprite_size
            self.image = pygame.image.load(self.down).convert_alpha()
        return False

    # Collect items in the labyrinth by step up
    def collect_item(self, wlist, syringe, screen):
        wall = pygame.image.load(image_wall).convert()

        for item in wlist:
            if item.x == self.x and item.y == self.y:
                self.nb_item += 1
                item.x = -1
                item.y = -1
                if self.nb_item == 3:
                    self.nb_item += 1
                    screen.blit(wall, (11*sprite_size, 0))
                    screen.blit(wall, (12*sprite_size, 0))
                    screen.blit(wall, (13*sprite_size, 0))
                    screen.blit(syringe.image, (syringe.x_display,
                                                syringe.y_display))
                else:
                    screen.blit(item.image, (item.x_display, item.y_display))

    # Test enemmy contact with or without all objects
    def contact_test_ennemy(self, list_ennemy, x, y, screen):
        finish = list_ennemy[0]
        Rect_position_ennemy = pygame.Rect(x, y, player_size, player_size)
        dead_p = pygame.image.load(dead_player).convert()

        # Read list of ennemy
        for ennemy in list_ennemy:
            if finish.x == x and finish.y == y:
                if self.nb_item == 4:
                    finish.x = -1
                    finish.y = -1
                    # Draw a black rectangle in the old position of the player
                    pygame.draw.rect(screen, BLACK, Rect_position_ennemy, 0)
                    # End of the game with all objects
                    self.game_over("You Win", screen)
                    return False
                else:
                    # draw an image
                    Rect_position_player = pygame.Rect(self.x, self.y,
                                                       player_size,
                                                       player_size)
                    pygame.draw.rect(screen, BLACK, Rect_position_player, 0)
                    screen.blit(dead_p, (self.x, self.y))
                    self.x = 0
                    self.y = 0
                    # End of the game without all objects
                    self.game_over("Game Over", screen)
                    return True
            return False

    # Display message game over
    def game_over(self, str_message, screen):
        # This is a font we use to draw text on the screen (size 48)
        font = pygame.font.Font(None, 48)
        # font rendering in white
        text = font.render(str_message, True, WHITE)
        text_rect = text.get_rect()
        # Display message in the center of the screen
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

    # Display ennemy
    def display(self,screen):
        screen.blit(self.image, (self.x,self.y))