"""Para essa prática eu criei um software que condicione o usuária a ver qual a diferença de manipulação será
exibida na tela"""
while True:
    print('='*30)
    resp = (input('Qual exemplo deseja ver: (A) ou (B)\n A- Cópia por LIGAÇÃO\n B- Cópia dos ITENS\nDigite aqui ->'
                  '')).upper()[0]
    while resp not in 'AB':
        resp = (input('Caractere inválido. Digite novamente.\nQual exemplo deseja ver: (a) ou (b)\n '
                      'A- Cópia por LIGAÇÃO;\n'
                      'B- Cópia dos ITENS;\nDigite aqui -> ')).upper()[0]
    if resp == 'A':
       a = [2, 3, 4, 7]
       b = a
       b[2] = 8
       print(f'Lista A: {a}')
       print(f'Lista B: {b}')
    else:
        a = [2, 3, 4, 7]
        b = a[:]
        b[2] = 8
        print(f'Lista A: {a}')
        print(f'Lista B: {b}')
    resp1 = input('Deseja ver novamente?[S/N]: ').upper()[0]
    while resp1 not in 'SN':
        resp1 = input('Erro caractere inválido. Deseja ver novamente?[S/N]: ').upper()[0]
    if resp1 == 'N':
        break
