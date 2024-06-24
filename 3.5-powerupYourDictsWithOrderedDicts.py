d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 4
d[5] = 5
for k, v in d.items():
    print(k, v)

import collections
d = collections.OrderedDict()
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 4
d[5] = 5
for k, v in d.items():
    print(k, v)

d1 = {}
d1[1] = 1
d1[2] = 2
d1[3] = 3
d2 = {}
d2[3] = 3
d2[2] = 2
d2[1] = 1
print(d1 == d2)

d1 = collections.OrderedDict()
d1[1] = 1
d1[2] = 2
d1[3] = 3
d2 = collections.OrderedDict()
d2[3] = 3
d2[2] = 2
d2[1] = 1
print(d1 == d2)
