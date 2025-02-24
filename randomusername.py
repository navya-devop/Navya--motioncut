import random


adjectives = ["Awesome", "Bold", "Creative", "Daring", "Epic", "Fearless", "Gaming", "Heroic", "Incredible", "Jawdropping", "Kooky", "Legendary", "Maverick", "Nimble", "Optimistic", "Pioneering", "Quirky", "Radical", "Savvy", "Tenacious", "Unstoppable", "Visionary", "Witty", "Xtreme", "Yearning", "Zesty"]

# List of nouns
nouns = ["Ace", "Blaze", "Cosmos", "Dynamo", "Eclipse", "Flare", "Galaxy", "Havoc", "Ignite", "Jolt", "Kairos", "Luminary", "Maelstrom", "Nemesis", "Oasis", "Pulse", "Quake", "Rampage", "Specter", "Tornado", "Uprising", "Vortex", "Wave", "Xfactor", "Yonder", "Zephyr"]

# List of suffixes
suffixes = ["", "_Master", "_Pro", "_Legend", "_Xtreme", "_Gamer", "_Warrior", "_Hero", "_Champion"]

# List of special characters
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-"]

def generate_username(length=None, structure=None, include_numbers=True, include_special_chars=True):
    username = ""
    
    if structure:
        for part in structure:
            if part == "adjective":
                username += random.choice(adjectives)
            elif part == "noun":
                username += random.choice(nouns)
            elif part == "suffix":
                username += random.choice(suffixes)
            elif part == "number":
                username += str(random.randint(0, 9))
            elif part == "special_char":
                username += random.choice(special_chars)
    else:
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        suffix = random.choice(suffixes)
        username = f"{adjective}{noun}{suffix}"
    
    if include_numbers:
        username += str(random.randint(0, 9))
    
    if include_special_chars:
        username += random.choice(special_chars)
    
    if length and len(username) > length:
        username = username[:length]
    
    return username

def main():
    print("Random user name generator")
    print("-----------------------------------------")
    num_usernames = int(input("How many usernames would you like to generate? "))
    
    include_numbers = input("Include numbers in the usernames? (yes/no): ")
    include_numbers = include_numbers.lower() == "yes"
    
    include_special_chars = input("Include special characters in the usernames? (yes/no): ")
    include_special_chars = include_special_chars.lower() == "yes"
    
    length = input("Set a specific length for the usernames? (enter a number or leave blank): ")
    length = int(length) if length else None
    
    structure = input("Set a specific structure for the usernames? (e.g. 'adjective-noun-suffix' or leave blank): ")
    structure = structure.split("-") if structure else None
    
    for i in range(num_usernames):
        username = generate_username(length, structure, include_numbers, include_special_chars)
        print(f"Username {i+1}: {username}")

if __name__ == "__main__":
    main()

