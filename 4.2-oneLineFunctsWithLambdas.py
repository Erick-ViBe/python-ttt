# Lambdas
# lambda args: expression

x = [12, 318, 29, 122, 417, 204]

y = filter(lambda x: x % 3 == 0, x)
print(list(y))

y = map(lambda x: x * 2, x)
print(list(y))

import functools
y = functools.reduce(lambda x, y: x + y, x)
print(y)
