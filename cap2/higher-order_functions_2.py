#  {2}

def numbers():
    for i in range(1024):
        print( "=", i)
        yield i

def sum_to(n):
    sum = 0
    for i in numbers():
        if i == n: break
        sum +=i
    return sum


print(sum_to(5))
# Strict and non-strict evaluation
