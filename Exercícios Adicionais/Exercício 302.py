# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".
# Exemplos:
# Digite um número inteiro: 12345
# não

# Digite um número inteiro: 1011
# sim

n = input("Digite um número inteiro: ")

has_repeating_digits = False

if len(n) > 1:
    for i in range(len(n) - 1):
        c1 = n[i]
        c2 = n[i + 1]

        if c1 == c2:
            has_repeating_digits = True
            break

print("sim" if has_repeating_digits else "não")
