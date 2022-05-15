# variáveis

rat_beth = int(input(''))
rat_adv = int(input(''))
res = input('')
prob = 1 / (1 + (10 ** ((rat_adv - rat_beth) / 400)))

# possibilidades de resultado e outputs

if res ==  'vitoria':
    rat_novo = rat_beth + 40 * (1 - prob)
    print(f'O novo rating da Beth Harmon é {int(rat_novo)}')
elif res == 'empate':
    rat_novo = rat_beth + 40 * (0.5 - prob)
    print(f'O novo rating da Beth Harmon é {int(rat_novo)}')
elif res == 'derrota':
    rat_novo = rat_beth + 40 * (-prob)
    print(f'O novo rating da Beth Harmon é {int(rat_novo)}')
else:
    print('Resultado da partida invalido')
