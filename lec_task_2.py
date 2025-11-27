import numpy as np
def mean_arifmetic(array):
    s = 1
    for element in array:
        s = s * element

    return s

test = np.array([3, 6, 7, 9, 1])
print(mean_arifmetic(test))
