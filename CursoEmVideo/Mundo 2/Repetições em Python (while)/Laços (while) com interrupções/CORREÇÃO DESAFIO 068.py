from random import randint

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''  # tipo recebe nda justamente para cair no while abaixo
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]>: ')).strip().upper()[0]
    print(f'Você - ({jogador})\nComputador - ({computador})\nResutado = {total}')
    print(f'tipo: {tipo}')
