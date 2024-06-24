x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

r1 = []

for number_list in x:
    for number in number_list:
        r1.append(number)

print(r1)

import itertools
r2 = list(itertools.chain(*x))

print(r2)
