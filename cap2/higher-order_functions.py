#  3
import math

def isprime(p):
    if p < 2: return False
    if p == 2: return True
    if p % 2 == 0: return False
    return not any(p == 0 for p in range(3, int(math.sqrt(p)) + 1, 2))


for i in range(1000000):
    if isprime(i):
        print(i)





# Recursion instead of a explicit loop
