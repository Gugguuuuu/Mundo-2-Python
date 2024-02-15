# EXERCICIO 41
from datetime import date
nome = str(input('Digite o nome do atleta : '.strip().title()))
nascimento = int(input('Digite sua data de nascimento : '))
idade = date.today().year - nascimento
if idade <= 9:
    categoria = '\033[32mMIRIM\033[m'
elif idade <= 14 and idade > 9:
    categoria = '\033[33m\INFANTIL033[m'
elif idade <= 19 and idade > 14:
    categoria = '\033[34mJÚNIOR\033[m'
elif idade <= 25 and idade > 19:
    categoria = '\033[36;47mSÊNIOR\033[m'
elif idade > 25:
    categoria = '\033[35mMASTER\033[m'
print('O atleta {}, que tem {}, participara do torneio de natação na categoria {}.'.format(nome, idade, categoria)) 
