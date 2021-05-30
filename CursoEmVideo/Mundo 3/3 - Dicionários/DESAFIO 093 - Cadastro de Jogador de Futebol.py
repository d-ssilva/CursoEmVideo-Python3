"""Crie um app, que gerencie o aproveitamento de um jogador de futebol.
   O app vair ler o nome do jogador e quantas partidas_l ele jogou.
   Depois vai ler a quantidade de gols feitos em cada partida.
   No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o
   campeonato"""
jogador = dict()
partidas_l = []
gol = partida_v = totgols = 0

jogador['nome'] = input('Nome: ').capitalize()
partida_v = int(input('Quantidade de partidas: '))
for c in range(0, partida_v):
    gol = int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}ª partida: '))
    partidas_l.append(gol)
    totgols += gol
jogador['partidas'] = partidas_l
jogador['total'] = totgols
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f' => {k.capitalize()} - {v}')
print('-='*20)
print(f'Nome: {jogador["nome"]}:')
for i, v in enumerate(jogador['partidas']):
    print(f'   - Na partida {i+1} fez {v} gols')
print('-='*20)