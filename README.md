# Space Invaders

A compact Space Invaders clone built with Pygame. The project focuses on classic arcade gameplay: enemy waves, player shields, bullet management, and a lightweight HUD.

## Requirements
- Python 3.10+
- [Pygame](https://www.pygame.org/) 2.5+ (install with `pip install pygame`)

## Installation & Run
1. (Optional) create a virtualenv: `python -m venv .venv` and activate it.
2. Install dependencies: `pip install pygame`.
3. Start the game: `python main.py`.

## Controls
- `W`, `A`, `S`, `D` — move the ship
- `SPACE` — shoot
- `ESC` or closing the window — exit the game

## Project Structure
- `main.py` — entry point and game loop setup
- `settings.py` — window size, colors, speeds, and other constants
- `entities/` — player, enemies, bullets, and cover logic
- `effects/` — HUD, collisions, starfield background, and game-over screen
- `assets/` — sprite assets used by the game
![alt text](assets/image.png)