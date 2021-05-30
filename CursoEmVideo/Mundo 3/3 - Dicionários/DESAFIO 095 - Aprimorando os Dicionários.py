"""Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
   de detalhes do aproveitamento de cada jogador."""
jogador = dict()
partidas_l = []
time = []
gol = partida_v = totgols = 0

while True:
    jogador.clear()
    jogador['nome'] = input('Nome: ').capitalize()
    partida_v = int(input('Quantidade de partidas: '))
    partidas_l.clear()
    for c in range(0, partida_v):
        gol = int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}ª partida: '))
        partidas_l.append(gol)
    jogador['partidas'] = partidas_l[:]
    jogador['total'] = sum(jogador['partidas'])
    time.append(jogador.copy())
    resp = input('Quer continuar?[S/N] -> ').upper()[0]
    while resp not in 'SN':
        resp = input('\033[:31mCaractere inválido\033[m. Quer continuar?[S/N] -> ').upper()[0]
    if resp == 'N':
        break
    print('-='*20)

print('='*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('='*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) -> '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'!ERRO. Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['partidas']):
            print(f'     No jogo {i+1} fez {g} gols.')
        print(f'     Totalizando {time[busca]["total"]}.')
    print('='*40)
print('='*40)
print('FIM')
