"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes """

print("|", ":"*10, 'Bem vindo ao analisador de triângulos', ":"*10, "|")
e1 = float(input('Insira o comprimento do 1º eixo: '))
e2 = float(input('Insira o comprimento do 2º eixo: '))
e3 = float(input('Insira o comprimento do 3º eixo: '))

if (e1 <= e2 + e3) and (e2 <= e1 + e3) and (e3 <= e1 + e2):
    print('Os seguimentos acima formam um triângulo: ', end='')
    if e1 == e2 == e3:
        print('EQUILATERO')
    elif (e1 != e2) and (e3 != e1) and (e2 != e3):
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os eixo digitados NÃO podem formar um triângulo')