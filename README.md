# pcg-spawn-alerts
Monitors Pokémon Community Game (PCG) Pokémon spawns and sends Discord alerts for desired Pokémon.

## Configuration
1. Open the `config.py` file.
2. Replace the placeholder webhook URL with your **Discord webhook URL**:
```python
webhook_url = "DISCORD_WEBHOOK_URL"
```
3. Add the Pokémon you want alerts for using their Pokédex IDs:
```python
pokemon_watchlist = {6, 384, 493}  # Example: Charizard, Rayquaza, Arceus
```
- You can add or remove IDs depending on which Pokémon you want alerts for.

## Usage
Run the script with:
```bash
python alerts.py
```
- The script will continuously monitor spawns and send alerts for the Pokémon in your watchlist.
- Press Ctrl+C to stop the script.
