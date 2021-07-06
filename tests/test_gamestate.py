from snakegame.state import GameState, TileState, NORTH, SOUTH, EAST, WEST

def sample_starting_state():
    return GameState(
        [
            [ TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL ],
            [ TileState.WALL,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.APPLE,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.SNAKE_HEAD,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.SNAKE_TAIL,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL ]
        ],
        [ (3,4), (4,4) ],
        NORTH,
        1
        )

def test_snake_moves_up():
    s = sample_starting_state()
    s.evaluate(100, NORTH)
    assert s.snake_body == [ (2,4), (3,4) ]
    head = s.snake_body[0]
    tail = s.snake_body[-1]
    assert s.grid[head[1]][head[0]] == TileState.SNAKE_HEAD
    assert s.grid[tail[1]][tail[0]] == TileState.SNAKE_TAIL
    assert s.grid[4][4] == TileState.EMPTY