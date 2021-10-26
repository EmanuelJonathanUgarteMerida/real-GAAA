import pygame as pg

from util import SpriteSheet

pg.init
pantalla = pg.display.set_mode((500, 500))

sheetMostro = SpriteSheet('mostro.png')

json_mostro=mostro

image = sheetMostro.get_image(0, 0, 100, 100)

game_over = False
while not game_over:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game_over = True

    pantalla.fill((255,255,255))
    pantalla.blit(image, image.get_rect())
    pg.display.flip()
