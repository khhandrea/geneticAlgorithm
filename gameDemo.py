import pygame as pg
from pygame.locals import *
import time
from datetime import datetime
from datetime import timedelta
import random

"""
todo

v catch deviation of gameboard
v block right-back turn
v clear when snake fill the gameboard
  interval get faster
v change head color
  sound effect (on off)
  score
v frame
  restart
"""

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GAMEBOARD_WIDTH = 20
GAMEBOARD_HEIGHT = 20
GAMEBOARD_POSITION = [12, 12]

INTERVAL_VALUE = 0.2
TURN_INTERVAL = timedelta(seconds=INTERVAL_VALUE)  # get faster eating apple
SPEED_RATIO = 0.9
IS_GETTING_FASTER = 1

BLOCK_SIZE = 20

BACKGROUND_COLOR = 53, 59, 72

# high contrast theme
GAMEBOARD_COLOR = 0, 0, 0
SNAKE_COLOR = 255, 255, 255
HEAD_COLOR = 255, 255, 255
APPLE_COLOR = 255, 0, 0

"""
# greenish theme
GAMEBOARD_COLOR = 33, 140, 116
SNAKE_COLOR = 255, 211, 42
HEAD_COLOR = 255, 168, 1
APPLE_COLOR = 234, 32, 39
"""

"""
# bluish theme
GAMEBOARD_COLOR = 18, 137, 167
SNAKE_COLOR = 34, 47, 62
HEAD_COLOR = 30, 49, 46
APPLE_COLOR = 249, 127, 81
"""

DIRECTION_ON_KEY = {
    pg.K_UP: 'north',
    pg.K_DOWN: 'south',
    pg.K_LEFT: 'west',
    pg.K_RIGHT: 'east',
}


class Snake:
    color = SNAKE_COLOR
    head_color = HEAD_COLOR

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]
        self.direction = 'north'

    def draw(self, screen):
        draw_block(screen, HEAD_COLOR, self.positions[0])
        for position in self.positions[1:]:
            draw_block(screen, self.color, position)

    def crawl(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'north':
            self.positions = [(y-1, x)] + self.positions[:-1]
        elif self.direction == 'south':
            self.positions = [(y+1, x)] + self.positions[:-1]
        elif self.direction == 'east':
            self.positions = [(y, x+1)] + self.positions[:-1]
        elif self.direction == 'west':
            self.positions = [(y, x-1)] + self.positions[:-1]

    def turn(self, direction):
        if direction == 'north' and self.direction == 'south':
            pass
        elif direction == 'south' and self.direction == 'north':
            pass
        elif direction == 'west' and self.direction == 'east':
            pass
        elif direction == 'east' and self.direction == 'west':
            pass
        else:
            self.direction = direction

    def grow(self):
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'north':
            self.positions.append((y-1, x))
        elif self.direction == 'south':
            self.positions.append((y+1, x))
        elif self.direction == 'east':
            self.positions.append((y, x-1))
        elif self.direction == 'west':
            self.positions.append((y, x-1))


class Apple:
    color = APPLE_COLOR

    def __init__(self, position=(5, 5)):
        self.position = position

    def draw(self, screen):
        draw_block(screen, self.color, self.position)


class GameBoard:
    width = 20
    height = 20

    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()

    def draw(self, screen):
        self.apple.draw(screen)
        self.snake.draw(screen)

    def process_turn(self):
        self.snake.crawl()  # movement

        if self.snake.positions[0] in self.snake.positions[1:]:  # self collision
            raise SnakeCollisionException()

        if self.snake.positions[0][0] > GAMEBOARD_WIDTH-1 \
                or self.snake.positions[0][0] < 0 \
                or self.snake.positions[0][1] > GAMEBOARD_HEIGHT-1 \
                or self.snake.positions[0][1] < 0:  # deviate gameboard
            raise SnakeCollisionException

        if self.snake.positions[0] == self.apple.position:  # eat apple
            self.snake.grow()
            self.put_new_apple()

    def put_new_apple(self):
        if len(self.snake.positions) > 360:
            raise SnakeExcessiveException
        self.apple = Apple((random.randint(0, 19), random.randint(0, 19)))
        for position in self.snake.positions:
            if self.apple.position == position:
                self.put_new_apple()
                break


class SnakeExcessiveException(Exception):  # exception for clear
    pass


class SnakeCollisionException(Exception):  # exception for collision
    pass


# initialize
pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_board = GameBoard()
last_turn_time = datetime.now()


def draw_background(screen):
    rect = pg.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.draw.rect(screen, BACKGROUND_COLOR, rect)


def draw_gameboard(screen):
    rect = pg.Rect(
        (GAMEBOARD_POSITION[1], GAMEBOARD_POSITION[0]),
        (GAMEBOARD_WIDTH * BLOCK_SIZE, GAMEBOARD_HEIGHT * BLOCK_SIZE))
    pg.draw.rect(screen, GAMEBOARD_COLOR, rect)


def draw_block(screen, color, position):
    block = pg.Rect(
        (GAMEBOARD_POSITION[1] + position[1] * BLOCK_SIZE+1,
         GAMEBOARD_POSITION[0] + position[0] * BLOCK_SIZE+1),
        (BLOCK_SIZE-2, BLOCK_SIZE-2))
    pg.draw.rect(screen, color, block)


while True:
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:  # quit
            exit()

    if event.type == pg.KEYDOWN:
        if event.key in DIRECTION_ON_KEY:
            game_board.snake.turn(DIRECTION_ON_KEY[event.key])

    if TURN_INTERVAL < datetime.now() - last_turn_time:
        try:
            game_board.process_turn()
        except SnakeCollisionException:
            exit()
        last_turn_time = datetime.now()

    draw_background(screen)
    draw_gameboard(screen)
    game_board.draw(screen)
    pg.display.update()  # update
