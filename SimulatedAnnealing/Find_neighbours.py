from random import randrange
import numpy as np
def find_neighbours(vector):
    flip_idx = randrange(len(vector))
    neighbour = np.array(vector)
    neighbour[flip_idx] = 1 - neighbour[flip_idx]
    return neighbour

