import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calculate the Body Mass Index (BMI) for a list of individuals."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists.")

    if len(height) != len(weight):
        raise ValueError(
            "The length of the height list and the weight list "
            "must be the same."
        )

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("List elements must be int or float.")
        if h <= 0 or w < 0:
            raise ValueError(
                "Height must be positive and weight non-negative."
            )

    try:
        np_height = np.array(height, dtype=float)
        np_weight = np.array(weight, dtype=float)
        bmi = np_weight / (np_height ** 2)
        return bmi.tolist()
    except Exception as e:
        raise ValueError(f"An error occurred while calculating BMI: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI values and return a list of booleans."""
    if not isinstance(bmi, list):
        raise TypeError("The BMI parameter must be a list.")
    if not isinstance(limit, (int, float)):
        raise TypeError("The limit parameter must be an integer or float.")

    return [x > limit for x in bmi]


# random notes
'''
- "height" and "weight" or either a list of integers or a list of
  floats. The function should return a list of floats
- the "->" is the return type of the function
- "np_height = np.array(height)" convert a py list to a numpy array
  who is contigu in memory (like in c, better for math)
- "tolist()" reconvert numpy array in py list
'''
