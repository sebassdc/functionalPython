#def sum(seq):
#    if len(seq) == 0: return 0
#    return seq[0] + sum(seq[1:])


def until(n, filter_func, v):
    if v == n: return []
    if filter_func(v):
        return [v] + until(n, filter_func, v + 1)
    else:
        return until(n, filter_func, v + 1)


#print(until(10, lambda x: x % 3 == 0 or x % 5 == 0, 0))

x = sum(n for n in range(1, 10) if n % 3 == 0 or n % 5 == 0)

print(x)

