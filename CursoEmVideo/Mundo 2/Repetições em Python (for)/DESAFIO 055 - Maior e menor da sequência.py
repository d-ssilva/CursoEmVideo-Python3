"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso
lidos."""
maior = 0
menor = 0
for c in range(1, 6, 1): #estrutura de repetição para digitação dos pesos
    peso = float(input('Digite o peso da {}ª pessoa   -> '.format(c)))
    if c == 1: #atribuindo pesos na primeira digitação
        maior = peso
        menor = peso
    else:
        if peso > maior: #identificando o maior peso
            maior = peso
        if peso < menor: #identificando o menor
            menor = peso
print('O \033[34mmenor\033[m peso digitado foi \033[34m{}Kg\033[m.\nO \033[31mmaior\033[m peso digitado foi \033[31m{}'
      'Kg\033[m.'.format(menor, maior))
