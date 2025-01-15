from typing import Dict, Any

class GameConfig:
    DEFAULT_CONFIG = {
        "map_size": {
            "width": 10,
            "height": 10
        },
        "starting_resources": {
            "gold": 1000,
            "wood": 500,
            "iron": 300,
            "food": 800
        },
        "unit_costs": {
            "infantry": {"gold": 100, "food": 50},
            "cavalry": {"gold": 200, "food": 75},
            "archer": {"gold": 150, "food": 50},
            "siege": {"gold": 300, "wood": 100, "iron": 50}
        },
        "turn_timeout": 30  # seconds
    }
    
    def __init__(self, custom_config: Dict[str, Any] = None):
        self.config = self.DEFAULT_CONFIG.copy()
        if custom_config:
            self._update_config(custom_config)
            
    def _update_config(self, custom_config: Dict[str, Any]) -> None:
        for key, value in custom_config.items():
            if isinstance(value, dict) and key in self.config:
                self.config[key].update(value)
            else:
                self.config[key] = value
                
    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default) 