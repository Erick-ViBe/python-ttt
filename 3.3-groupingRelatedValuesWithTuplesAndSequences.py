x_tuple = (44, 'a string')
print(x_tuple)

x_singleton = (44,)
print(x_singleton)

def function_returning_multiple_values():
    return 4, 5

x, y = function_returning_multiple_values()
print(x)
print(y)

x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

x, _ = function_returning_multiple_values()
print(x)
