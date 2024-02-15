# EXERCICIO 55
peso = float(input('Digite o peso da 1ª pessoa : '))
maior = peso
menor = peso

for i in range(2, 6):
    peso = float(input('Digite o peso da {}ª pessoa : '.format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = 0
print('O maior peso lido foi {}\nO menor foi {}'.format(maior, menor))
    