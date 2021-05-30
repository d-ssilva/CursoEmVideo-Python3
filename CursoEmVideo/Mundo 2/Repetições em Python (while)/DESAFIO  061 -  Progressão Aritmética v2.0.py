"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura WHILE"""
"""DESAFIO 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão"""
print('Gerador de PA')
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end='')
    termo += razão
    cont += 1
print('PAUSA')
