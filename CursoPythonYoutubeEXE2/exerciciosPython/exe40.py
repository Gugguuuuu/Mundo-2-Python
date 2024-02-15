# EXERCICIO 40
i = 0
soma_das_notas = 0
con = 's'
while con == 's':
    notas = float(input('Digite sua nota : '))
    soma_das_notas = soma_das_notas + notas
    i = i + 1
    con = str(input('''
Você vai continuar a inserir notas ? 
[ s ] ou [ n ]
resposta : '''))
if con == 'n' and i > 0:
    media = soma_das_notas / i
    if media < 7:
        print('A media das suas notas é \033[31m{:.1f}\033[m'.format(media))
    elif media >= 7:
        print('A media das suas notas foram \033[32m{:.1f}\033[m'.format(media))
    