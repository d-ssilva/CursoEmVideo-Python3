"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a:

-    listagem de números gerados e também
-    indique o menor e o maior valor que estão na tupla."""
from random import randint

while True:
    print('='*20)
    lista = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    print(f'Os números gerados foram: {lista}')
    print(f'A ordem dos números é {sorted(lista)}')
    print(f'O maior valor da listagem é: {max(lista)}')
    print(f'O menor valor da listagem é: {min(lista)}')
    print('=' * 20)
    resp = input('Deseja fazer dnv? [S/N] -> ').upper().strip()[0]
    while resp not in 'SN':
        resp = input('Caractere inválido, tente novamente [S/N] -> ').upper().strip()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA!')
