# EXERCICIO 58
from random import randint
valor = randint(1, 20)
erros = 0
print('\033[33mO computador pensou em um numero de\033[m \033[35m1 a 20\033[m')
palpite = int(input('Digite o numero que você acha que o computador pensou : '))
while palpite != valor:
    print('\033[31mVocê errou tente novamente\033[m')
    if palpite > valor:
        print('O valor a ser encontrado é menor')
    elif palpite < valor:
        print('O valor a ser encontrado é maior')
    palpite = int(input('Digite o numero que você acha que o computador pensou : '))
    erros += 1
print('\033[32mParabéns\033[m, você acertou com \033[31m{} erros\033[m'.format(erros))