"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
    e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros"""
from time import sleep

print("="*10, "|"'GUANABARA STORE', "|", "="*10)
valor = float(input('Digite o valor da compra -> R$'))
print("-"*40)
print('Escolha sua forma de pagamento? ')
print('[ 1 ] - À vista dinheiro/cheque (5% desc).')
print('[ 2 ] - À vista no cartão.')
print('[ 3 ] - 2x no cartão (sem juros).')
print('[ 4 ] - 3x ou mais no cartão (20% de juros).')
pag = int(input('Digite aqui -> '))

if pag == 1:
    valor = valor - (valor * 0.05)
    print('O valor da compra sofreu redução.\nTotalizando R${:.2f} para pagamento.'.format(valor))
elif pag == 2:
    print('Total p/ pagamento é de R${:.2f}'.format(valor))
elif pag == 3:
    parc = valor / 2
    print('Sua compra foi parcelada em 2x de R${:.2f}'.format(parc))
elif pag == 4:
    qtdparc = int(input('Digite o número de parcelas desejadas -> '))
    valorporc = valor * 0.2
    valor = valor + valorporc
    parc = valor / qtdparc
    print('O valor da compra sofreu acréscimo de R${:.2f}.\nTotalizando {} parcelas de R${:.2f}'.format(valorporc,
                                                                                                      qtdparc, parc))
else:
    print('Informação inserida deve ser de 1 à 4!')

print('\nMUITO OBRIGADO PELA PREFERÊNCIA!!')
