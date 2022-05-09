import numpy as np
from matplotlib import pyplot
import random

# number of red cards in the deck. Total number of cards in deck is 2n
n = 26
num_simulations = 20
# color='cool'
# color='jet'
color='Blues'

# "r" for red, "b" for black
deck = ["r" for i in range(n)] + ["b" for i in range(n)]

# (n+1) x (n+1) matrix of all zeros. will count frequencies
# dimension n+1 because we need to include the point (n, n) and (0, 0)
data = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(num_simulations):
    random.shuffle(deck)

    # x is red, y is black
    current_x = n
    current_y = n
    for card in deck:
        data[current_y][current_x] += 1

        if card == "r":
            current_x -= 1
        else:
            current_y -= 1

    data[current_y][current_x] += 1

    assert current_y == 0 and current_x == 0

pyplot.figure(figsize=(5,5))

pyplot.title(f"Game Paths with {n*2} Cards, games = {num_simulations}")
pyplot.xlabel("Red")
pyplot.ylabel("Black")

pyplot.imshow(data, cmap=color)
pyplot.gca().invert_yaxis()

pyplot.show()