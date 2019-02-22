# Game constants
import os

# On peut utiliser toutes les methodes

#os.path()
# Screen settings
numbers_sprite_side = 15
sprite_size = 50
player_size = 50
screen_side = numbers_sprite_side * sprite_size

# Title
screen_titre = "Save MacGyver"

# Images List
path = "Images/"
os.path.dirname(path)

#images_root = os.path()
#images_root = "C:\\Users\\joana.sousadasilva\\Documents\\Projet_Macgyver-master\\Images\\"
#image_wall = images_root + "walls2.png"
image_player = path + "MacGyver.png"
image_accueil = path + "tile-crusader-logo.png"
image_wall = path + "brick.png"
image_start = path + "depart.png"
image_finish = path + "Gardien.png"

needle_object = path + "aiguille.png"
plastic_tube_object = path + "tube_plastique.png"
ether_object = path + "ether.png"
syringe_object = path + "seringue.png"
dead_player = path + "dead_player2.png"

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)