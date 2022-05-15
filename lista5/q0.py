nome = input()
velocidade = int(input())
pista = input()
moedas = int(input())


def velocidade_moeda(x):
    if x == 'Mario Kart Stadium':
        return 3
    elif x == 'Bowsers Castle':
        return 4
    elif x == 'Moo Moo Meadows':
        return 5
    elif x == 'Yoshi Valley':
        return 6
    elif x == 'Rainbow Road':
        return 7


def velocidade_final(x, y):
    if y == 0:
        return x
    else:
        x += velocidade_moeda(pista)
        y -= 1
        return velocidade_final(x, y)


print(f'Correndo na pista {pista}, {nome} coletou {moedas} moedas e terminou a corrida na incrivel velocidade de {velocidade_final(velocidade, moedas)} km/h.')
