from enum import Enum

class TileState(Enum):
    EMPTY = 0
    SNAKE_HEAD = 1
    SNAKE_BODY = 2
    SNAKE_TAIL = 3
    APPLE = 4
    WALL = 5


SOUTH = (1,0)
EAST = (0,1)
WEST = (0,-1)
NORTH = (-1,0)

class GameState:
    def __init__(self, grid, snake_body, snake_direction, snake_speed):
        self.snake_body = snake_body
        self.snake_direction = snake_direction
        self.snake_speed = snake_speed
        self.grid = grid
        self.elapsed_time = 0

    def evaluate(self, frame_time, player_input):
        self.elapsed_time = self.elapsed_time + frame_time
        if self.elapsed_time > 15:
            new_pos = (self.snake_body[0][1] + player_input[1], self.snake_body[0][0] + player_input[0])
            self.snake_body.insert(0,new_pos)
            old_pos = self.snake_body.pop()
            
