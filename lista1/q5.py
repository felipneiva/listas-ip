nome1, nota1, duracao1 = input('').split('-')
nome2, nota2, duracao2 = input('').split('-')
nome3, nota3, duracao3 = input('').split('-')
if nota1 > nota2 and nota1 > nota3:
    print(nome1)
elif nota2 > nota1 and nota2 > nota3:
    print(nome2)
elif nota3 > nota1 and nota3 > nota2:
    print(nome3)
elif float(nota1) < 4 and float(nota2) < 4 and float(nota3) < 4:
    print('Nota minima nao atingida')
elif nota1 == nota2:
    if duracao1 < duracao2:
        print(nome1)
    if duracao2 < duracao1:
        print(nome2)
elif nota1 == nota3:
    if duracao1 < duracao3:
        print(nome1)
    if duracao3 < duracao1:
        print(nome3)
elif nota2 == nota3:
    if duracao2 < duracao3:
        print(nome2)
    if duracao3 < duracao2:
        print(nome3)
elif nota1 == nota2 == nota3:
    if duracao1 < duracao2 and duracao1 < duracao3:
        print(nome1)
    if duracao2 < duracao1 and duracao2 < duracao3:
        print(nome2)
    if duracao3 < duracao1 and duracao3 < duracao2:
        print(nome3)

