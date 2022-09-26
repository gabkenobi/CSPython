# Escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.

xs = []
zero_input = False
while not zero_input:
    x = int(input("Digite um número inteiro: "))

    if x:
        xs.append(x)
    else:
        break

for x in reversed(xs):
    print(x)
