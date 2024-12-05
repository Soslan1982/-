numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(2, len(numbers)):
    is_prime = True
    for j in range(2, i):
        if (i % j) == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print("Primes:", primes)
for k in range(len(numbers) + 1):
    is_prime_2 = False
    for n in range(2, k):
        if (k % n) == 0:
            is_prime_2 = True
            break
    if is_prime_2:
        not_primes.append(k)
print("Not_primes:", not_primes)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(2, 15):
    is_prime = True
    for j in range(2, i):
        if (i % j) == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print("Primes:", primes)
for k in range((15) + 1):
    is_prime_2 = False
    for n in range(2, k):
        if (k % n) == 0:
            is_prime_2 = True
            break
    if is_prime_2:
        not_primes.append(k)
print("Not_primes:", not_primes)
