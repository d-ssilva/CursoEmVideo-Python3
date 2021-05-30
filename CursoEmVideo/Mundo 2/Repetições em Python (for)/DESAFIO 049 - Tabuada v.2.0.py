"""Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for."""

n = int(input('Digite um número cujo você deseje ver a tabuada: '))
f = int(input('Digite até qual algarismo o número escolhido será digitado: '))
f = f + 1
for c in range(1, f, 1):
    r = c * n
    print(" {} x {} = {}".format(n, c, r))
