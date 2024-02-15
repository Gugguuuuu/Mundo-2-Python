# EXERCICIO 45
from time import sleep
print('-='*40, '\nVamos jogar JOKENPO', '\n', '-='*40)

sleep(1.5)

escolhas = ['tesoura', 'papel', 'pedra']

jogador = int(input('''
[ 0 ] para tesoura 
[ 1 ] para papel 
[ 2 ] para pedra     
                    
Digite sua escolha : '''))

sleep(0.5)
from random import randint

computador = randint(1, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')

print('-='*40, '\n Você jogou {}\n'.format(escolhas[jogador]),'Computador jogou {}'.format(escolhas[computador]) )

sleep(0.3)

if computador == 0:
    if jogador == 0:
        print('\033[0;37;40mEMPATE.\033[m')
    elif jogador == 1:
        print('\033[0;31mCOMPUTADOR VENCEU...\033[m')
    elif jogador == 2:
        print('\033[0;32mVOCÊ VENCEU!!!\033[m')

elif computador == 1:
    if jogador == 0:
        print('\033[0;32mVOCÊ VENCEU!!!\033[m')
    elif jogador == 1:
        print('\033[0;37;40mEMPATE.\033[m')
    elif jogador == 2:
        print('\033[0;31mCOMPUTADOR VENCEU...\033[m')


elif computador == 2:
    if jogador == 0:
        print('\033[0;31mCOMPUTADOR VENCEU...\033[m')
    elif jogador == 1:
        print('\033[0;32mVOCÊ VENCEU!!!\033[m')
    elif jogador == 2:
        print('\033[0;37;40mEMPATE...\033[m')