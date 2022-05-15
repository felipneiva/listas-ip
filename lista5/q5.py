def busca_binaria(lista, inicio, fim):
    if fim >= inicio:
        meio = (inicio + fim) // 2
        if lista[meio] == 'Ghost Potrificationizer - E. Gadd':
            return meio
        elif lista[meio] > 'Ghost Potrificationizer - E. Gadd':
            return busca_binaria(lista, inicio, meio-1)
        elif lista[meio] < 'Ghost Potrificationizer - E. Gadd':
            return busca_binaria(lista, meio+1, fim)
    else:
        return -1


def poder(numero):
    if str(numero) == str(numero)[::-1]:
        return numero
    else:
        reverso = str(numero)[::-1]
        numero += int(reverso)
        return poder(numero)


estante = []
n = int(input())
for i in range(n):
    item = input()
    estante.append(item)

if busca_binaria(estante, 0, n-1) == -1:
    print('Mamma mia! Só Mario poderá me salvar agora!')
else:
    posicao = busca_binaria(estante, 0, n-1) + 1
    if poder(posicao * 7) < 50:
        print('É uma catástrofe, eu tenho a arma mas só posso usá-la uma vez')
    elif 50 <= poder(posicao * 7) < 100:
        print('Terei que usar a minha arma com sabedoria!')
    elif 100 <= poder(posicao * 7) < 200:
        print('A arma está bem carregada, me dei bem!')
    elif 200 <= poder(posicao * 7):
        print('Aha! EU NÃO TENHO MAIS MEDO DE NADA! PODEM VIR!')
