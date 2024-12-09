import requests
import random

# Function to fetch a random Pokémon name
def get_random_pokemon_name():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=100'  # Fetches the first 100 Pokémon
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_list = response.json()['results']
        return random.choice(pokemon_list)['name']
    else:
        return None