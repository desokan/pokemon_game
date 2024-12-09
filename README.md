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

## List Comprehension

```json => Example Data
pokemon_data = {
    "abilities": [
        {
            "ability": {"name": "static", "url": "https://pokeapi.co/api/v2/ability/9/"},
            "is_hidden": False,
            "slot": 1
        },
        {
            "ability": {"name": "lightning-rod", "url": "https://pokeapi.co/api/v2/ability/31/"},
            "is_hidden": True,
            "slot": 3
        }
    ]
}
```

1. pokemon_data['abilities']:

   - Extract the list of abilities from the Pokémon data.

   ```python => Output
   [
       {
           "ability": {"name": "static", "url": "https://pokeapi.co/api/v2/ability/9/"},
           "is_hidden": False,
           "slot": 1
       },
       {
           "ability": {"name": "lightning-rod", "url": "https://pokeapi.co/api/v2/ability/31/"},
           "is_hidden": True,
           "slot": 3
       }
   ]
   ```

2. Iterating with for ability in pokemon_data['abilities']:

   - Each ability is one dictionary from the abilities list.

   ```python => First iteration
   {
       "ability": {"name": "static", "url": "https://pokeapi.co/api/v2/ability/9/"},
       "is_hidden": False,
       "slot": 1
   }
   ```

   ```python => Second iteration
   {
       "ability": {"name": "lightning-rod", "url": "https://pokeapi.co/api/v2/ability/31/"},
       "is_hidden": True,
       "slot": 3
   }
   ```

3. ability['ability']:

   - Access the "ability" key within each dictionary.

   ```python => First iteration
   {"name": "static", "url": "https://pokeapi.co/api/v2/ability/9/"}
   ```

   ```python => Second iteration
   {"name": "lightning-rod", "url": "https://pokeapi.co/api/v2/ability/31/"}
   ```

4. `ability['ability']['name']`

   - Extract the "name" key from the nested dictionary.

   ```python => First iteration
   "static"
   ```

   ```python => First iteration
   "lightning-rod"
   ```

5. List Comprehension:
   `abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]`

   ```py => Final output
   ["static", "lightning-rod"]
   ```

## Output

```py
Step 1: Extract the abilities list
[{'ability': {'name': 'static', 'url': 'https://pokeapi.co/api/v2/ability/9/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'lightning-rod', 'url': 'https://pokeapi.co/api/v2/ability/31/'}, 'is_hidden': True, 'slot': 3}]

Step 2: Extract each ability dictionary
{'ability': {'name': 'static', 'url': 'https://pokeapi.co/api/v2/ability/9/'}, 'is_hidden': False, 'slot': 1}
{'ability': {'name': 'lightning-rod', 'url': 'https://pokeapi.co/api/v2/ability/31/'}, 'is_hidden': True, 'slot': 3}

Step 3: Extract the 'ability' sub-dictionary
{'name': 'static', 'url': 'https://pokeapi.co/api/v2/ability/9/'}
{'name': 'lightning-rod', 'url': 'https://pokeapi.co/api/v2/ability/31/'}

Step 4: Extract the 'name' from 'ability'
static
lightning-rod

Step 5: Use list comprehension to extract all names
['static', 'lightning-rod']
```

List comprehension is a concise and elegant way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, range, or dictionary).

```python
new_list = [expression for item in iterable if condition]
```

## Components

1. expression:

   - Defines how each element in the new list should be generated.

2. for item in iterable:

   - Iterates over each element of the given iterable (like a list, range, or dictionary).

3. if condition (optional):

   - Adds a filter to include only certain elements.
