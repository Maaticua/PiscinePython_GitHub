import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """ Calculate the Body Mass Index (BMI) for a list of individuals."""
    if (len(height) != len(weight)):
        raise ValueError("The length of the height list and the weight list must be the same.")
    
    if isinstance(height, list) != True or isinstance(weight, list) != True:
        raise TypeError("Both height and weight must be lists.")
    
    try:
        # BMI = weight / (height ** 2)
        np_height = np.array(height)
        np_weight = np.array(weight)
        BMI = np_weight / (np_height ** 2)
        return BMI.tolist()
    except Exception as e:
        raise ValueError(f"An error occurred while calculating BMI: {e}")

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Apply a limit to the BMI values and return a list of booleans indicating if each BMI exceeds the limit."""
    if not isinstance(bmi, list):
        raise ValueError("The length of the BMI list and the limit list must be the same.")
    return [x > limit for x in bmi]


# random notes
'''
- "height" and "weight" or either a list of integers or a list of floats. The function should return a list of floats
- the "->"is the return type of the function
- "np_height = np.array(height)" convert a py list to a numpy array who is contigu in memory (like in c, better for math)
- "tolist()" reconvert numpy array in py list

'''