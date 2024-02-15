# EXERCICIO 64
print('\033[1;2;7;37;40mDigite alguns numeros e você vera a soma de todos e digite [ 999 ] para encerra o progama\033[m')
n = float(input('Digite um numero : '))
soma = 0
i = 0 
while n != 999:   
    soma += n
    n = int(input('Digite outro numero : '))
    i += 1
print('\033[1;33mVocê digitou\033[m \033[1;32m{} numeros\033[m\033[1;34m A soma de todos esses numeros é\033[m \033[1;35m{}\033[m'.format(i, soma))