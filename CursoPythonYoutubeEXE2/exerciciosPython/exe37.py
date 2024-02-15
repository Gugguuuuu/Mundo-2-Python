# EXERCICIO 37
n = int(input('Digite um numero '))
opcoes = int(input('''
Digite um numero de cada opção para a base ser convertida
[ 1 ] para binario
[ 2 ] para hexadecimal
[ 3 ] para octal 
Digite a sua opção : 
'''))
if opcoes == 1:
    n = bin(n)
    resultado = 'O valor convertido para binario é : \033[0;32m{}\033[m'.format(n)
elif opcoes == 2:
    n = hex(n)
    resultado = 'O valor convertido para hexadecimal é : \033[0;32m{}\033[m'.format(n)
elif opcoes == 3:
    n = oct(n)
    resultado = 'O valor convertido para octal é : \033[0;32m{}\033[m'.format(n)
else:
    resultado = 'Digite uma opcão valida'
print(resultado)
