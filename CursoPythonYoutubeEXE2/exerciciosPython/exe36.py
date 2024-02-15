# EXERCICIO 36
casa = float(input('Digite o valor da casa : '))
salario = float(input('Digite seu salario : '))
anos = int(input('Digite em quantos anos voce vai comprar a casa : '))
prestacao = casa / (anos * 12)
if prestacao <= salario * 0.3:
    print('\033[0;32mEMPRESTIMO APROVADO\033[m. O valor da casa é {:.2f}, você vai pagar em anos {:.0f}, e a prestação sera de {:.2f} '.format(casa, anos, prestacao))
else:
    print('\033[0;31mEMPRESTIMO NEGADO\033[m')