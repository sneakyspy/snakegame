from snakegame.state import GameState, Coordinate, TileState, NORTH, SOUTH, EAST, WEST

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
        [ Coordinate(4,3), Coordinate(4,4) ],
        NORTH,
        1
        )

def sample_starting_state2():
    return GameState(
        [
            [ TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL ],
            [ TileState.WALL,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.APPLE,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.SNAKE_HEAD,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.SNAKE_BODY,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.SNAKE_TAIL,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.EMPTY,TileState.WALL ],
            [ TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL,TileState.WALL ]
        ],
        [ Coordinate(4,3), Coordinate(4,4), Coordinate(4,5) ],
        NORTH,
        1
        )




def test_tile_set_get():
    s = sample_starting_state()
    assert s.get_tile(Coordinate(0,0)) == TileState.WALL
    assert s.get_tile(Coordinate(3,0)) == TileState.WALL
    assert s.get_tile(Coordinate(1,2)) == TileState.APPLE
    assert s.set_tile(Coordinate(0,0), TileState.APPLE) == (TileState.WALL, TileState.APPLE)
    assert s.get_tile(Coordinate(0,0)) == TileState.APPLE

def test_snake_moves_up():
    s = sample_starting_state()
    print(s.get_ascii_render())
    s.move_snake()
    print(s.get_ascii_render())
    assert s.snake_body == [ Coordinate(4,2), Coordinate(4,3) ]
    head = s.snake_body[0]
    tail = s.snake_body[-1]
    assert s.get_tile(head) == TileState.SNAKE_HEAD
    assert s.get_tile(tail) == TileState.SNAKE_TAIL
    assert s.get_tile(Coordinate(4,4)) == TileState.EMPTY

def test_snake_dies_at_wall():
    s = sample_starting_state()
    print(s.get_ascii_render())
    s.move_snake()
    s.move_snake()
    s.move_snake()
    print(s.get_ascii_render())
    assert s.died == True
    head = s.snake_body[0]
    tail = s.snake_body[-1]

def test_bigger_snake_moves_up():
    s = sample_starting_state2()
    print(s.get_ascii_render())
    s.move_snake()
    print(s.get_ascii_render())
    assert s.snake_body == [ Coordinate(4,2), Coordinate(4,3), Coordinate(4,4) ]
    head = s.snake_body[0]
    body = s.snake_body[1]
    tail = s.snake_body[-1]
    assert s.get_tile(head) == TileState.SNAKE_HEAD
    assert s.get_tile(body) == TileState.SNAKE_BODY
    assert s.get_tile(tail) == TileState.SNAKE_TAIL
    assert s.get_tile(Coordinate(4,5)) == TileState.EMPTY

def test_bigsnake_can_turn():
    s = sample_starting_state2()
    print(s.get_ascii_render())
    s.move_snake()
    s.set_direction(EAST)
    s.move_snake()
    print(s.get_ascii_render())
    assert s.snake_body == [ Coordinate(5,2), Coordinate(4,2), Coordinate(4,3) ]
    

def test_ascii_render():
    s = sample_starting_state()
    a = """WWWWWWWW
W      W
W@     W
W   R  W
W   g  W
W      W
W      W
WWWWWWWW
"""
    assert a == s.get_ascii_render()