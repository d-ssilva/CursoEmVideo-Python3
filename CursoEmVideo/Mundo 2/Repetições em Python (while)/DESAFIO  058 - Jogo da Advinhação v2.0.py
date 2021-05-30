"""Melhore o jogo do DESAFIO 028 onde o computador vai pensar num número entre 0 e 10. Só que agora o jogador vai
tentar advinhar até acertar. mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
from time import sleep
def separador():
    print('='*15)

tentativas = 1
computador = randint(0, 10)

print('=-'*10, '|', 'Jogo da advinhação v2.0', '|', '=-'*10)
jogador = int(input('Informe um número qualquer entre 0 e 10: '))
print('Vou tentar advinhar...')
sleep(1.5)

while computador != jogador:
    tentativas += 1
    separador()
    print('Computador [{}], Você [{}]'.format(computador, jogador))
    jogador = int(input('\033[1;31mVocê errou!\033[m Tente novamente, um número qualquer entre 0 e 10: '))
    print('Vou tentar advinhar...')
    sleep(1.5)
    computador = randint(0, 10)

if tentativas == 1:
    separador()
    print('\033[1;32mVocê acertou\033[m de primeira!\nVocê apostou {} e o computador {}'.format(jogador, computador))
else:
    separador()
    print('\033[1;32mVocê acertou\033[m depois de {} tentativas\n(Computador [{}], Você [{}])'.format(tentativas, computador, jogador))
