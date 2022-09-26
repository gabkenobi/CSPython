# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
# longe
# na saída. Caso o contrário, quando a distância for menor que 10, imprima
# perto

import math


ax = int(input("Digite o valor em X do primeiro ponto: "))
ay = int(input("Digite o valor em Y do primeiro ponto: "))
bx = int(input("Digite o valor em X do segundo ponto: "))
by = int(input("Digite o valor em Y do segundo ponto: "))

d = math.sqrt((bx - ax) * (bx - ax) + (by - ay) * (by - ay))

if d >= 10:
    print("longe")
else:
    print("perto")
