import numpy as np
def calc_obj(obj_coeffs, takens,weights,capacity):
    value_vector = np.multiply(obj_coeffs, takens)
    weight_vector = np.multiply(weights, takens)
    tot_weight = weight_vector.sum()
    if tot_weight <= capacity:
        return value_vector.sum()
    else:
        return -np.inf