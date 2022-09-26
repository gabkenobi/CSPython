# Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

import math


def is_prime(n):
    if n < 2:
        prime = False
    elif n == 2 or n == 3:
        prime = True
    else:
        prime = True
        i = 2
        k = int(math.sqrt(n))
        while i <= k:
            if n % i == 0:
                prime = False
                break
            i += 1

    return prime


def n_primos(n):
    if n < 2:
        return
    else:
        primes = [x for x in range(2, n + 1) if is_prime(x)]
        return len(primes)
