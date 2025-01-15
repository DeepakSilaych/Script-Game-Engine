from typing import List, Tuple, Optional, Dict
from enum import Enum
from .unit import Unit, UnitType
from .map_definitions import MapDefinitions
from .unit import TerrainType

class TerrainEffects:
    """Defines how different terrains affect units"""
    
    # Movement cost multipliers for each terrain type
    MOVEMENT_COSTS = {
        TerrainType.LAND: {
            UnitType.INFANTRY: 1.0,
            UnitType.CAVALRY: 1.0,
            UnitType.ARCHER: 1.0,
            UnitType.SIEGE: 1.5,
            UnitType.NAVAL: float('inf'),  # Cannot move on land
            UnitType.AIRCRAFT: 1.0
        },
        TerrainType.WATER: {
            UnitType.INFANTRY: float('inf'),  # Cannot move on water
            UnitType.CAVALRY: float('inf'),
            UnitType.ARCHER: float('inf'),
            UnitType.SIEGE: float('inf'),
            UnitType.NAVAL: 1.0,
            UnitType.AIRCRAFT: 1.0
        },
        TerrainType.MOUNTAIN: {
            UnitType.INFANTRY: 2.0,
            UnitType.CAVALRY: 3.0,
            UnitType.ARCHER: 2.0,
            UnitType.SIEGE: float('inf'),  # Cannot move on mountains
            UnitType.NAVAL: float('inf'),
            UnitType.AIRCRAFT: 1.0
        },
        TerrainType.FOREST: {
            UnitType.INFANTRY: 1.5,
            UnitType.CAVALRY: 2.0,
            UnitType.ARCHER: 1.5,
            UnitType.SIEGE: 2.5,
            UnitType.NAVAL: float('inf'),
            UnitType.AIRCRAFT: 1.0
        },
        TerrainType.AIR: {
            UnitType.INFANTRY: float('inf'),
            UnitType.CAVALRY: float('inf'),
            UnitType.ARCHER: float('inf'),
            UnitType.SIEGE: float('inf'),
            UnitType.NAVAL: float('inf'),
            UnitType.AIRCRAFT: 1.0
        }
    }
    
    # Combat modifiers for each terrain type
    COMBAT_MODIFIERS = {
        TerrainType.LAND: {
            UnitType.INFANTRY: 1.0,
            UnitType.CAVALRY: 1.0,
            UnitType.ARCHER: 1.0,
            UnitType.SIEGE: 1.0,
            UnitType.NAVAL: 0.5,
            UnitType.AIRCRAFT: 1.0
        },
        TerrainType.MOUNTAIN: {
            UnitType.INFANTRY: 1.2,  # Infantry gets bonus on mountains
            UnitType.CAVALRY: 0.7,   # Cavalry is less effective
            UnitType.ARCHER: 1.3,    # Archers get height advantage
            UnitType.SIEGE: 0.5,
            UnitType.NAVAL: 0.0,
            UnitType.AIRCRAFT: 0.8
        },
        TerrainType.FOREST: {
            UnitType.INFANTRY: 1.1,  # Infantry slight bonus in forests
            UnitType.CAVALRY: 0.8,   # Cavalry penalty in forests
            UnitType.ARCHER: 0.7,    # Archers have reduced visibility
            UnitType.SIEGE: 0.6,
            UnitType.NAVAL: 0.0,
            UnitType.AIRCRAFT: 0.9
        }
    }

class GameMap:
    def __init__(self, map_name: str = "small_duel"):
        """Initialize map with predefined layout"""
        self.map_name = map_name
        self.width, self.height = MapDefinitions.get_map_size(map_name)
        self.terrain: List[List[TerrainType]] = MapDefinitions.get_terrain_map(map_name)
        self.spawn_points = MapDefinitions.get_spawn_points(map_name)
        
    def get_player_spawn_points(self, player_id: str) -> List[Tuple[int, int]]:
        """Get valid spawn points for a player"""
        return self.spawn_points.get(player_id, [])
        
    def is_valid_spawn_point(self, position: Tuple[int, int], player_id: str) -> bool:
        """Check if position is a valid spawn point for the player"""
        return position in self.get_player_spawn_points(player_id)
    
    def is_valid_position(self, position: Tuple[int, int]) -> bool:
        """Check if position is within map bounds"""
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height
        
    def get_terrain_at(self, position: Tuple[int, int]) -> Optional[TerrainType]:
        """Get terrain type at position"""
        if not self.is_valid_position(position):
            return None
        x, y = position
        return self.terrain[y][x]
        
    def set_terrain(self, position: Tuple[int, int], terrain_type: TerrainType) -> bool:
        """Set terrain type at position"""
        if not self.is_valid_position(position):
            return False
        x, y = position
        self.terrain[y][x] = terrain_type
        return True
    
    def get_movement_cost(self, unit_type: UnitType, position: Tuple[int, int]) -> float:
        """Calculate movement cost for a unit type on specific terrain"""
        terrain = self.get_terrain_at(position)
        if terrain is None:
            return float('inf')
        return TerrainEffects.MOVEMENT_COSTS[terrain][unit_type]
    
    def get_combat_modifier(self, unit_type: UnitType, position: Tuple[int, int]) -> float:
        """Get combat effectiveness modifier for a unit type on specific terrain"""
        terrain = self.get_terrain_at(position)
        if terrain is None:
            return 0.0
        return TerrainEffects.COMBAT_MODIFIERS.get(terrain, {}).get(unit_type, 1.0)
    
    def can_unit_move_to(self, unit: Unit, target_position: Tuple[int, int]) -> bool:
        """Check if a unit can move to the target position"""
        if not self.is_valid_position(target_position):
            return False
        
        movement_cost = self.get_movement_cost(unit.unit_type, target_position)
        return movement_cost < float('inf')
    
    def get_valid_moves(self, unit: Unit) -> List[Tuple[int, int]]:
        """Get all valid positions a unit can move to"""
        valid_moves = []
        for x in range(self.width):
            for y in range(self.height):
                pos = (x, y)
                if self.can_unit_move_to(unit, pos):
                    valid_moves.append(pos)
        return valid_moves

    def to_dict(self) -> Dict:
        """Convert map to dictionary representation"""
        return {
            'name': self.map_name,
            'size': (self.width, self.height),
            'terrain': [[t.value for t in row] for row in self.terrain],
            'spawn_points': self.spawn_points
        } 