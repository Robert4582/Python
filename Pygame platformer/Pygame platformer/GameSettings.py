#Game settings
TITLE = "MILO jumper"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONTNAME = 'arial'
HSFILE = "highscore.txt"

#Player settings
PLAYERACC = 0.5
PLAYERFRICTION = -0.12
PLAYERGRAV = 0.8
PLAYERJUMP = 20

#starting platforms
PLATFORMLIST = [(0, HEIGHT - 40, WIDTH, 40),
                (WIDTH/2 -50, HEIGHT *3 / 4, 100, 20), 
                (125, HEIGHT - 350, 130, 20),
                (400, 170, 50, 20),
                (10, 25, 100, 20)]

#Colors definded
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE