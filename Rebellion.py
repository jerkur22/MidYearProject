from pygame import *
import sys
from os.path import abspath, dirname
from random import randint, choice

BASE_PATH = abspath(dirname(__file__))

IMAGE_PATH = BASE_PATH + '/images/'
SOUND_PATH = BASE_PATH + '/sounds/'

#colors for use later
GREY = (105,105,105)
RED = (237, 28, 36)
WHITE = (255, 255, 255)
BLUE = (80, 255, 239)

SCREEN = display.set_mode((1000,800))

IMG_NAMES = ['']#insert image names of all the things

IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES} # INSPIRATION FROM leerob

class Ywing(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = IMAGES[''] # INSERT THE IMAGE NAME OF THE YWING


