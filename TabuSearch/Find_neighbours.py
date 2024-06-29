import numpy as np
def find_neighbours(vector):
    neighbours = np.zeros([len(vector), len(vector)], dtype=int)
    for index in range(len(vector)):
        value = vector[index]
        temp = np.array(vector)
        temp[index] = 1-value
        neighbours[index] = temp
    return neighbours

