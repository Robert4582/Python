import sys
import pygame
import copy
from DataBase import*
from Enemy_class import *
from settings import *
from PlayerClass import *

pygame.init()
vec = pygame.math.Vector2


class App:

    def __init__(self):
        self.screem = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'intro'
        self.cell_width = MAZE_WIDTH // 28
        self.cell_Height = MAZE_HEIGHT // 30
        self.enemies = []
        self.walls = []
        self.coins = []
        self.enemies = []
        self.e_pos = []
        self.p_pos = vec(1, 1)
        self.highscore_database = HishScore()
        self.current_high_score = 0
        self.load()
        self.player = Player(self, vec(self.p_pos))
        self.i = 10
     #   self.highscore_database.RemoveTable("HighScore")
        self.highscore_database.Update_high_score()
     #  self.highscore_database.Add_score_to_data_base(4)
      #  self.highscore_database.RemoveTable()


    def run(self):
        while self.running:
            if self.state == 'intro':
                self.start_events()
                self.start_Update()
                self.start_draw()
            elif self.state == "playing":
                self.Playing_events()
                self.Playing_Update()
                self.Playing_draw()
            elif self.state == "GameOver":
                self.game_over_events()
                self.game_over_Update()
                self.game_over_draw()
            else:
                self.running = False
        pygame.quit()
        sys.exit()

    ################### HELPER fucntions ######################


    def draw_text(self, words, screen, pos, size, colour, font_name, centred=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centred:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load('background.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))
        self.current_score = self.highscore_database.get_HighScore()
        # openning walls file
        # greating wall list with co-ords of walls
        with open("Walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xide, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xide, yidx))
                    if char == "C":
                        self.coins.append(vec(xide, yidx))
                    if char == "p":
                        self.p_pos = [xide, yidx]
                    elif char in ["2", "3", "4", "5"]:
                        self.e_pos.append([xide, yidx])
                    if char == "B":
                        pygame.draw.rect(self.background, BLACK, (xide * self.cell_width, yidx * self.cell_Height,
                                                                  self.cell_width, self.cell_Height))

        self.make_enemies()

    def draw_grid(self):
        for x in range(WIDTH // self.cell_width):
            pygame.draw.line(self.background, Gray, (x * self.cell_width, 0),
                             (x * self.cell_width, HEIGHT))
        for y in range(HEIGHT // self.cell_Height):
            pygame.draw.line(self.background, Gray, (0, y * self.cell_Height),
                             (HEIGHT, y * self.cell_Height))

    #  for wall in self.walls:
    #      W = wall[0]
    #      pygame.draw.rect(self.background, (100, 200, 200), (W.x * self.cell_width,
    #                                                       W.y * self.cell_Height,
    #                                                       self.cell_width,
    #                                                       self.cell_Height))
    # for coin in self.coins:
    #     pygame.draw.rect(self.background, (55, 52, 60), (coin.x * self.cell_width,
    #                                                      coin.y * self.cell_Height,
    #                                                      self.cell_width,
    #                                                      self.cell_Height))

    def make_enemies(self):
        for idx, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, vec(pos), idx))

    def reset(self):
        self.player.lives = 3
        self.player.current_score = 0
        self.player.grid_pos = vec(self.player.starting_pos)
        self.player.pix_pos = self.player.get_pix_pos()
        self.player.direction *= 0

        self.coins = []
        self.highscore_database.Update_high_score()
        self.current_score = self.highscore_database.get_HighScore()
        for enemy in self.enemies:
            enemy.grid_pos = vec(enemy.starting_pos)
            enemy.pix_pos = enemy.get_pix_pos()
            enemy.direction *= 0

        with open("Walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xide, char in enumerate(line):
                    if char == 'C':
                        self.coins.append(vec(xide,yidx))
        self.state ="playing"
    # i = 0
    # for pos in self.e_pos:
    #     self.enemies.append(Enemy(self, pos, i))
    #     i+=1

    ####################### Intro fucntions ######################

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_Update(self):

        pass

    def start_draw(self):
        self.screem.fill(BLACK)

        self.draw_text('PUSH SPACE BAR', self.screem, [WIDTH / 2, HEIGHT / 2 - 50], START_TEXT_SIZE, (170, 132, 58),
                       START_FONT, True)
        self.draw_text('1 Player Only', self.screem, [WIDTH / 2, HEIGHT / 2 + 50], START_TEXT_SIZE, (33, 137, 156),
                       START_FONT, True)
        self.draw_text('HighScore', self.screem, [2, 0], START_TEXT_SIZE, (255, 255, 255),
                       START_FONT)
        pygame.display.update()

    ######################### Playing ######################

    def Playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))

    def Playing_Update(self):

        self.player.Update()
        for enemy in self.enemies:
            enemy.update()

        for enemy in self.enemies:
            if enemy.grid_pos == self.player.grid_pos:
                self.RemoveLife()

    def Playing_draw(self):
        self.screem.fill(BLACK)

        self.screem.blit(self.background, (Top_button_Buffer / 2, Top_button_Buffer / 2))
        self.draw_coins()

        self.draw_grid()
        self.draw_text("CURRENT SCORE: " + str(self.player.current_score), self.screem, (50, 0), 16, WHITE,
                       START_FONT, False)
        self.draw_text("High SCORE: "+ str(self.current_score), self.screem, (WIDTH // 2 + 60, 0), 16, WHITE, START_FONT, False)

        for enemy in self.enemies:
            enemy.draw()

        self.player.draw()

        pygame.display.update()

    def RemoveLife(self):
        self.player.lives -= 1
        print(self.player.lives)
        if self.player.lives == 0:
            self.state = "GameOver"
            self.highscore_database.Add_score_to_data_base(self.player.current_score)
            print("GameOver")
        else:
            print(self.p_pos)
            self.player.grid_pos = vec(self.player.starting_pos)
            self.player.pix_pos = self.player.get_pix_pos()
            self.player.direction *= 0
            for enemy in self.enemies:
                enemy.grid_pos = vec(enemy.starting_pos)
                enemy.pix_pos = enemy.get_pix_pos()
                enemy.direction *= 0

    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screem, (59, 22, 49),
                               (int(coin.x * self.cell_width) + self.cell_width // 2 + Top_button_Buffer // 2,
                                int(coin.y * self.cell_Height) + self.cell_Height // 2 + Top_button_Buffer // 2), 5)

        ######################### GameOver ######################

    def game_over_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                d =2
                self.highscore_database.RemoveTable()
                self.current_high_score = 0
    def game_over_Update(self):
        pass

    def game_over_draw(self):
        self.screem.fill(BLACK)
        self.draw_text("GAME OVER", self.screem, [WIDTH / 2, HEIGHT / 2 - 100], 60, RED, START_FONT, True)
        self.draw_text("Press space to play Again", self.screem,[WIDTH / 2, HEIGHT / 2 - 50], 20, RED, START_FONT, True)
        self.draw_text("Press escape to quit", self.screem, [WIDTH / 2, HEIGHT / 2 + 150], 20, RED, START_FONT, True)
        self.draw_text("Reset Hirghscore Press R", self.screem, [WIDTH / 2, HEIGHT / 2 + 250], 20, RED, START_FONT, True)

        pygame.display.update()
