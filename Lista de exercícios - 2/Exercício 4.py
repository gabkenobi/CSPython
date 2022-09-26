# Receba um número inteiro na entrada e imprima
# FizzBuzz
# na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

n = int(input("Digite um número inteiro: "))

if not n % (3 * 5):
    print("FizzBuzz")
else:
    print(n)
