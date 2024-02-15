# EXERCICIO 49
n = float(input('Digite um numero : '))
t = int(input('Digite o tamanho da tabuada : '))
print('=#'*10)
for i in range(0, t):
    i += 1
    print('# {} X {} = {} #'.format(n, i, n * i))
print('=#'*10)