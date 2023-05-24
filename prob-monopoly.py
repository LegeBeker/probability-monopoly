import matplotlib.pyplot as plt
import numpy as np
import random

data = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

fig, ax = plt.subplots(1, figsize=(15, 5))

squares = list(data.keys())
values = list(data.values())

ax.bar(squares, values, color='maroon')

while True:
    key = random.choice(list(data.keys()))
    data[key] += 1

    ax.bar(squares, data.values(), color='maroon')

    for rect, label in zip(ax.patches, data.values()):
        height = rect.get_height()

    plt.xlabel("Amount landed on square")
    plt.ylabel("Monopoly squares")
    plt.title("Land probability Monopoly")
    plt.draw()
    plt.pause(0.1)
    ax.clear()
