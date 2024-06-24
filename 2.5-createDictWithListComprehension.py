keys = ['x', 'y', 'z']
values = [1, 2, 3]

x = dict((k, v) for k, v in zip(keys, values))

print(x)
