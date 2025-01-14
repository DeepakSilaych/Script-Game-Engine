### **Army Building Game Ideation**

This **Army Building Game** involves constructing and managing an army, strategizing the use of resources, and engaging in battles. Users will create a **battle script** for a 1v1 match, where each turn involves specifying conditions, actions, and effects based on predefined options.

---

### **Core Concepts**

1. **Terrains**: The game map is composed of various terrains, each with specific properties.
   - **Land**: Regular ground where most units move freely.
   - **Waterways**: Areas like rivers, lakes, and seas where only water-based units can move.
   - **Airways**: Open air regions where air units (e.g., aircraft) can fly.
   - **Mountains**: Difficult terrain that impedes movement and can provide high ground for ranged units.
   - **Forests**: Provide cover but slow down movement; can hide units from sight.

2. **Resources**: Players collect resources to build and upgrade their army.
   - **Gold**: Used to train units and upgrade facilities.
   - **Wood**: Needed for constructing buildings and fortifications.
   - **Iron**: Used for weapons and armor upgrades.
   - **Food**: Required to maintain an army’s morale and support growth.

3. **Army Units**: Players can build different types of units to form an army.
   - **Infantry**: Ground units that are versatile but vulnerable to air and ranged attacks.
   - **Cavalry**: Fast-moving units that excel at flanking and fast strikes.
   - **Archers**: Ranged units with long attack range but low defense.
   - **Siege Machines**: Heavy, slow units designed for destroying fortifications and strongholds.
   - **Naval Units**: Ships and boats that operate in waterways.
   - **Aircraft**: Airborne units for fast strikes and surveillance.

4. **Battle Mechanics**:
   - Players engage in combat using a predefined set of moves in a 1v1 battle.
   - Units move across the terrain, attacking, defending, and interacting with the environment.
   - Each player submits a script to determine their actions in each turn.
   
5. **Match Format**: 1v1 combat where players command their army on a grid-based map with a time limit per turn.

---

### **Game Design Breakdown**

#### **1. Terrain Features**
| Terrain Type   | Properties                                | Movement Rules                                        | Effects                                  |
|----------------|-------------------------------------------|-------------------------------------------------------|------------------------------------------|
| **Land**       | Normal terrain, varied for map design.    | All units can move here.                              | Neutral terrain for all unit types.      |
| **Waterways**  | Rivers, lakes, seas.                      | Only naval units can move here.                       | Impedes ground units; enhances naval units. |
| **Airways**    | Open air spaces for flying units.         | Only airborne units can move here.                    | Air units move freely.                   |
| **Mountains**  | Steep, rocky regions.                     | Slows down movement for all but air units.             | Provides high ground for ranged units, gives vision advantage. |
| **Forests**    | Wooded regions with dense trees.          | Slows ground units' movement; air units are unaffected. | Conceals units, granting stealth.        |

---

#### **2. Resources and Buildings**
| Resource Type | Description                                         | Use Case                          |
|---------------|-----------------------------------------------------|-----------------------------------|
| **Gold**      | Main resource for unit production and upgrades.    | Build units, upgrade structures. |
| **Wood**      | Required for constructing buildings and fortifications. | Build fortifications and defensive structures. |
| **Iron**      | Used for crafting weapons and armor.               | Upgrade units, build siege machines. |
| **Food**      | Maintains the morale of the army and growth.        | Necessary for army upkeep.       |

---

#### **3. Unit Types and Stats**
| Unit Type     | Movement Type    | Attack Type      | Defense Type   | Cost (Resources) | Special Abilities                  |
|---------------|------------------|------------------|----------------|------------------|-------------------------------------|
| **Infantry**  | Ground (Land)    | Melee (Short Range) | Medium Armor   | Gold, Wood, Food | Standard unit, versatile.          |
| **Cavalry**   | Ground (Land)    | Melee (Short Range) | Light Armor    | Gold, Wood, Food | High speed, can flank.             |
| **Archers**   | Ground (Land)    | Ranged (Long Range) | Light Armor    | Gold, Wood, Food | High attack range, vulnerable to melee. |
| **Siege**     | Ground (Land)    | Ranged (Long Range) | Heavy Armor    | Gold, Iron, Wood | Slow but effective against structures. |
| **Naval**     | Waterways        | Melee/Ranged (varies) | Medium Armor   | Gold, Iron, Food | Specialized for water combat.      |
| **Aircraft**  | Airways          | Ranged (Long Range) | Light Armor    | Gold, Iron, Food | High mobility, weak defense.       |

