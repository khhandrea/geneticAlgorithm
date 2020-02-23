import pygame as pg
# https://python.bakyeono.net/chapter-12-1.html

# initialize
pg.init()
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
size = [400, 300]
screen = pg.display.set_mode(size)
pg.display.set_caption("Game Title")
done = False
clock = pg.time.Clock()

# main loop
while not done:
    # fps
    clock.tick(10)

    # Main Event Loop
    for event in pg.event.get():  # User did something
        if event.type == pg.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # main
    pg.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 5)
    pg.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 0)
    pg.draw.lines(screen, RED, False, [[50, 150], [
        50, 250], [200, 250], [200, 150]], 5)
    pg.draw.rect(screen, BLACK, [75, 175, 75, 50], 5)
    pg.draw.rect(screen, BLUE, [75, 175, 75, 50], 0)
    pg.draw.line(screen, BLACK, [112, 175], [112, 225], 5)
    pg.draw.line(screen, BLACK, [75, 200], [150, 200], 5)

    # update
    pg.display.flip()
