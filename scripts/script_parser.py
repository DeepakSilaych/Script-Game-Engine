from typing import List, Dict, Any
from game.action import Action
from game.game_state import GameState

class ScriptParser:
    def __init__(self):
        self.valid_actions = ["move", "attack", "defend", "heal"]
        
    def parse_script(self, script_text: str) -> List[Action]:
        actions = []
        lines = script_text.strip().split('\n')
        
        for line in lines:
            if line.strip() and not line.startswith('#'):
                try:
                    action = self._parse_line(line)
                    if action:
                        actions.append(action)
                except ValueError as e:
                    print(f"Error parsing line: {line}")
                    print(f"Error: {e}")
                    
        return actions
        
    def _parse_line(self, line: str) -> Optional[Action]:
        # Basic parsing logic - to be expanded
        parts = line.split()
        if not parts or parts[0] not in self.valid_actions:
            return None
            
        action_type = parts[0]
        target = self._parse_target(parts[1:])
        
        return Action(action_type, target)
        
    def _parse_target(self, target_parts: List[str]) -> Dict[str, Any]:
        # Basic target parsing - to be expanded
        return {"raw": " ".join(target_parts)} 