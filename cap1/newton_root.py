
def next_(n, x):
    return (x + n / x)/2


def repeat(f, a):
    yield a
    for v in repeat(f, f(a)):
        yield v


def within(epsilon, iterable):
    def head_tail(epsilon, a, iterable):
        b = next(iterable)
        if abs(a-b) <= epsilon: return b
        return head_tail(epsilon, b, iterable)
    return head_tail(epsilon, next(iterable), iterable)

def sqrt(a0, epsilon, n):
    return within(epsilon, repeat(lambda x: next_(n, x), a0))


print(sqrt(1.0, .0001, 3))