---

#### **4. Script Actions, Conditions, and Effects**
Users will provide a script containing **conditions**, **actions**, and **effects** that control their army in battle. 

##### **Script Structure**
1. **Condition**: Defines when an action should take place.
   - **Example**: If an enemy unit is within range of my archers.
   - **Example**: If my infantry is below 50% health.

2. **Action**: Defines the move or attack that the unit performs.
   - **Example**: Move forward.
   - **Example**: Attack enemy unit.

3. **Effect**: Defines the consequence of the action (e.g., damage, movement, buff).
   - **Example**: Deal 20 damage to the enemy infantry.
   - **Example**: Heal my cavalry by 10 health.

##### **Example Turn (Script)**
| Turn # | Condition                                    | Action                                    | Effect                                              |
|--------|----------------------------------------------|-------------------------------------------|-----------------------------------------------------|
| 1      | If my archers are within range of enemy      | Attack enemy infantry                     | Deal 25 damage to enemy infantry                    |
| 2      | If my cavalry is near a mountain             | Move towards the mountain for cover       | Move cavalry to (5, 5), gain defensive bonus.       |
| 3      | If my siege machine is within range of enemy fortress | Attack enemy fortress                     | Deal 50 damage to enemy fortress.                   |
| 4      | If my infantry health is less than 50%       | Retreat to nearest friendly fort          | Move infantry to (7, 6) and heal 10 HP.             |

---

### **Game Phases**

1. **Building Phase** (Pre-Battle):
   - Players gather resources.
   - Players construct buildings (e.g., barracks, siege workshops).
   - Players train units (e.g., infantry, cavalry, archers, etc.).

2. **Movement & Battle Phase** (In-Game):
   - Each player moves and battles based on their script.
   - Players decide the movement and attack strategies.
   - The game engine calculates the results of each turn based on the predefined conditions and effects in the scripts.

3. **End Game**:
   - The game ends when:
     - One player eliminates the other’s army.
     - A player’s base or main unit is destroyed.
   - Players are scored based on:
     - Efficiency of resource use.
     - Number of units surviving.
     - Number of successful attacks.

---

### **Battle Mechanics Breakdown**
| Unit Type     | Movement Speed | Attack Speed | Range (if applicable) | Special Effects |
|---------------|----------------|--------------|-----------------------|-----------------|
| **Infantry**  | 1 tile/turn    | 1 attack/turn | Melee                 | Standard attack |
| **Cavalry**   | 2 tiles/turn   | 1 attack/turn | Melee                 | Flank bonus     |
| **Archers**   | 1 tile/turn    | 1 attack/turn | 3-5 tiles             | High range, low defense |
| **Siege**     | 1 tile/turn    | 1 attack/turn | 5-8 tiles             | Strong against buildings |
| **Naval**     | 1-2 tiles/turn | 1 attack/turn | Melee, Ranged         | Can only move in waterways |
| **Aircraft**  | 3 tiles/turn   | 1 attack/turn | 5-10 tiles            | High mobility, weak defense |

---

### **Example Game Setup**
1. **Map**: A 10x10 grid with:
   - Land in the center.
   - Waterways on the sides.
   - Forests scattered around the center.
   - Mountains placed near the corners.

2. **Player 1**: 
   - Start in the top left corner.
   - Has an army of infantry, archers, and siege units.

3. **Player 2**: 
   - Start in the bottom right corner.
   - Has an army of cavalry, naval units, and aircraft.

---

### **Gameplay Constraints and Rules**
1. **Turn Time Limit**: Each player has 30 seconds per turn to submit their script.
2. **Resource Management**: Players must gather resources and manage them to maintain their army.
3. **Victory Conditions**: Eliminate the opponent’s army or destroy their main base.
4. **Battle Environment

**: Terrain and resources influence the outcome of the battle (e.g., forests provide stealth for infantry, mountains offer high ground for archers).

---

This ideation sets the groundwork for a dynamic and strategic army-building game where players must adapt to different terrains, manage resources, and carefully script their moves for success.