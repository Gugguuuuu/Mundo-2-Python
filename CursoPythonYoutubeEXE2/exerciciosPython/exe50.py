# EXERCICIO 50
soma = 0
for i in range(6):
    i += 1
    n = float(input('Digite o {}° numero : '.format(i)))
    if n % 2 == 0:
        soma += n
print('O resultado da soma so dos numeros pares é : {}'.format(soma))