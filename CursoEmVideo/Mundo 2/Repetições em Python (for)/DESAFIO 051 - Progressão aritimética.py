"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão"""


def sep():
    print('=' * 10)

print("="* 10, "|", 'PROGRESSÃO ARITIMÉTICA', "|","="* 10)
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=' -> ')

print('ACABOU')
