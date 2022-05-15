# variaveis

nome1 = input('')
vida1 = int(input(''))
ataque1 = int(input(''))
defesa1 = int(input(''))
nome2 = input('')
vida2 = int(input(''))
ataque2 = int(input(''))
defesa2 = int(input(''))
dano1 = 0
dano2 = 0
dano3 = 0

# round 1

print('Round 1')
movimento1 = str(input(''))
movimento2 = str(input(''))
if movimento1 == 'jab':
    if movimento2 == 'bloqueio':
        dano1 = ataque1 - (ataque1 * (defesa2/100))
    elif movimento2 == 'esquiva':
        ataque2 *= 1.1
        dano1 = 0
    elif movimento2 == 'X':
        dano1 = ataque1
elif movimento1 == 'direto':
    if movimento2 == 'bloqueio':
        dano1 = (ataque1 * 1.3) - (ataque1 * (defesa2/100))
    elif movimento2 == 'esquiva':
        ataque2 *= 1.2
        dano1 = 0
    elif movimento2 == 'X':
        dano1 = ataque1 * 1.4
vida2 = vida2 - dano1
if vida2 <= 0:
    print(f'NOSSO CAMPEAO E {nome1.upper()} COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND')

# round 2

else:
    print('Round 2')
    movimento3 = str(input(''))
    movimento4 = str(input(''))
    if movimento3 == 'jab':
        if movimento4 == 'bloqueio':
            dano2 = ataque2 - (ataque2 * (defesa1 / 100))
        elif movimento4 == 'esquiva':
            ataque1 *= 1.1
            dano2 = 0
        elif movimento4 == 'X':
            dano2 = ataque2
    elif movimento3 == 'direto':
        if movimento4 == 'bloqueio':
            dano2 = (ataque2 * 1.3) - (ataque2 * (defesa1 / 100))
        elif movimento4 == 'esquiva':
            ataque1 *= 1.2
            dano2 = 0
        elif movimento4 == 'X':
            dano2 = ataque2 * 1.4
    vida1 = vida1 - dano2
    if vida1 <= 0:
        print(f'NOSSO CAMPEAO E {nome2.upper()}')

# round3
    else:
        print('Round 3')
        print(f'{nome1.upper()} SO TEM MAIS UM ROUND PARA DERRUBAR SEU ADVERSARIO')
        movimento5 = str(input(''))
        movimento6 = str(input(''))
        if movimento5 == 'jab':
            if movimento6 == 'bloqueio':
                dano3 = ataque1 - (ataque1 * (defesa2 / 100))
            elif movimento6 == 'esquiva':
                ataque2 *= 1.1
                dano3 = 0
            elif movimento6 == 'X':
                dano3 = ataque1
        elif movimento5 == 'direto':
            if movimento6 == 'bloqueio':
                dano3 = (ataque1 * 1.3) - (ataque1 * (defesa2 / 100))
            elif movimento6 == 'esquiva':
                ataque2 *= 1.2
                dano3 = 0
            elif movimento6 == 'X':
                dano3 = ataque1 * 1.4
        vida2 = vida2 - dano3
        if vida2 <= 0:
            print(f'NOSSO CAMPEAO E {nome1.upper()}')
        else:
            print(f'NOSSO CAMPEAO E {nome2.upper()}')
