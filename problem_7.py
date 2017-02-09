from problem_3 import is_prime


def get_prime(n):
    primes = []
    counter = 2
    while len(primes) < n:
        if is_prime(counter):
            primes.append(counter)
        counter += 1
    return primes[-1]

print(get_prime(10001))
