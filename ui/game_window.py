import pygame
import sys
from typing import Optional, Tuple
from game.map import GameMap
from .map_renderer import MapRenderer
from .colors import Colors

class GameWindow:
    def __init__(self, title: str = "Script Game Engine"):
        pygame.init()
        pygame.display.set_caption(title)
        
        # Initialize display
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        
        # Game state
        self.game_map: Optional[GameMap] = None
        self.map_renderer: Optional[MapRenderer] = None
        self.map_offset: Tuple[int, int] = (0, 0)
        
    def load_map(self, map_name: str) -> None:
        """Load a new map"""
        self.game_map = GameMap(map_name)
        self.map_renderer = MapRenderer(self.game_map)
        
        # Center the map on screen
        self.map_offset = (
            (self.screen_size[0] - self.map_renderer.width) // 2,
            (self.screen_size[1] - self.map_renderer.height) // 2
        )
    
    def handle_events(self) -> bool:
        """Handle pygame events. Returns False if the game should quit"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.VIDEORESIZE:
                self.screen_size = (event.w, event.h)
                self.screen = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
                if self.map_renderer:
                    # Recenter map
                    self.map_offset = (
                        (self.screen_size[0] - self.map_renderer.width) // 2,
                        (self.screen_size[1] - self.map_renderer.height) // 2
                    )
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.map_renderer:
                    # Adjust mouse position by map offset
                    mouse_pos = (
                        event.pos[0] - self.map_offset[0],
                        event.pos[1] - self.map_offset[1]
                    )
                    grid_pos = self.map_renderer.screen_to_grid(mouse_pos)
                    if grid_pos:
                        print(f"Clicked cell: {grid_pos}")
                        terrain = self.game_map.get_terrain_at(grid_pos)
                        print(f"Terrain: {terrain}")
        return True
    
    def render(self) -> None:
        """Render the game window"""
        # Clear screen
        self.screen.fill(Colors.BACKGROUND)
        
        # Render map if loaded
        if self.map_renderer and self.game_map:
            self.map_renderer.render(self.screen, self.map_offset)
        
        # Update display
        pygame.display.flip()
    
    def run(self) -> None:
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.render()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit() 