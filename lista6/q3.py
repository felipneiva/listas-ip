premios = {'bichinho de pelucia': {'qtd': 10, 'preço': 750}, 'boneco articulado com armadura': {'qtd': 20, 'preço': 1000},
           'estatua de cena memoravel': {'qtd': 10, 'preço': 1250}, 'camiseta tematica': {'qtd': 10, 'preço': 500},
           'chaveiro': {'qtd': 50, 'preço': 250}, 'bolinhas': {'qtd': 10000, 'preço': 1000}}

resumo = {'dinheiro': 0, 'vendas': 0, 'resgates': 0, 'recebidas': 0, 'premios': 100}

continua = True

while continua:
    entrada = input()
    if entrada == 'comprar':
        quantidade = int(input())
        if premios['bolinhas']['qtd'] >= quantidade:
            print(f'O jogador comprou {quantidade} bolinhas por {quantidade*1000} ienes.')
            premios['bolinhas']['qtd'] -= quantidade
            resumo['dinheiro'] += quantidade*1000
            resumo['vendas'] += 1
        else:
            print('Nao ha mais bolinhas disponiveis, melhor esperar um pouco.')
    elif entrada == 'trocar':
        premio, nbolinhas = input().split(' - ')
        if premio in premios:
            if premios[premio]['qtd'] > 0 and int(nbolinhas) >= premios[premio]['preço']:
                print(f'O jogador trocou {premios[premio]["preço"]} bolinhas por um {premio}.')
                premios['bolinhas']['qtd'] += premios[premio]["preço"]
                premios[premio]['qtd'] -= 1
                resumo['resgates'] += 1
                resumo['premios'] -= 1
                resumo['recebidas'] += premios[premio]["preço"]
            elif premios[premio]['qtd'] > 0 and int(nbolinhas) < premios[premio]['preço']:
                print(f'O jogador precisa de mais {premios[premio]["preço"] - int(nbolinhas)} bolinhas para trocar por um {premio}.')
            elif premios[premio]['qtd'] <= 0:
                print(f'O jogador veio trocar suas bolinhas mas o premio {premio} nao esta disponivel.')
        else:
            print(f'O jogador veio trocar suas bolinhas mas o premio {premio} nao esta disponivel.')
    elif entrada == 'hora de fechar':
        continua = False


print('\nO resumo do dia foi:')
print(f'Arrecadado: {resumo["dinheiro"]} ienes em {resumo["vendas"]} vendas;')
print(f'Bolinhas: {premios["bolinhas"]["qtd"]} restantes;')
print(f'Resgates feitos: {resumo["resgates"]};')
print(f'Bolinhas recebidas: {resumo["recebidas"]};')
print(f'Premios: {resumo["premios"]} restantes;')
print('Deu a hora, amanha tem mais!')