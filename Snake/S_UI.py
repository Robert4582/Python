from App import *
from Button_class import *

from Cheack_box import *


class S_UI:
    def __init__(self, app):
        self.app = app
        self.cheack_box_pos = -140
        self.i = 0
        self.Start_Spil_Button = Button(self, self.app, (WIDTH / 2 - 100, HEIGHT / 2 - 200), (200, 100), WHITE,
                                        "Start spil", 30)

        # self.MakeCheackboxs()
        self.cheack_box_list = []
        self.Draw_squres()
        for i in range(0, 9):
            self.cheack_box_list.append(
                checkbox(self, self.app, (WIDTH / 2 + self.cheack_box_pos, HEIGHT / 2 + 200), (200, 100), 10, 6, WHITE,
                         "Start spil", 500))

        self.cheack_box_list[0].pushed = True

        self.Timer =0
        #   pygame.draw.ellipse(self.app.screen, RED, [300, 10, 50, 20])

    #     pygame.draw.circle(self.app.screen, BLU, [60, 250], 40)

    ###################### Start Screem ############################################################

    def Start_Screen(self):
        self.Start_Events()
        self.Start_Draw()
        self.Start_Update()

    def SetlistFalse(self):
        for var in self.cheack_box_list:
            var.pushed = False

    def Start_Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.Start_Spil_Button.Check_Push():
                    self.app.state = "run"
                for checkbox in self.cheack_box_list:
                    if checkbox.Check_Push():
                        self.SetlistFalse()

                        if not checkbox.pushed:
                            checkbox.pushed = True
                        else:
                            checkbox.pushed = False

                pass

    def Set_speed(self):
        if self.cheack_box_list[0].pushed:
            self.app.Snake.speed = 2
            print(self.app.Snake.speed)
        if self.cheack_box_list[1].pushed:
            self.app.Snake.speed = 3
        if self.cheack_box_list[2].pushed:
            self.app.Snake.speed = 4
        if self.cheack_box_list[3].pushed:
            self.app.Snake.speed = 5
        if self.cheack_box_list[4].pushed:
            self.app.Snake.speed = 6
        if self.cheack_box_list[5].pushed:
            self.app.Snake.speed = 7
        if self.cheack_box_list[6].pushed:
            self.app.Snake.speed = 8
        if self.cheack_box_list[7].pushed:
            self.app.Snake.speed = 9
        if self.cheack_box_list[8].pushed:
            self.app.Snake.speed = 10

    def Start_Update(self):
        self.Set_speed()

    #  print("hallo there")

    def Draw_Hiscore(self):
        self.app.draw_text("High score", self.app.screen, [WIDTH - 200, 60], 25, WHITE, START_FONT, True)
        H = self.app.Database_Highscore.get_HighScore_list()
        print("score", H)
        i = 0
        for score in H:
            print(i)
            i += 1
            self.app.draw_text(str(score[0]), self.app.screen, [WIDTH - 210, 60 + i * 30], 25, WHITE, START_FONT, True)
            if i == 20:
                break

        if self.Timer > 60:
            self.Draw_squres()
            self.Timer = 0
        self.Timer += 1
    def Start_Draw(self):
        self.Start_Spil_Button.RunButton()
        #      self.checkbox_speed_1.RunButton()
        self.Draw_Hiscore()
        self.app.draw_text("WELCOME TO RAINBOW SNAKE", self.app.screen, [WIDTH / 2, 60], 25, WHITE, START_FONT, True)

        self.app.draw_text("Set speed på snake", self.app.screen, [WIDTH / 2 + 10, 500], 25, WHITE, START_FONT, True)

        self.set_Checkbox_Pos()
        self.RunCheackBox()
        pygame.display.update()

    def set_Checkbox_Pos(self):

        for check_box in self.cheack_box_list:
            self.i += 1
            check_box.pos = vec(WIDTH / 2 + 30 * self.i + self.cheack_box_pos, HEIGHT / 2 + 200)
            self.app.draw_text(str(self.i), self.app.screen,
                               [WIDTH / 2 + 30 * self.i + self.cheack_box_pos, HEIGHT / 2 + 175], 15, WHITE, START_FONT,
                               True)

        self.i = 0

    def MakeCheackboxs(self):

        self.checkbox_speed_1 = checkbox(self, self.app, (WIDTH / 2 + self.cheack_box_pos, HEIGHT / 2 + 200),
                                         (200, 100), 10, 6, WHITE,
                                         "Start spil", 500)
        self.checkbox_speed_2 = checkbox(self, self.app, (WIDTH / 2 - 30 + self.cheack_box_pos, HEIGHT / 2 + 200),
                                         (200, 100), 10, 6, WHITE,
                                         "Start spil", 500)
        self.checkbox_speed_3 = checkbox(self, self.app, (WIDTH / 2 - 60 + self.cheack_box_pos, HEIGHT / 2 + 200),
                                         (400, 100), 10, 6, WHITE,
                                         "Start spil", 500)
        self.checkbox_speed_4 = checkbox(self, self.app, (WIDTH / 2 - 90 + self.cheack_box_pos, HEIGHT / 2 + 200),
                                         (200, 100), 10, 6, WHITE,
                                         "Start spil", 500)
        self.checkbox_speed_5 = checkbox(self, self.app, (WIDTH / 2 - 120 + self.cheack_box_pos, HEIGHT / 2 + 200),
                                         (200, 100), 10, 6, WHITE,
                                         "Start spil", 500)
        self.checkbox_speed_6 = checkbox(self, self.app, (WIDTH / 2 - 150 + self.cheack_box_pos, HEIGHT / 2 + 200),
                                         (200, 100), 10, 6, WHITE,
                                         "Start spil", 500)
        self.checkbox_speed_7 = checkbox(self, self.app, (WIDTH / 2 - 180 + self.cheack_box_pos, HEIGHT / 2 + 200),
                                         (200, 100), 10, 6, WHITE,
                                         "Start spil", 500)
        self.checkbox_speed_8 = checkbox(self, self.app, (WIDTH / 2 - 210 + self.cheack_box_pos, HEIGHT / 2 + 200),
                                         (200, 100), 10, 6, WHITE,
                                         "Start spil", 500)
        self.checkbox_speed_9 = checkbox(self, self.app, (WIDTH / 2 - 240 + self.cheack_box_pos, HEIGHT / 2 + 200),
                                         (200, 100), 10, 6, WHITE,
                                         "Start spil", 500)

    def RunCheackBox(self):
        for check_box in self.cheack_box_list:
            check_box.RunButton()

    def Draw_squres(self):

        for i in range(0, 25):
            pygame.draw.rect(self.app.screen, self.app.Get_random_color(), (12, 12 + i * 28, 22, 22))


        for i in range(0, 25):
            pygame.draw.rect(self.app.screen, self.app.Get_random_color(), (WIDTH -36, 12 + i * 28, 22, 22))

        for i in range(0, 43):
            pygame.draw.rect(self.app.screen, self.app.Get_random_color(), ( 40 + i * 28, 12, 22, 22))

        for i in range(0, 43):
            pygame.draw.rect(self.app.screen, self.app.Get_random_color(), (40 + i * 28, HEIGHT-36, 22, 22))

    #  for i in range(0, 30):
      #      pygame.draw.rect(self.app.screen, self.app.Get_random_color(), (WIDTH-23, 26 + i * 22, 24, 24))
#
      #  for i in range(0, 57):
      #      pygame.draw.rect(self.app.screen, self.app.Get_random_color(), (25 + i * 22, 4, 24, 24))
#
      #  for i in range(0, 57):
      #      pygame.draw.rect(self.app.screen, self.app.Get_random_color(), (26 + i * 22 ,HEIGHT -18, 24, 24))
