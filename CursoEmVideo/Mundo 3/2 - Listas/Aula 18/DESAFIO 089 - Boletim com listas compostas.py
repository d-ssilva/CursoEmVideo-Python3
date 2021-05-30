"""Crie um programa que leia nome e 2 notas de vários alunos e guarde tudo em uma
   lista_geral composta.
   No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
   as notas de cada aluno individualmente."""
n1 = n2 = media = cont = 0
l_geral = []
l_aux = []
while True:
    l_aux.append(input('Nome: '))
    l_aux.append(float(input('Nota 1: ')))
    l_aux.append(float(input('Nota 2: ')))
    l_aux.append((l_aux[1] + l_aux[2]) / 2)
    l_geral.append(l_aux[:])
    resp = input('Quer continuar?[S/N] -> ').upper()[0]
    while resp not in 'SN':
        resp = input('\033[:31mCaractere inválido\033[m. Quer continuar?[S/N] -> ').upper()[0]
    cont += 1
    l_aux.clear()
    if resp == 'N':
        break
print('='*30)
for c in range(0, cont):
    print(f'Nome: {l_geral[c]}')
    for l in range (0, cont):
        print(f'Nome: {l_geral[l]}')
        print(f'Nota1: {l_geral[l+1]}')
        print(f'Nota2: {l_geral[l+2]}')
        print(f'Média: {l_geral[l+3]}')
