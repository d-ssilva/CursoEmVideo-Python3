"""Faça um programa que mostre uma contagem regressiva para o estouro de fogos de artificio, indo de
10 até 0, com uma pausa de 1 segundo entre eles."""
from time import sleep
from emoji import emojize

def time():
    sleep(1)

time()
print('A contagem regressiva para o estouros dos fogos', "|", "-="*10)
time()
print('Começando em...')
time()
for c in range(9, 0, -1):
    print(c)
    time()
print(emojize('Consegui!! :boom::dizzy:', use_aliases=True))
