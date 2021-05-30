"""Crie um programa que leia uma frase qualquer e diga se ela é um Palíndromo, desconsiderando
 os espaços"""

frase = str(input('Escreva uma frase qualquer.\n-> ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('A frase: {} \n\033[:32mÉ um palíndromo!\033[m'.format(frase))
else:
    print('A frase: {} \n\033[:31mÉ um palíndromo!\033[m'.format(frase))
