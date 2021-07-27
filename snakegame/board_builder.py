from snakegame.state import GameState, Coordinate, TileState, NORTH
import math


def board_builder(row_count, column_count):
    grid = []
    for row_number in range(0, row_count):
        grid.insert(row_number, [])
        for column_number in range(0, column_count):
            if row_number == 0 or column_number == 0 or row_number == row_count - 1 or column_number == column_count - 1:
                tile = TileState.WALL
            else:
                tile = TileState.EMPTY
            grid[row_number].insert(column_number, tile)
    snakehead = Coordinate(math.floor(column_count/2), math.floor(row_count/2)-1)
    snaketail = Coordinate(snakehead.x, snakehead.y +1)
    s = GameState(grid, [snakehead, snaketail], NORTH, 1)
    print(s.get_ascii_render())
    s.set_tile(snakehead, TileState.SNAKE_HEAD)
    s.set_tile(snaketail, TileState.SNAKE_TAIL)
    return s