# EXERCICIO 66
n = 0
i = 0
soma = 0
media = 0
while True:
    n = float(input(f'Digite o {i+1}° numero [999 encerra]: '))
    if n != 999:
        soma += n
        i += 1
    elif n == 999:
        break
media = soma / i
print(f'Você digitou {i} numeros\nA soma é {soma}\nE a media é {media} ')