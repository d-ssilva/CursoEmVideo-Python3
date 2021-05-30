"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
   dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no
   dado."""
from random import randint
import time
import operator
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = list()
print(f'Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou \033[033m{v}\033[m no dado.')
    time.sleep(1)
ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print('-='*13)
print('Ranking: ')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    time.sleep(1)
