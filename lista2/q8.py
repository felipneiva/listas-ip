# variáveis

acidez = 20
agua = 15
tempero = 10

# comando while

while not agua == acidez == tempero:

    pontos = int(input(''))
    acao = input('')
    if acao == 'reduzir agua':
        agua -= pontos
        tempero += (pontos - 1)
    elif acao == 'adicionar agua':
        agua += pontos
        tempero -= (pontos + 2)
    elif acao == 'reduzir acidez':
        acidez -= pontos
    elif acao == 'aumentar acidez':
        acidez += pontos
    elif acao == 'aumentar tempero':
        tempero += pontos

    minimo = min(acidez, agua, tempero)

    if agua == acidez == tempero:
        print('Tem sabor, tem apresentacion, tem tudibon! sobe no mezanin')
    else:
        if agua == minimo:
            print('Muit seca! melhorre a combinaçon')
        if tempero == minimo:
            print('Falta tomperro! non agradou meu paladar')
        if acidez == minimo:
            print('Falta acidez! non pode subir o mezanin')



