import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ affiche la shepe en 2d, tronque, print la nouvelle"""

    if not isinstance(family, list):  # check type
        raise TypeError("family must be a list")

    if len(family) == 0:  # check empty
        raise ValueError("family must not be empty")

    ref_size = len(family[0])  # check size all members
    for member in family:
        if not isinstance(member, list):
            raise TypeError("each member of family must be a list")
        if len(member) != ref_size:
            raise ValueError("all members of family must have the same size")

    np_family = np.array(family)  # conversion numpy array pour attribu .cshape
    print(f"My shape is: {np_family.shape}")

    np_family_tronc = np_family[start:end]

    print(f"My new shape is: {np_family_tronc.shape}")
    return np_family_tronc.tolist()
