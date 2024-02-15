# EXERCICIO 53
p = str(input('Digite uma palavra/frase : '.lower()))
con = len(p) - 1
resultado = ''
espacos = p.count(' ')
for i in range(con):
    if p[i] != p[con]:
        palin = False
    else:
        palin = True
    con = con - 1
if palin == True and espacos == 0:
    resultado = 'A palavra é um palindro'
elif  palin == False and espacos == 0:
     resultado = 'A palavra não é um palindro'
elif palin == True and espacos >= 1:
    resultado = 'A frase é um palindro'
elif palin == False and espacos >= 1:
    resultado = 'A frase não é um palindro'
else:
    resultado = 'Digite corretamente'

print(resultado)
