dicionarios = []

for i in range(5):
    carta = {}
    nome, custo = input().split(' - ')
    carta['nome'] = nome
    carta['custo'] = custo
    dicionarios.append(carta)

for i in range(len(dicionarios)):
    for j in range(i+1, len(dicionarios)):
        if dicionarios[i]['custo'] > dicionarios[j]['custo']:
            dicionarios[i], dicionarios[j] = dicionarios[j], dicionarios[i]

for carta in dicionarios:
    print(carta['nome'] + ' - ' + carta['custo'])
