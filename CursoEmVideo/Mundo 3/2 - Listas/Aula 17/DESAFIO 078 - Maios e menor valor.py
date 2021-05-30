"""Faça um programa que leia 5 valores núméricos e guarde-os em uma lista_geral.
   No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista_geral"""
lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c+1}° valor, posiçao {c}: ')))

print('=-'*30)
print(f'O maior valor digitado foi : {max(lista)}\nNas posições: ', end='')
maior = max(lista)
for i, j in enumerate(lista):
    if j == maior:
        print(f'{i}', end=' - ')
print('x')
print(f'O menor valor digitado foi : {min(lista)}\nNas posições: ', end='')
menor = min(lista)
for i, j in enumerate(lista):
    if j == menor:
        print(f'{i}', end=' - ')
