# EXERCICIO 69
homen = mulheres = idade = sexo = maior = i = 0
continuar = 's'
c = 'CADRASTAMENTO'
print('\033[1;7;37;40m  \033[m'*20)
print(f'\033[1;7;37;40m{c:^40}\033[m')
print('\033[1;7;37;40m  \033[m'*20)
while True:
    if continuar  == 's':
        sexo = str(input('Digite o sexo ( \033[1;35mF\033[m | \033[1;34mM\033[m )')).lower().strip()
        while sexo != 'f' and sexo != 'm':
            print('\033[1;31mDIGITA UMA OPÇÃO VALÍDA\033[m')
            sexo = str(input('Digite o sexo ( \033[1;35mF\033[m | \033[1;34mM\033[m )')).lower().strip()[0]
        idade = int(input('Digite sua idade : '))
        i += 1    
        if sexo == 'm':
            homen += 1
        if idade >= 18:
            maior += 1
        if idade < 18 and sexo == 'f':
            mulheres += 1
    if continuar == 'n':
        break
    continuar = str(input('Você vai continuar a cadrastar? ( \033[1;32mS\033[m | \033[1;31mN\033[m)')).lower().strip()
    while continuar != "s" and continuar != 'n':
        print('\033[1;31mDIGITA UMA OPÇÃO VALÍDA\033[m')
        continuar = str(input('Você vai continuar a cadrastar? ( \033[1;32mS\033[m | \033[1;31mN\033[m)')).lower().strip()
print(f'''
\033[1;36;44mANALISANDO...\033[m
    \033[1;32mVocê cadrastou\033[m \033[1;34m{homen} homens\033[m
    \033[1;32mVocê cadrastou\033[m \033[1;33m{maior} maiores de idade\033[m
    \033[1;32mVocê cadrastou\033[m \033[1;35m{mulheres} mulheres menores de idade\033[m     
      ''')