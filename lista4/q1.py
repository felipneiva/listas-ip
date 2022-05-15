inventario = []
slots = int(input())
ocupados = int(input())
for i in range(ocupados):
    inventario.append(input().split(' - '))
pochetes = int(input())


def espacos():
    sobrando = slots - ocupados
    return sobrando


def novos_espacos():
    novos = espacos() + 2 * pochetes
    return novos


print(f'Voce possui {slots} slots no inventario e {ocupados} estao ocupados.')
print(f'Espacos sobrando [{espacos()}]')

if ocupados == 0:
    print('\nSeu inventário ainda está vazio. Que sorte... ou azar. Tome cuidado.')
elif ocupados > 0:
    print('\nLista de itens:')
    for item in inventario:
        print(f'{item[0]} [{item[1]}]')

if pochetes == 0:
    print('\nVocê ainda não encontrou pochetes. Seus espaços continuam os mesmos.')
elif pochetes > 0:
    print(f'\nVoce conseguiu {pochetes} pochete(s) e agora possui {slots + 2 * pochetes} slots de inventario.')
    print(f'Espacos sobrando [{novos_espacos()}]')