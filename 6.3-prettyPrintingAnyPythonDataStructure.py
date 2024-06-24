















x = [1, 2, [3, 4, 5, "knight", [3, 4, 5, "knight"]], 15]

print(x)

import pprint
pprint.pprint(x, width=20, indent=4)
pprint.pprint(x, width=20, indent=4, depth=1)

from pprint import pprint as _p
_p(x, width=20, depth=2)
