lista = []
lifestyle = []
utilidades = []
dancinhas = []
seguidores_lifestyle = []
seguidores_utilidades = []
seguidores_dancinhas = []
views_lifestyle = []
views_utilidades = []
views_dancinhas = []

n = int(input())

for i in range(n):
    lista.append(input().split(', '))

for famoso in lista:
    if famoso[3] == 'Lifestyle':
        lifestyle.append(famoso)
        if famoso[1][-1] == 'M':
            seguidores_lifestyle.append(float(famoso[1][:-1]) * 10**6)
        elif famoso[1][-1] == 'K':
            seguidores_lifestyle.append(float(famoso[1][:-1]) * 10**3)
        if famoso[2][-1] == 'M':
            views_lifestyle.append(float(famoso[2][:-1]) * 10**6)
        elif famoso[2][-1] == 'K':
            views_lifestyle.append(float(famoso[2][:-1]) * 10**3)
    elif famoso[3] == 'Utilidades':
        utilidades.append(famoso)
        if famoso[1][-1] == 'M':
            seguidores_utilidades.append(float(famoso[1][:-1]) * 10**6)
        elif famoso[1][-1] == 'K':
            seguidores_utilidades.append(float(famoso[1][:-1]) * 10**3)
        if famoso[2][-1] == 'M':
            views_utilidades.append(float(famoso[2][:-1]) * 10**6)
        elif famoso[2][-1] == 'K':
            views_utilidades.append(float(famoso[2][:-1]) * 10**3)
    elif famoso[3] == 'Dancinhas':
        dancinhas.append(famoso)
        if famoso[1][-1] == 'M':
            seguidores_dancinhas.append(float(famoso[1][:-1]) * 10**6)
        elif famoso[1][-1] == 'K':
            seguidores_dancinhas.append(float(famoso[1][:-1]) * 10**3)
        if famoso[2][-1] == 'M':
            views_dancinhas.append(float(famoso[2][:-1]) * 10**6)
        elif famoso[2][-1] == 'K':
            views_dancinhas.append(float(famoso[2][:-1]) * 10**3)

for i in range(len(views_lifestyle)):
    for j in range(i+1, len(views_lifestyle)):
        if views_lifestyle[i] > views_lifestyle[j]:
            views_lifestyle[i], views_lifestyle[j] = views_lifestyle[j], views_lifestyle[i]

for i in range(len(views_utilidades)):
    for j in range(i+1, len(views_utilidades)):
        if views_utilidades[i] > views_utilidades[j]:
            views_utilidades[i], views_utilidades[j] = views_utilidades[j], views_utilidades[i]

for i in range(len(views_dancinhas)):
    for j in range(i+1, len(views_dancinhas)):
        if views_dancinhas[i] > views_dancinhas[j]:
            views_dancinhas[i], views_dancinhas[j] = views_dancinhas[j], views_dancinhas[i]

print('Lifestyle;')
if len(lifestyle) > 0:
    media_lifestyle = str((sum(seguidores_lifestyle) / len(seguidores_lifestyle)) / 10**6)
    posicao = media_lifestyle.index('.')
    media_lifestyle = media_lifestyle[:posicao + 2]
    maxviews_lifestyle = str(views_lifestyle[-1] / 10 ** 6)
    posicao = maxviews_lifestyle.index('.')
    if len(maxviews_lifestyle[posicao + 1:]) == 1:
        maxviews_lifestyle += '0'
    print(f'Quantidade de Tiktokers: {len(lifestyle)}')
    print(f'Media de seguidores: {media_lifestyle:}M')
    print(f'Maximo de visualizações: {maxviews_lifestyle:}M')
else:
    print('Nao foram informados dados sobre esta categoria.')

print('\nUtilidades;')
if len(utilidades) > 0:
    media_utilidades = str(sum(seguidores_utilidades) / len(seguidores_utilidades) / 10**6)
    posicao = media_utilidades.index('.')
    media_utilidades = media_utilidades[:posicao + 2]
    maxviews_utilidades = str(views_utilidades[-1] / 10 ** 6)
    posicao = maxviews_utilidades.index('.')
    if len(maxviews_utilidades[posicao + 1:]) == 1:
        maxviews_utilidades += '0'
    print(f'Quantidade de Tiktokers: {len(utilidades)}')
    print(f'Media de seguidores: {media_utilidades:}M')
    print(f'Maximo de visualizações: {maxviews_utilidades:}M')
else:
    print('Nao foram informados dados sobre esta categoria.')

print('\nDancinhas;')
if len(dancinhas) > 0:
    media_dancinhas = str(sum(seguidores_dancinhas) / len(seguidores_dancinhas) / 10 ** 6)
    posicao = media_dancinhas.index('.')
    media_dancinhas = media_dancinhas[:posicao + 2]
    maxviews_dancinhas = str(views_dancinhas[-1] / 10 ** 6)
    posicao = maxviews_dancinhas.index('.')
    if len(maxviews_dancinhas[posicao+1:]) == 1:
        maxviews_dancinhas += '0'
    print(f'Quantidade de Tiktokers: {len(dancinhas)}')
    print(f'Media de seguidores: {media_dancinhas:}M')
    print(f'Maximo de visualizações: {maxviews_dancinhas:}M')
else:
    print('Nao foram informados dados sobre esta categoria.')

for famoso in lista:
    if famoso[1][-1] == 'M':
        famoso[1] = float(famoso[1][:-1]) * 10**6
    elif famoso[1][-1] == 'K':
        famoso[1] = float(famoso[1][:-1]) * 10**3

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i][1] > lista[j][1]:
            lista[i], lista[j] = lista[j], lista[i]

mais_seguidores = float(lista[-1][1]) / 10**6
mais_seguidores = str(mais_seguidores)
posicao = mais_seguidores.index('.')
mais_seguidores = mais_seguidores[:posicao + 2]
print(f'\nOs olhares do mundo estao sobre {lista[-1][0].upper()}, que conta com {mais_seguidores:}M de seguidores vendo seus videos diarios de {lista[-1][-1]}!')