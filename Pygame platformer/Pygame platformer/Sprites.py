import pygame as py
from GameSettings import *
import os
#shorting of pygames math vector libary
vec = py.math.Vector2

gameFolder = os.path.dirname(__file__)
imgFolder = os.path.join(gameFolder, "img")

#Player class
class Player(py.sprite.Sprite):
    
    def __init__(self, game):
        #creation of player and giving it pos, vel and acc
        py.sprite.Sprite.__init__(self)
        self.game = game
        self.image = py.image.load(os.path.join(imgFolder, "milo2.png")).convert()
        self.image = py.transform.scale(self.image,(60, 75))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH /2, HEIGHT / 2)
        self.pos = vec(WIDTH /2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.x += 1
        hits = py.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = - PLAYERJUMP

    def update(self):
        #update of player
        self.acc = vec(0, PLAYERGRAV)
        keys = py.key.get_pressed()
        if keys[py.K_LEFT]:
            self.acc.x = - PLAYERACC
        if keys[py.K_RIGHT]:
            self.acc.x = PLAYERACC

        self.acc.x += self.vel.x * PLAYERFRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class Platform(py.sprite.Sprite):

    def __init__(self, x, y, w, h):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

