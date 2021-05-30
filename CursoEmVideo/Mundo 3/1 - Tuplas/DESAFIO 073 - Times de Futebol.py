"""Crie uma tupla preenchida com os 15 primeiros colocados da Tabela do Conferencia Oestre da Nba,
 na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da GSW."""

lista = ('Uttah Jazz', 'Suns', 'Clippers', 'Lakers', 'Nuggets', 'Trail Blazers', 'Mavericks', 'Spurs', 'Grizzlies',
         'Golden State Warriors', 'Kings', 'Pelicans', 'Thunder', 'Rockets', 'Timberwolves')

print('\033[1:32mAtual listagem da conferencia Oeste:\033[m')
col = 1
for t in lista:
    print(f'{col}ª - ', t)
    col += 1

print(f'Os 5 primeiros colocados são {lista[0:5]}')
print(f'Os 4 últimos colocados são {lista[-4:]}')
print(f'O Golden esta em {lista.index("Golden State Warriors")+1}ª posição.')
