liberos = []
levantadores = []
centrais = []
ponteiros = []
opostos = []
jogadores = []

samuel = False
continua = True
valido = True

while continua:
    jogador = False
    entrada = input()
    if entrada == 'adicionar':
        nome, posicao = input().split(': ')
        jogadores.append(nome)
        if posicao == 'Libero':
            liberos.append(nome)
            if len(liberos) > 2:
                print('ERRO: liberos demais, nao temos uniformes suficientes')
                continua = False
        elif posicao == 'Levantador':
            levantadores.append(nome)
            if len(levantadores) >= 5:
                print('Cuidado! voce ja possui 5 levantadores')
        elif posicao == 'Central':
            centrais.append(nome)
            if len(centrais) >= 5:
                print('Cuidado! voce ja possui 5 centrais')
        elif posicao == 'Ponteiro':
            ponteiros.append(nome)
            if len(ponteiros) >= 5:
                print('Cuidado! voce ja possui 5 ponteiros')
        elif posicao == 'Oposto':
            opostos.append(nome)
            if len(opostos) >= 5:
                print('Cuidado! voce ja possui 5 opostos')
        if len(jogadores) > 18:
            print('ERRO: voce estrapolou o numero de jogadores')
            continua = False
    elif entrada == 'relatorio':
        print('No nosso time ja possuimos:')
        print(f'Liberos: {len(liberos)}')
        print(f'Levantadores: {len(levantadores )}')
        print(f'Ponteiros: {len(ponteiros)}')
        print(f'Centrais: {len(centrais)}')
        print(f'Opostos: {len(opostos)}')
        print(f'TOTAL: {len(jogadores)}')
    elif entrada == 'nomes':
        posicao = input()
        if posicao == 'Libero':
            if len(liberos) > 0:
                print('Os liberos sao:')
                for nome in liberos:
                    print(nome)
            else:
                print('Ainda nao temos jogadores nessa posicao')
        elif posicao == 'Levantador':
            if len(levantadores) > 0:
                print('Os levantadores sao:')
                for nome in levantadores:
                    print(nome)
            else:
                print('Ainda nao temos jogadores nessa posicao')
        elif posicao == 'Central':
            if len(centrais) > 0:
                print('Os centrais sao:')
                for nome in centrais:
                    print(nome)
            else:
                print('Ainda nao temos jogadores nessa posicao')
        elif posicao == 'Ponteiro':
            if len(ponteiros) > 0:
                print('Os ponteiros sao:')
                for nome in ponteiros:
                    print(nome)
            else:
                print('Ainda nao temos jogadores nessa posicao')
        elif posicao == 'Oposto':
            if len(opostos) > 0:
                print('Os opostos sao:')
                for nome in opostos:
                    print(nome)
            else:
                print('Ainda nao temos jogadores nessa posicao')
    elif entrada == 'buscar':
        pessoa = input()
        if pessoa == 'Samuel':
            for nome in jogadores:
                if nome == 'Samuel':
                    samuel = True
            if samuel:
                print('Sim, Samuel, voce ja esta na lista de jogadores')
            else:
                print('Como voce pode esquecer de si mesmo? Voce nao esta na lista')
        else:
            for nome in jogadores:
                if pessoa == nome:
                    jogador = True
            if jogador:
                print(f'Sim, {pessoa} esta na lista de jogadores')
            else:
                print(f'O jogador {pessoa} nao esta na lista de jogadores')
    elif entrada == 'fim':
        continua = False
    else:
        print('***COMANDO INVALIDO***')

if len(liberos) != 2:
    valido = False
if len(levantadores) < 2:
    valido = False
if len(centrais) < 2:
    valido = False
if len(ponteiros) < 2:
    valido = False
if len(opostos) < 2:
    valido = False
if len(jogadores) > 18:
    valido = False
if valido:
    print(f'O Navegantes esta pronto para disputar o Estadual! Desejem sorte aos nossos {len(jogadores)} jogadores!')
elif not valido:
    print('Quem mandou ficar perdendo tempo com TikTok... Agora o Navegantes nao conseguira jogar o estadual :(')