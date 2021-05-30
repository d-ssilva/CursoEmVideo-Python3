"""Faça um programa que tenha uma função maior(), que receba vários parâmetros com valores inteiros.
   Seu programa tem que analisar todos os valores e dizer qual dele é o maior."""
lista = []
def msg():
    print('=' * 40)
    print(f'{"Mostrando o maior número":^40}')
    print('=' * 40)
def maior(list):
    while len(list) < 2:
        list.append(int(input(f'Digite o {len(list)+1}º número: ')))
    while True:
        print('=' * 20)
        resp = int(input('Quer quantas vezes mais?[999 para parar] -> '))
        print('=' * 20)
        if resp == 999:
            break
        for resp in range(0, resp):

            list.append(int(input(f'Digite o {len(list)+1}º número: ')))
    print('=' * 20)
    print(f'O maior número digitado foi {max(list)}')


msg()
maior(lista)
