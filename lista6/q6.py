def ship(dic1, dic2):
    nome1 = list(dic1['Nome'])
    nome2 = list(dic2['Nome'])
    index1 = ''
    index2 = ''
    fim = False
    for letra1 in nome1:
        if fim:
            break
        for letra2 in nome2[1:]:
            if letra1 == letra2:
                index1 = nome1.index(letra1)
                index2 = nome2.index(letra2)
                fim = True
                break
    if fim:
        return ''.join(nome1[:index1] + nome2[index2:]), True
    else:
        metade1 = len(nome1) // 2
        metade2 = len(nome2) // 2
        return ''.join(nome1[:metade1] + nome2[metade2:]), False


def azeitona(dic1, dic2):
    if (dic1['Azeitona'] == 'sim' and dic2['Azeitona']) == 'nao' or (dic1['Azeitona'] == 'nao' and dic2['Azeitona'] == 'sim'):
        return True
    else:
        return False


def midia(dic1, dic2, tipo):
    semelhancas = 0
    for resposta1 in dic1[tipo]:
        for resposta2 in dic2[tipo]:
            if resposta1 == resposta2:
                semelhancas += 1
    return semelhancas


signos = {'01': 'Capricórnio', '02': 'Aquário', '03': 'Peixes', '04': 'Áries', '05': 'Touro', '06': 'Gêmeos',
          '07': 'Câncer', '08': 'Leão', '09': 'Virgem', '10': 'Libra', '11': 'Escorpião', '12': 'Sagitário'}

agua = ('Câncer', 'Peixes', 'Escorpião')
fogo = ('Áries', 'Leão', 'Sagitário')
terra = ('Touro', 'Virgem', 'Capricórnio')
ar = ('Gêmeos', 'Libra', 'Aquário')

informacoes1 = {}
informacoes2 = {}

pessoa1 = True
pessoa2 = True
porcentagem = 0

print('Digite seu nome e o nome do/da Crush:')

informacoes1['Nome'] = input()
informacoes2['Nome'] = input()

while pessoa1:
    entrada = input()
    if entrada == '---':
        pessoa1 = False
    else:
        entrada = entrada.split(' ')
        if len(entrada) == 2:
            informacoes1[entrada[0]] = entrada[1]
        else:
            informacoes1[entrada[0]] = entrada[1:]

while pessoa2:
    try:
        entrada = input().split(' ')
        if len(entrada) == 2:
            informacoes2[entrada[0]] = entrada[1]
        else:
            informacoes2[entrada[0]] = entrada[1:]
    except EOFError as e:
        pessoa2 = False

if ship(informacoes1, informacoes2)[-1]:
    porcentagem += 20

if 'Azeitona' in informacoes1 and 'Azeitona' in informacoes2:
    if azeitona(informacoes1, informacoes2):
        porcentagem += 50

if 'Filmes' in informacoes1 and 'Filmes' in informacoes2:
    porcentagem += midia(informacoes1, informacoes2, 'Filmes') * 2

if 'Series' in informacoes1 and 'Series' in informacoes2:
    porcentagem += midia(informacoes1, informacoes2, 'Series') * 2

if 'Musicas' in informacoes1 and 'Musicas' in informacoes2:
    porcentagem += midia(informacoes1, informacoes2, 'Musicas') * 2

if 'Livros' in informacoes1 and 'Livros' in informacoes2:
    porcentagem += midia(informacoes1, informacoes2, 'Livros') * 2

if 'Aniversario' in informacoes1 and 'Aniversario' in informacoes2:
    mes1 = informacoes1['Aniversario'].split('/')[1]
    mes2 = informacoes2['Aniversario'].split('/')[1]
    if mes1 == mes2:
        porcentagem += 10
    else:
        if (signos[mes1] in ar and signos[mes2] in agua) or (signos[mes2] in ar and signos[mes1] in agua):
            porcentagem += 5
        elif (signos[mes1] in fogo and signos[mes2] in terra) or (signos[mes2] in fogo and signos[mes1] in terra):
            porcentagem += 5

for caracteristica in informacoes1:
    if caracteristica != 'Azeitona' and caracteristica != 'Aniversario' and caracteristica != 'Filmes' and caracteristica != 'Series' and caracteristica != 'Musicas':
        if informacoes1[caracteristica] == informacoes2[caracteristica]:
            porcentagem += 3

print(f'Hmmm, estou sentindo a conexão entre vocês... {ship(informacoes1, informacoes2)[0]} é um bom ship!')
print(f'Vocês combinam {porcentagem}%!')
