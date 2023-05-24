import random


def play_round(player_spot, data):
    die_roll = random.randint(1, 6) + random.randint(1, 6)
    player_spot += die_roll

    while player_spot + 1 > len(data):
        player_spot -= len(data)

    data[list(data.keys())[player_spot]] += 1

    return player_spot, data


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
