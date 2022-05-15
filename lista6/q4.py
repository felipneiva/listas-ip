armadilhas = {}

casas = int(input())

if not (2 <= casas <= 10):
    print('Faixa não permitida')
else:
    for i in range(casas):
        armadilhas[i + 1] = int(input())

    jogador1 = (input(), input())
    jogador2 = (input(), input())
    jogador3 = (input(), input())

    vivos = {jogador1: True, jogador2: True, jogador3: True}

    jogo = True
    rodada = 1
    while (vivos[jogador1] or vivos[jogador2] or vivos[jogador3]) and rodada != casas + 1:
        if vivos[jogador1] and jogo:
            escolha1 = int(input())
            if escolha1 == armadilhas[rodada]:
                vivos[jogador1] = False
                if vivos[jogador2] or vivos[jogador3]:
                    print(f'{jogador1[0]} caiu de uma altura de 30 metros e morreu! :O')
                else:
                    print('Todos os jogadores morreram!')
            else:
                if rodada != casas:
                    print(f'{jogador1[0]} pulou uma casa!')
                else:
                    jogo = False
        if vivos[jogador2] and jogo:
            escolha2 = int(input())
            if escolha2 == armadilhas[rodada]:
                vivos[jogador2] = False
                if vivos[jogador1] or vivos[jogador3]:
                    print(f'{jogador2[0]} caiu de uma altura de 30 metros e morreu! :O')
                else:
                    print('Todos os jogadores morreram!')
            else:
                if rodada != casas:
                    print(f'{jogador2[0]} pulou uma casa!')
                else:
                    jogo = False
        if vivos[jogador3] and jogo:
            escolha3 = int(input())
            if escolha3 == armadilhas[rodada]:
                vivos[jogador3] = False
                if vivos[jogador1] or vivos[jogador2]:
                    print(f'{jogador3[0]} caiu de uma altura de 30 metros e morreu! :O')
                else:
                    print('Todos os jogadores morreram!')
            else:
                if rodada != casas:
                    print(f'{jogador3[0]} pulou uma casa!')
                else:
                    jogo = False
        rodada += 1

    if vivos[jogador1]:
        print(f'{jogador1[0]}, mais conhecido como {jogador1[1]}, ganhou o jogo! Parabéns!')
    elif vivos[jogador2]:
        print(f'{jogador2[0]}, mais conhecido como {jogador2[1]}, ganhou o jogo! Parabéns!')
    elif vivos[jogador3]:
        print(f'{jogador3[0]}, mais conhecido como {jogador3[1]}, ganhou o jogo! Parabéns!')