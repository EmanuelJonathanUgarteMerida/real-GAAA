import pygame as pg
import json

from util import SpriteSheet

pg.init
clock=pg.time.Clock()
pantalla = pg.display.set_mode((500, 500))

sheetMostro = SpriteSheet('peleador.png')

json_mostro_content=open('peleador.json','r')
data=json.load(json_mostro_content)
json_lines=json_mostro_content.readlines()
json_mostro_content.close()
imagenes=[]
colorkey=data['colorkey']
for i in data['hit']:
	imagenes.append(sheetMostro.get_image(i['x'],i['y'],i['width'],i['height'],colorkey))
imagen=imagenes[0]
contador=0
pos=1
game_over = False
while not game_over:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game_over = True
            elif event.key == pg.K_RIGHT:
                imagen=imagenes[pos]
                pos+=1
                if pos == len(imagenes):
                    pos=0
				

    pantalla.fill((255,255,255))
    pantalla.blit(imagen, imagen.get_rect())
    pg.display.flip()
