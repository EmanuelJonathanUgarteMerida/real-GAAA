import pygame as pg
import os


class SpriteSheet():
    def __init__(self, name):
        self.sprite_sheet = pg.image.load(
            os.path.join('png', name)).convert_alpha()

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((255, 255, 255))
        return image
