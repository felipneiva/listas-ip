# variáveis
numero = int(input(''))
arma = 'nada'
tipo = 'nada'

# arma

if numero == 1:
    arma = 'Cassetete'
elif numero == 2:
    arma = 'Garrafa de Whisky'
elif numero == 3:
    arma = 'Soco Ingles'
elif numero == 4:
    arma = 'Lamina Escondida'
elif numero == 5:
    arma = 'Pe de Cabra'
elif numero == 6:
    arma = 'Canivete'

# tipo da arma

if numero == 2 or numero == 4 or numero == 6:
    tipo = 'cortante'
elif numero == 1 or numero == 3 or numero == 5:
    tipo = 'atordoante'

# output

if numero > 6 or numero < 1:
    print('Numero invalido')
else:
    print(f'A arma corpo a corpo escolhida foi: {arma}')
    print(f'A arma corpo a corpo escolhida e {tipo}')
