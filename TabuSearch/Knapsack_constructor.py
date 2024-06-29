import numpy as np
def knapsack_construct(obj_coeffs, weights, capacity):
    val_density = obj_coeffs/weights
    current_weight = 0
    taken = np.zeros((len(weights),), dtype=int)
    order = sorted(range(len(val_density)), key=lambda k: val_density[k], reverse=True)
    for index in order:
        if current_weight + weights[index] <= capacity:
            taken[index] = 1
            current_weight = current_weight + weights[index]

    return taken
