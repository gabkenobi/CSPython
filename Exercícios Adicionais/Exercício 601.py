# Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.


def maior_elemento(xs):
    if len(xs) == 0:
        return
    elif len(xs) == 1:
        return xs[0]
    else:
        max = xs[0]
        for x in xs:
            if x > max:
                max = x
        return max
