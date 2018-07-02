#  {3}

#not any(n % p == 0 for p in range(2, int(math.sqrt(n)+1)))

def isprimer(n):
    def isprime(k, coprime):
        """Is k relatively prime to the value coprime?"""
        if k < coprime*coprime: return True
        if k % coprime == 0: return False
        return isprime(k, coprime + 2)
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return isprime(n, 3)


for i in range(1000000):
    if isprimer(i):
        print(i)





# Recursion instead of a explicit loop
