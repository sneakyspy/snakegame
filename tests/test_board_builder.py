from snakegame.state import GameState, Coordinate, TileState, NORTH, SOUTH, EAST, WEST
from snakegame.board_builder import board_builder
from unittest.mock import patch, call

@patch("random.randint")
def test_accurate_board(mock_randint):
    mock_randint.return_value = 3
    s = board_builder(7,5)
    a = """WWWWW
W   W
W R W
W g@W
W   W
W   W
WWWWW
"""
    print(s.get_ascii_render())
    mock_randint.assert_has_calls( [ call(0,4), call(0,6) ] )
    assert a == s.get_ascii_render()