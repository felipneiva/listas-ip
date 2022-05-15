def zelda(matriz, x, y, princesa, derrota):
    if princesa:
        for linha in matriz[1:-1]:
            print(''.join(linha)[1:-1])
        return 'Vamos embora daqui Princesa!!!'
    elif derrota:
        return 'HAHAHAHA você nunca irá resgatá-la, Link!!!'
    else:
        if matriz[y + 1][x] == '.':
            matriz[y + 1][x] = 'L'
            y += 1
            for linha in matriz[1:-1]:
                print(''.join(linha)[1:-1])
            print('Caminharei pelo Sul e certamente irei encontrar-te, Zelda')
            print('')
            return zelda(matriz, x, y, princesa, derrota)
        elif matriz[y + 1][x] == 'Z':
            matriz[y + 1][x] = 'L'
            y += 1
            for linha in matriz[1:-1]:
                print(''.join(linha)[1:-1])
            print('Caminharei pelo Sul e certamente irei encontrar-te, Zelda')
            print('')
            princesa = True
            return zelda(matriz, x, y, princesa, derrota)
        elif matriz[y + 1][x] != '.':
            if matriz[y][x + 1] == '.':
                matriz[y][x+1] = 'L'
                x += 1
                for linha in matriz[1:-1]:
                    print(''.join(linha)[1:-1])
                print('Caminharei pelo Leste e certamente irei encontrar-te, Zelda')
                print('')
                return zelda(matriz, x, y, princesa, derrota)
            elif matriz[y][x + 1] == 'Z':
                matriz[y][x+1] = 'L'
                x += 1
                for linha in matriz[1:-1]:
                    print(''.join(linha)[1:-1])
                print('Caminharei pelo Leste e certamente irei encontrar-te, Zelda')
                print('')
                princesa = True
                return zelda(matriz, x, y, princesa, derrota)
            elif matriz[y][x + 1] != '.':
                if matriz[y-1][x] == '.':
                    matriz[y-1][x] = 'L'
                    y -= 1
                    for linha in matriz[1:-1]:
                        print(''.join(linha)[1:-1])
                    print('Caminharei pelo Norte e certamente irei encontrar-te, Zelda')
                    print('')
                    return zelda(matriz, x, y, princesa, derrota)
                elif matriz[y-1][x] == 'Z':
                    matriz[y - 1][x] = 'L'
                    y -= 1
                    for linha in matriz[1:-1]:
                        print(''.join(linha)[1:-1])
                    print('Caminharei pelo Norte e certamente irei encontrar-te, Zelda')
                    print('')
                    princesa = True
                    return zelda(matriz, x, y, princesa, derrota)
                elif matriz[y - 1][x] != '.':
                    if matriz[y][x-1] == '.':
                        matriz[y][x - 1] = 'L'
                        x -= 1
                        for linha in matriz[1:-1]:
                            print(''.join(linha)[1:-1])
                        print('Caminharei pelo Oeste e certamente irei encontrar-te, Zelda')
                        print('')
                        return zelda(matriz, x, y, princesa, derrota)
                    elif matriz[y][x-1] == 'Z':
                        matriz[y][x - 1] = 'L'
                        x -= 1
                        for linha in matriz[1:-1]:
                            print(''.join(linha)[1:-1])
                        print('Caminharei pelo Oeste e certamente irei encontrar-te, Zelda')
                        print('')
                        princesa = True
                        return zelda(matriz, x, y, princesa, derrota)
                    elif matriz[y][x-1] != '.':
                        derrota = True
                        return zelda(matriz, x, y, princesa, derrota)


achou = False
perdeu = False

labirinto = []

n = int(input())
yl = int(input())
xl = int(input())

for i in range(n):
    linha = list(input())
    linha.insert(0, '#')
    linha.append('#')
    labirinto.append(linha)

labirinto.insert(0, ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'])
labirinto.append(['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'])

print(zelda(labirinto, xl+1, yl+1, achou, perdeu))
