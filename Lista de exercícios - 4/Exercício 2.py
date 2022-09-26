# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
# Exemplos de execução no shell do Python:
# >>> maior_primo(100)
# 97
# >>> maior_primo(7)
# 7

# Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.

import math


def maior_primo(n):
    def is_prime(n):
        if n < 2:
            prime = False
        elif n == 2 or n == 3:
            prime = True
        else:
            prime = True
            i = 2

            while i <= math.sqrt(n):
                if n % i == 0:
                    prime = False
                    break

                i += 1

        return prime

    if n < 2:
        return
    else:
        greater_prime = 2
        for i in range(2, n + 1):
            if is_prime(i):
                greater_prime = i

        return greater_prime
