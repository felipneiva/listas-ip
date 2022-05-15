def numero_inimigos(a, b, c):
    inimigos = ((10 * a) + b) - c
    print(f'Haverá {inimigos} inimigos na rodada {a+1}')


n = int(input())
rodada = 0

for i in range(n):
    if i == 0:
        print('Haverá 10 inimigos na rodada 1')
    else:
        kills, vivos = input().split('-')
        rodada += 1
        print(rodada, int(kills), int(vivos))
        numero_inimigos(rodada+1, int(kills), int(vivos))
