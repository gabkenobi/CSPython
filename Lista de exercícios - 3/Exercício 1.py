# Escreva um programa que receba um número natural n  na entrada e imprima n, !  (fatorial) na saída.
# Exemplo:
# Digite o valor de n: 5
# 120
# Dica: lembre-se que o fatorial de 0 vale 1!

n = int(input("Digite o valor de n: "))

f = 1
i = 0

while i < n:
    i += 1
    f *= i

print(f)
