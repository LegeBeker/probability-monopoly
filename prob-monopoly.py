import matplotlib.pyplot as plt
import numpy as np
import random

data = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
player_spot = 0


fig, ax = plt.subplots(1, figsize=(15, 5))

squares = list(data.keys())
values = list(data.values())

ax.bar(squares, values, color='maroon')

while True:
    die_roll = random.randint(1, 6) + random.randint(1, 6)
    player_spot += die_roll

    while player_spot + 1 > len(data):
        player_spot -= len(data)

    data[list(data.keys())[player_spot]] += 1

    # Bar update logic
    ax.bar(squares, data.values(), color='maroon')

    for rect, label in zip(ax.patches, data.values()):
        height = rect.get_height()

    plt.xlabel("Amount landed on square")
    plt.ylabel("Monopoly squares")
    plt.title("Land probability Monopoly")
    plt.pause(0.1)
    ax.clear()
    if not plt.get_fignums():
        break

plt.show()
