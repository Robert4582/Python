from Settings import *
from App import *
from Button_class import *
from Text_Box_Classe import *
from database import *


class UI:
    def __init__(self, app):
        self.app = app
        self.stateUI = 'Start_Screen'

        self.writing = False
        self.ChangeUi = False
        ################ Start Screeen ###############################
        self.Buy_button = Button(self, self.app, (WIDTH / 2 - 50, HEIGHT / 2 + 50), (100, 50), RED, "Buy Stock", 15)
        self.Text_Box_PassWord = Text_Box(self, self.app, (WIDTH / 2 - 150, HEIGHT / 2 - 50), (300, 50), WHITE)
        self.Text_Box_name = Text_Box(self, self.app, (WIDTH / 2 - 150, HEIGHT / 2 + 50), (300, 50), WHITE)
        self.Login_button = Button(self, self.app, (WIDTH / 2 - 50, HEIGHT / 2 + 150), (100, 50), RED, "Login", 15)
        self.Login_Create_Account = Button(self, self.app, (WIDTH / 2 + 250, HEIGHT / 2 + 250), (200, 50), RED,
                                           "Create new account", 15)


        self.UsherID = ""
        self.Password = ""

    def RunUI(self):
        if self.app.UiState == "Start_Screen":
            self.Start_Screen()

    ###################### Start Screem ############################################################
    def Start_Screen(self):
        self.Start_Events()
        self.Start_Draw()

        self.Start_Update()



    def Start_Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.Login_Create_Account.Check_Push():
                    self.ChangeUi = True
                    self.app.screen.fill(BLACK)
                    self.app.state = "Ui_Crate_account"

                    print(self.app.state)

                elif self.Login_button.Check_Push():
                    self.Get_UsherID_and_Password()

                if self.Text_Box_PassWord.Check_Push():
                    self.Text_Box_name.state = "Not_ready"
                    self.Text_Box_PassWord.state = "Ready_To_write"

                if self.Text_Box_name.Check_Push():
                    self.Text_Box_name.state = "Ready_To_write"
                    self.Text_Box_PassWord.state = "Not_ready"

            if event.type == pygame.KEYDOWN:
                self.Text_Box_PassWord.write_text(event)
                self.Text_Box_name.write_text(event)

    def Start_Update(self):
        pass


    #  print("hallo there")

    def Start_Draw(self):
        #    self.Buy_button.RunButton()
        self.Text_Box_PassWord.Run_Text_Button()
        self.Text_Box_name.Run_Text_Button()
        self.Login_button.RunButton()
        self.Login_Create_Account.RunButton()

        self.app.draw_text('Welcome to the stock market', self.app.screen, [WIDTH / 2, HEIGHT / 2 - 200], 30, WHITE,
                           START_FONT, True)
        self.app.draw_text('UsherID', self.app.screen, [WIDTH / 2, HEIGHT / 2 - 75], 30, WHITE, START_FONT, True)
        self.app.draw_text('PasseWord', self.app.screen, [WIDTH / 2, HEIGHT / 2 + 25], 30, WHITE, START_FONT, True)


        if self.ChangeUi:
            self.app.screen.fill(BLACK)


        pygame.display.update()

    ################################################# Help methons  #####################

    def CheckPasseWord(self, usherID, Password):
        pass

    def ChangeUI(self):
        pass

    def Get_UsherID_and_Password(self):


        self.UsherID = self.Text_Box_name.Clear_and_get_Text()
        self.Password = self.Text_Box_PassWord.Clear_and_get_Text()
