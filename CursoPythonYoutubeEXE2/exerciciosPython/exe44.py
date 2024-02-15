# EXERCICIO 44
valor = float(input('Digite o valor de sua compra : '))
pagamento = str(input('''
Opções de pagamento :
[ 1 ] para a vista dinheiro/cheque 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço normal 
[ 4 ] 3x ou mais no cartão: 20% de juros                  
Digite sua opção e pagamento : '''))
if pagamento == '1':
    desconto = valor - (valor*0.1)
    print('A vista o produto antes era  de {:.2f}R$ agora é {:.2f}R$'.format(valor, desconto))
elif pagamento == '2':
    desconto = valor - (valor*0.05)
    print('A vista no cartão o produto antes era de {:.2f}R$ agora é {:.2f}R$'.format(valor, desconto))
elif pagamento == '3':
    desconto = valor / 2
    print('Em duas vezes no cartão o preço é normal saindo de {:.2f}R$ para 2X de {:.2f}R$'.format(valor, desconto))
elif pagamento == '4':
    prestações = int(input('Digite em até quantas veses você que parcelar : '))
    desconto = valor + (valor*0.2)
    print('Em 3 veses ou mais o produto tem 20% de juros sendo assim {}R$ saindo de {:.2f}R$ para {}X de {:.2f}R$'.format(desconto,valor, prestações, desconto / prestações))