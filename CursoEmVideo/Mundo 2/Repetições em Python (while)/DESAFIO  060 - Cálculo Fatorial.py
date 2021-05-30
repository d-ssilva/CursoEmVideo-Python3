"""Faça um programa que leia um nímero qualquer e mostre seu fatorial
ex:
 5! = 5x4x3x2x1 = 120"""
#from math import factorial
n = int(input('Digite um número: '))
c = n
f = 1
print('Calculado {}!'.format(n), end='')
while c > 0:
    print(' {} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f))
