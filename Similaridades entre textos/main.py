import re


def le_assinatura():
    """A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos"""
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    """A funcao recebe um texto e devolve uma lista das sentencas dentro do texto"""
    sentencas = re.split(r"[.!?]+", texto)
    if sentencas[-1] == "":
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca"""
    return re.split(r"[,:;]+", sentenca)


def separa_palavras(frase):
    """A funcao recebe uma frase e devolve uma lista das palavras dentro da frase"""
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez"""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    diffs = []
    for i in range(len(as_a)):
        diff = abs(as_a[i] - as_b[i])
        diffs.append(diff)

    s = sum(diffs) / 6

    return s


def calcula_assinatura(texto):
    sentences = separa_sentencas(texto)
    phrases = []
    for sentence in sentences:
        phrases += separa_frases(sentence)

    words = []
    for phrase in phrases:
        words += separa_palavras(phrase)

    wal = sum([len(word) for word in words]) / len(words)
    ttr = n_palavras_diferentes(words) / len(words)
    hlr = n_palavras_unicas(words) / len(words)
    sal = sum([len(sentence) for sentence in sentences]) / len(sentences)
    sac = len(phrases) / len(sentences)
    pal = sum([len(phrase) for phrase in phrases]) / len(phrases)

    sig = [wal, ttr, hlr, sal, sac, pal]

    return sig


def avalia_textos(textos, ass_cp):
    m = None
    txt = None

    print(f"Avaliando {len(textos)}")

    for i in range(len(textos)):
        print(f"Texto {i+1}")
        f = calcula_assinatura(textos[i])
        print(f"f = {f}")
        s = compara_assinatura(f, ass_cp)
        print(f"s = {s}")

        if (m is None) or (s < m):
            txt = i + 1
            m = s

    return txt


def main():
    sig = le_assinatura()
    txts = le_textos()

    avalia_textos(txts, sig)


def test():
    txts = ["A", "B", "C"]
    sig = [4.325, 0.7375, 0.5875, 54.125, 2.0, 26.5625]

    avalia_textos(txts, sig)


if __name__ == "__main__":
    main()
