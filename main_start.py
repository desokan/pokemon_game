from sys import *

from get_pokemon_data import *
from display_pokemon_stats import *
from get_random_pokemon_name import *
from battle import *

arguments = argv[1:]

# Main game loop
def main():
    print("Welcome to the Pokémon Battle Game!\n")

    # Step 1: Player chooses a Pokémon
    while True:
        # player_choice = input("Enter the name of your Pokémon: ").strip()
        player_choice = arguments[0]
        player_pokemon = get_pokemon_data(player_choice)
        if player_pokemon:
            break
        print("Invalid Pokémon name. Please try again.")

    # Display player's Pokémon stats
    display_pokemon_stats(player_pokemon)

    # Step 2: CPU selects a random Pokémon
    cpu_choice = get_random_pokemon_name()
    cpu_pokemon = get_pokemon_data(cpu_choice)

    print(f"The CPU has chosen {cpu_pokemon['name'].capitalize()}!")
    display_pokemon_stats(cpu_pokemon)

    # Step 3: Battle
    print("The battle begins!")
    battle(player_pokemon, cpu_pokemon)

# Run the game
if __name__ == "__main__":
    main()