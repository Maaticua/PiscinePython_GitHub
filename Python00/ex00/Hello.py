ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
ft_set.remove("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# Notes diverse:
'''
list = dynamic array, can be modified and doublons allowed (add, remove, change elements)
tuple = static array, cannot be modified. redeclaration is the key for modification.
set = collection of unique elements, the word is hashed and the value is stored in a hash table.
dict = key-value pairs, can be modified, keys are unique, values can be modified. for exemple the '0' of a str[0] is a word like "hello"
'''