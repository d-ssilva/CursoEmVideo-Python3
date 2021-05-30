"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista_geral.
   Caso o número já exista lá dentro, ele não será adicionado.
   No final, serão exibidos todos os valores únicos digitador, em ordem crescente."""

lista = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Valor inserido com sucesso!')
    else:
        print('Valor repitido não pode ser inserido, tente outro número')
    resp = input('Quer continuar?[S/N] -> ').upper()[0]
    while resp not in 'SN':
        resp = input('\033[:31mCaractere inválido\033[m. Quer continuar?[S/N] -> ').upper()[0]
    if resp == 'N':
        break
print(f'Os valore digitados foram: {sorted(lista)}')
