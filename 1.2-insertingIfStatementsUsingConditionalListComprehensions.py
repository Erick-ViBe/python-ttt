x = [1, 2, 3, 4, 5, 6]

r1 = []

for number in x:
    if number % 2 == 0:
        r1.append(number * 2)
    else:
        r1.append(number)

print(r1)

# List comprehension with conditional
# [action / for declaration / conditional]

r2 = [(number * 2 if number % 2 == 0 else number) for number in x]

print(r2)
