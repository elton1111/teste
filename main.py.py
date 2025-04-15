def most_tabu(tabu):
    for l in tabu:
        print('|'.join(l))
    print('-' * (len(tabu[0]) * 2 - 1))


def movim_valid(tabu, l, c):
    linhas = len(tabu)
    colunas = len(tabu[0])
    return 0 <= l < linhas and 0 <= c < colunas and tabu[l][c] == ' '


def chegou_destino(l, c):
    return l == 0 and c == 3


def proximo_movim(tabu, l_atual, c_atual, profu):
    melhor_profu = float('inf')
    melhor_l, melhor_c = l_atual, c_atual

    direcoes = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # direita, esquerda, cima, baixo

    for d_linha, d_coluna in direcoes:
        nova_l = l_atual + d_linha
        nova_c = c_atual + d_coluna

        if movim_valid(tabu, nova_l, nova_c):
            if chegou_destino(nova_l, nova_c):
                return nova_l, nova_c, profu

            tabu[nova_l][nova_c] = '*'
            r_l, r_c, r_profu = proximo_movim(
                tabu, nova_l, nova_c, profu + 1
            )
            tabu[nova_l][nova_c] = ' '  # backtrack

            if r_profu < melhor_profu:
                melhor_profu = r_profu
                melhor_l, melhor_c = r_l, r_c

    return melhor_l, melhor_c, melhor_profu


def main():
    tabu = [
        [' ', 'X', ' ', ' '],
        [' ', 'X', ' ', 'X'],
        [' ', ' ', ' ', 'X'],
        [' ', 'X', ' ', ' ']
    ]

    l_atual, c_atual = 3, 0
    tabu[l_atual][c_atual] = '*'

    most_tabu(tabu)

    while not chegou_destino(l_atual, c_atual):
        nova_l, nova_c, profu = proximo_movim(
            tabu, l_atual, c_atual, 1
        )

        if profu == float('inf'):
            print("Caminho até o destino não encontrado.")
            return

        l_atual, c_atual = nova_l, nova_c
        tabu[l_atual][c_atual] = '*'
        most_tabu(tabu)

    print("Destino alcançado!")


if __name__ == "__main__":
    main()

