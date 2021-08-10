from snakegame.state import Coordinate, GameState, TileState, NORTH, EAST, SOUTH, WEST
from snakegame.board_builder import board_builder
from snakegame.time_manager import TimeManager
import pygame
TEAL = pygame.color.Color(163, 240, 238)
RED = pygame.color.Color(255, 0, 0)
GREEN = pygame.color.Color(0, 255, 0)
TAILGREEN = pygame.color.Color(187, 255, 0)
HEADRED = pygame.color.Color(255, 255, 0)
WALL = pygame.color.Color(0, 171, 165)
WIDTH, HEIGHT = 800, 800


def px_per_tile(surface, state):
    px_x_per_tile = surface.get_width() / state.column_count
    px_y_per_tile = surface.get_height() / state.row_count
    return px_x_per_tile, px_y_per_tile


def tile2px(surface, state, coordinate):
    px_x_per_tile, px_y_per_tile = px_per_tile(surface, state)
    px_x = coordinate.x * px_x_per_tile
    px_y = coordinate.y * px_y_per_tile
    return px_x, px_y, px_x_per_tile, px_y_per_tile



PAINTMAP = {
    TileState.EMPTY: TEAL,
    TileState.SNAKE_HEAD: HEADRED,
    TileState.APPLE: RED,
    TileState.SNAKE_BODY: GREEN,
    TileState.SNAKE_TAIL: TAILGREEN,
    TileState.WALL: WALL
    }

def render_state(surface, state):
    surface.fill(TEAL)
    for row_number in range(0, state.row_count):
        for column_number in range(0, state.column_count):
            c = Coordinate(column_number, row_number)
            pygame.draw.rect(surface, PAINTMAP[state.get_tile(c)], tile2px(surface, state, c))
    pygame.display.flip()

def turn():
    pass


def play():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake_game")
    new_direction = NORTH
    pygame.init()
    s = board_builder(32,32)
    t = TimeManager(s)
    x = 0
    run = True
    last_tick = pygame.time.get_ticks()
    while run:
        this_tick = pygame.time.get_ticks()
        elapsed = this_tick - last_tick
        last_tick = this_tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            new_direction = NORTH
        elif pressed_keys[pygame.K_d]:
            new_direction = EAST
        elif pressed_keys[pygame.K_s]:
            new_direction = SOUTH
        elif pressed_keys[pygame.K_a]:
            new_direction = WEST
        else:
            pass
        if not s.died:
            s.set_direction(new_direction)
            t.handle_time_passed(elapsed)
        render_state(window, s)
    pygame.quit()


if __name__ == "__main__":
    play()