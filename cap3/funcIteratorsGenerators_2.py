#  {2}
# Functions as first-class objects
import collections

class Mersenne1(collections.Callable):
    def __init__(self, algorithm):
        self.pow2 = algorithm
    def __call__(self, arg):
        return self.pow2(arg)-1


def shifty(b):
    return 1 << b


def multy(b):
    if b == 0: return 1
    return 2 * multy(b - 1)


def faster(b):
    if b == 0: return 1
    if b % 2 == 1: return 2 * faster(b - 1)
    t = faster(b//2)
    return t*t


m1s = Mersenne1(shifty)
m1m = Mersenne1(multy)
m1f = Mersenne1(faster)

print("m1s()", m1s.pow2(10))
print("m1m()", m1m.pow2(10))
print("m1f()", m1f.pow2(10))
