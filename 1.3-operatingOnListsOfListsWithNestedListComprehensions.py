x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

r1 = []

for number_list in x:
    for number in number_list:
        if number % 2 == 0:
            r1.append(number)

print(r1)

r_wrong = [[number for number in number_list if number % 2 == 0] for number_list in x]

print(r_wrong)

r2 = [number for number_list in x for number in number_list if number % 2 == 0]

print(r2)
