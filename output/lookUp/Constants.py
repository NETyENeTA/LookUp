import pygame as pg
from random import randrange as rnd

vec2 = pg.math.Vector2
RES = vec2(320, 568)
FPS = 90
ALPHA = 120

RANGS = 999
KOEF1 = 5  # (level skill)
KOEF2 = 5  # 0 -> ? +KOEF1 (level skill)

paths = {
    'fonts': 'assets/fonts/',
    'images': 'assets/images/',
}

pg.init()
