"""Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for Impar. Desconsidere-o"""

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Foram digitados {} números pares, a soma deles é {}'.format(cont, soma))