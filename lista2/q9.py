# vidas, palavra inicial e palavra desejada

vidas = 3
palavra = '-----------------'
palavra_final = 'PROVA-DO-ANJO-BBB'
letras_digitadas = 0

# letras ainda que ainda não foram chutadas

a, b, c, d, e, f, g, h, i, j, k, l, m = False, False, False, False, False, False, False, False, False, False, False, False, False
n, o, p, q, r, s, t, u, v, w, x, y, z = False, False, False, False, False, False, False, False, False, False, False, False, False


# comando while

while vidas > 0 and not(palavra == palavra_final):
    letra = input('').upper()
    letras_digitadas += 1
    if letra == 'P' and not p:
        print('Parabens, voce conseguiu mais uma letra!')
        p = True
        palavra = palavra[0].replace('-', 'P') + palavra[1:]
    elif letra == 'R' and not r:
        print('Parabens, voce conseguiu mais uma letra!')
        r = True
        palavra = palavra[0] + palavra[1].replace('-', 'R') + palavra[2:]
    elif letra == 'O' and not o:
        print('Parabens, voce conseguiu mais uma letra!')
        o = True
        palavra = palavra[0:2] + palavra[2].replace('-', 'O') + palavra[3:7] + palavra[7].replace('-', 'O') + palavra[8:12] + palavra[12].replace('-', 'O') + palavra[13:]
    elif letra == 'V' and not v:
        print('Parabens, voce conseguiu mais uma letra!')
        v = True
        palavra = palavra[0:3] + palavra[3].replace('-', 'V') + palavra[4:]
    elif letra == 'A' and not a:
        print('Parabens, voce conseguiu mais uma letra!')
        a = True
        palavra = palavra[0:4] + palavra[4].replace('-', 'A') + palavra[5:9] + palavra[9].replace('-', 'A') + palavra[10:]
    elif letra == 'D' and not d:
        print('Parabens, voce conseguiu mais uma letra!')
        d = True
        palavra = palavra[0:6] + palavra[6].replace('-', 'D') + palavra[7:]
    elif letra == 'N' and not n:
        print('Parabens, voce conseguiu mais uma letra!')
        n = True
        palavra = palavra[0:10] + palavra[10].replace('-', 'N') + palavra[11:]
    elif letra == 'J' and not j:
        print('Parabens, voce conseguiu mais uma letra!')
        j = True
        palavra = palavra[0:11] + palavra[11].replace('-', 'J') + palavra[12:]
    elif letra == 'B' and not b:
        print('Parabens, voce conseguiu mais uma letra!')
        b = True
        palavra = palavra[0:14] + palavra[14:].replace('-', 'B')
    elif letra == 'P' and p:
        print(f'Voce ja digitou a letra {letra}')
    elif letra == 'R' and r:
        print(f'Voce ja digitou a letra {letra}')
    elif letra == 'O' and o:
        print(f'Voce ja digitou a letra {letra}')
    elif letra == 'V' and v:
        print(f'Voce ja digitou a letra {letra}')
    elif letra == 'A' and a:
        print(f'Voce ja digitou a letra {letra}')
    elif letra == 'D' and d:
        print(f'Voce ja digitou a letra {letra}')
    elif letra == 'N' and n:
        print(f'Voce ja digitou a letra {letra}')
    elif letra == 'J' and j:
        print(f'Voce ja digitou a letra {letra}')
    elif letra == 'B' and b:
        print(f'Voce ja digitou a letra {letra}')
    else:
        if letra == 'C' and not c:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            c = True
        elif letra == 'E' and not e:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            e = True
        elif letra == 'F' and not f:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            f = True
        elif letra == 'G' and not g:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            g = True
        elif letra == 'H' and not h:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            h = True
        elif letra == 'I' and not i:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            i = True
        elif letra == 'K' and not k:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            k = True
        elif letra == 'L' and not l:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            l = True
        elif letra == 'M' and not m:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            m = True
        elif letra == 'Q' and not q:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            q = True
        elif letra == 'S' and not s:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            s = True
        elif letra == 'T' and not t:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            t = True
        elif letra == 'U' and not u:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            u = True
        elif letra == 'W' and not w:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            w = True
        elif letra == 'X' and not x:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            x = True
        elif letra == 'Y' and not y:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            y = True
        elif letra == 'Z' and not z:
            vidas -= 1
            if vidas > 0:
                print(f'Que pena, voce tem mais {vidas} chances!')
            z = True
        elif letra == 'C' and c:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'E' and e:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'F' and f:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'G' and g:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'H' and h:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'I' and i:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'K' and k:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'L' and l:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'M' and m:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'Q' and q:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'S' and s:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'T' and t:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'U' and u:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'W' and w:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'X' and x:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'Y' and y:
            print(f'Voce ja digitou a letra {letra}')
        elif letra == 'Z' and z:
            print(f'Voce ja digitou a letra {letra}')

    if vidas > 0:
        print(palavra)

# outputs(vitória ou derrota)

if palavra == palavra_final:
    print('Boa, voce e o novo Anjo da semana!')
elif vidas <= 0:
    print('Fim de jogo, sem almoco do anjo pra voce!')
