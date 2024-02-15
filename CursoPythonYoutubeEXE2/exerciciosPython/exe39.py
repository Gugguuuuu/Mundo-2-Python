# EXERCICIO 39
idade = int(input('Digite sua idade : '))
if idade < 18:
    falta = 18 - idade 
    print('Você ainda \033[0;31mnâo\033[m prescisa se alista para o exercito. Falta {} anos'.format(idade))
elif idade > 18:
    falta = idade - 18
    print('Você \033[0;32mtem\033[m que se alista para o exercito. Seu alistamento foi á {} anos'.format(falta))
else:
    print('Seu alistamento é \033[0;37magora\033[m!!!')