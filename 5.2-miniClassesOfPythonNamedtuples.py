x = ("Joe", "Programmer", 20)
print(x)
print(x[0])
print(x[1])
print(x[2])

import collections
miniclass = collections.namedtuple("Mini", "name job experience")
print(type(miniclass))

mini_1 = miniclass(name="Joe", job="Programmer", experience=20)
print(mini_1)
print(mini_1.name)
print(mini_1.job)
print(mini_1.experience)
