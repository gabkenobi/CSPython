# Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
# Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.


def computador_escolhe_jogada(n, m):
    p = n % (m + 1)
    if p == 0:
        return m
    else:
        return p


def usuario_escolhe_jogada(n, m):
    is_pieces_ammount_valid = False

    while not is_pieces_ammount_valid:
        p = int(input("Quantas peças você vai tirar? "))

        if p <= 0 or p > m or p > n:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            return p


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Você começa!")
        current_turn = "player"
    else:
        print("Computador começa!")
        current_turn = "computer"

    while n > 0:
        last_turn = current_turn

        if current_turn == "player":
            removed_pieces = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {removed_pieces} peças")
            current_turn = "computer"
        else:
            removed_pieces = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {removed_pieces} peças")
            current_turn = "player"

        n -= removed_pieces
        if n > 0:
            print(f"Agora restam {n} peças no tabuleiro")

    if last_turn == "player":
        print("Fim do jogo! Você ganhou!")
    else:
        print("Fim do jogo! O computador ganhou!")

    return last_turn


def campeonato():
    player_score = 0
    computer_score = 0
    for i in range(3):
        print(f"**** Rodada {i + 1} ****")
        winner = partida()

        if winner == "player":
            player_score += 1
        else:
            computer_score += 1

    print("**** Fim do campeonato ****")
    print(f"Placar: Você {player_score} X {computer_score} Computador")


def main():
    choice = input(
        """
  Bem-vindo ao jogo do NIM! Escolha:
  
  1 - para jogar uma partida isolada
  2 - para jogar um campeonato
  """
    )

    if choice == "1":
        partida()
    elif choice == "2":
        print("Você escolheu um campeonato!")
        campeonato()


main()
