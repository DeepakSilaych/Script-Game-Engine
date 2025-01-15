from typing import Dict, Optional, List
from .player import Player
from .map import GameMap
from .unit import Unit

class GameState:
    def __init__(self, width: int = 10, height: int = 10):
        self.map = GameMap(width, height)
        self.players: Dict[str, Player] = {}
        self.current_player_id: Optional[str] = None
        self.turn_number: int = 0
        self.game_over: bool = False
        
    def add_player(self, player: Player) -> None:
        self.players[player.player_id] = player
        if self.current_player_id is None:
            self.current_player_id = player.player_id
            
    def get_unit_at_position(self, position: tuple) -> Optional[Unit]:
        for player in self.players.values():
            for unit in player.units:
                if unit.position == position:
                    return unit
        return None
        
    def update_unit_position(self, unit: Unit, new_position: tuple) -> bool:
        if not self.map.is_valid_position(new_position):
            return False
        unit.position = new_position
        return True
        
    def next_turn(self) -> None:
        player_ids = list(self.players.keys())
        current_index = player_ids.index(self.current_player_id)
        next_index = (current_index + 1) % len(player_ids)
        self.current_player_id = player_ids[next_index]
        if next_index == 0:
            self.turn_number += 1 