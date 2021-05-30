"""Faça um programa que ajude um jogador da MEGA SENA a cria palpites. O programa vai perguntar
   quantos jogos serão gerado e vai sortear 6 números entre 1 e 60 para cada jogo, cadstrando tudo
   em uma lista_geral composta"""
from random import randint
from time import sleep
l_Aux = []
l_Palpites = []
constante = 60
n_Sorteado = 0
print('='*30)
print(f'{"SORTEADOR DA MEGA-SENA":^30}')
print('='*30)
n_jogos = int(input('Quantos jogos deseja fazer: '))
print('='*30)
for l in range(0, n_jogos):
   for c in range(0, 6):
       n_Sorteado = randint(0, constante)
       while n_Sorteado == l_Palpites[:]:
           n_Sorteado = randint(0, constante)
       l_Palpites.append(n_Sorteado)
   l_Aux.append(l_Palpites[:])
   l_Palpites.clear()
print(f'Eis aqui seus bilhetes:\n', end='')
print('='*30)
for i in range(0, n_jogos):
    print(f'{i+1}º - { sorted(l_Aux[i])}\n')
    sleep(0.5)
print('='*30)
