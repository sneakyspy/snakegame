import random
from enum import Enum



class TileState(Enum):
    EMPTY = 0
    SNAKE_HEAD = 1
    SNAKE_BODY = 2
    SNAKE_TAIL = 3
    APPLE = 4
    WALL = 5

SOUTH = (0,1)
EAST = (1,0)
WEST = (-1,0)
NORTH = (0,-1)


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def str(self):
        return f"[{self.x},{self.y}]"

    def __repr__(self):
        return self.str()
 
    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        return False

class GameState:
    def __init__(self, grid, snake_body, snake_direction, snake_speed):
        self.snake_body = snake_body
        self.snake_direction = snake_direction
        self.snake_speed = snake_speed
        self.grid = grid
        self.row_count = len(self.grid)
        self.column_count = len(self.grid[0])
        self.died = False
        
    def get_tile(self, coord):
        return self.grid[coord.y][coord.x]
    
    def set_tile(self, coord, state):
        old_value = self.grid[coord.y][coord.x]
        self.grid[coord.y][coord.x] = state
        new_value = self.grid[coord.y][coord.x]
        return old_value, new_value
    
    def set_direction(self, direction):
        self.snake_direction = direction
    
    def generate_apple(self):
        while True:
            x = random.randint(0, self.column_count - 1)
            y = random.randint(0, self.row_count - 1)
            if self.get_tile(Coordinate(x, y)) == TileState.EMPTY:
                self.set_tile(Coordinate(x, y), TileState.APPLE)
                return
        
    def move_snake(self):     
        if self.died:
            return
        nbody_pos = self.snake_body[0] 
        new_pos = Coordinate(nbody_pos.x + self.snake_direction[0], nbody_pos.y + self.snake_direction[1])
        tile = self.get_tile(new_pos)
        if tile in (TileState.WALL, TileState.SNAKE_HEAD, TileState.SNAKE_BODY, TileState.SNAKE_TAIL):
            self.died = True
            #if the snake, dies then do not continue code
        elif tile == TileState.APPLE:
            self.snake_body.insert(0, new_pos)
            self.set_tile(new_pos, TileState.SNAKE_HEAD)
            self.set_tile(nbody_pos, TileState.SNAKE_BODY)
            self.generate_apple()
            
        else:
            self.set_tile(nbody_pos, TileState.SNAKE_BODY)
            self.snake_body.insert(0, new_pos)
            old_pos = self.snake_body.pop()
            self.set_tile(old_pos, TileState.EMPTY)
            self.set_tile(new_pos, TileState.SNAKE_HEAD)
            tail_pos = self.snake_body[-1]
            self.set_tile(tail_pos, TileState.SNAKE_TAIL)
        
    def update(self):
        Value = NORTH
        if True:
            self.set_direction(Value)
            self.move_snake()
            return
    
    
    
    def get_ascii_render(self):
        ascii_map = {
            TileState.EMPTY: " ",
            TileState.SNAKE_HEAD: "R",
            TileState.APPLE: "@",
            TileState.SNAKE_BODY: "G",
            TileState.SNAKE_TAIL: "g",
            TileState.WALL: "W"
            }
        
        ascii_art = ""
        for row in self.grid:
            for tile in row:
                ascii_art = ascii_art + ascii_map[tile]
            ascii_art = ascii_art + "\n"
        return ascii_art
