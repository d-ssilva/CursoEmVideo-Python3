"""Crie um programa que simule um funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será
o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1"""
from random import randint
qtced50 = 50
qtced20 = 20
qtced10 = 10
qtced1 = 1
totalnotas = 0
print('='*20, 'CAIXA ELETRÔNICO', '='*20)
saldo = randint(500, 1000)
while True:
    print(f'Seu saldo é de \033[32m{saldo:.2f}\033[m')
    print('='*58)
    print('SACAR [1]')
    print('DEPOSITAR [2]')
    print('SAIR [3]')
    opc = int(input('Digite a opção desejada -> '))
    print('='*58)

    while opc != 1 and opc != 2 and opc != 3:
        opc = int(input('ERRO: Opção inserida inválida.\nDigite a opção desejada novamente -> '))
        print('=' * 58)

    if opc == 1:
        saque = int(input('Quanto deseja sacar? R$'))
        while saque > saldo:
            saque = int(input('ERRO:Valor do saque maior que o saldo em conta.\nDigite novamente -> R$'))
        saldo -= saque  # retira o saldo da conta o valor digitado
        cinquenta = int(saque / 50)  # processa a quantidade de notas de 50 reais
        saque = saque % 50  # adiciona ao valor de saque a diferença da divisão de cima

        vinte = int(saque / 20)
        saque = saque % 20

        dez = int(saque / 10)
        saque = saque % 10

        dois = int(saque / 2)
        saque = saque % 2

        print('=' * 58)
        print('{} Notas(s) R$ 50,00.'.format(cinquenta))
        print('{} Notas(s) R$ 20,00.'.format(vinte))
        print('{} Notas(s) R$ 10,00.'.format(dez))
        print('{} Notas(s) R$ 2,00.'.format(dois))
        print('=' * 58)
    elif opc == 2:
        deposito = float(input('Quanto deseja depositar? R$'))
        saldo += deposito
    elif opc == 3:
        break
print('OPERAÇÃO FINALIZADA')
