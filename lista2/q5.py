# variáveis

letra = input('')
numero = int(input(''))


# letra X

o = 0
meio = numero - 4
valoromax = 0
valormeiomin = ''

# entrada inválida

if numero <= 1 or numero % 2 == 0 or (letra != 'T' and letra != 'X' and letra != 'O'):
    print('Entrada não permitida')

# entrada válida

else:
    if letra == 'O':
        for i in range(0, numero):
            if i == 0:
                print(numero * 'X')
                print()
            elif i == numero - 1:
                print(numero * 'X')
            else:
                print('X' + (numero - 2) * '0' + 'X')
                print()
    elif letra == 'T':
        for i in range(0, numero):
            if i == 0:
                print(numero * 'X')
                print()
            elif i == numero - 1:
                print(int((numero / 2)) * '0' + 'X' + int((numero / 2)) * '0')
            else:
                print(int((numero / 2)) * '0' + 'X' + int((numero / 2)) * '0')
                print()
    elif letra == 'X':
        for i in range(0, numero):
            if i == 0:
                print('X' + (numero - 2) * '0' + 'X')
                print()
            elif i == (numero - 1) / 2:
                print(int((numero / 2)) * '0' + 'X' + int((numero / 2)) * '0')
                print()
            elif i == numero - 1:
                print('X' + (numero - 2) * '0' + 'X')
            else:
                while len((o+1) * '0' + 'X' + meio * '0' + 'X' + (o+1) * '0') == numero:
                    print((o+1) * '0' + 'X' + meio * '0' + 'X' + (o+1) * '0')
                    print()
                    valoromax = o
                    valormeiomin = meio
                    o += 1
                    meio -= 2
                if (numero - 1) / 2 < i < numero - 1:
                    print((valoromax + 1) * '0' + 'X' + valormeiomin * '0' + 'X' + (valoromax + 1) * '0')
                    print()
                    valoromax -= 1
                    valormeiomin += 2




