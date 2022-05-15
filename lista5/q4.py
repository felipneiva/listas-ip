def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def barra_vida(vidab, vida):
    barra = []
    fracao = (vida / vidab) * 10
    if vida < 0:
        asteriscos = 0
    else:
        asteriscos = int(fracao + 0.99)
    for i in range(asteriscos):
        barra.append('*')
    for i in range(10-asteriscos):
        barra.append('-')
    return barra


def luta(n1, n2, a1, a2, d1, d2, ae1, ae2, vb, v1, v2, r):
    if v1 <= 0:
        return f'O vencedor da luta foi {n2}'
    elif v2 <= 0:
        return f'O vencedor da luta foi {n1}'
    r += 1

    if r < 5:
        if r % 2 != 0:
            v2 -= (a1 - d2)
            print(f'\nROUND {r}:')
            print(f'VIDA {n1}:')
            print(' '.join(barra_vida(vb, v1)))
            print(f'VIDA {n2}:')
            print(' '.join(barra_vida(vb, v2)))
            return luta(n1, n2, a1, a2, d1, d2, ae1, ae2, vb, v1, v2, r)
        elif r % 2 == 0:
            v1 -= (a2 - d1)
            print(f'\nROUND {r}:')
            print(f'VIDA {n1}:')
            print(' '.join(barra_vida(vb, v1)))
            print(f'VIDA {n2}:')
            print(' '.join(barra_vida(vb, v2)))
            return luta(n1, n2, a1, a2, d1, d2, ae1, ae2, vb, v1, v2, r)
    else:
        if r % 2 != 0:
            if fibonacci(r) % 2 == 0:
                v2 -= ae1
                print(f'\nROUND {r}:')
                print(f'VIDA {n1}:')
                print(' '.join(barra_vida(vb, v1)))
                print(f'VIDA {n2}:')
                print(' '.join(barra_vida(vb, v2)))
                return luta(n1, n2, a1, a2, d1, d2, ae1, ae2, vb, v1, v2, r)
            else:
                v2 -= (a1 - d2)
                print(f'\nROUND {r}:')
                print(f'VIDA {n1}:')
                print(' '.join(barra_vida(vb, v1)))
                print(f'VIDA {n2}:')
                print(' '.join(barra_vida(vb, v2)))
                return luta(n1, n2, a1, a2, d1, d2, ae1, ae2, vb, v1, v2, r)
        elif r % 2 == 0:
            if fibonacci(r) % 2 == 0:
                v1 -= ae2
                print(f'\nROUND {r}:')
                print(f'VIDA {n1}:')
                print(' '.join(barra_vida(vb, v1)))
                print(f'VIDA {n2}:')
                print(' '.join(barra_vida(vb, v2)))
                return luta(n1, n2, a1, a2, d1, d2, ae1, ae2, vb, v1, v2, r)
            else:
                v1 -= (a2 - d1)
                print(f'\nROUND {r}:')
                print(f'VIDA {n1}:')
                print(' '.join(barra_vida(vb, v1)))
                print(f'VIDA {n2}:')
                print(' '.join(barra_vida(vb, v2)))
                return luta(n1, n2, a1, a2, d1, d2, ae1, ae2, vb, v1, v2, r)


nome1 = input()
ataque1 = int(input())
defesa1 = int(input())
ataque_esp1 = int(input())
nome2 = input()
ataque2 = int(input())
defesa2 = int(input())
ataque_esp2 = int(input())
vida_base = int(input()) * 100
nround = 0

print(luta(nome1, nome2, ataque1, ataque2, defesa1, defesa2, ataque_esp1, ataque_esp2, vida_base, vida_base, vida_base, nround))
