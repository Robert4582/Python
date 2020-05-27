import pygame

from Settings import *
import math

vec = pygame.math.Vector2


class checkbox:
    def __init__(self, UI, app, pos, size, Circle_size, Detect, colour, button_text, text_size=20,
                 text_colour=PLAYER_COLOUR,
                 font_name=START_FONT):
        self.app = app
        self.UI = UI
        self.Detect_hover = Detect
        self.pos = vec(pos)
        self.colour = colour
        self.size = vec(size)
        self.Hover = False
        self.button_text = button_text
        self.text_colour = text_colour
        self.text_size = text_size
        self.Circle_size = Circle_size
        self.font_name = font_name
        self.pushed = False

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
        D = 0
        Mouse_pos = vec(pygame.mouse.get_pos())
        M_x = Mouse_pos.x
        M_Y = Mouse_pos.y
        pos_x = self.pos.x
        pos_y = self.pos.y

        D_X = (M_x - pos_x) * 2
        #   print(D_X)
        D_Y = (M_Y - pos_y) * 2
        #     print(D_Y)

        if D_Y < 0:
            D_Y *= -1
        if D_X < 0:
            D_X *= -1
        #   print(f)

        f = D_X + D_Y
        if f < 0:
            pass
            #     print("f er negative ", f)
            f *= -1
        #     print("made f pos ", f)
        if f != 0:
            #     print(f)
            D = math.sqrt(f)
        else:
            D = 10
        print(D)
        if D < self.Detect_hover:
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

        pygame.draw.circle(self.app.screen, self.colour, [int(self.pos.x), int(self.pos.y)], self.Circle_size)

        if self.pushed:
              pygame.draw.circle(self.app.screen, WHITE, [int(self.pos.x), int(self.pos.y)], self.Circle_size - 3)
    # self.Buttum_text()

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
