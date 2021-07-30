from snakegame.state import GameState, Coordinate, TileState, NORTH, SOUTH, EAST, WEST
from snakegame.board_builder import board_builder
from snakegame.time_manager import TimeManager
from unittest.mock import patch, call

@patch("random.randint")
def test_time(mock_randint):
    mock_randint.return_value = 3
    s = board_builder(7,5)
    t = TimeManager(s)
    t.handle_time_passed(400)
    assert s.get_tile(Coordinate(2,2)) == TileState.SNAKE_HEAD
    t.handle_time_passed(101)
    assert s.get_tile(Coordinate(2,1)) == TileState.SNAKE_HEAD
    s.set_direction(EAST)
    t.handle_time_passed(1200)
    print(s.get_ascii_render())
    assert s.died