# EXERCICIO 51
i  = int(input('Digite o primeiro termo : '))
r = int (input('Digite a razão : '))
t = int(input('Você quer quantos termos : '))
t = i + (t - 1) * r
y  = 0

for c in range(i, t + r, r):
    print('{}'.format(c), end=' -> ')
    y = y + 1
print('ACABOU')
    

