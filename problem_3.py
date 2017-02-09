def get_largest_prime_factor(number):
    primes = [x for x in range(10000) if is_prime(x)]
    for x in reversed(primes):
        if is_prime(x) and number % x == 0:
            return x


def is_prime(number):
    if number == 0 or number == 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    return True

if __name__ == 'main':
    print(get_largest_prime_factor(600851475143))
