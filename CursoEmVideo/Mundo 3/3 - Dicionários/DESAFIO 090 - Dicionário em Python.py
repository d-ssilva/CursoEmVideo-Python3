"""Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
   No final mostre o conteúdo da estrutura na tela"""
from emoji import emojize
aluno = dict()
aluno['nome'] = input('Nome: ').capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = emojize(':thumbs_up:')
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = emojize(':hand_with_fingers_splayed:')
else:
    aluno['situação'] = emojize(':thumbs_down:')
print('-='*10)
for k, v in aluno.items():
    print(f' - {k.capitalize()}: {v}')
