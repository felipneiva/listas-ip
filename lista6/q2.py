def probab(pessoa, empresas):
    prob_inicial = (pessoa['anos'] / pessoa['idade']) * 100 if pessoa['idade'] != 0 else 0
    if pessoa['idade'] >= 50 and prob_inicial >= 30:
        if pessoa['empresa'] == empresas['maior']:
            return int(prob_inicial + (0.15 * prob_inicial))
        elif pessoa['empresa'] == empresas['meio']:
            return int(prob_inicial + (0.10 * prob_inicial))
        elif pessoa['empresa'] == empresas['menor']:
            return int(prob_inicial + (0.05 * prob_inicial))
    elif pessoa['idade'] <= 30 and prob_inicial >= 40:
        if pessoa['empresa'] == empresas['maior']:
            return int(prob_inicial + (0.30 * prob_inicial))
        elif pessoa['empresa'] == empresas['meio']:
            return int(prob_inicial + (0.25 * prob_inicial))
        elif pessoa['empresa'] == empresas['menor']:
            return int(prob_inicial + (0.20 * prob_inicial))
    elif prob_inicial >= 20:
        if pessoa['empresa'] == empresas['maior']:
            return int(prob_inicial + (0.10 * prob_inicial))
        elif pessoa['empresa'] == empresas['meio']:
            return int(prob_inicial + (0.05 * prob_inicial))
        elif pessoa['empresa'] == empresas['menor']:
            return int(prob_inicial + (0.03 * prob_inicial))
    else:
        return int(prob_inicial)


candidatos = []
nomes = []

rivais = {'maior': input(), 'meio': input(), 'menor': input()}
continua = True

while continua:
    try:
        nome, idade, empresa, anos = input().split(' ')
        candidato = {'nome': nome, 'idade': int(idade), 'empresa': empresa, 'anos': int(anos)}
        candidato['prob'] = probab(candidato, rivais)
        if candidato["nome"] in nomes:
            print(f'{candidato["nome"]} ja esta participando da avaliacao!')
        elif candidato['empresa'] not in rivais.values():
            print(f'Nao ha ligacoes entre {candidato["nome"]} e as empresas concorrentes, prossiga tranquilamente com a entrevista.')
        else:
            nomes.append(nome)
            candidatos.append(candidato)
    except EOFError as e:
        continua = False

print('[ALERTA]! A SEGUIR UMA LISTA DOS POSSIVEIS ESPIOES')
for n in candidatos:
    print(f'{n["nome"]}:')
    print(f'- Idade: {n["idade"]}')
    print(f'- Antiga corporacao: {n["empresa"]}')
    print(f'- Anos trabalhos: {n["anos"]}')
    print(f'- Probabilidade de ser espiao: {n["prob"]}%')
