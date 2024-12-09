# Battle logic: Compare height and weight to determine the winner
def battle(player_pokemon, cpu_pokemon):
    player_score = player_pokemon['height'] + player_pokemon['weight']
    cpu_score = cpu_pokemon['height'] + cpu_pokemon['weight']

    print(f"Your Pokémon: {player_pokemon['name'].capitalize()} (Score: {player_score})")
    print(f"CPU Pokémon: {cpu_pokemon['name'].capitalize()} (Score: {cpu_score})\n")

    if player_score > cpu_score:
        print("You win!")
    elif player_score < cpu_score:
        print("CPU wins!")
    else:
        print("It's a tie!")