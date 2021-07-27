from snakegame.state import GameState, Coordinate, TileState, NORTH, SOUTH, EAST, WEST
from snakegame.board_builder import board_builder

def test_accurate_board():
    s = board_builder(8, 8)
    a = """WWWWWWWW
W      W
W      W
W   R  W
W   g  W
W      W
W      W
WWWWWWWW
"""
    assert a == s.get_ascii_render()