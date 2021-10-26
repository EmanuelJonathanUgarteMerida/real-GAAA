import pygame as pg
import json

from util import SpriteSheet

pg.init
clock = pg.time.Clock()
pantalla = pg.display.set_mode((500, 500))
sprite_sheet = SpriteSheet('pong.png', 'pong.json')

imagenes = []
for data in sprite_sheet.data['paddle']['evo1']:
    imagenes.append(sprite_sheet.get_image(
        data['x'], data['y'], data['width'], data['height']))

image = imagenes[0]
x = 0
contador = 0
pos = 1
game_over = False
while not game_over:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game_over = True
            elif event.key == pg.K_RIGHT:
                if pos < len(imagenes):
                    image = imagenes[pos]
                    pos += 1
                else:
                    pos = 0

    pantalla.fill((255, 255, 255))
    pantalla.blit(image, image.get_rect())
    pg.display.flip()
