"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""
import datetime
cont = 0
ncont = 0
anoatual = datetime.date.today().year
for c in range(1, 8, 1):
    nasc = int(input('Digite o ano de nascimento do {}º candidato: '.format(c)))
    idade = (anoatual - nasc)
    if idade >= 18:
        cont += 1
    else:
        ncont += 1
print('\n{} - \033[32maprovado(s)\033[m.\n{} - \033[31mreprovado(s)\033[m.'.format(cont, ncont))
