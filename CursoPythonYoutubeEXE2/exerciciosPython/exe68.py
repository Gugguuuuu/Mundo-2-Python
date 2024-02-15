# EXERCICIO 68
from random import randint
tot = com = v = d = 0
continuar = 's'
print('-'*25, '\n\033[1;7;37;40mVAMOS JOGAR PAR OU ÍMPAR\033[m\n', '-'*25)
while True:
    if continuar == 's': #so vai ocorre enquanto continuar for = s
        escolha = str(input('Digite sua escolha ( \033[1;33mP\033[m | \033[1;34mI\033[m )')).lower().strip()# pede para digitar P ou I
        while escolha != 'i' and escolha != 'p':# se o usuario digitr errado o progama não vai deixar e vai pedir para digitar P ou I denovo
            print('\033[1;31mOPÇÃO INVALÍDA DIGITE NOVAMENTE\033[m')
            escolha = str(input('Par ou impar? ( \033[1;33mP\033[m | \033[1;34mI\033[m )')).lower().strip()
        # faz que o computador sorteie uma numero aleatorio entre 1 a 10
        # pede pro usuario digitar um numero
        # e soma os dois valores para depois poder verificar se ele é par ou impar
        com = randint(0, 10)
        n =  int(input('Digite o numero : '))
        tot = n + com
        # faz a verificação se o tot é par ou impar tambem verificado a escolha do usuario
        if escolha == 'p':
            if tot % 2 == 0:
                print(f'\033[1;32mVocê venceu!.\033[m \033[1;33mComputador jogou {com}\033[m e \033[1;34mvoce jogou {n}\033[m \033[1;35mTotal {tot}\033[m')
                v += 1
            else:
                print(f'\033[1;31mGAME OVER... \033[m \033[1;33mComputador jogou {com}\033[m e \033[1;34mvoce jogou {n}\033[m \033[1;35mTotal {tot}\033[m')
                d += 1
        elif escolha == 'i':
            if tot % 2 != 0:
                print(f'\033[1;32mVocê venceu!\033[m\033[m \033[1;33mComputador jogou {com}\033[m e \033[1;34mvoce jogou {n}\033[m \033[1;35mTotal {tot}\033[m')
                v += 1
            else:
                print(f'\033[1;31mGAME OVER...\033[m\033[m \033[1;33mComputador jogou {com}\033[m e \033[1;34mvoce jogou {n}\033[m \033[1;35mTotal {tot}\033[m')
                d += 1
    # faz com que o progama seja interrompido se o usuario digitar N
    elif continuar == 'n':
        break     
    # pergunta se ele quer continuar e se ele digitar algo invalído pede para ele digitar de novo
    continuar = str(input('Você quer continuar ( \033[1;32mS\033[m | \033[1;31mN\033[m )')).lower().strip()
    while continuar != 's' and continuar != 'n':
        print('\033[1;31mDIGITE UMA OPÇÃO VALÍDA\033[m')
        continuar = str(input('Você quer continuar ( \033[1;32mS\033[m | \033[1;31mN\033[m )')).lower().strip()
# da o resultado
print(f'\033[1;34mEncerramos e você venceu\033[m \033[1;32m{v} partidas\033[m \033[1;34me perdeu\033[m \033[1;31m{d} partidas\033[m')
