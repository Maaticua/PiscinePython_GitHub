def all_thing_is_obj(object: any) -> int:
    
    guess = type(object)

    if guess == list:
        print("List : <class 'list'>")
    elif guess == tuple:
        print("Tuple : <class 'tuple'>")
    elif guess == set:
        print("Set : <class 'set'>")
    elif guess == dict:
        print("Dict : <class 'dict'>")
    elif guess == str:
        print(f"{object} is in the kitchen : {guess}")
    else:
        print("Type not found")
    return 42