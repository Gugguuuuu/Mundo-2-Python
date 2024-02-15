print('=#'*10, '\n\033[7;37;40mSEQUENCIA DE FIBONATE\033[m\n', '=#'*10)
termos = int(input('Digite a quantidade de termos que você quer : '))
termo1 = 0
termo2 = 1
termo3 = 0
contador = 0
mais = None

print('{} -> {} -> '.format(termo1, termo2), end='')
while contador < termos - 2:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    print('{}'.format(termo3), end=' -> ')
    contador += 1
    if contador == termos - 2:
        print('PAUSA')
        mais = int(input('\nVocê quer mais quantos termos : '))
        termos += mais
    elif mais == 0:
        contador = termos - 2


print('FIM')