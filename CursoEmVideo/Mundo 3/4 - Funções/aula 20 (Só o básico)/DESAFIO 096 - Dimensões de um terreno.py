"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno rentangular
   (largura e comprimento) e mostre a área do terreno."""
def linha(msg):
    print('=' * 40)
    print(f'{msg:^40}')
    print('=' * 40)
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreo é de {area}m².')


#  PROGRAMA PRINCIPAL
linha('CALCULADOR DE ÁREA')
larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
linha('RESULTADO')
area(larg, comp)
