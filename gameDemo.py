import pygame as pg
import time
from datetime import datetime
from datetime import timedelta

# https://python.bakyeono.net/chapter-12-1.html

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

BLOCK_SIZE = 20

BACKGROUND_COLOR = 18, 137, 167
SNAKE_COLOR = 34, 47, 62
APPLE_COLOR = 249, 127, 81


class Snake:
    color = SNAKE_COLOR

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]
        self.direction = 'north'

    def draw(self, screen):
        for position in self.positions:
            draw_block(screen, self.color, position)


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


# initialize
pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_background(screen):
    rect = pg.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.draw.rect(screen, BACKGROUND_COLOR, rect)


def draw_block(screen, color, position):
    block = pg.Rect((position[1] * BLOCK_SIZE+1, position[0]
                     * BLOCK_SIZE+1), (BLOCK_SIZE-2, BLOCK_SIZE-2))
    pg.draw.rect(screen, color, block)


game_board = GameBoard()

while True:
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:  # quit
            exit()

    draw_background(screen)
    game_board.draw(screen)
    pg.display.update()  # update
