













x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List Slicing
# list[start:stop:step]

print(x[0:3])
# First 3 items
# [1, 2, 3]

print(x[3:])
# Remove first 3 items
# [4, 5, 6, 7, 8, 9]

print(x[:6])
# Remove items after 6 place
# [1, 2, 3, 4, 5, 6]

print(x[0:6:2])
# Remove items after 6 place, step by 2
# [1, 3, 5]

print(x[:-3])
# Remove last 3 items
# [1, 2, 3, 4, 5, 6]

print(x[::-1])
# Reverse
# [1, 2, 3, 4, 5, 6]
# [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(x[-3::-1])
# Remove last 2 items and reverse
# [7, 6, 5, 4, 3, 2, 1]
