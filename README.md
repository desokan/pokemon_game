# Pokemon

## Core Objectives

Learn API Interaction: Gain hands-on experience working with an API (specifically PokéAPI) in Python.
Build a Game: Create a game using Python where the game data is sourced from an API.

## Project Guidelines

Teamwork: Work in groups of 2-3 to build a single game.
API Usage: Utilize the PokéAPI to obtain Pokémon data for your game.
Pokémon Selection: At least the CPU's Pokémon should be randomly selected, while the player can choose or have a random Pokémon.
Game Mechanics: Implement a battle system where Pokémon fight, and a winner is determined.
Focus: Prioritize API interaction over complex game graphics or Pygame integration.
Creativity: Explore incorporating various Pokémon abilities, stats, or other unique features into the game.
Collaboration: Use Git to manage your project collaboratively in a shared repository.

## Starter Code

```py
import requests
import json

# Get the list of Pokémon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a Pokémon
print('Enter your pokemon:')

# get the user's choice
choice = input().lower()

# Get the Pokémon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# To get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# To format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the Pokémon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {} kgs'.format(weight_formatted))
print('Height: {} m'.format(height_formatted))
print('Ability: {}'.format(ability['name']))
```
