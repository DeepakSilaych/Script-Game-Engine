import logging
from typing import Optional

class GameLogger:
    def __init__(self, name: str = "game_engine", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            
    def info(self, message: str) -> None:
        self.logger.info(message)
        
    def error(self, message: str) -> None:
        self.logger.error(message)
        
    def debug(self, message: str) -> None:
        self.logger.debug(message)
        
    def warning(self, message: str) -> None:
        self.logger.warning(message) 