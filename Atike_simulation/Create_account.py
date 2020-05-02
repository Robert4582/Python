from Settings import *
from App import *
from Button_class import *
from Text_Box_Classe import *
from database import *


class Ui_Create_Account:
    def __init__(self, app):

        self.app = app
        self.stateUI = 'Start_Screen'

        self.writing = False
        self.ChangeUi = False
        ################ Start Screeen ###############################

        self.Text_Box_name = Text_Box(self, self.app, (WIDTH / 2 - 150, HEIGHT / 2 - 150), (300, 50), WHITE)
        self.Text_Box_Last_name = Text_Box(self, self.app, (WIDTH / 2 - 150, HEIGHT / 2 - 75), (300, 50), WHITE)
        self.Text_Box_UsherId = Text_Box(self, self.app, (WIDTH / 2 - 150, HEIGHT / 2 + 75), (300, 50), WHITE)
        self.Text_Box_PassWord = Text_Box(self, self.app, (WIDTH / 2 - 150, HEIGHT / 2), (300, 50), WHITE)

        self.Buy_button = Button(self, self.app, (WIDTH / 2 - 50, HEIGHT / 2 + 50), (100, 50), RED, "Buy Stock", 15)
        self.Create_account = Button(self, self.app, (WIDTH / 2 - 100, HEIGHT / 2 + 150), (200, 50), RED,
                                     "CreateAccount", 15)

        self.UsherID = ""
        self.Password = ""
        self.FirstName = ""
        self.LarstName = ""

    def RunUI(self):
        if self.app.UiState == "Start_Screen":
            self.C_A()

    ###################### Start Screem ############################################################
    def C_A(self):
        self.C_A_Events()
        self.C_A_Draw()
        self.C_A_Update()

    def C_A_Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if self.Create_account.Check_Push():

                    self.Get_UsherID_and_Password()

                if self.Text_Box_name.Check_Push():
                    self.Text_Box_name.state = "Ready_To_write"
                    self.Text_Box_PassWord.state = "Not_ready"
                    self.Text_Box_Last_name.state = "Not_ready"
                    self.Text_Box_UsherId.state = "Not_ready"

                if self.Text_Box_Last_name.Check_Push():
                    self.Text_Box_name.state = "Not_ready"
                    self.Text_Box_PassWord.state = "Not_ready"
                    self.Text_Box_Last_name.state = "Ready_To_write"
                    self.Text_Box_UsherId.state = "Not_ready"

                if self.Text_Box_UsherId.Check_Push():
                    self.Text_Box_name.state = "Not_ready"
                    self.Text_Box_PassWord.state = "Not_ready"
                    self.Text_Box_Last_name.state = "Not_ready"
                    self.Text_Box_UsherId.state = "Ready_To_write"

                if self.Text_Box_PassWord.Check_Push():
                    self.Text_Box_name.state = "Not_ready"
                    self.Text_Box_Last_name.state = "Not_ready"
                    self.Text_Box_UsherId.state = "Not_ready"
                    self.Text_Box_PassWord.state = "Ready_To_write"




            if event.type == pygame.KEYDOWN:  ## write text in box
                self.Text_Box_PassWord.write_text(event)
                self.Text_Box_name.write_text(event)
                self.Text_Box_UsherId.write_text(event)
                self.Text_Box_Last_name.write_text(event)

    def C_A_Update(self):
        pass

    #  print("hallo there")

    def C_A_Draw(self):
        #    self.Buy_button.RunButton()

        self.Text_Box_name.Run_Text_Button()
        self.Text_Box_name.AddTextInbox("First name", 20, BLACK)

        self.Text_Box_Last_name.Run_Text_Button()
        self.Text_Box_Last_name.AddTextInbox("Last name", 20, BLACK)

        self.Text_Box_UsherId.Run_Text_Button()
        self.Text_Box_UsherId.AddTextInbox("UserID", 20, BLACK)

        self.Text_Box_PassWord.Run_Text_Button()
        self.Text_Box_PassWord.AddTextInbox("PassWord", 20, BLACK)

        self.Create_account.RunButton()

        self.app.draw_text('Crate a ned Account', self.app.screen, [WIDTH / 2, HEIGHT / 2 - 250], 30, WHITE, START_FONT,
                           True)

        if self.ChangeUi:
            self.app.screen.fill(BLACK)

        pygame.display.update()

    ################################################# Help methons  #####################

    def Cheack_New_Account(self):
        pass

    def Get_UsherID_and_Password(self):
        self.UsherID = self.Text_Box_UsherId.Clear_and_get_Text()
        self.Password = self.Text_Box_PassWord.Clear_and_get_Text()
        self.FirstName = self.Text_Box_name.Clear_and_get_Text()
        self.LarstName = self.Text_Box_Last_name.Clear_and_get_Text()
