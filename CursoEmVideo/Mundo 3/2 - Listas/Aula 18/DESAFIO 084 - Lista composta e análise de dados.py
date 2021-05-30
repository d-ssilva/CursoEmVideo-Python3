"""Faça um app que leia nome, peso de várias pessoas, guardando tudo em uma lista_geral. no final, mostre:
   A) Quantas pessoas foram cadastradas; (v)
   B) Uma listagem com as pessoas mais pesadas;
   C) Um listagem com pessoas mais leves;"""
pesado = leve = 0
lista_geral = []
pessoas = []
cont = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    cont += 1
    if cont == 1:
        pesado = leve = pessoas[1]
    else:
        if pessoas[1] > pesado:
            pesado = pessoas[1]
        if pessoas[1] < leve:
            leve = pessoas[1]
    lista_geral.append(pessoas[:])
    pessoas.clear()
    resp = input('Quer continuar?[S/N] -> ').upper()[0]
    while resp not in 'SN':
        resp = input('\033[:31mCaractere inválido\033[m. Quer continuar?[S/N] -> ').upper()[0]
    if resp == 'N':
        break
print(''*30)
print('='*30)
print(f'Número de pessoas cadastradas: {cont}')
print('='*30)
print(f'Listagem geral: {lista_geral}')
print('='*30)
print(f'O maior peso foi de {pesado}Kg.\nPeso de ', end='')
for p in lista_geral:
    if p[1] == pesado:
        print(f'{p[0]}', end=' ')
print('.')
print('='*30)
print(f'O menor peso foi de {leve}Kg.\nPeso de ', end='')
for p in lista_geral:
    if p[1] == leve:
        print(f'{p[0]}', end='')
print('.')
print('='*30)
