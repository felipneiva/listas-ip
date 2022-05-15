matriz = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]

yp = int(input())
xp = int(input())
yj = int(input())
xj = int(input())
yg = int(input())
xg = int(input())
yc = int(input())
xc = int(input())

matriz[yp][xp] = 'V'
matriz[yj][xj] = 'J'
matriz[yg][xg] = 'G'
matriz[yc][xc] = 'C'

objetos = ['V', 'J', 'G', 'C']


def jason():
    novox = xj
    novoy = yj
    if xj != xp:
        if xj > xp:
            matriz[yj][xj], matriz[yj][xj - 1] = matriz[yj][xj - 1], matriz[yj][xj]
            novox -= 1
        elif xj < xp:
            matriz[yj][xj], matriz[yj][xj + 1] = matriz[yj][xj + 1], matriz[yj][xj]
            novox += 1
    elif xj == xp:
        if yj > yp:
            if matriz[yj - 1][xj] != 'V' and matriz[yj - 1][xj] != 'G' and matriz[yj - 1][xj] != 'C':
                matriz[yj][xj], matriz[yj - 1][xj] = matriz[yj - 1][xj], matriz[yj][xj]
                novoy -= 1
            elif matriz[yj - 1][xj] == 'V':
                matriz[yj][xj], matriz[yj - 1][xj] = '-', matriz[yj][xj]
                objetos.remove('V')
                novoy -= 1
            elif matriz[yj - 1][xj] == 'G':
                matriz[yj][xj], matriz[yj - 1][xj] = '-', matriz[yj][xj]
                novoy -= 1
            elif matriz[yj - 1][xj] == 'C':
                matriz[yj][xj], matriz[yj - 1][xj] = '-', matriz[yj][xj]
                novoy -= 1
        elif yj < yp:
            if matriz[yj + 1][xj] != 'V' and matriz[yj + 1][xj] != 'G' and matriz[yj + 1][xj] != 'C':
                matriz[yj][xj], matriz[yj + 1][xj] = matriz[yj + 1][xj], matriz[yj][xj]
                novoy += 1
            elif matriz[yj + 1][xj] == 'V':
                matriz[yj][xj], matriz[yj + 1][xj] = '-', matriz[yj][xj]
                objetos.remove('V')
                novoy += 1
            elif matriz[yj + 1][xj] == 'G':
                matriz[yj][xj], matriz[yj + 1][xj] = '-', matriz[yj][xj]
                novoy += 1
            elif matriz[yj + 1][xj] == 'C':
                matriz[yj][xj], matriz[yj + 1][xj] = '-', matriz[yj][xj]
                novoy += 1
    return novox, novoy


def pessoa_gasolina():
    novox = xp
    novoy = yp
    if xp != xg:
        if xp > xg:
            matriz[yp][xp], matriz[yp][xp - 1] = matriz[yp][xp - 1], matriz[yp][xp]
            novox -= 1
        elif xp < xg:
            matriz[yp][xp], matriz[yp][xp + 1] = matriz[yp][xp + 1], matriz[yp][xp]
            novox += 1
    elif xp == xg:
        if yp > yg:
            if matriz[yp - 1][xp] != 'G':
                matriz[yp - 1][xp], matriz[yp][xp] = matriz[yp][xp], matriz[yp-1][xp]
                novoy -= 1
            elif matriz[yp - 1][xp == 'G']:
                matriz[yg][xg], matriz[yp][xp] = matriz[yp][xp], '-'
                objetos.remove('G')
                novoy -= 1
        elif yp < yg:
            if matriz[yp + 1][xp] != 'G':
                matriz[yp+1][xp], matriz[yp][xp] = matriz[yp][xp], matriz[yp+1][xp]
                novoy += 1
            elif matriz[yp + 1][xp] == 'G':
                matriz[yg][xg], matriz[yp][xp] = matriz[yp][xp], '-'
                objetos.remove('G')
                novoy += 1
    return novox, novoy


