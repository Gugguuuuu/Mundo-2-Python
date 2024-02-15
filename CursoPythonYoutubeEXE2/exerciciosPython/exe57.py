# EXERCICIO 57
nome = str(input('Digite seu nome : ')).strip().title()
sexo = str(input('Digite seu sexo ( M | F ) : ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print('\033[31mDIGITE UM SEXO VALIDO VOCÊ NÃO É UMA GELADEIRA DE 4 PORTAS\033[m')
    sexo = str(input('Digite seu sexo ( M | F) : ')).strip().upper()[0]
if sexo[0] == 'F':
    sexo = '\033[35mFeminino\033[m'
else:
    sexo = '\033[34mMasculino\033[m'
print('Olá {}, seu sexo é {}'.format(nome, sexo))