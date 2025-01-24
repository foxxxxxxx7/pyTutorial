import random


def generate_room_name():
    adjectives = ["Dark", "Misty", "Enchanted", "Ancient", "Echoing"]
    nouns = ["Cave", "Forest", "Chamber", "Corridor", "Vault"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"


def generate_room_description():
    descriptions = [
        "You hear the distant drip of water echoing through the air.",
        "The walls are covered in glowing moss, casting a faint light.",
        "An eerie silence fills the room, broken only by your footsteps.",
        "You feel a chilling breeze that seems to come from nowhere.",
        "The room smells of damp earth and forgotten memories."
    ]
    return random.choice(descriptions)


def generate_directions():
    directions = ["north", "south", "east", "west"]
    random.shuffle(directions)
    return directions[:random.randint(2, 4)]


def generate_adventure():
    num_rooms = random.randint(5, 10)
    rooms = {}

    for i in range(1, num_rooms + 1):
        room_name = generate_room_name()
        room_desc = generate_room_description()
        room_exits = generate_directions()
        rooms[i] = {"name": room_name, "description": room_desc, "exits": room_exits}

    return rooms


def play_adventure(rooms):
    current_room = 1
    visited = set()

    print("Welcome to your adventure! Type 'quit' to exit.\n")

    while True:
        room = rooms[current_room]
        print(f"You are in the {room['name']}.")
        print(room["description"])
        print("Exits:", ", ".join(room["exits"]))

        visited.add(current_room)
        choice = input("Which direction would you like to go? ").strip().lower()

        if choice == "quit":
            print("Thanks for playing!")
            break
        elif choice in room["exits"]:
            # Randomly decide the next room (arbitrary for simplicity)
            next_room = random.choice(list(rooms.keys()))
            while next_room == current_room or next_room in visited:
                next_room = random.choice(list(rooms.keys()))
            current_room = next_room
        else:
            print("You can't go that way!")
        print()


# Generate and play the adventure
adventure_rooms = generate_adventure()
play_adventure(adventure_rooms)
