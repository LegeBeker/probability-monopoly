import random


def play_round(player_spot, data):
    die_roll = random.randint(1, 6) + random.randint(1, 6)
    player_spot += die_roll

    while player_spot + 1 > len(data):
        player_spot -= len(data)

    data[list(data.keys())[player_spot]] += 1


def get_fields():
    return {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0
    }
