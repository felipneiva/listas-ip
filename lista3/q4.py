lista = []
lista_antes = []

n = int(input())

for i in range(n):
    lista.append(input().split('-'))

for nome in lista:
    lista_antes.append(nome)

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if int(lista[i][-1]) > int(lista[j][-1]):
            lista[i], lista[j] = lista[j], lista[i]
        elif int(lista[i][-1]) == int(lista[j][-1]):
            if len(lista[i][0]) > len(lista[j][0]):
                lista[i], lista[j] = lista[j], lista[i]
            elif len(lista[i][0]) == len(lista[j][0]):
                if lista_antes.index(lista[i]) > lista_antes.index(lista[j]):
                    lista[i], lista[j] = lista[j], lista[i]

for nome_seguidores in lista:
    print('-'.join(nome_seguidores))
