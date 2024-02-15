# EXERCICIO 65
con = 'S'
c = 0
soma_n = 0
media = 0

while con == 'S':
    n = int(input('Digite um numero : '))
    con = str(input('\033[1mVocê quer continuar?\033[m ( \033[32mS\033[m | \033[31mN\033[m )')).upper().strip()

    if c == 0:
        maior = n
        menor = n
    c += 1

    if n > maior:
        maior = n
    elif n < menor:
        menor = n

    soma_n += n
    while con != 'S' and con !='N':
        print('\033[1;31mDIGITE UMA OPÇÃO VALIDA\033[m')
        con = str(input('\033[1mVocê quer continuar?\033[m ( \033[32mS\033[m | \033[31mN\033[m )')).upper().strip()


media = soma_n / c

print('''\033[1;7;37;40mAnalisando os dados...\033[m
O maior numero digitado foi \033[1;32m{}\033[m
O menor digitado foi \033[1;31m{}\033[m
E a media total de todos os numeros digitados foi \033[1;35m{:.2f}\033[m\n
Você digitou {} numeros. 
'''.format(maior, menor, media, c))

# print('O maior numero é \033[35m{}\033[m e o menor é \033[31m{}\033[m'.format(maior, menor))