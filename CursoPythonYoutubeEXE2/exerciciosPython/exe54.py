# EXERCICIO 54
from datetime import date 
maior = 0
menor = 0
for i in range(1, 8):
    id = int(input('Em que ano a \033[33m{}°\033[m nasceu : '.format(i)))
    idade = date.today().year - id
    if idade >= 18:
        maior += 1
    else:
        menor += 1
if maior > menor:
    resultado = '\033[32mAcesso Liberado!!!\033[m'
else:
    resultado = '\033[31mAcesso Negado\033[m tem \033[33m{}\033[m maiores de idade e so \033[34m{}\033[m menores de idade'.format(maior, menor)
print('Dessas pessoa \033[32m{}\033[m maior de idade e \033[31m{}\033[m são menor de idade'.format(maior, menor))
print(resultado)