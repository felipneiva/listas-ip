# listas

homens = []
mulheres = []
generos = []

# número de pessoas

n = int(input())

# separa os nomes dos homens, das mulheres e dos generos em listas

for i in range(0, n):
    nome_genero = input()
    nome, genero = nome_genero.split('-')
    genero = genero.strip()
    nome = nome.strip()
    if genero == 'M':
        homens.append(nome)
    elif genero == 'F':
        mulheres.append(nome)
    generos.append(genero)

# quantidade de homens e de mulheres

qtdh = 0
qtdm = 0

for genero in generos:
    if genero == 'M':
        qtdh += 1
    if genero == 'F':
        qtdm += 1

# apenas homens

if qtdm == 0:
    for homem in homens:
        print(f'{homem}, ', end='')
    print('Querem cafe?')
    print(f'Serao necessarias {len(homens)} porcoes de cafe')

# apenas mulheres

elif qtdh == 0:
    for mulher in mulheres:
        print(f'{mulher}, ', end='')
    print('Desculpa, so pros meninos HAHAHAHAAHHAHAHA')
    print('Nao tem meninos na lista, nao precisa fazer cafe, Neuma')

# homens e mulheres

elif qtdh > 0 and qtdm > 0:
    for homem in homens:
        print(f'{homem}, ', end='')
    print(f'Querem cafe?')
    for mulher in mulheres:
        print(f'{mulher}, ', end='')
    print('Desculpa, so pros meninos HAHAHAHAAHHAHAHA')
    print(f'Serao necessarias {len(homens)} porcoes de cafe')


