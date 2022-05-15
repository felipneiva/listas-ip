# variaveis

vilao1 = input('')
poder1 = int(input(''))
local1 = int(input(''))
vilao2 = input('')
poder2 = int(input(''))
local2 = int(input(''))
destruicao1 = ((poder1 **2) * local1) / 2
destruicao2 = ((poder2 **2) * local2) / 2

# outputs

if (poder1 or poder2) < 0:
    print('Nem faco essa comparacao! Quero ser um vingador, busco coisas maiores.')
elif destruicao1 > destruicao2:
    print(f'Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {vilao1}.')
elif destruicao2 > destruicao1:
    print(f'Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {vilao2}.')
elif destruicao1 == destruicao2:
    if (destruicao1 % 2) == 0:
        print('E quem disse que isso e problema meu? Vou chamar o senhor Stark.')
    else:
        print('Vou chamar uns reforcos de outro universo... rsrs')
