# Variables can be updated or reassigned as the program runs.
# The '=' sign assigns a new value to the existing 'box'.
player_health = 100
player_health = player_health - 25  # Damage from monster
player_health = player_health + 10  # Healing from potion

print(f"After the battle and a potion, your final health is: {player_health}")
