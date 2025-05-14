# Rikira Clay
# 04/27/2025
# P5HW_LastnameFirstname.py
# This program allows the user to create and interact with game characters using functions, loops, and dictionaries.

def create_character():
    print("\n--- Create Your Character ---")
    name = input("Enter character name: ")
    health = int(input("Enter health (0-100): "))
    strength = int(input("Enter strength (0-100): "))
    magic = int(input("Enter magic (0-100): "))
    
    character = {
        "name": name,
        "health": health,
        "strength": strength,
        "magic": magic
    }
    return character

def display_character(character):
    print("\n--- Character Stats ---")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")

def attack(attacker, defender):
    print(f"\n{attacker['name']} attacks {defender['name']}!")
    damage = attacker["strength"]
    defender["health"] -= damage
    if defender["health"] < 0:
        defender["health"] = 0
    print(f"{defender['name']} now has {defender['health']} health.")

def main():
    characters = []
    while True:
        print("\n--- Character Game Menu ---")
        print("1. Create Character")
        print("2. Display Characters")
        print("3. Attack (Player 1 attacks Player 2)")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            character = create_character()
            characters.append(character)
            print(f"{character['name']} created successfully!")
        
        elif choice == "2":
            if not characters:
                print("No characters created yet.")
            else:
                for char in characters:
                    display_character(char)

        elif choice == "3":
            if len(characters) < 2:
                print("You need at least two characters to attack.")
            else:
                attack(characters[0], characters[1])

        elif choice == "4":
            print("Exiting game. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Run the game
main()
