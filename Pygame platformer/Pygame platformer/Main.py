import pygame as py
import random
from GameSettings import *
from Sprites import *
from os import path as pa


class Game:
    def __init__(self):
        #initialize the game
        py.init()
        py.mixer.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        py.display.set_caption(TITLE)
        self.clock = py.time.Clock()
        self.running = True
        self.fontname = py.font.match_font(FONTNAME)
        self.LoadData()

    def LoadData(self):
        # highscore load
        self.dir = pa.dirname(__file__)
        with open(pa.join(self.dir, HSFILE), "r+") as file:
            try:
                self.highscore = int(file.read())
            except:
                self.highscore = 0

    def New(self):
        #creates new game
        self.score = 0
        self.AllSprites = py.sprite.Group()
        self.platforms = py.sprite.Group()
        self.player = Player(self)
        self.AllSprites.add(self.player)
        for plat in PLATFORMLIST:
            p = Platform(*plat)
            self.AllSprites.add(p)
            self.platforms.add(p)
        self.Run()

    def Run(self):
        #runs game
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.Events()
            self.Update()
            self.Draw()

    def Update(self):
        #updates game
        self.AllSprites.update()

        if self.player.vel.y > 0:
            hits = py.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        if self.player.rect.bottom > HEIGHT:
            for sprite in self.AllSprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH-width), random.randrange(-75, -30), width, 20)
            self.platforms.add(p)
            self.AllSprites.add(p)

    def Events(self):
        #events in game
        for event in py.event.get():

            if event.type == py.QUIT:
                if self.playing:
                    self.playing = False
                running = False

            if event.type == py.KEYDOWN:
                if event.key == py.K_UP:
                    self.player.jump()

    def Draw(self):
        #draws game
        self.screen.fill(BGCOLOR)
        self.AllSprites.draw(self.screen)
        self.Drawtext(str(self.score), 20, WHITE, WIDTH / 2, 10)

        py.display.flip()

    def ShowStartScreen(self):
        self.screen.fill(BGCOLOR)
        self.Drawtext(TITLE, 50, BLACK, WIDTH / 2, HEIGHT / 4)
        self.Drawtext("Use arrows to move and jump", 25, BLACK, WIDTH /2, HEIGHT / 2)
        self.Drawtext("Press a key to play", 25, BLACK, WIDTH /2, HEIGHT * 3 / 4)
        self.Drawtext("high score: " + str(self.highscore), 25, BLACK, WIDTH /2, 20)
        py.display.flip()
        self.WaitForKey()

    def ShowGOScreen(self):
        if not self.running:
            return

        self.screen.fill(BGCOLOR)
        self.Drawtext("YOU DEAD", 50, RED, WIDTH / 2, HEIGHT / 4)
        self.Drawtext("Your score was " + str(self.score), 25, BLACK, WIDTH /2, HEIGHT / 2)
        self.Drawtext("Press a key to play again", 25, RED, WIDTH /2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.Drawtext("NEW HIGH SCORE", 25, BLUE, WIDTH /2, HEIGHT / 2 + 40)
            with open(pa.join(self.dir, HSFILE), "w") as file:
                file.write(str(self.score))
        else:
            self.Drawtext("high score: " + str(self.highscore), 25, BLACK, WIDTH /2, HEIGHT / 2 + 40)

        py.display.flip()
        self.WaitForKey()

    def WaitForKey(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in py.event.get():
                if event.type == py.QUIT:
                    waiting = False
                    self.running = False
                if event.type == py.KEYUP:
                     waiting = False

    def Drawtext(self, text, size, color, x, y):
        font = py.font.Font(self.fontname, size)
        textsurface = font.render(text, True, color)
        textrect = textsurface.get_rect()
        textrect.midtop = (x, y)
        self.screen.blit(textsurface, textrect)

g = Game()
g.ShowStartScreen()
while g.running:
    g.New()
    g.ShowGOScreen()

py.quit()