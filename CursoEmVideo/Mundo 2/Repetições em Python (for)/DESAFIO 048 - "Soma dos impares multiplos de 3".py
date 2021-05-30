"""Fala um programa que:
- CALCULE a SOMA entre TODOS os [numeros IMPARES] que são multiplos de três
e que se encontram no intervalo de 1 até 500"""
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:  # identificando se um número é impar e multiplo de 3
        cont += 1
        soma += c
        print(c, ' + ', end='')
print('A soma de todos os valores multiplos de 3 é {}.\nForam comutados {} valores.'.format(soma,cont), end='')

