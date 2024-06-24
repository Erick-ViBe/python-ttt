x = [1, 2, 3, 4, 5]

r1 = []

for number in x:
    r1.append(number * 2)

print(r1)

# List comprehension
# [action / for declaration]

r2 = [number * 2 for number in x]

print(r2)
