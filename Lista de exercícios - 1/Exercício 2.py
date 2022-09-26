# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:
# Exemplo:
# • Entrada de Dados:
# Digite a primeira nota: 4
# Digite a segunda nota: 5
# Digite a terceira nota: 6
# Digite a quarta nota: 7
# • Saída de Dados:
# A média aritmética é 5.

grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))
grade3 = float(input("Digite a terceira nota: "))
grade4 = float(input("Digite a quarta nota: "))

average = sum([grade1, grade2, grade3, grade4]) / 4

print("A média aritmética é", average)
