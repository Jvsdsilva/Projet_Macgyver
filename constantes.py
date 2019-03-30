# Game constants
import os

# Screen settings
NUMBERS_SPRITE_SIDE = 15
SPRITE_SIZE = 50
PLAYER_SIZE = 50
SCREEN_SIDE = NUMBERS_SPRITE_SIDE * SPRITE_SIZE

# Title
SCREEN_TITLE = "Save MacGyver"

# Images List
PATH = "Images/"

# Use of all methodes of OS
os.path.dirname(PATH)

IMAGE_PLAYER = PATH + "MacGyver.png"
IMAGE_WALL = PATH + "brick.png"
IMAGE_START = PATH + "depart.png"
IMAGE_FINISH = PATH + "Gardien.png"

NEEDLE_OBJECT = PATH + "aiguille.png"
PLASTIC_TUBE_OBJECT = PATH + "tube_plastique.png"
ETHER_OBJECT = PATH + "ether.png"
SYRINGE_OBJECT = PATH + "seringue.png"
DEAD_PLAYER = PATH + "dead_player.png"

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)