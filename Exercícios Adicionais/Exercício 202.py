# Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
# O programa deve receber os parâmetros a , b , e c  da equação, respectivamente, e imprimir o resultado na saída da seguinte maneira:
# Quando não houver raízes reais imprima:
# esta equação não possui raízes reais
# Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:
# a raiz desta equação é X
# ou
# a raiz dupla desta equação é X
# onde X é o valor da raiz dupla
# Quando houver duas raízes reais imprima:
# as raízes da equação são X e Y
# onde X e Y são os valor das raízes.
# Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente. Exemplos:
# as raízes da equação são 1.0 e 2.0
# as raízes da equação são -2.0 e 0.0

import math


a = int(input("Digite o parâmetro *a* da fórmula: "))
b = int(input("Digite o parâmetro *b* da fórmula: "))
c = int(input("Digite o parâmetro *c* da fórmula: "))

delta = (b * b) - (4 * a * c)

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    x = (-b + delta) / (2 * a)
    print("a raiz desta equação é", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if x1 < x2:
        print(f"as raízes da equação são {x1} e {x2}")
    else:
        print(f"as raízes da equação são {x2} e {x1}")
