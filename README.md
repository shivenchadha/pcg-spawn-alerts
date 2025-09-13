# pcg-spawn-alerts
Monitors Pokémon Community Game (PCG) Pokémon spawns and sends Discord alerts for desired Pokémon.

## Setup
Make sure you have both `main.py` and `config.py` in the same folder before running the script.

## Configuration
1. Open the `config.py` file.
2. Replace the placeholder webhook URL with your **Discord webhook URL**:
```python
webhook_url = "YOUR_DISCORD_WEBHOOK_URL"
```
3. Add the Pokémon you want alerts for using their Pokédex IDs:
```python
pokemon_watchlist = {6, 384, 493}  # Example: Charizard, Rayquaza, Arceus
```
- You can add or remove IDs depending on which Pokémon you want alerts for.

## Usage
Run the script with:
```bash
python main.py
```
- The script will continuously monitor spawns and send alerts for the Pokémon in your watchlist.
- Press Ctrl+C to stop the script.
