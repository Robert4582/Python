import pygame

from Settings import *

vec = pygame.math.Vector2


class Button:
    def __init__(self, UI, app, pos, size, colour, button_text, text_size=20, text_colour=PLAYER_COLOUR,
                 font_name=START_FONT):
        self.app = app
        self.UI = UI
        self.pos = vec(pos)
        self.colour = colour
        self.size = vec(size)
        self.Hover = False
        self.button_text = button_text
        self.text_colour = text_colour
        self.text_size = text_size
        self.font_name = font_name

    def Check_Push(self):

        if self.Hover:
            print("Events")
            return True
        else:
            return False

    def Buttum_text(self):
        font = pygame.font.SysFont(self.font_name, self.text_size)
        text = font.render(self.button_text, False, self.text_colour)
        text_size = text.get_size()
        x = self.pos.x + self.size.x / 2 - (text_size[0] // 2)
        y = self.pos.y + self.size.y / 2 - (text_size[1] // 2)

        self.app.screen.blit(text, (x, y))

    def Check_hover(self):
        Mouse_pos = vec(pygame.mouse.get_pos())
        if Mouse_pos.x > self.pos.x and Mouse_pos.x < self.pos.x + self.size.x:
            if Mouse_pos.y > self.pos.y and Mouse_pos.y < self.pos.y + self.size.y:
                self.colour = WHITE
                #       print("Hower")
                self.Hover = True
        else:
            self.Hover = False
            self.colour = RED
            return False

    def RunButton(self):
        self.UpdateButton()
        self.DrawButton()

    def UpdateButton(self):
        self.Check_hover()

    def DrawButton(self):

        pygame.draw.rect(self.app.screen, self.colour, (self.pos.x, self.pos.y, self.size.x, self.size.y))
        self.Buttum_text()

    # def user_imput(self, event):
    #    if event.key != 13 and event.key != 273 and event.key != 274 and event.key != 275 and event.key != 8 and event.key != 127:
    #        self.text.insert(self.cursor_pos, event.unicode)
    #        self.cursor_pos += 1
    #    elif event.key == 8 and self.cursor_pos > 0 and len(self.text) > 0:
    #        del self.text[self.cursor_pos - 1]
    #        self.cursor_pos -= 1
    #    elif event.key == 276 and self.cursor_pos != 0:
    #        self.cursor_pos -= 1
    #    elif event.key == 275 and self.cursor_pos < len(self.text):
    #        self.cursor_pos += 1
    #    elif event.key == 127 and self.cursor_pos < len(self.text):
    #        del self.text[self.cursor_pos]
    #        print("delete")
    #    print("evenet")
