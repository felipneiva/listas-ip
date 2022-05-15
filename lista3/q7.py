legenda = []
ruidos = 0

for i in range(10):
    trecho = input()
    if not trecho == 'tss' and not trecho == 'zzz':
        legenda.append(trecho)

ruidos = 10 - len(legenda)


for linha in legenda:
    posicao = legenda.index(linha)
    if linha[:3] == 'zzz':
        if linha[-3:] == 'zzz' or linha[-3:] == 'tss':
            legenda.remove(linha)
            legenda.insert(posicao, linha[3:-3])
            ruidos += 2
        else:
            legenda.remove(linha)
            legenda.insert(posicao, linha[3:])
            ruidos += 1
    elif linha[-3:] == 'zzz':
        if linha[:3] == 'zzz' or linha[:3] == 'tss':
            legenda.remove(linha)
            legenda.insert(posicao, linha[3:-3])
            ruidos += 2
        else:
            legenda.remove(linha)
            legenda.insert(posicao, linha[:-3])
            ruidos += 1
    elif linha[:3] == 'tss':
        if linha[-3:] == 'zzz' or linha[-3:] == 'tss':
            legenda.remove(linha)
            legenda.insert(posicao, linha[3:-3])
            ruidos += 2
        else:
            legenda.remove(linha)
            legenda.insert(posicao, linha[3:])
            ruidos += 1
    elif linha[-3:] == 'tss':
        if linha[:3] == 'zzz' or linha[:3] == 'tss':
            legenda.remove(linha)
            legenda.insert(posicao, linha[3:-3])
            ruidos += 2
        else:
            legenda.remove(linha)
            legenda.insert(posicao, linha[:-3])
            ruidos += 1

if len(legenda) == 0:
    print('Eita, a legenda simplesmente inexiste! Tudo era ruido!')
else:
    print('Legenda final:\n')
    for linha in legenda:
        print(linha.strip())

    if 4 >= ruidos >= 1 and len(legenda) >= 8:
        print('\nTodo o ruido foi removido e voce mandou bem! A legenda saiu certinha. Pode subir!')
    elif ruidos == 0:
        print('\nNem precisava rodar, o audio ja estava limpinho e a legenda ta nos conformes. Marca o @billyraycyrus')
    elif ruidos > 4 or len(legenda) < 8:
        print('\nIh, tem alguma coisa errada com a legenda, ta estranha. Melhor dar uma verificada e regravar.')