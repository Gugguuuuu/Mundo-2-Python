# EXERCICIO 48
n = int(input('Digite um numero : '))
soma = 0
c = 0
for i in range(1, n+1):
    if i % 3 == 0 and i % 2 != 0:
        c += 1
        soma += i
print('todos os {} volores somandos dão {}'.format(c, soma))
#20938.75.