"""Faça um programa que leia o sexo, mas só aceite os valores 'M' ou 'F'.
- Caso esteja errado, peça a digitação novamente até ter um valor correto"""

sexo = str(input('Insira o sexo [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('ERROR!, Digite sexo novamente: ')).upper()
print('Sexo registrado!')
