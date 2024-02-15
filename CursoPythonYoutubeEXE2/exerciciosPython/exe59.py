# EXRCICIO 59
from time import sleep
n1 = float(input('Digite um numero : '))
n2 = float(input('Digite outro numero : '))
v = 0

print('''
Suas opções :
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair do progama
''')
op = int(input('Digite sua opção : '))

maior = 0


while op != 5:
    if op > 0:
        if op == 1:
            soma = n1 + n2
            print('A soma de {:.2f} com {:.2f} é {:.2f}'.format(n1, n2, soma))

        elif op == 2:
            multiplicar = n1 * n2
            print('O pruduto de {:.2f} com {:.2f} é {:.2f}'.format(n1, n2, multiplicar))

        elif op == 3:
            if n1 > n2: 
                maior = n1
            elif n2 > n1:
                maior = n2
            elif n1 == n2:
                maior = 'o dois são iguais'
            print('O maior entre {} e {} é {}'.format(n1, n2, maior))

        elif op == 4 and v == 0:
            if op == 4:
                n1 = float(input('Digite seu novo 1° numero : '))
                n2 = float(input('Digite seu novo 2° numero :  '))
                v += 1
                print('''
        
Suas opções :
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair do progama
''')
        elif op == 4 and v > 0:
            print('\033[31mVOCÊ SO PODE ESCOLHER NOVOS NUMEROS UMA VEZ\033[m')
        elif op > 5 or op < 0:  
            print('\033[31mDigite uma opção valída\033[m')
    sleep(1.3)

    op = int(input('Digite sua outra opção : '))
print('\033[36mFINALIZANDO...\033[m')
sleep(0.5)
print('\033[33mVOCÊ SAIU DO PROGAMA\033[m')
        