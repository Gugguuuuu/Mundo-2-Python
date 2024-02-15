# EXERCICIO 70
tot = mais1000 = barato = nomeBarato = i = 0
continuar = 's'
while True:
    if continuar == 's':
        nome = str(input('Digite o nome do produto : ')).title()
        preço = float(input('Digite o preço do pruduto : '))
        tot = tot + preço
        i += 1
        if preço > 1000:
            mais1000 += 1
        if i == 1:
            barato = preço
            nomeBarato = nome
        elif preço < barato:
            barato = preço
            nomeBarato = nome
        continuar = str(input(f'Quer cadrastar um {i+1} produto? [S/N] ')).lower().strip()
    while continuar != 's' and continuar != 'n':
        print('\033[1;31mDIGITE UMA OPÇÃO VALÍDA\033[m')
        continuar = str(input(f'Quer cadrastar um {i+1} produto? [S/N] ')).lower().strip()
    if continuar == 'n':
        break
print(f'O total da compra dos {i} produtos foi R${tot}')
print(f'Temos {mais1000} produtos custando mais de R$1000')
print(f'O produto mais barato foi {nomeBarato} e custou R${barato}')
