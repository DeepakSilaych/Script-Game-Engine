# Script-Game-Engine

A Python-based game engine for a script-driven army building game. Players write scripts to control their armies in turn-based 1v1 battles.

## Game Overview

This is a strategic army building game where players:
- Build and manage armies with different unit types
- Write battle scripts to control unit actions
- Manage resources (Gold, Wood, Iron, Food)
- Battle on diverse terrain types
- Compete in 1v1 turn-based matches

### Unit Types
- Infantry: Versatile ground units
- Cavalry: Fast-moving units for flanking
- Archers: Ranged units with long attack range
- Siege Machines: Heavy units for destroying fortifications
- Naval Units: Water-based units
- Aircraft: Mobile airborne units

### Terrain Types
- Land: Standard terrain for ground units
- Waterways: Rivers and seas for naval units
- Airways: Open spaces for flying units
- Mountains: Provides high ground advantage
- Forests: Offers cover and stealth

## Features

- Turn-based strategy game engine
- Script-driven unit control system
- Dynamic battle map (10x10 grid)
- Resource management system
- Multiple unit types with unique abilities
- Diverse terrain effects
- Real-time battle visualization

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Unix/MacOS: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the game:
```bash
python main.py
```

2. Write your battle script following this format:
```python
# Example battle script
if enemy_in_range:
    attack_enemy_infantry
if unit_health < 50:
    retreat_to_base
```

3. Submit your script and watch the battle unfold!

## Project Structure

- `docs/`: Documentation and game concepts
  - `concept.md`: Detailed game mechanics
  - `architecture.md`: Technical architecture
- `game/`: Core game logic
  - `game_state.py`: Game state management
  - `map.py`: Battle map implementation
  - `unit.py`: Unit type definitions
- `ui/`: User interface components
  - `game_window.py`: Main game window
  - `map_renderer.py`: Map visualization
  - `colors.py`: UI color schemes
- `tests/`: Unit and integration tests
- `assets/`: Game assets
- `utils/`: Utility functions

## Running Tests

```bash
pytest
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - See LICENSE file for details
