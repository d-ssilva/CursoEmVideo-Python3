"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
    No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Trasferidor', 4.30,
            'Compasso', 9.90,
            'Mochila', 110.10,
            'Caneta', 1.30,
            'Livro', 35.10)
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:  # filtra as posições pares, Que são os nomes dos produtos
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}') # filtra as posições impares, Que são os preços dos produtos
print('='*40)