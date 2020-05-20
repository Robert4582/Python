from App import *

from Settings import *
import random


class fruit:
    def __init__(self, app, color):
        self.app = app
        self.pos =  vec(random.randint(2, 61), random.randint(3, 32))
        self.color = color

    def draw_fruit(self):
        pygame.draw.rect(self.app.screen, self.color, (int(self.pos.x)*20, int(self.pos.y)*20, cell_Width, cell_Height))

    def SetNewPosition(self):
        self.pos = vec(random.randint(2, 61), random.randint(3, 32))

    def Set_color(self, color):
        self.color = color