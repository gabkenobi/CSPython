# Receba um número inteiro na entrada e imprima
# Buzz
# se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

n = int(input("Digite um número inteiro: "))

if not n % 5:
    print("Buzz")
else:
    print(n)
