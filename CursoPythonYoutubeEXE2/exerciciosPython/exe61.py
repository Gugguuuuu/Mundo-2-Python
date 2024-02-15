# EXERCICIO 61
p = int(input('Digite o primeiro termo : '))
r = int(input('Digite a razão : '))
t = p
c = 1
while c <= 10:
    print(t, end=' -> ')
    t += r
    c += 1
print('\033[33mFIM\033[m')
