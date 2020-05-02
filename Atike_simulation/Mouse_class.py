import pygame


from Settings import *

vec = pygame.math.Vector2


class Mouse:
    def __init__(self, app):
        self.app =app
        self.Mouse_position = vec(1, 1)
        self.Cursor = pygame.image.load('cursor_PNG102.png')

    def RunMouse(self):
        self.UpdateMouse()
        self.DrawMouse()
    def UpdateMouse(self):
      #  print("UdataMouse Position")

      self.Mouse_position = vec(pygame.mouse.get_pos())
      #  print(self.Mouse_position)
      pygame.display.update()


    def DrawMouse(self):
        self.app.screen.fill(BLACK)
      #  print(self.Mouse_position.x)
        self.app.screen.blit(self.Cursor, (self.Mouse_position.x,self.Mouse_position.y))

