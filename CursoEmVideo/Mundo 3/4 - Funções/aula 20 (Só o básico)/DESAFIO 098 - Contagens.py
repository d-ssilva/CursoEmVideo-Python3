"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim
   e passo e realize a contagem.

   Seu programa tem que realizar 3 contagens através da função criada:
   A) De 1 até 10, de 1 em 1
   B) De 10 até 0, de 2 em 2
   C) Uma contagem personalizada (o programa deve identificar caracteristicas da digitação do user)"""
from time import sleep
def msg(msg):
    print('='*40)
    print(f'{msg:^40}')
    print('='*40)
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('='*40)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(0.7)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
    print('=' * 40)
#  PROGRAMA PRINCIPAL
msg('O CONTADOR')
contador(1, 10, 1)
contador(10, 0, 2)
print(f'{"Sua vez de personalizar a contagem":^40}')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
