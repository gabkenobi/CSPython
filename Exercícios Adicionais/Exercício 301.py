# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
# Exemplos:
# Digite um número inteiro: 13
# primo

# Digite um número inteiro: 12
# não primo

import math


n = int(input("Digite um número inteiro: "))

if n < 2:
    is_prime = False
elif n == 2 or n == 3:
    is_prime = True
else:
    is_prime = True
    i = 2
    k = math.sqrt(n)

    while i <= k:
        if n % i == 0:
            is_prime = False
            break

        i += 1

print("primo" if is_prime else "não primo")
