# # EXERCICIO 60
# import math
# n = int(input('Digite um numero : '))
# fac = math.factorial(n)
# print('O fatorial desse numero é {}'.format(fac))
n = int(input('Digite um numero : '))
c = n
f = 1
print(f'O fatorial de {n}! é = ', end='')
while c > 0:
    f *= c
    print(c, end=' ')
    print(' x ' if c > 1 else ' =', end=' ')
    c -= 1
print(f)
