# Script-Game-Engine

A Python-based game engine for a script-driven army building game. Players write scripts to control their armies in turn-based battles.

## Features

- Turn-based strategy game engine
- Script-driven unit control
- Multiple unit types (Infantry, Cavalry, Archers, etc.)
- Resource management
- Dynamic battle map with various terrain types

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

## Running Tests

```bash
pytest
```

## Project Structure

- `game/`: Core game logic and components
- `scripts/`: Script parsing and execution
- `ui/`: User interface components
- `tests/`: Unit and integration tests
- `assets/`: Game assets
- `utils/`: Utility functions

## License

MIT License - See LICENSE file for details
