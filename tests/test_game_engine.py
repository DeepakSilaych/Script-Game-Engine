import pytest
from game.game_state import GameState
from game.player import Player
from game.unit import Unit, UnitType

def test_game_initialization():
    game_state = GameState(10, 10)
    assert game_state.map.width == 10
    assert game_state.map.height == 10
    assert not game_state.game_over

def test_player_addition():
    game_state = GameState()
    player = Player("p1", "Player 1")
    game_state.add_player(player)
    assert "p1" in game_state.players
    assert game_state.current_player_id == "p1"

def test_unit_creation():
    unit = Unit("u1", UnitType.INFANTRY, "p1", (0, 0))
    assert unit.unit_id == "u1"
    assert unit.unit_type == UnitType.INFANTRY
    assert unit.health == 100 