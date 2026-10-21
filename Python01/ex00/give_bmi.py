import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calculate the Body Mass Index (BMI) for a list of individuals."""
    if len(height) != len(weight):
        raise ValueError(
            "The length of the height list and the weight list "
            "must be the same."
        )

    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists.")

    try:
        np_height = np.array(height)
        np_weight = np.array(weight)
        bmi = np_weight / (np_height ** 2)
        return bmi.tolist()
    except Exception as e:
        raise ValueError(f"An error occurred while calculating BMI: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI values and return a list of booleans."""
    if not isinstance(bmi, list):
        raise ValueError(
            "The length of the BMI list and the limit list "
            "must be the same."
        )
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
