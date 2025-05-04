# вводится неотрицательное целое число
# занести в список все его делители
# 16 -> [1,2,4,8,16]
from operator import delitem
import time
# n = int(input())
# deliteli = []
# for d in range(1, n + 1):
#     if n % d == 0:
#         deliteli.append(d)
# print(deliteli)
# start = time.perf_counter()
for n in range(801126, 801300):
    deliteli = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            deliteli.append(d)
            deliteli.append(n//d)
    print(deliteli)
# end = time.perf_counter()
# print(end - start)

# 9.66
# 0.014

# вводится число, определить, простое ли оно