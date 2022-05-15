def palindromo(frase):
    if ''.join(frase.split()) == ''.join(frase[::-1].split()):
        return True
    else:
        return False


def pangrama(frase):
    letras = 0
    for letra in 'abcdefghijlmnopqrstuvxz':
        if letra in frase:
            letras += 1
    if letras == 23:
        return True
    else:
        return False


def epizeuxis(frase):
    achou = False
    lista = [frase.split()]
    for i in range(len(lista[0])):
        for j in range(i + 1, len(lista[0])):
            if lista[0][i] == lista[0][i+1]:
                achou = True
    if achou:
        return True
    elif not achou:
        return False


n = int(input())

for i in range(n):
    frase = input()
    if palindromo(frase):
        print(f'Freddy, "{frase}" é um palíndromo!')
    elif pangrama(frase):
        print(f'Tenho certeza de que "{frase}" é um pangrama!')
    elif epizeuxis(frase):
        print(f'Freddy, Freddy, "{frase}" é definitivamente uma epizeuxe!')
    else:
        print('Essa aqui é uma pegadinha, não há nada aqui!')
