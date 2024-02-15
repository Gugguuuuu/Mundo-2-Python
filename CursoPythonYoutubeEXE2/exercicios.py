from random import randint
from time import sleep

i = n = t =  0
continuar = ''
pausa = 5
while i <= 10:
    n = randint(0, 10)
    t = randint(0, 10)
    print(f'{n} X {t} = ?')
    for c in range(1, 8):
        print(c, end='\r')
        sleep(pausa / 5)
    tabuada = int(input('Digite resposta : '))
    i += 1
    sleep(0.5)
    if tabuada == n * t:
        print(f'\033[1;32mVOCÊ ACERTOU A RESPOSTA ERA\033[m \033[33m{n*t}\033[m')
    else:
        print(f'\033[1;31mVOCÊ ERROU A RESPOSTA ERA\033[m \033[33m{n*t}\033[m')
    if i == 10:
        continuar = str(input('Você quer continuar? ( \033[1;32mS\033[m | \033[1;31mN\033[m ) ')).lower().strip()[0]
        while continuar != 's' and continuar != 'n':
            print('\033[1;31mDIGITE UMA OPÇÃO VALÍDA\033[m')
            continuar = str(input('\033[1;34mVocê quer continuar?\033[m ( \033[1;32mS\033[m | \033[1;31mN\033[m ) ')).lower().strip()[0]
    if continuar == 's':
        i = 0
        continuar = ''
    elif continuar == 'n':
        break
print('\033[1;33mACABOU\033[m')