"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar. No final mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais menorpreço"""
valortotal = preço = maisqmil = menorpreço = cont = 0
qtdtotal = 1
nomebarato = 'n/a'
print('{:=^20}'.format(' D - Store '))
while True:
    nproduto = str(input('Insira o nome do produto -> ')).capitalize()
    preço = float(input('Insira o preço -> R$'))
    valortotal += preço
    cont += 1
    if cont == 1 or preço < menorpreço:
        menorpreço = preço
        nomebarato = nproduto
    if preço > 1000:
        maisqmil += 1


    flag = str(input('Deseja continuar[S/N]: ')).upper()
    while flag not in 'SN':
        flag = str(input('Erro: Caractere inserido inválido.\nTente novamente, deseja continuar[S/N]: ')).upper()
    print('=' * 20)
    if flag == 'N':
        break
print('=' * 20)
print(f'O total gasto na compra é de R${valortotal}\n'
      f'O produto mais barato da compra foi {nomebarato}, custando R${menorpreço}\n'
      f'{maisqmil} produto(s) acima de R$1000,00.')
