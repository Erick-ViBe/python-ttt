x = {'a': 1, 'b': 2}

if 'a' in x:
    print(x['a'])

print(x.get('a', 0))

from collections import defaultdict

example_default_dict = defaultdict(list)
customer_arrival_times = [("tony", 1), ("sam", 2), ("tony", 14)]

for customer, time in customer_arrival_times:
    example_default_dict[customer].append(time)

print(example_default_dict)
