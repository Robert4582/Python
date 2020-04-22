from settings import *

vec = pygame.math.Vector2


class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = 1
        self.starting_pos = [pos.x, pos.y]

    def Update(self):

        if self.able_to_move:
            self.pix_pos += self.direction * self.speed

        if self.time_to_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()
        # setting grid positon in refence to grid position
        self.grid_pos[0] = (self.pix_pos[0] - Top_button_Buffer + self.app.cell_width // 2) // self.app.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - Top_button_Buffer + self.app.cell_Height // 2) // self.app.cell_Height + 1

        if self.on_Coin():
            self.eat_coin()

    #    print((self.pix_pos[1] - Top_button_Buffer+self.app.cell_Height//2) // self.app.cell_Height + 1)

    def draw(self):
        pygame.draw.circle(self.app.screem, PLAYER_COLOUR, (int(self.pix_pos.x), int(self.pix_pos.y)),
                           self.app.cell_width // 2 - 2)

        # drawubg the grid rect
        pygame.draw.rect(self.app.screem, RED,
                         (self.grid_pos[0] * self.app.cell_width + Top_button_Buffer // 2,
                          self.grid_pos[1] * self.app.cell_Height + Top_button_Buffer // 2,
                          self.app.cell_width,
                          self.app.cell_Height), 1)
        for x in range(self.lives):
            pygame.draw.circle(self.app.screem, PLAYER_COLOUR, (30 + 20*x, HEIGHT-10), 8)

    def move(self, direction):
        self.stored_direction = direction

    def get_pix_pos(self):
        return vec((self.grid_pos.x * self.app.cell_width) + Top_button_Buffer // 2 + self.app.cell_width // 2,
                   (self.grid_pos.y * self.app.cell_Height) + Top_button_Buffer // 2 + self.app.cell_width // 2)

    def time_to_move(self):
        if int(self.pix_pos.x + Top_button_Buffer // 2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y + Top_button_Buffer // 2) % self.app.cell_Height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

    def can_move(self):

        for wall in self.app.walls:



            if vec(self.grid_pos + self.direction) == wall:
        #        print("WALL")
                return False
        return True

    def on_Coin(self):

        if self.grid_pos in self.app.coins:
            if int(self.pix_pos.x + Top_button_Buffer // 2) % self.app.cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    return True
            if int(self.pix_pos.y + Top_button_Buffer // 2) % self.app.cell_Height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True
        else:
            return False

    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.current_score += 10
