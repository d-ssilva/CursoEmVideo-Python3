"""Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
from random import randint
cont = 0
par = 'PAR'
impar = 'ÍMPAR'
print('=-'*10, '|', 'JOGO DO PAR OU ÍMPAR v3.0', '|', '-='*10)
while True:
    print('=' * 71)
    jogador = int(input('Digite seu número -> '))
    escolha_jog = str(input('Escolha entre PAR ou ÍMPAR -> ')).upper()[0]
    print('=' * 71)
    while escolha_jog not in 'PI':
        escolha_jog = str(input('Erro: Opção invãlida. Escolha entre PAR ou ÍMPAR -> ')).upper()[0]
        print('=' * 71)
    if escolha_jog == 'P' or escolha_jog == 'I':
        computador = randint(0, 10)
        resultado = jogador + computador
        print(f'(JOGADOR) -> {jogador}\n(COMPUTADOR) ->{computador}')
        print(f'{jogador} + {computador} = {resultado}')
        print('=' * 71)
# --- até aqui é inserção e saída de valores ---
    if resultado % 2 == 0: # verificando de o resultado é PAR ou ÍMPAR
        resultadomaster = 'P'
        print(f'O resultador é {par}')
    else:
        resultadomaster = 'I'
        print(f'O resultador é {impar}')
    if escolha_jog == resultadomaster: # verificação se o jogador perde ou ganha
        print('O jogador \033[1:32mvence\033[m essa rodada')
        cont += 1
    else:
        print(f'O jogador \033[1:31mperde\033[m essa rodada\nCom \033[1:33m{cont}\033[m vitórias consecutivas')
        print('=' * 71)
        break
