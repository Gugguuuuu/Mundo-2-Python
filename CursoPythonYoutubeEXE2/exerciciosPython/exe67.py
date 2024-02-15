# EXRCICIO 67
i = 0
n = int(input(f'Digite o \033[1;34m{i+1}°\033[m e você e tera sua tabuada [ 0 ] PARA ACABAR : ')) 
while True:
    if n <= 0:
        break
    else: 
        print('=#'*12,f'\n\033[1;7;37;40m TABUADA DO \033[m\033[1;7;37;44m{n} \033[m\n','=#'*12)
        print('~'*15)
        for i in range(1, 11):
            print(f'{n} x {i} = {n*i}')   
        print('~'*15, '\n')
    n = int(input('Digite o proximo numero [ 0 ] PARA ACABAR : '))
print('\033[1;34mFINALIZANDO...\033[m\n\033[1;33mVocê saiu do progama tabuada\033[m')   