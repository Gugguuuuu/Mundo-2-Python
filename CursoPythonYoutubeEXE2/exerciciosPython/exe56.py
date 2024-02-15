# EXERCICIO 56
maior = 0
media = 0
m = 0
menores = 0
for i in range(1, 5):
    nome = str(input('''
-=-=-=-=-=- {}° Pessoa -=-=-=-=-=-
nome : '''.format(i))).strip()
    idade = int(input('Idade : '))
    sexo = str(input('Sexo(M | F) : ')).strip().lower()
    if i == 1 and sexo == 'm':
        maior = idade
        n = nome
    else:
        if idade > maior:
            maior = idade
    if sexo != 'm' and sexo != 'f':
        print('\033[31mINSIRA UM SEXO VALIDO\033[m')
    if sexo == 'f' and idade < 20:
        menores += 1

    m += idade
    media = m / 4
print('O homem mais velho é o {} e ele tem {} anos\nA media total da idade do grupo é {:.2f}\nE nesse grupo tem {} mulheres menores de 20 anos'.format(n.title(), maior, media, menores))


