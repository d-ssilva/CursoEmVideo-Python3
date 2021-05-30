"""Crie um programa que leia nome e 2 notas de vários alunos e guarde tudo em uma
   lista_geral composta.
   No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
   as notas de cada aluno individualmente."""
ficha = []
while True:
    print('='*30)
    nome = input('Nome: ').capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar?[S/N] -> ').upper()[0]
    while resp not in 'SN':
        resp = input('\033[:31mCaractere inválido\033[m. Quer continuar?[S/N] -> ').upper()[0]
    if resp == 'N':
        break

print('='*30)
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('='*30)
while True:
    print('='*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) -> '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('='*30)
print('PROGRAMA FINALIZADO')