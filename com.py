import math
n = 10000
s = sum(map(int, str(math.factorial(n))))
print(8 ** ( (11*s) % 4 ))
