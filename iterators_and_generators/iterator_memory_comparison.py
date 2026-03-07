L = [x for x in range(1, 10000)]

# for i in L:
#   print(i*2)

import sys

print(sys.getsizeof(L) / 64)

x = range(1, 10000)

# for i in x:
#   print(i*2)

print(sys.getsizeof(x) / 64)
