# variaveis

nome1 = input('')
pont1 = int(input(''))
nome2 = input('')
pont2 = int(input(''))
nome3 = input('')
pont3 = int(input(''))

# pontuacoes diferentes

if pont1 < pont2 < pont3:
    print(nome1, pont1)
    print(nome2, pont2)
    print(nome3, pont3)
elif pont1 < pont3 < pont2:
    print(nome1, pont1)
    print(nome3, pont3)
    print(nome2, pont2)
elif pont2 < pont3 < pont1:
    print(nome2, pont2)
    print(nome3, pont3)
    print(nome1, pont1)
elif pont2 < pont1 < pont3:
    print(nome2, pont2)
    print(nome1, pont1)
    print(nome3, pont3)
elif pont3 < pont2 < pont1:
    print(nome3, pont3)
    print(nome2, pont2)
    print(nome1, pont1)
elif pont3 < pont1 < pont2:
    print(nome3, pont3)
    print(nome1, pont1)
    print(nome2, pont2)

# todas as pontuacoes iguais

elif pont1 == pont2 == pont3:
    if nome1 < nome2 < nome3:
        print(nome1, pont1)
        print(nome2, pont2)
        print(nome3, pont3)
    elif nome1 < nome3 < nome2:
        print(nome1, pont1)
        print(nome3, pont3)
        print(nome2, pont2)
    elif nome2 < nome3 < nome1:
        print(nome2, pont2)
        print(nome3, pont3)
        print(nome1, pont1)
    elif nome2 < nome1 < nome3:
        print(nome2, pont2)
        print(nome1, pont1)
        print(nome3, pont3)
    elif nome3 < nome2 < nome1:
        print(nome3, pont3)
        print(nome2, pont2)
        print(nome1, pont1)
    elif nome3 < nome1 < nome2:
        print(nome3, pont3)
        print(nome1, pont1)
        print(nome2, pont2)

# casos com 2 pontuacoes iguais

elif pont1 == pont2 < pont3:
    if nome1 < nome2:
        print(nome1, pont1)
        print(nome2, pont2)
        print(nome3, pont3)
    elif nome2 < nome1:
        print(nome2, pont2)
        print(nome1, pont1)
        print(nome3, pont3)
elif pont3 < pont1 == pont2:
    if nome2 < nome1:
        print(nome3, pont3)
        print(nome2, pont2)
        print(nome1, pont1)
    elif nome1 < nome2:
        print(nome3, pont3)
        print(nome1, pont1)
        print(nome2, pont2)
elif pont1 == pont3 < pont2:
    if nome1 < nome3:
        print(nome1, pont1)
        print(nome3, pont3)
        print(nome2, pont2)
    elif nome3 < nome1:
        print(nome3, pont3)
        print(nome1, pont1)
        print(nome2, pont2)
elif pont2 < pont1 == pont3:
    if nome1 < nome3:
        print(nome2, pont2)
        print(nome1, pont1)
        print(nome3, pont3)
    elif nome3 < nome1:
        print(nome2, pont2)
        print(nome3, pont3)
        print(nome1, pont1)
elif pont2 == pont3 < pont1:
    if nome2 < nome3:
        print(nome2, pont2)
        print(nome3, pont3)
        print(nome1, pont1)
    elif nome3 < nome2:
        print(nome3, pont3)
        print(nome2, pont2)
        print(nome1, pont1)
elif pont1 < pont2 == pont3:
    if nome2 < nome3:
        print(nome1, pont1)
        print(nome2, pont2)
        print(nome3, pont3)
    elif nome3 < nome2:
        print(nome1, pont1)
        print(nome3, pont3)
        print(nome2, pont2)

