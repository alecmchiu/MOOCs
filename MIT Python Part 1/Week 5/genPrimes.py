def genPrimes():
    primes = []
    if len(primes) == 0:
        primes.append(2)
        yield 2
    found = False
    n = 2
    while True:
        found = True
        n += 1
        for i in range(len(primes)-1):
            if (n % primes[i]) == 0:
                found = False
        if found:
            primes.append(n)
            yield n

if __name__ == '__main__':
    n = 17
    prime = genPrimes()
    for i in range(n):
        print(next(prime))