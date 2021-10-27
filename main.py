import pygame as pg
import os

from util import SpriteSheet

pg.init
clock = pg.time.Clock()
pantalla = pg.display.set_mode((500, 500))
sprite_sheet = SpriteSheet('ken.png', 'ken.json')
gaa = pg.image.load(os.path.join('png', 'gaa.png'))
gaa.set_colorkey((255, 255, 255))
gaa_rect = gaa.get_rect()
gaa_rect.center = (200, 250)

imagenes = []
for data in sprite_sheet.data['beaten']:
    imagenes.append(sprite_sheet.get_image(
        data['x'], data['y'], data['width'], data['height'], 1))

image = imagenes[0]
x = 0
contador = 0
pos = 1
game_over = False
velocidad_x = 5
velocidad_y = 5
contador_ken = 0
frames = 5
while not game_over:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game_over = True
            elif event.key == pg.K_RIGHT:
                if pos == len(imagenes):
                    pos = 0
                image = imagenes[pos]
                pos += 1

    if gaa_rect.left <= 0 or gaa_rect.right >= 500:
        velocidad_x = -velocidad_x
    elif gaa_rect.top <= 0 or gaa_rect.bottom >= 500:
        velocidad_y = -velocidad_y

    if frames == 5:
        frames = 0
        if contador_ken == len(imagenes):
            contador_ken = 0
        image = imagenes[contador_ken]
        contador_ken += 1
    else:
        frames += 1

    gaa_rect.x += velocidad_x
    gaa_rect.y += velocidad_y

    pantalla.fill((255, 255, 255))
    pantalla.blit(image, image.get_rect())
    pg.display.flip()
