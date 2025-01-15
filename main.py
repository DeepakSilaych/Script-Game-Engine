from ui.game_window import GameWindow
from utils.logger import GameLogger

logger = GameLogger(__name__)

def main():
    try:
        # Create game window
        window = GameWindow("Script Game Engine - Map Viewer")
        
        # Load initial map
        logger.info("Loading map: small_duel")
        window.load_map("small_duel")
        
        # Start game loop
        logger.info("Starting game loop")
        window.run()
        
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        raise

if __name__ == "__main__":
    main() 