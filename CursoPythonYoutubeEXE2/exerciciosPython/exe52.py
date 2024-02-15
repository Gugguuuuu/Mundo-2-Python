# EXERCICIO 52
n = int(input('Digite um numero para ver se é primo : '))
d = 0

for c in range(1, n+1):
    
    if n % c == 0:
        resultado = '\033[32m{}\033[m'.format(c)
        d += 1
    elif n % c != 0:
        resultado = '\033[31m{}\033[m'.format(c)

    print(resultado, end=' ')
print('Foi divisivél \033[35m{} veses\033[m'.format(d))

if d == 2:
    print('O numero \033[34m{}\033[m \033[32mÉ PRIMO\033[m'.format(n))
else:
    print('O numero \033[34{}\033[m \033[31mNÃO É PRIMO\033[m'.format(n))

    