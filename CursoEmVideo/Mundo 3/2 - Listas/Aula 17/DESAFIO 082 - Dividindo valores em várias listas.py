"""Crie um programa que vai ler vários números e colocar em uma lista_geral.
   Depois disso, crie duas listas extras que vão conter apenas os valores pares e impares digitados, respectivamente

   Ao final mostre o conteúdo das três listas geradas."""
lista_principal = list()
while True:
    lista_principal.append(int(input('Digite um número: ')))
    resp = input('Quer continuar?[S/N] -> ').upper()[0]
    while resp not in 'SN':
        resp = input('\033[:31mCaractere inválido\033[m. Quer continuar?[S/N] -> ').upper()[0]
    if resp == 'N':
        break
lista_par = []
lista_impar = []
for i, v in enumerate(lista_principal):
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)
print(f'Lista principal: {lista_principal}')
print(f'Lista par: {sorted(lista_par)}')
print(f'Lista impar: {sorted(lista_impar)}')
