import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Prints the 2D array shape, slices it, and returns the new list."""
    if not isinstance(family, list):
        raise TypeError("Family must be a list.")
    if len(family) == 0:
        raise ValueError("Family must not be empty.")

    ref_size = len(family[0])
    for member in family:
        if not isinstance(member, list):
            raise TypeError("Each member of family must be a list.")
        if len(member) != ref_size:
            raise ValueError("All members of family must have the same size.")

    np_family = np.array(family)
    print(f"My shape is: {np_family.shape}")

    np_family_tronc = np_family[start:end]
    print(f"My new shape is: {np_family_tronc.shape}")

    return np_family_tronc.tolist()
