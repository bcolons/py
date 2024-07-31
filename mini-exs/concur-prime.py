import os
import time as t
import concurrent.futures
import math

print('cpus: '+str(os.cpu_count()))
PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    time=t.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    print(t.time()-time)
    time=t.time()
    for number, res in zip(PRIMES,map(is_prime, PRIMES)):
        print('%d is prime: %s' % (number, res))
    print(t.time()-time)

if __name__ == '__main__':
    main()
