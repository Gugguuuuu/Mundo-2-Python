# EXERCICIO 43
altura = float(input('Digite sua altura : '))
peso = float(input('Digite seu peso em KG : '))
IMC  = peso / (pow(altura, 2))
if IMC <= 18.5:
    resultado = '\033[31mabaixo do peso\033[m'
elif IMC >= 18.25 and IMC <= 25:
    resultado = '\033[32mpeso ideal\033[m'
elif IMC >= 25 and IMC <=30:
    resultado = '\033[33msobrepeso\033[m'
elif IMC >= 30 and IMC <= 40:
    resultado = '\033[31mobesidade\033[m'
elif IMC > 40:
    resultado = '\033[31mobesidade mórbida\033[m'
print('Seu IMC(Índice de Massa Corporal) é de \033[34m{:.2f}\033[m e está em {}'.format(IMC, resultado))