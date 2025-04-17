tabuleiro = [" " for _ in range(9)]

def mostrar_tabuleiro():
    print()
    for i in range(0, 9, 3):
        print(f"{tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

def ganhou(tab, jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(tab[pos] == jogador for pos in c) for c in combinacoes)

def empatou(tab):
    return all(c != " " for c in tab)

def minimax(tab, prof, maximizando):
    if ganhou(tab, "X"):
        return -10 + prof
    if ganhou(tab, "O"):
        return 10 - prof
    if empatou(tab):
        return 0

    if maximizando:
        melhor = -float("inf")
        for i in range(9):
            if tab[i] == " ":
                tab[i] = "O"
                val = minimax(tab, prof + 1, False)
                tab[i] = " "
                melhor = max(melhor, val)
        return melhor
    else:
        melhor = float("inf")
        for i in range(9):
            if tab[i] == " ":
                tab[i] = "X"
                val = minimax(tab, prof + 1, True)
                tab[i] = " "
                melhor = min(melhor, val)
        return melhor

def escolher_jogada(tab):
    melhor_val = -float("inf")
    posicao = -1

    for i in range(9):
        if tab[i] == " ":
            tab[i] = "O"
            val = minimax(tab, 0, False)
            tab[i] = " "
            if val > melhor_val:
                melhor_val = val
                posicao = i

    return posicao

def jogar():
    while True:
        mostrar_tabuleiro()

    
        while True:
            try:
                jogada = int(input("Sua vez (0-8): "))
                if 0 <= jogada <= 8 and tabuleiro[jogada] == " ":
                    break
                else:
                    print("ivalida  posição.")
            except:
                print("Só vale de 0 a 8.")
        
        tabuleiro[jogada] = "X"

        if ganhou(tabuleiro, "X"):
            mostrar_tabuleiro()
            print("você ganhou!")
            break
        if empatou(tabuleiro):
            mostrar_tabuleiro()
            print("empatou!")
            break
        
        print("vez do PC...")
        pos = escolher_jogada(tabuleiro)
        tabuleiro[pos] = "O"

        if ganhou(tabuleiro, "O"):
            mostrar_tabuleiro()
            print("PC ganhou!")
            break
        if empatou(tabuleiro):
            mostrar_tabuleiro()
            print("empatou!")
            break

print("Jogo da Velha")
print("Você joga com X, o PC com O")
print("Posições:")
print("0 | 1 | 2")
print("--+---+--")
print("3 | 4 | 5")
print("--+---+--")
print("6 | 7 | 8")

jogar()
     