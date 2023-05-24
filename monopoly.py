import random


def play_round(player_spot, data):
    go = True
    amount_double = 0
    while go == True:
        amount_double += 1

        if amount_double == 3:
            data, player_spot = jail(data, player_spot)

        amount_roll, go = die_roll()

        player_spot += amount_roll

        while player_spot + 1 > len(data):
            player_spot -= len(data)

        data[list(data.keys())[player_spot]] += 1

        if list(data.keys())[player_spot] == "Chance":
            chance = get_chance()
            if chance == "Jail":
                data, player_spot = jail(data, player_spot)
            else:
                if not isinstance(chance, int):
                    player_spot = list(data.keys()).index(chance)
                else:
                    player_spot += chance
            if chance != 0:
                data[list(data.keys())[player_spot]] += 1
        elif list(data.keys())[player_spot] == "Community Chest":
            chest = get_chest()
            if chest == "Jail":
                data, player_spot = jail(data, player_spot)
            else:
                if not isinstance(chest, int):
                    player_spot = list(data.keys()).index(chest)
                else:
                    player_spot += chest
            if chest != 0:
                data[list(data.keys())[player_spot]] += 1
        elif list(data.keys())[player_spot] == "Go To Jail":
            jail(data, player_spot)

    return player_spot, data


def die_roll():
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    return (first + second), (first == second)


def jail(data, player_spot):
    data["Jail"] += 3
    player_spot = list(data.keys()).index("Jail")
    return data, player_spot


def get_chance():
    chance_cards = [
        "Go",
        "Illinois Avenue",
        "St. Charles Place",
        "UTILITY",
        "RAILROAD",
        0,
        0,
        -3,
        "Jail",
        0,
        0,
        "Reading Railroad",
        "Boardwalk",
        0,
        0,
        0
    ]

    choice = random.choice(chance_cards)

    if choice == "UTILITY":
        return random.choice(["Electric Company", "Water Works"])
    elif choice == "RAILROAD":
        return random.choice(["Reading Railroad", "Pennsylvania Railroad", "B. & O. Railroad", "Short Line"])
    else:
        return choice


def get_chest():
    chest_cards = [
        "Go",
        0,
        0,
        0,
        0,
        "Jail",
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ]

    return random.choice(chest_cards)


def get_fields():
    return {
        "Go": 0,
        "Mediterranean Avenue": 0,
        "Community Chest": 0,
        "Baltic Avenue": 0,
        "Income Tax": 0,
        "Reading Railroad": 0,
        "Oriental Avenue": 0,
        "Chance": 0,
        "Vermont Avenue": 0,
        "Connecticut Avenue": 0,
        "Jail": 0,
        "St. Charles Place": 0,
        "Electric Company": 0,
        "States Avenue": 0,
        "Virginia Avenue": 0,
        "Pennsylvania Railroad": 0,
        "St. James Place": 0,
        "Community Chest": 0,
        "Tennessee Avenue": 0,
        "New York Avenue": 0,
        "Free Parking": 0,
        "Kentucky Avenue": 0,
        "Chance": 0,
        "Indiana Avenue": 0,
        "Illinois Avenue": 0,
        "B. & O. Railroad": 0,
        "Atlantic Avenue": 0,
        "Ventnor Avenue": 0,
        "Water Works": 0,
        "Marvin Gardens": 0,
        "Go To Jail": 0,
        "Pacific Avenue": 0,
        "North Carolina Avenue": 0,
        "Community Chest": 0,
        "Pennsylvania Avenue": 0,
        "Short Line": 0,
        "Chance": 0,
        "Park Place": 0,
        "Luxury Tax": 0,
        "Boardwalk": 0
    }
