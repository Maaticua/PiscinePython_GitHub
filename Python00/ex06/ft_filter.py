def ft_filter(function_to_apply, iterable):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""

    if function_to_apply is None:
        return iter([item for item in iterable if item])
    return iter([item for item in iterable if function_to_apply(item)])
    

# note random
'''
[ <ce_qu_on_garde> for <variable_temporaire> in <tableau> if <condition> ]
[x for x in tab] = [1, 2, 3]
[x * 10 for x in tab] = [10, 20, 30]
[42 for x in tab] = [42, 42, 42]
'''