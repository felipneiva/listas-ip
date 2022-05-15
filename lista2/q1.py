# variáveis

letra = input('')
participantes = int(input(''))
aparicoes = 0
ganhador = ''
palavra_ganhador = ''
mais_aparicoes = aparicoes
vezes = 0

for i in range(1, participantes+1):
    aparicoes = 0
    nome_palavra = input('')
    nome, palavra = nome_palavra.split('-')

    for c in range(0, len(palavra)):
        if palavra[c] == letra:
            aparicoes += 1

        if i == 1:
            ganhador = nome
            palavra_ganhador = palavra
            mais_aparicoes = aparicoes
        else:
            if aparicoes > mais_aparicoes:
                ganhador = nome
                palavra_ganhador = palavra
                mais_aparicoes = aparicoes

if ganhador == 'Prior':
    print(f'Joga y joga! Mago Prior e o novo lider com a palavra {palavra_ganhador} com {mais_aparicoes} aparicoes da letra {letra}.')
else:
    print(f'Vish! O Mago Prior pode ir pro paredao, ja que quem ganhou foi {ganhador}, com a palavra {palavra_ganhador} e {mais_aparicoes} aparicoes da letra {letra}.')
