# Receba 3 números inteiros na entrada e imprima
# crescente
# se eles forem dados em ordem crescente. Caso contrário, imprima
# não está em ordem crescente

a = int(input("Digite o primeiro inteiro: "))
b = int(input("Digite o segundo inteiro: "))
c = int(input("Digite o terceiro inteiro: "))

if a < b < c:
    print("crescente")
else:
    print("não está em ordem crescente")
