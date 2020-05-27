import pygame

from Settings import *

vec = pygame.math.Vector2


class Text_Box:
    def __init__(self, Ui, app, pos_v2, size_V2, colour, state='', active_colour=WHITE, border=True,
                 border_color=(0, 0, 0), border_width=2, place_text='', font_name='arial, text_size =20',
                 text_colour=(0, 0, 0)):
        self.cursor_pos = 0
        self.app = app
        self.Ui = Ui
        #   self.surface = surface

        self.pos = vec(pos_v2)
        self.x = self.pos.x
        self.y = self.pos.y
        self.size = vec(size_V2)
        self.HEIGHT = self.size.y
        self.WIDTH = self.size.x
        self.colour = colour
        self.start_colour = colour
        self.state = "Not_Ready"
        self.Text_In_box = False
        self.Show_Box_Name = True
        # self.active_colour = active_colour
        # self.border = border
        # self.state = state
        # self.image = pygame.surface((WIDTH, HEIGHT))
        # self.rect = self.image.get_rect()
        # self.rect.topleft = self.pos
        # self.border_color = border_color
        # self.border_width = border_width
        # self.place_texy = place_text
        # self.text = []
        # self.font_name = font_name
        # self.font_size = 20
        # self.text_colour = text_colour
        # self.cursor = 0
        # self.ative = False
        # self.hovered = False
        self.Hover = False
        self.Ready_to_wirte = False
        self.Text = []
        self.Cursor_pos = 0
        self.i = 0

    #
    def AddTextInbox(self, Text, text_size, text_colour):
        if not self.Text_In_box and self.Show_Box_Name == True:
            font = pygame.font.SysFont(START_FONT, text_size)
            text = font.render(Text, False, text_colour)
            text_size = text.get_size()
            x = self.pos.x + self.size.x / 2 - (text_size[0] // 2)
            y = self.pos.y + self.size.y / 2 - (text_size[1] // 2)

            self.app.screen.blit(text, (x, y))

    def show_text(self):

        text = ''.join(self.Text)
        font = pygame.font.SysFont(START_FONT, 20)
        adtext = font.render(text, False, RED)
        text_size = adtext.get_size()
        x = self.pos.x
        y = self.pos.y + self.size.y / 2 - (text_size[1] // 2)
        self.app.screen.blit(adtext, (x + 10, y))

    def Check_Push(self):

        if self.Hover:
            # if self.Ui.writing == False:
            #   #if self.state != "Ready_To_write":
            #   #    self.state = "Ready_To_write"
            #   #    self.Ui.writing = True
            #    pass
            return True
        else:
            return False

    def Check_hover(self):
        Mouse_pos = vec(pygame.mouse.get_pos())
        if self.pos.x < Mouse_pos.x < self.pos.x + self.size.x \
                and self.pos.y < Mouse_pos.y < self.pos.y + self.size.y:
            self.colour = Gray
            if not self.Hover:
                self.Hover = True
                self.Show_Box_Name = False

            #  print(self.Hover)
        else:
            self.colour = self.start_colour
            if self.Hover:
                self.Hover = False
                self.Show_Box_Name = True
            #     print(self.Hover)
            return False

    def write_text(self, event):
        print(self.state)
        if self.state == "Ready_To_write":
            if event.key != 1 and event != 273 and event.key != 274 and event.key != 275 and event.key != 8 and event.key != 127 and event.key != 13:
                self.Text.insert(self.cursor_pos, event.unicode)
                self.cursor_pos += 1

            elif event.key == 8 and self.cursor_pos > 0 and len(self.Text) > 0:
                del self.Text[self.cursor_pos - 1]
                self.cursor_pos -= 1
            elif event.key == 13:
                print(event.key)
                self.state = "Not_ready"
                self.Ui.writing = False

            print(self.cursor_pos)

    def Clear_and_get_Text(self):
        string = ''.join(self.Text)
        self.Text.clear()
        self.cursor_pos = 0
        return string
    def Return_Text(self):
        string = ''.join(self.Text)
        return string
    def Run_Text_Button(self):
        self.UpdateButton()
        self.DrawButton()

    def UpdateButton(self):
        self.Check_hover()
        if len(self.Text) <= 0:
            self.Text_In_box = False
        else:
            self.Text_In_box = True

    def DrawButton(self):

        # self.app.screen.blit("lalal", (100, 100))
        pygame.draw.rect(self.app.screen, self.colour, (self.pos.x, self.pos.y, self.size.x, self.size.y))
        pygame.draw.rect(self.app.screen, RED, (self.pos.x, self.pos.y, self.size.x, self.size.y), 2)

        self.show_text()

# def draw(self):

# def Click(self):
#     self.ative = True

# def user_imput(self, event):
#     if event.key != 13 and event.key != 273 and event.key != 274 and event.key != 275 and event.key != 8 and event.key != 127:
#         self.text.insert(self.cursor_pos, event.unicode)
#         self.cursor_pos += 1
#     elif event.key == 8 and self.cursor_pos > 0 and len(self.text) > 0:
#         del self.text[self.cursor_pos - 1]
#         self.cursor_pos -= 1
#     elif event.key == 276 and self.cursor_pos != 0:
#         self.cursor_pos -= 1
#     elif event.key == 275 and self.cursor_pos < len(self.text):
#         self.cursor_pos += 1
#     elif event.key == 127 and self.cursor_pos < len(self.text):
#         del self.text[self.cursor_pos]
#         print("delete")
#     print("evenet")
