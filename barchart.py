import matplotlib.pyplot as plt


def bar_init(x, y):
    fig, ax = plt.subplots(1, figsize=(15, 5))
    ax.bar(x, y, color='maroon')
    return fig, ax


def update_chart(x, data, ax):
    ax.bar(x, data.values(), color='maroon')

    for rect, label in zip(ax.patches, data.values()):
        height = rect.get_height()

    plt.xlabel("Amount landed on square")
    plt.ylabel("Monopoly squares")
    plt.title("Land probability Monopoly")
    plt.pause(0.1)
    ax.clear()
    if not plt.get_fignums():
        quit()
