from typing import Dict, List
from .unit import TerrainType
class MapDefinitions:
    """Predefined map layouts for the game"""
    
    MAPS = {
        "small_duel": {
            "name": "Small Duel",
            "description": "A small 8x8 map perfect for 1v1 battles",
            "size": (8, 8),
            "terrain": [
                # L = Land, W = Water, M = Mountain, F = Forest, A = Air
                "LLFFLLLL",
                "LLFFLWWL",
                "LLLLWWWL",
                "MMLLWWLL",
                "LLWWLLMM",
                "LWWWLLLL",
                "LWWLLFFLL",
                "LLLLFFLL"
            ],
            "spawn_points": {
                "player1": [(0, 0), (0, 1), (1, 0)],
                "player2": [(7, 7), (7, 6), (6, 7)]
            }
        },
        
        "island_warfare": {
            "name": "Island Warfare",
            "description": "Naval-focused map with multiple islands",
            "size": (12, 12),
            "terrain": [
                "WWWWWWWWWWWW",
                "WWLLFFLLWWWW",
                "WLLFFFLLWWWW",
                "WLLFFLLLWWWW",
                "WWWWWWWWWWWW",
                "WWWLLFFLLWWW",
                "WWWLLFFLLWWW",
                "WWWWWWWWWWWW",
                "WWWWLLFFLLLW",
                "WWWWLLFFFLLW",
                "WWWWLLFFLLWW",
                "WWWWWWWWWWWW"
            ],
            "spawn_points": {
                "player1": [(1, 1), (2, 1), (1, 2)],
                "player2": [(10, 10), (9, 10), (10, 9)]
            }
        },
        
        "mountain_pass": {
            "name": "Mountain Pass",
            "description": "Strategic mountain passages between players",
            "size": (10, 10),
            "terrain": [
                "LLMMLLMMLL",
                "LLLMLLLMLL",
                "FFLLLLLLFF",
                "MMLLLLLMMM",
                "LLLLWWLLLL",
                "LLLLWWLLLL",
                "MMMLLLLLMM",
                "FFLLLLLLFF",
                "LLMLLLMLLL",
                "LLMMLLMMLL"
            ],
            "spawn_points": {
                "player1": [(0, 0), (1, 0), (0, 1)],
                "player2": [(9, 9), (8, 9), (9, 8)]
            }
        }
    }
    
    @classmethod
    def get_terrain_map(cls, map_name: str) -> List[List[TerrainType]]:
        """Convert string-based terrain map to TerrainType map"""
        if map_name not in cls.MAPS:
            raise ValueError(f"Map '{map_name}' not found")
            
        map_data = cls.MAPS[map_name]
        terrain_map = []
        
        terrain_conversion = {
            'L': TerrainType.LAND,
            'W': TerrainType.WATER,
            'M': TerrainType.MOUNTAIN,
            'F': TerrainType.FOREST,
            'A': TerrainType.AIR
        }
        
        for row in map_data["terrain"]:
            terrain_row = [terrain_conversion[char] for char in row]
            terrain_map.append(terrain_row)
            
        return terrain_map
    
    @classmethod
    def get_spawn_points(cls, map_name: str) -> Dict:
        """Get spawn points for the specified map"""
        if map_name not in cls.MAPS:
            raise ValueError(f"Map '{map_name}' not found")
        return cls.MAPS[map_name]["spawn_points"]
    
    @classmethod
    def get_map_size(cls, map_name: str) -> tuple:
        """Get the size of the specified map"""
        if map_name not in cls.MAPS:
            raise ValueError(f"Map '{map_name}' not found")
        return cls.MAPS[map_name]["size"] 