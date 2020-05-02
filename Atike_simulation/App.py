import sys

import pygame
from Settings import *
from Start_UI import *
from Test import *
from Mouse_class import *
from database import *
from Get_Stock_Prices import *
from Create_account import *

clock = pygame.time.Clock()

pygame.init()
class App:
    def __init__(self):
        self.state = 'Ui_start'
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.UI = UI(self)
        self.Ui_Create_account = Ui_Create_Account(self)
        self.UsherData_base = Bruger_Data_Base()



      #  self.Test = test(self)
#
#
      #  self.Stock_date = Stock_Data()
        self.UiState = "Start_Screen"
        self.M = Mouse(self)
        self.load()

    #        UI.RunUI()

    def run(self):

        while self.running:
            clock.tick(200)
            if self.state == 'Ui_start':
                self.UI.RunUI()
            elif self.state == "Ui_Crate_account":

                self.Ui_Create_account.RunUI()
            elif self.state == "Ui_Your_profile":
                self.running = False

        #    self.M.RunMouse()
        pygame.quit()

        sys.exit()

    ######################################### Helper function ##############################

    def draw_text(self, words, screen, pos, size, colour, font_name, centred=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centred:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    def load(self):
        pass

    def game_over_events(self):
        pass
