def somar(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + somar(n // 10)


def primo(x, i=2):
    if x <= 2:
        if x == 2:
            return True
        else:
            return False
    if x % i == 0:
        return False
    if i * i > x:
        return True
    return primo(x, i+1)


def fatorial(x):
    if int(x) == 0:
        return 1
    else:
        return int(x) * fatorial(int(x)-1)


labirinto = True
seq_acertos = 0
seq_erros = 0

while labirinto:
    entrada = input()
    if entrada == 'Somar':
        numero = int(input())
        if somar(numero) % 2 == 0:
            print(f'O número {somar(numero)} é par, siga por aqui Link!')
            seq_acertos += 1
            seq_erros = 0
        else:
            print('Por aqui não.')
            seq_erros += 1
            seq_acertos = 0
    elif entrada == 'Primo':
        numero = int(input())
        if primo(numero):
            print(f'O número {numero} é primo, continue herói!')
            seq_acertos += 1
            seq_erros = 0
        else:
            print('Por aqui não.')
            seq_erros += 1
            seq_acertos = 0
    elif entrada == 'Fatorial':
        numero, resultado = input().split(' ')
        if fatorial(numero) == int(resultado):
            print(f'A resposta é mesmo {resultado} Link, esse caminho está certo!')
            seq_acertos += 1
            seq_erros = 0
        else:
            print(f'Por aqui não.')
            seq_erros += 1
            seq_acertos = 0
    else:
        print('Por aqui não.')
        seq_erros += 1
        seq_acertos = 0
    if seq_acertos == 3:
        print('Com a sua ajuda o Link finalmente conseguiu sair do labirinto!!!')
        labirinto = False
    if seq_erros == 3:
        print('Hoje não é um bom dia para o nosso herói...')
        labirinto = False