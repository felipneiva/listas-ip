def palindromo(x):
    if len(x) <= 1:
        return True
    else:
        if x[0] == x[-1]:
            x = x[1:-1]
            return palindromo(x)
        else:
            return False


palindromos = 0
n = int(input())


for i in range(n):
    pista = input()
    if palindromo(pista):
        palindromos += 1
    elif not palindromo(pista):
        for j in range(len(pista)):
            pista = 'a' + pista
            if palindromo(pista):
                palindromos += 1

print(palindromos)
if palindromos == n:
    print('ACHEI!!! Peach, estou a caminho.')
else:
    print('Essa não!!! Estou na direção errada.')
