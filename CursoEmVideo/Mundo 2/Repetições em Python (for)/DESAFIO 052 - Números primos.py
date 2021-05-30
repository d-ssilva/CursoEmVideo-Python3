"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo 
(Um número é classificado como primo se ele é maior do que um e é divisível apenas por um e por ele mesmo)"""

print("="*10, "|", "IDENTIFICADOR DE NÚMEROS PRIMOS!", "|", "="*10)
num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO extenso {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('{} - \033[32mé um número primo\033[m!'.format(num))
else:
    print('{} - \033[31mnão é um número primo\033[m!'.format(num))
