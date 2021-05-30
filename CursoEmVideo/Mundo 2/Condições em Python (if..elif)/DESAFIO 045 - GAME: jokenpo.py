from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

def divisor():
    print("-="*15)

# interação com usuário
print("="*10, "|", 'Vamos jogar Jo-Ken-Po!', "|", "="*10)
print('Suas opções são:\n[ 0 ] - PEDRA;\n[ 1 ] - PAPEL;\n[ 2 ] - TESOURA;')
jogador = int(input('Escolha sua jogada -> '))
divisor()

# resolução do jogo
divisor()
print('RESOLUÇÃO')
print('O computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))
divisor()

# estrutura condicional
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif computador == 2:
        print('EMPATE!')
else:
    print('JOGADA INVÁLIDA')
divisor()
print('FIM DE JOGO!')
divisor()