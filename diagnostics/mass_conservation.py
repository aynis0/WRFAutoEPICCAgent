import numpy as np


def check_mass(old_data, new_data):

    old_mass = np.sum(old_data)
    new_mass = np.sum(new_data)

    diff = abs(new_mass - old_mass) / old_mass * 100

    print(f"Original Mass : {old_mass:.2f}")
    print(f"Interpolated  : {new_mass:.2f}")
    print(f"Difference(%) : {diff:.4f}")

    if diff < 1:
        print("Mass conservation PASSED")
    else:
        print("Mass conservation FAILED")
