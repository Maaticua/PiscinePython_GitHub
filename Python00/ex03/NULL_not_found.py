def NULL_not_found(object: any) -> int:
    guess_type = type(object)

    if object is None:
        print(f"Nothing: {object} {guess_type}")
    elif guess_type is float and object != object:
        print(f"Cheese: {object} {guess_type}")
    elif guess_type is bool and object is False:
        print(f"Fake: {object} {guess_type}")
    elif guess_type is int and object == 0:
        print(f"Zero: {object} {guess_type}")
    elif guess_type is str and object == "":
        print(f"Empty: {guess_type}")
    else:
        print("Type not Found")
        return 1
    return 0