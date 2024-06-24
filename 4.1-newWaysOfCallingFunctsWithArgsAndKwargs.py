def typical_func(one, two, three):
    """
    Args:
    one, two, three str: strings
    """
    return one + two + three

typical_func("mary", "had a", "little lamb")

def kw_functions(a=1, b=2):
    return a + b

things_to_add = {
    "a": 10,
    "b": 20,
}

x = kw_functions(**things_to_add)

print(x)
