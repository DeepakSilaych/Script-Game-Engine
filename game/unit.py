from enum import Enum
from typing import Tuple, Dict, Optional, List
from dataclasses import dataclass

class UnitType(Enum):
    INFANTRY = "infantry"
    CAVALRY = "cavalry"
    ARCHER = "archer"
    SIEGE = "siege"
    NAVAL = "naval"
    AIRCRAFT = "aircraft"

@dataclass
class UnitStats:
    """Base stats for each unit type"""
    health: int
    attack: int
    defense: int
    movement: int
    range: Tuple[int, int]  # (min_range, max_range)
    vision: int
    cost: Dict[str, int]

class UnitStatistics:
    """Defines base statistics for all unit types"""
    
    BASE_STATS = {
        UnitType.INFANTRY: UnitStats(
            health=100,
            attack=10,
            defense=10,
            movement=2,
            range=(1, 1),
            vision=3,
            cost={"gold": 100, "food": 50}
        ),
        UnitType.CAVALRY: UnitStats(
            health=120,
            attack=15,
            defense=8,
            movement=4,
            range=(1, 1),
            vision=4,
            cost={"gold": 200, "food": 75}
        ),
        UnitType.ARCHER: UnitStats(
            health=80,
            attack=12,
            defense=5,
            movement=2,
            range=(2, 4),
            vision=5,
            cost={"gold": 150, "food": 50}
        ),
        UnitType.SIEGE: UnitStats(
            health=150,
            attack=20,
            defense=15,
            movement=1,
            range=(2, 5),
            vision=2,
            cost={"gold": 300, "wood": 100, "iron": 50}
        ),
        UnitType.NAVAL: UnitStats(
            health=200,
            attack=15,
            defense=12,
            movement=3,
            range=(1, 3),
            vision=4,
            cost={"gold": 250, "wood": 150}
        ),
        UnitType.AIRCRAFT: UnitStats(
            health=100,
            attack=15,
            defense=5,
            movement=5,
            range=(1, 4),
            vision=6,
            cost={"gold": 300, "iron": 100}
        )
    }

class UnitStatus(Enum):
    READY = "ready"
    MOVED = "moved"
    ATTACKED = "attacked"
    EXHAUSTED = "exhausted"
    DEAD = "dead"

class Unit:
    def __init__(self, unit_id: str, unit_type: UnitType, player_id: str, position: Tuple[int, int]):
        self.unit_id = unit_id
        self.unit_type = unit_type
        self.player_id = player_id
        self.position = position
        
        # Get base stats from UnitStatistics
        base_stats = UnitStatistics.BASE_STATS[unit_type]
        self.max_health = base_stats.health
        self.health = self.max_health
        self.attack = base_stats.attack
        self.defense = base_stats.defense
        self.movement = base_stats.movement
        self.range = base_stats.range
        self.vision = base_stats.vision
        
        # Additional attributes
        self.status = UnitStatus.READY
        self.experience = 0
        self.level = 1
        self.buffs: List[Dict] = []
        self.debuffs: List[Dict] = []

    def take_damage(self, damage: int) -> None:
        """Apply damage to the unit, considering defense"""
        actual_damage = max(0, damage - self.get_total_defense())
        self.health = max(0, self.health - actual_damage)
        if self.health == 0:
            self.status = UnitStatus.DEAD

    def heal(self, amount: int) -> None:
        """Heal the unit by the specified amount"""
        if self.status != UnitStatus.DEAD:
            self.health = min(self.max_health, self.health + amount)

    def can_attack(self, target_position: Tuple[int, int]) -> bool:
        """Check if the unit can attack the target position"""
        if self.status in [UnitStatus.ATTACKED, UnitStatus.EXHAUSTED, UnitStatus.DEAD]:
            return False
            
        distance = self._calculate_distance(target_position)
        min_range, max_range = self.range
        return min_range <= distance <= max_range

    def can_move(self) -> bool:
        """Check if the unit can move"""
        return self.status == UnitStatus.READY

    def get_total_attack(self) -> int:
        """Calculate total attack including buffs/debuffs"""
        base_attack = self.attack
        buff_multiplier = 1.0
        
        for buff in self.buffs:
            if buff.get("attribute") == "attack":
                buff_multiplier += buff.get("value", 0)
                
        for debuff in self.debuffs:
            if debuff.get("attribute") == "attack":
                buff_multiplier -= debuff.get("value", 0)
                
        return int(base_attack * max(0.1, buff_multiplier))

    def get_total_defense(self) -> int:
        """Calculate total defense including buffs/debuffs"""
        base_defense = self.defense
        buff_multiplier = 1.0
        
        for buff in self.buffs:
            if buff.get("attribute") == "defense":
                buff_multiplier += buff.get("value", 0)
                
        for debuff in self.debuffs:
            if debuff.get("attribute") == "defense":
                buff_multiplier -= debuff.get("value", 0)
                
        return int(base_defense * max(0.1, buff_multiplier))

    def add_buff(self, buff: Dict) -> None:
        """Add a buff to the unit"""
        self.buffs.append(buff)

    def add_debuff(self, debuff: Dict) -> None:
        """Add a debuff to the unit"""
        self.debuffs.append(debuff)

    def clear_status(self) -> None:
        """Reset unit status for new turn"""
        if self.status != UnitStatus.DEAD:
            self.status = UnitStatus.READY
            
    def _calculate_distance(self, target_position: Tuple[int, int]) -> int:
        """Calculate Manhattan distance to target position"""
        x1, y1 = self.position
        x2, y2 = target_position
        return abs(x2 - x1) + abs(y2 - y1)

    def to_dict(self) -> Dict:
        """Convert unit to dictionary representation"""
        return {
            'unit_id': self.unit_id,
            'unit_type': self.unit_type.value,
            'player_id': self.player_id,
            'position': self.position,
            'health': self.health,
            'max_health': self.max_health,
            'attack': self.get_total_attack(),
            'defense': self.get_total_defense(),
            'movement': self.movement,
            'range': self.range,
            'vision': self.vision,
            'status': self.status.value,
            'level': self.level,
            'experience': self.experience
        } 
    
class TerrainType(Enum):
    LAND = "land"
    WATER = "water"
    MOUNTAIN = "mountain"
    FOREST = "forest"
    AIR = "air"