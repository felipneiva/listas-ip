lista = []
acao = ''
continua = True

while continua:
    acao = input()
    if acao == 'adicionar':
        nome, idx = input().split(' ')
        lista.insert(int(idx), nome)
    elif acao == 'remover':
        entrada = input()
        lista.remove(entrada)
    elif acao == 'atualizar indice':
        nome, idx = input().split(' ')
        anterior = lista.index(nome)
        lista.remove(nome)
        lista.insert(int(idx), nome)
        if anterior == int(idx):
            print('Nada mudou, a lista permanece igual')
    elif acao == 'imprimir lista atual':
        for nome in lista[0:-1]:
            print(nome, end=' ')
        print(lista[-1])
    elif acao == 'lista finalizada':
        continua = False
    else:
        print('Opçao não encontrada')

print('A lista ficou da seguinte forma:')
for nome in lista[0:-1]:
    print(nome, end=' ')
print(lista[-1])