def pessoa_carro():
    novox = xp
    novoy = yp
    if yp != yc:
        if xp != xc:
            if xp > xc:
                matriz[yp][xp], matriz[yp][xp - 1] = matriz[yp][xp - 1], matriz[yp][xp]
                novox -= 1
            elif xp < xc:
                matriz[yp][xp], matriz[yp][xp + 1] = matriz[yp][xp + 1], matriz[yp][xp]
                novox += 1
        elif xp == xc:
            if yp > yc:
                if matriz[yp - 1][xp] != 'C':
                    matriz[yp - 1][xp], matriz[yp][xp] = matriz[yp][xp], matriz[yp-1][xp]
                    novoy -= 1
                else:
                    matriz[yp - 1][xp], matriz[yp][xp] = matriz[yp][xp], '-'
                    objetos.remove('C')
                    novoy -= 1
            elif yp < yc:
                if matriz[yp + 1][xp] != 'C':
                    matriz[yp + 1][xp], matriz[yp][xp] = matriz[yp][xp], matriz[yp+1][xp]
                    novoy += 1
                else:
                    matriz[yp + 1][xp], matriz[yp][xp] = matriz[yp][xp], '-'
                    objetos.remove('C')
                    novoy += 1
    elif yp == yc:
        if xp > xc:
            if matriz[yp][xp - 1] != 'C':
                matriz[yp][xp], matriz[yp][xp - 1] = matriz[yp][xp - 1], matriz[yp][xp]
                novox -= 1
            else:
                matriz[yp][xp], matriz[yp][xp - 1] = '-', matriz[yp][xp]
                objetos.remove('C')
                novox -= 1
        elif xp < xc:
            if matriz[yp][xp + 1] != 'C':
                matriz[yp][xp], matriz[yp][xp + 1] = matriz[yp][xp + 1], matriz[yp][xp]
                novox += 1
            else:
                matriz[yp][xp], matriz[yp][xp + 1] = '-', matriz[yp][xp]
                objetos.remove('C')
                novox += 1
    return novox, novoy


def distancia():
    dist = ''
    distancia = int((((xp - xj)**2) + ((yp - yj)**2))**0.5)
    if distancia <= 3:
        dist = 'E melhor correr, o Jason vai me pegar!'
    elif 3 < distancia <= 4:
        dist = 'Consigo ver o Jason daqui, preciso apressar o passo!'
    elif distancia > 4:
        dist = 'Ufa, o Jason ainda esta longe, mas nao posso diminuir o ritmo.'
    return dist


while 'V' in objetos and 'G' in objetos:
    xj, yj = jason()
    if 'V' in objetos:
        xp, yp = pessoa_gasolina()
    for linha in matriz:
        print(' '.join(linha))
    if 'G' in objetos and 'V' in objetos:
        print('Nao peguei nenhum objeto nessa rodada :(')
        print(distancia())
        print()
    elif 'V' in objetos and 'G' not in objetos:
        print('Deu bom! Peguei a Gasolina nessa rodada.')
        print(distancia())
        print()
    elif 'V' not in objetos:
        print('Oh nao, o Jason me pegou, F total!')

if 'V' in objetos:
    xj, yj = jason()
    for linha in matriz:
        print(' '.join(linha))
    if 'C' in objetos and 'V' in objetos:
        print('Nao peguei nenhum objeto nessa rodada :(')
        print(distancia())
        print()

while 'V' in objetos and 'C' in objetos:
    xj, yj = jason()
    if 'V' in objetos:
        xp, yp = pessoa_carro()
    for linha in matriz:
        print(' '.join(linha))
    if 'C' in objetos and 'V' in objetos:
        print('Nao peguei nenhum objeto nessa rodada :(')
        print(distancia())
        print()
    elif 'V' in objetos and 'C' not in objetos:
        print('Consegui chegar no carro, agora e so ligar e fugir daqui!')
    elif 'V' not in objetos:
        print('Oh nao, o Jason me pegou, F total!')