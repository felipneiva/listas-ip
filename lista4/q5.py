sobreviventes = ['Sam', 'Chris', 'Ashley', 'Jessica', 'Mike', 'Emily', 'Matt']

matriz = [[-1, 5, 5, 5, 5, 5, 5], [5, -1, 6, 5, 5, 5, 5], [5, 6, -1, 5, 5, 5, 5], [5, 5, 5, -1, 7, 4, 5],
          [5, 5, 5, 7, -1, 3, 4], [5, 5, 5, 4, 3, -1, 7], [5, 5, 5, 5, 4, 7, -1]]


def interacao(a, b, c):
    index1 = 0
    index2 = 0
    if a == 'Sam':
        index1 = 0
    elif a == 'Chris':
        index1 = 1
    elif a == 'Ashley':
        index1 = 2
    elif a == 'Jessica':
        index1 = 3
    elif a == 'Mike':
        index1 = 4
    elif a == 'Emily':
        index1 = 5
    elif a == 'Matt':
        index1 = 6
    if b == 'Sam':
        index2 = 0
    elif b == 'Chris':
        index2 = 1
    elif b == 'Ashley':
        index2 = 2
    elif b == 'Jessica':
        index2 = 3
    elif b == 'Mike':
        index2 = 4
    elif b == 'Emily':
        index2 = 5
    elif b == 'Matt':
        index2 = 6
    if c == 'O':
        matriz[index1][index2] += 1
        matriz[index2][index1] += 1
    elif c == 'X':
        matriz[index1][index2] -= 1
        matriz[index2][index1] -= 1


def sobreviver(a):
    index = 0
    if a in sobreviventes:
        if a == 'Sam':
            index = 0
        elif a == 'Chris':
            index = 1
        elif a == 'Ashley':
            index = 2
        elif a == 'Jessica':
            index = 3
        elif a == 'Mike':
            index = 4
        elif a == 'Emily':
            index = 5
        elif a == 'Matt':
            index = 6
        if (sum(matriz[index]) + 1) / 6 > 5:
            print(f'UFA!!! foi por pouco mas {a} conseguiu escapar do Wendigo.')
        else:
            print(f'{a} infelizmente nao conseguiu sobreviver ao ataque do Wendigo.')
            sobreviventes.remove(a)
    else:
        print('entrada invalida!!! voce so pode jogar com jogadores vivos')


def sobrevive(a, b):
    index1 = 0
    index2 = 0
    if a in sobreviventes and b in sobreviventes:
        if a == 'Sam':
            index1 = 0
        elif a == 'Chris':
            index1 = 1
        elif a == 'Ashley':
            index1 = 2
        elif a == 'Jessica':
            index1 = 3
        elif a == 'Mike':
            index1 = 4
        elif a == 'Emily':
            index1 = 5
        elif a == 'Matt':
            index1 = 6
        if b == 'Sam':
            index2 = 0
        elif b == 'Chris':
            index2 = 1
        elif b == 'Ashley':
            index2 = 2
        elif b == 'Jessica':
            index2 = 3
        elif b == 'Mike':
            index2 = 4
        elif b == 'Emily':
            index2 = 5
        elif b == 'Matt':
            index2 = 6
        if matriz[index1][index2] > 6:
            print(f'felizmente {b} ajudou {a} a escapar do Wendigo.')
        else:
            print(f'que pena! {b} nao conseguiu ajudar {a} do ataque do Wendigo.')
            sobreviventes.remove(a)
    else:
        print('entrada invalida!!! voce so pode jogar com jogadores vivos')

interacoes = int(input())
for i in range(interacoes):
    inter = input().split(' ')
    interacao(inter[0], inter[2], inter[1])

dinamicas = int(input())
for i in range(dinamicas):
    entrada = input()
    if entrada == 'Sam' or entrada == 'Chris' or entrada == 'Ashley' or entrada == 'Jessica' or entrada == 'Mike' or entrada == 'Emily' or entrada == 'Matt':
        sobreviver(entrada)
    else:
        entrada = entrada.split(' ')
        sobrevive(entrada[0], entrada[2])

if len(sobreviventes) > 0:
    print('\nSobreviventes:')
    for nome in sobreviventes:
        print(nome)
else:
    print('\nTristemente, ninguém sobreviveu')


