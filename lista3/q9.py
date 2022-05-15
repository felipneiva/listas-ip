matriz = []
linhas, colunas = input().split()

for i in range(int(linhas)):
    linha = input()
    linha = '...' + linha + '...'
    matriz.append(linha)

matriz.insert(0, (int(colunas) + 6) * '.')
matriz.insert(0, (int(colunas) + 6) * '.')
matriz.insert(0, (int(colunas) + 6) * '.')
matriz.append((int(colunas) + 6) * '.')
matriz.append((int(colunas) + 6) * '.')
matriz.append((int(colunas) + 6) * '.')

achou = False

idxl = 0
for linha in matriz:
    if achou:
        break
    idx = 0
    for caractere in linha:
        if caractere == '*':
            if linha[idx-1] == linha[idx+1] == matriz[idxl-1][idx] == matriz[idxl+1][idx] == '*':
                if linha[idx-2] == linha[idx+2] == matriz[idxl-2][idx] == matriz[idxl+2][idx] == '.':
                    achou = True
                    print('Nao foi um dos melhores, mas ta valendo...')
                    break
                elif linha[idx-2] == linha[idx+2] == matriz[idxl-2][idx] == matriz[idxl+2][idx] == '*':
                    if linha[idx-3] == linha[idx+3] == matriz[idxl-3][idx] == matriz[idxl+3][idx] == '.':
                        achou = True
                        print('Esta perfeito, quase peguei toda a premiaçao, UHUL!!')
                        break
                    elif linha[idx-3] == linha[idx+3] == matriz[idxl-3][idx] == matriz[idxl+3][idx] == '*':
                        if linha[idx-4] == linha[idx+4] == matriz[idxl-4][idx] == matriz[idxl+4][idx] == '.':
                            achou = True
                            print('AEEEEW, ACHEI O PRECIOSO!!!!')
                            break
        idx += 1
    idxl += 1
if not achou:
    print('Puts, dessa vez nao tive sorte...')