#EXERCICIO 62 
c = 0
termos = 10
t = 0
mais = None
pergunta = None
while c != termos:
    if c == 0:
        p = int(input('Digite o primeiro termo : '))
        r = int(input('Digite a razão : '))
        t = p
    print(t, end=' -> ')
    t += r
    c += 1
    if c == termos:
        pergunta = str(input('Deseja continuar? ( S | N ) ')).lower().strip()
        if pergunta == 's':
            mais = int(input('\nDigite quantos termos você quer a mais : '))
            termos += mais
        else:
            c = termos
print('\033[33mFIM\033[m\n\033[34mProguessão finalizado com\033[m \033[35m{} termos\033[m'.format(termos))