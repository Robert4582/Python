import pygame
import queue

pygame.init()

# Set up the drawing window
from Snake import *
from Fruit import *
from DataBase import *
from Settings import *
from S_UI import *

class App:
    def __init__(self, ):

        self.liste = []


        self.state = "S_UI"
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.init()

        self.S_UI = S_UI(self)

        self.Database_Highscore = HishScore()


        self.Snake_pos = vec(640, 360)
        self.Snake = snake(self, self.Snake_pos, RED, vec(0, -1))

        self.fruit = fruit(self, self.Get_random_color())
        self.Row_x = 0
        self.RoW_y = 0
        self.score = 0

    def run(self):

        while self.running:
            self.clock.tick(60)
            # Did the user click the window close button?

            # Fill the background with white
            if self.state == "S_UI":
                self.S_UI.Start_Screen()

            if self.state == "run":
              self.Run_event()
              self.Run_update()
              self.Run_draw()

            # Flip the display

        # Done! Time to quit.
        pygame.quit()

    #        while self.running:
    #
    #            print("hey")
    #
    #            if self.state == "run":
    #                self.Run_event()
    #                self.Run_update()
    #                self.Run_draw()
    #
    #    pygame.quit()
    #
    def Run_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.Movement(event)
                if event.key == pygame.K_RETURN:
                    self.screen.fill(BLACK)
                    self.Snake.ResetSnake()
                    self.state = "S_UI"
                    self.S_UI.Timer = 60


    def Run_update(self):
        self.Snake.update()

        if self.Snake.S_Grip_p == self.fruit.pos:
            self.score += 10 - (self.Snake.speed-2)
            self.Snake.Number_body_parts += 1
            self.fruit.SetNewPosition()
            self.Snake.AddBodypart(self.Snake.Grid_pos, self.fruit.color)
            self.fruit.Set_color(self.Get_random_color())

    def Run_draw(self):

        self.DrawGrid()
        self.fruit.draw_fruit()
        #   pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
        self.Snake.DrawSnake()
        self.draw_text("Score:" + str(self.score), self.screen, [WIDTH / 1.15, 30], 25, WHITE, START_FONT, True)
        self.draw_text("Rainbow snake", self.screen, [WIDTH / 2, 30], 25, WHITE, START_FONT, True)
        self.draw_text("Press enter to go to menu", self.screen, [WIDTH / 6, 30], 25, WHITE, START_FONT, True)
        pygame.display.flip()
        self.screen.fill(BLACK)



    ################## Helper Fuctions #########################



    def draw_text(self, words, screen, pos, size, colour, font_name, centred=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centred:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    def Get_random_color(self):
        numb = random.randint(1, 10)
        return self.switch_Colors(numb)

    def switch_Colors(argument, number):
        print(number)
        switcher = {
            1: RED,
            2: ORANGE,
            3: YELLOW,
            4: GREEN,
            5: TURKIS,
            6: PURBLE,
            7: BLU,
            8: PURBLE,
            9: Gray,
            10: WHITE,

        }
        return switcher.get(number, "Invalid color")

    def Movement(self, event):

        if self.Snake.rdy_for_m:
            if event.key == pygame.K_LEFT and self.Snake.Direction != vec(1, 0):
                self.Snake.SetDirection(vec(-1, 0))
                self.Snake.rdy_for_m = False
            if event.key == pygame.K_RIGHT and self.Snake.Direction != vec(-1, 0):
                self.Snake.SetDirection(vec(1, 0))
                self.Snake.rdy_for_m = False
            if event.key == pygame.K_UP and self.Snake.Direction != vec(0, 1):
                self.Snake.SetDirection(vec(0, -1))
                self.Snake.rdy_for_m = False
            if event.key == pygame.K_DOWN and self.Snake.Direction != vec(0, -1):
                self.Snake.SetDirection(vec(0, 1))
                self.Snake.rdy_for_m = False

    def DrawGrid(self):
        pygame.draw.line(self.screen, Gray,
                         ((WIDTH - SNAKE_CAGE_WIDTH) / 2 + self.Row_x * cell_Width, (HEIGHT - SNAKE_CAGE_HEIGHT) / 2),
                         ((WIDTH - SNAKE_CAGE_WIDTH) / 2 + self.Row_x * cell_Width,
                          HEIGHT - (HEIGHT - SNAKE_CAGE_HEIGHT) / 2))
        for x in range(SNAKE_CAGE_WIDTH // cell_Width):
            self.Row_x += 1
          # pygame.draw.line(self.screen, Gray,
          #                  ((WIDTH - SNAKE_CAGE_WIDTH) / 2 + x * cell_Width, (HEIGHT - SNAKE_CAGE_HEIGHT) / 2),
          #                  ((WIDTH - SNAKE_CAGE_WIDTH) / 2 + x * cell_Width,
          #                   HEIGHT - (HEIGHT - SNAKE_CAGE_HEIGHT) / 2))
        ## larst linse x

        pygame.draw.line(self.screen, Gray,
                         ((WIDTH - SNAKE_CAGE_WIDTH) / 2 + self.Row_x * cell_Width, (HEIGHT - SNAKE_CAGE_HEIGHT) / 2),
                         ((WIDTH - SNAKE_CAGE_WIDTH) / 2 + self.Row_x * cell_Width,
                          HEIGHT - (HEIGHT - SNAKE_CAGE_HEIGHT) / 2))

        pygame.draw.line(self.screen, Gray,
                         ((WIDTH - SNAKE_CAGE_WIDTH) / 2, cell_Height * self.RoW_y + (HEIGHT - SNAKE_CAGE_HEIGHT) / 2),
                         (WIDTH - (WIDTH - SNAKE_CAGE_WIDTH) / 2,
                          cell_Height * self.RoW_y + (HEIGHT - SNAKE_CAGE_HEIGHT) / 2))

        for y in range(SNAKE_CAGE_HEIGHT // cell_Height):
            self.RoW_y += 1
         #  pygame.draw.line(self.screen, Gray,
         #                   ((WIDTH - SNAKE_CAGE_WIDTH) / 2, cell_Height * y + (HEIGHT - SNAKE_CAGE_HEIGHT) / 2),
         #                   (WIDTH - (WIDTH - SNAKE_CAGE_WIDTH) / 2,
         #                    cell_Height * y + (HEIGHT - SNAKE_CAGE_HEIGHT) / 2))

        pygame.draw.line(self.screen, Gray,
                         ((WIDTH - SNAKE_CAGE_WIDTH) / 2, cell_Height * self.RoW_y + (HEIGHT - SNAKE_CAGE_HEIGHT) / 2),
                         (WIDTH - (WIDTH - SNAKE_CAGE_WIDTH) / 2,
                          cell_Height * self.RoW_y + (HEIGHT - SNAKE_CAGE_HEIGHT) / 2))
        self.RoW_y = 0
        self.Row_x = 0
