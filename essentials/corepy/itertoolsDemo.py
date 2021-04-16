from itertools import count, islice
from filterComprehensions import is_prime

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(thousand_primes)
print(list(thousand_primes)[-10:])
prime_sum = sum(islice((x for x in count() if is_prime(x)), 1000))
print(prime_sum)
