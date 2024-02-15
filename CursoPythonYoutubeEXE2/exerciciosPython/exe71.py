cinquenta = vinte = dez = cinco =  um = i = 0
continuar = 's'
while True:
    if continuar == 's':
        saque = int(input('Digite o valor de saque : '))
        if saque >= 50:
            while saque >= 50:
                saque -= 50
                cinquenta += 1
            print(f'Sâo \033[1;36m{cinquenta}\033[m notas de \033[1;31R$50\033[m')
        if saque >= 20:
            while saque >= 20:
                saque -= 20
                vinte += 1
            print(f'Sâo \033[1;36m{vinte}\033[m notas de \033[1;32R$20\033[m')
        if saque >= 10:
            while saque >= 10:
                saque -= 10
                dez += 1
            print(f'Sâo \033[1;36m{dez}\033[m notas de \033[1;34R$10\033[m')
        if saque >= 5:
            while saque >= 5:
                saque -= 5
                cinco += 1
            print(f'Sâo \033[1;36m{cinco}\033[m notas de \033[1;31R$5\033[m')
        if saque >= 1:
            while saque >= 1:
                saque -= 1
                um += 1
            print(f'Sâo \033[1;36m{um}\033[m moedas de \033[1;35R$1\033[m')
        cinquenta = vinte = dez = cinco = um = 0
        i += 1
        continuar = str(input(f'Vai fazer um \033[1;34m{i+1}°\033[m saque? ( \033[1;32mS\033[m | \033[1;31mN\033[m)')).lower().strip() [0]
        while continuar != "s" and continuar != 'n':
            print('\033[1;31mDIGITA UMA OPÇÃO VALÍDA\033[m')
            continuar = str(input(f'Vai fazer um \033[1;34m{i+1}°\033[msaque? ( \033[1;32mS\033[m | \033[1;31mN\033[m)')).lower().strip()[0]
    else:
        break
print(f'\033[1;34mVOCÊ SAIU DO CHAIXA ELETRONICO. VOCÊ FEZ {i} SAQUES\033[m')
