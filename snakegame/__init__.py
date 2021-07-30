from snakegame.state import Coordinate, GameState, NORTH, EAST, SOUTH, WEST
from snakegame.board_builder import board_builder
from snakegame.time_manager import TimeManager
import pygame

def play():
    pressed_keys = pygame.key.get_pressed()
    s = board_builder(64)
    t = TimeManager(s)
    x = 0
    while s.died == False:
        if pressed_keys[K_w]:
            s.set_direction(NORTH)
        elif pressed_keys[K_d]:
            s.set_direction(EAST)
        elif pressed_keys[K_s]:
            s.set_direction(SOUTH)
        elif pressed_keys[K_a]:
            s.set_direction(WEST)
        else:
            pass
        t.handle_time_passed(s)
    