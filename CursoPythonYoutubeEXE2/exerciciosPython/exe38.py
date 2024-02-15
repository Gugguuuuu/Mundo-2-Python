# EXERCICIO 38
n = float(input('Digite um numero : '))
n1 = float(input('Digite outro numero : '))
if n > n1:
    resultado = 'O numero \033[0;32m{}\033[m é maior que \033[0;31m{}\033[m'.format(n, n1)
elif n1 > n:
    resultado = 'O numero \033[0;32m{}\033[m é maior que \033[0;31m{}\033[m'.format(n1, n)
elif n == n1:
    resultado = 'Os dois numeros são iguais'
print(resultado)