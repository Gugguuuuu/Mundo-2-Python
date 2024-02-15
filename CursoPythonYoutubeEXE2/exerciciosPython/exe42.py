# EXERCICIO 42
s = float(input('Digite o valor de um segmento de reta : '))
s1 = float(input('Digite outro valor de um segmento de reta : '))
s2 = float(input('Digite mais outro valor de segmento de reta : '))
soma = s + s1 + s2
if s <= soma - s and s1 <= soma - s1 and s2 <= soma - s2: 
    if s == s1 == s2:
        resultado = '\033[32mEQUILATERO\033[m'
    elif s == s1 or s == s2 or s1 == s2:
        resultado = '\033[34mISOCELES\033[m'
    elif s != s1 != s2 != s:
        resultado = '\033[31mESCALENO\033[m'
    print('Com os segmentos {:.2f}, {:.2f}, {:.2f} da para forma um triangulo {}'.format(s, s1, s2, resultado))    
else:
    print('\033[31mNÃO DA PARA FORMA TRIANGULO COM ESSES SEGMENTOS\033[m')