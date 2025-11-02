import requests
import time
import config


def get_pokemon_dictionary(watchlist_ids: set) -> dict | None:
    """
    Fetches names of Pokémon from PokeAPI and creates a dictionary
    of watchlisted Pokémon IDs and names.
    """
    watchlist_names = {}
    
    url = "https://pokeapi.co/api/v2/pokemon/?limit=100000"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        pokemon_data = response.json()

        for pokemon in pokemon_data["results"]:
            url_parts = pokemon["url"].split("/")
            pokedex_id = int(url_parts[-2])

            if pokedex_id in watchlist_ids:
                watchlist_names[pokedex_id] = pokemon["name"].title()

        return watchlist_names

    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error fetching Pokémon data: {e}.")
        return None


def main():
    spawn_url = "https://poketwitch.bframework.de/info/events/last_spawn/"
    webhook_url = config.webhook_url
    watchlist_ids = config.pokemon_watchlist

    watchlist_names = None
    while watchlist_names is None:
        watchlist_names = get_pokemon_dictionary(watchlist_ids)
        if watchlist_names is None:
            print("Failed to get data. Retrying in 3 seconds...")
            time.sleep(3)

    print("Initialized successfully.")

    previous_spawn = None
    while True:
        try:
            response = requests.get(spawn_url, timeout=10)
            response.raise_for_status()

            spawn_data = response.json()
            pokedex_id = spawn_data["order"]

            #Check if spawn data has been updated
            if pokedex_id == previous_spawn:
                time.sleep(1)
                continue

            if pokedex_id in watchlist_ids:
                response = requests.post(
                    webhook_url,
                    json={"content": f"{watchlist_names[pokedex_id]} Spawn"},
                    timeout=10,
                )
                response.raise_for_status()
                print(f"Alert sent for {watchlist_names[pokedex_id]}.")

            previous_spawn = pokedex_id
            # 3 second delay to give site time to update data for new spawn
            time.sleep(spawn_data["next_spawn"] + 3)

        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}. Retrying in 3 seconds...")
            time.sleep(3)
        except (KeyError, ValueError) as e:
            print(f"Error processing API response: {e}. Retrying in 1 second...")
            time.sleep(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Retrying in 1 second...")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopping...")
