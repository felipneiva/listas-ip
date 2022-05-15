# variáveis

rodadas = int(input(''))
jogador1 = input('')
jogador2 = input('')
jogador3 = input('')
perdedor = ''
primeiro = ''
segundo = ''
soma1 = 0
soma2 = 0
soma3 = 0

# primeira fase

for i in range(0, rodadas):
    jogada1 = int(input(''))
    jogada2 = int(input(''))
    jogada3 = int(input(''))
    soma1 += jogada1
    soma2 += jogada2
    soma3 += jogada3
    if soma1 >= 200:
        primeiro = jogador1
        if soma2 > soma3:
            segundo, perdedor = jogador2, jogador3
            print(f'{perdedor} ja esta confirmado no paredao')
        elif soma3 > soma2:
            segundo, perdedor = jogador3, jogador2
            print(f'{perdedor} ja esta confirmado no paredao')
        break
    elif soma2 >= 200:
        primeiro = jogador2
        if soma1 > soma3:
            segundo, perdedor = jogador1, jogador3
            print(f'{perdedor} ja esta confirmado no paredao')
        elif soma3 > soma1:
            segundo, perdedor = jogador3, jogador1
            print(f'{perdedor} ja esta confirmado no paredao')
        break
    elif soma3 >= 200:
        primeiro = jogador3
        if soma1 > soma2:
            segundo, perdedor = jogador1, jogador2
            print(f'{perdedor} ja esta confirmado no paredao')
        elif soma2 > soma1:
            segundo, perdedor = jogador2, jogador1
            print(f'{perdedor} ja esta confirmado no paredao')
        break

if soma1 < 200 and soma2 < 200 and soma3 < 200:
    if soma1 > soma2 > soma3:
        primeiro, segundo, perdedor = jogador1, jogador2, jogador3
    elif soma1 > soma3 > soma2:
        primeiro, segundo, perdedor = jogador1, jogador3, jogador2
    elif soma2 > soma1 > soma3:
        primeiro, segundo, perdedor = jogador2, jogador1, jogador3
    elif soma2 > soma3 > soma1:
        primeiro, segundo, perdedor = jogador2, jogador3, jogador1
    elif soma3 > soma1 > soma2:
        primeiro, segundo, perdedor = jogador3, jogador1, jogador2
    elif soma3 > soma2 > soma1:
        primeiro, segundo, perdedor = jogador3, jogador2, jogador1
    print(f'{perdedor} ja esta confirmado no paredao')
print(f'1° - {primeiro}')
print(f'2° - {segundo}')


# segunda fase

jogador1 = primeiro
jogador2 = segundo
rodadas2 = int(input(''))
soma1 = 0
soma2 = 0
for c in range(0, rodadas2):
    jogada1 = int(input(''))
    jogada2 = int(input(''))
    soma1 += jogada1
    soma2 += jogada2
if soma1 > soma2:
    print(f'Nosso paredao sera entre {jogador2} e {perdedor}')
elif soma2 > soma1:
    print(f'Nosso paredao sera entre {jogador1} e {perdedor}')
