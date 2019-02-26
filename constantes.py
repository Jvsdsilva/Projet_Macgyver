# Game constants
import os

# Screen settings
numbers_sprite_side = 15
sprite_size = 50
player_size = 50
screen_side = numbers_sprite_side * sprite_size

# Title
screen_titre = "Save MacGyver"

# Images List
path = "Images/"

# On peut utiliser toutes les methodes
os.path.dirname(path)

image_player = path + "MacGyver.png"
image_wall = path + "brick.png"
image_start = path + "depart.png"
image_finish = path + "Gardien.png"

needle_object = path + "aiguille.png"
plastic_tube_object = path + "tube_plastique.png"
ether_object = path + "ether.png"
syringe_object = path + "seringue.png"
dead_player = path + "dead_player.png"

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)