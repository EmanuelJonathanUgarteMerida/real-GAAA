import pygame as pg
import os


class Ball:
    def __init__(self, name_image):
        self.image = pg.image.load(os.path.join('png', name_image))
    
    def change_states(self,mode):
        pass
