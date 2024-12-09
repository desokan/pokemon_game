# Function to display Pokémon stats
def display_pokemon_stats(pokemon_data):
    name = pokemon_data['name'].capitalize()
    height = pokemon_data['height'] / 10  # Convert decimetres to metres
    weight = pokemon_data['weight'] / 10  # Convert hectograms to kilograms
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]

    print(f"\n{name}'s Stats:")
    print(f"Height: {height} m")
    print(f"Weight: {weight} kg")
    print(f"Abilities: {', '.join(abilities)}\n")