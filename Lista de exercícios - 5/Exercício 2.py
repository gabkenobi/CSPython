# Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
# Por exemplo:
# digite a largura: 10
# digite a altura: 3
# ##########
# #        #
# ##########

# digite a largura: 2
# digite a altura: 2
# ##
# ##

width = int(input("digite a largura: "))
height = int(input("digite a altura: "))

for i in range(height):
    for j in range(width):
        if not ((0 < i < height - 1) and (0 < j < width - 1)):
            print("#", end="")
        else:
            print(" ", end="")
    print()
