"""Faça um programa que tenha uma lista chamada números e duas funções: sorteia() e somaPar().
   A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda,
   função vai mostrar a soma entre todos os valores
   PARES sorteados pela função anterior."""
from random import randint
numeros = []
def msg(msg):
    print('='*40)
    print(f'{msg:^40}')
    print('='*40)

def somaPar(lista = []):
    soma = 0
    pos = 0
    for i in range(0, len(lista)):
        if lista[pos] % 2 == 0:
            soma += lista[pos]
        pos += 1
    if soma == 0:
        print('Nenhum número par foi sorteado!')
    else:
        print(f'A soma de todos os números pares é {soma}')

def sorteia(lista = []):  # FUNÇÃO que sorteia 5 números
    for i in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Lista sorteada foi: ', end='')
    for i in lista:
        print(f'{i} - ', end='')
    print('Fim!')
    somaPar(lista[:])


#  PROGRAMA PRINCIPAL
mensagem = 'PROGRAMA DE SORTEIO'
msg(mensagem)
sorteia(numeros)
