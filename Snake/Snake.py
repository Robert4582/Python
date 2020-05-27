from App import *
from Settings import *
from queue import LifoQueue


class snake:
    def __init__(self, app, pos, Color, Start_Diretion):
        self.App = app
        self.x = pos.x
        self.y = pos.y
        self.S_pos = vec(self.x, self.y)
        self.color = Color
        self.Heigt = 20
        self.width = 20
        self.Direction = Start_Diretion
        self.S_D = Start_Diretion
        self.Snake_moves = []
        self.Snake_moves.append(self.Direction)
        self.Grid_pos = pos
        self.S_Grip_p = self.Grid_pos // 20
        self.s = 0
        self.speed = 2
        self.Snake_heads_l_P = vec(0, 0)



        self.Number_body_parts = 2
        self.bodyParts = []
        self.snakeFormer_pos = []
        self.i = 0
        self.reset = False
        self.h = 0
        self.rdy_for_m = False

        self.AddBodypart(vec(self.Grid_pos.x / 20, self.Grid_pos.y / 20 + 1), PLAYER_COLOUR)
        self.AddBodypart(vec(self.Grid_pos.x / 20, self.Grid_pos.y / 20 + 2), RED)
        self.AddBodypart(vec(self.Grid_pos.x / 20, self.Grid_pos.y / 20 + 3), WHITE)

        # self.AddBodypart(vec(self.Grid_pos.x / 20, self.Grid_pos.y / 20 + 4), Gray)
        # self.AddBodypart(vec(self.Grid_pos.x / 20, self.Grid_pos.y / 20 + 5), PLAYER_COLOUR)
        # self.AddBodypart(vec(self.Grid_pos.x / 20, self.Grid_pos.y / 20 + 6), WHITE)
        self.F_D = self.Direction
        ## startValues##

    # print(self.S_Grip_p)

    def update(self):
        self.Move()
        self.setSimple_Grip_P()
        self.CheckSnake_hit_self()
      #  print("gogogoo", self.speed)

    #     print(self.S_pos)

    #   print(self.Grid_pos)

    def DrawSnake(self):
        #     print(int(self.Grid_pos.x))
        self.DrawbodyParts()

        if self.Grid_pos.x != 1 * 20 and self.Grid_pos.x != 62 * 20 and self.Grid_pos.y != 2* 20 and self.Grid_pos.y != 33 * 20:
            pygame.draw.rect(self.App.screen, self.color,
                         (int(self.Grid_pos.x + -1), int(self.Grid_pos.y - 1), self.width + 3, self.Heigt +3))

    ########################### Methons ###########################################################
    def SetDirection(self, Direction):

        if len(self.Snake_moves) < 2:
            self.Snake_moves.append(Direction)
        self.Direction = Direction

    def Move(self):
        self.Snake_Gos_through_Walls()
        self.s += 1

        if self.s == self.speed:
            ## Update snaks form postions
            x = self.Grid_pos.x
            y = self.Grid_pos.y
            self.snakeFormer_pos.append(vec(x, y))
            #     print(print(self.snakeFormer_pos))
            print("gogogoo", self.speed)
            # self.Grid_pos += self.Direction * 20
            self.Grid_pos += self.Direction * 20
            F_D = self.Direction

            self.rdy_for_m = True
            self.s = 0
            self.Update_Bodypart_pos()

    def DrawbodyParts(self):

        for x in self.bodyParts:
            x.DrawBodypart()

    def Update_Bodypart_pos(self):

        if len(self.snakeFormer_pos) >= 0:
            self.h += 1
            #  print("hEJ", self.h)
            for body in self.bodyParts:
                #  if self.h == 1 and self.i == -2:
                #      break
                # print(self.i)
                # print("number of pos", len(self.snakeFormer_pos))
                # print("snakepos", len(self.snakeFormer_pos) - 1 + self.i)
                # print(self.snakeFormer_pos)
                if self.i <= -len(self.snakeFormer_pos):
                    #    print("hey")
                    body.pos += self.S_D
                else:
                    body.pos = self.snakeFormer_pos[len(self.snakeFormer_pos) - 1 + self.i] / 20

                #    if body.pos * 20 != self.Grid_pos:

                #  print(body.pos * 20, self.Grid_pos)
                #  print(body.pos * 20, self.Grid_pos )
                self.i -= 1
            self.i = 0

    def CheckSnake_hit_self(self):
        SnakeHead_P = vec(self.Grid_pos.x * 20, self.Grid_pos.y * 20)
        for body in self.bodyParts:
            #  print(self.Grid_pos)
            #     print( body.pos *20)
            if self.Grid_pos == body.pos * 20:
                self.ResetSnake()

    def ResetSnake(self):
        print("Reset")
        self.App.Database_Highscore.Add_score_to_data_base(self.App.score)
        self.App.score = 0
        self.bodyParts.clear()
        self.Direction = self.S_D
        s = self.S_pos
        self.s = 0
        self.Grid_pos = vec(self.x, self.y)
        self.AddBodypart(vec(self.Grid_pos.x / 20, self.Grid_pos.y / 20 + 1), self.App.Get_random_color())
        self.AddBodypart(vec(self.Grid_pos.x / 20, self.Grid_pos.y / 20 + 2), self.App.Get_random_color())
        self.AddBodypart(vec(self.Grid_pos.x / 20, self.Grid_pos.y / 20 + 3), self.App.Get_random_color())

    def AddBodypart(self, pos, Color):
        self.bodyParts.append(SnakeBodyPart(self.App, pos, Color))

    def setSimple_Grip_P(self):
        self.S_Grip_p = self.Grid_pos // 20

    def Snake_Gos_through_Walls(self):

        if self.Grid_pos.x//20 < 2:
            self.Grid_pos.x = 61 * 20
        if self.Grid_pos.x//20 > 61:
            self.Grid_pos.x = 2 * 20

        if self.Grid_pos.y//20 < 3:
            self.Grid_pos.y = 32 * 20
            print("apwdpawdkpawkdpakwd")
        if self.Grid_pos.y//20 > 32:
             self.Grid_pos.y = 3*20



class SnakeBodyPart:
    def __init__(self, app, pos, color):
        self.app = app
        self.pos = pos
        self.color = color

    def DrawBodypart(self):
        pygame.draw.rect(self.app.screen, self.color,
                         ((int(self.pos.x) * 20 + 1), (int(self.pos.y) * 20) + 1, cell_Height - 1, cell_Height - 1))
