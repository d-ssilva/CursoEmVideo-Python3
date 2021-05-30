"""Crie um programa que vai ler vários números e colocar em uma lista_geral.
   Depois disso, mostre:

   A)Quantos números foram digitados. R:len
   B)A lista_geral de valores, ordenada de forma decrescente. R:sort(reverse=True)
   C)Se o valor 5 foi digitado e esta ou não na lista_geral.R: ?"""
lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Quer continuar?[S/N] -> ').upper()[0]
    while resp not in 'SN':
        resp = input('\033[:31mCaractere inválido\033[m. Quer continuar?[S/N] -> ').upper()[0]
    if resp == 'N':
        break
print(f'O total de {len(lista)} valor(s).')
if 5 in lista:
    print(f'O valor 5 foi digitado na posição {lista.index(5)}°')
else:
    print('O número 5 não foi digitado')
lista.sort(reverse=True)
print(f'Ordem decrescente: {lista}')
