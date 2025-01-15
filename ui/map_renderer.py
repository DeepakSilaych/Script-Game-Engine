import pygame
from typing import Tuple, Optional
from game.map import GameMap, TerrainType
from .colors import Colors

class MapRenderer:
    def __init__(self, game_map: GameMap, cell_size: int = 60):
        self.game_map = game_map
        self.cell_size = cell_size
        self.width = game_map.width * cell_size
        self.height = game_map.height * cell_size
        
        # Create surface for the map
        self.surface = pygame.Surface((self.width, self.height))
        
    def get_cell_rect(self, x: int, y: int) -> pygame.Rect:
        """Get the rectangle for a cell position"""
        return pygame.Rect(
            x * self.cell_size,
            y * self.cell_size,
            self.cell_size,
            self.cell_size
        )
    
    def get_terrain_color(self, terrain: TerrainType) -> Tuple[int, int, int]:
        """Get color for terrain type"""
        return {
            TerrainType.LAND: Colors.LAND,
            TerrainType.WATER: Colors.WATER,
            TerrainType.MOUNTAIN: Colors.MOUNTAIN,
            TerrainType.FOREST: Colors.FOREST,
            TerrainType.AIR: Colors.AIR
        }[terrain]
    
    def screen_to_grid(self, screen_pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        """Convert screen coordinates to grid coordinates"""
        x, y = screen_pos
        grid_x = x // self.cell_size
        grid_y = y // self.cell_size
        
        if 0 <= grid_x < self.game_map.width and 0 <= grid_y < self.game_map.height:
            return (grid_x, grid_y)
        return None
    
    def render(self, surface: pygame.Surface, offset: Tuple[int, int] = (0, 0)) -> None:
        """Render the map to the given surface"""
        # Clear the surface
        self.surface.fill(Colors.BACKGROUND)
        
        # Draw terrain
        for y in range(self.game_map.height):
            for x in range(self.game_map.width):
                cell_rect = self.get_cell_rect(x, y)
                terrain = self.game_map.get_terrain_at((x, y))
                color = self.get_terrain_color(terrain)
                
                # Draw terrain cell
                pygame.draw.rect(self.surface, color, cell_rect)
                # Draw grid lines
                pygame.draw.rect(self.surface, Colors.GRID, cell_rect, 1)
        
        # Draw spawn points
        for player_id, spawn_points in self.game_map.spawn_points.items():
            color = Colors.PLAYER1 if player_id == "player1" else Colors.PLAYER2
            for x, y in spawn_points:
                cell_rect = self.get_cell_rect(x, y)
                # Draw spawn point indicator (circle)
                pygame.draw.circle(
                    self.surface,
                    color,
                    (cell_rect.centerx, cell_rect.centery),
                    self.cell_size // 4
                )
        
        # Blit the map surface to the main surface
        surface.blit(self.surface, offset) 