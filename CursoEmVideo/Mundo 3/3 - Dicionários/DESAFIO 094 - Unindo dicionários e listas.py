"""Crie um programa que leia nome, sexo e idade de vários pessoas, guardando os dados de
   cada pessoa em um dicionário e todos os dicionários em uma lista.
   No final, mostre:
   A) Quantas pessoas foram cadastradas (v);
   B) A média de idade do grupo (v);
   C) Uma lista com todas a mulheres;
   D) Uma lista com todas a pessoas com idade acima da média;"""
totp = media = totidade = 0
lprincipal = []
lmulheres = []
lacima = []
dpessoas = {}
while True:
    dpessoas['nome'] = input('Nome: ').capitalize()
    dpessoas['sexo'] = input('Sexo [M/F]: ').upper()[0]
    while dpessoas['sexo'] not in 'MF':
        dpessoas['sexo'] = input('\033[:31mCaractere inválido\033[m. Sexo [M/F]: ').upper()[0]
    #  SESSÃO IDADE
    dpessoas['idade'] = int(input('Idade: '))
    totidade += dpessoas['idade']
    lprincipal.append(dpessoas.copy())  # ADD - lista principal
    if totp == 0:
        lacima.append(dpessoas.copy())
        if dpessoas['sexo'] == 'F':
            lmulheres.append(dpessoas.copy())
    else:
        if media < dpessoas['idade']:
            lacima.append(dpessoas.copy())  # ADD - lista de pessoas acima da média
        if dpessoas['sexo'] == 'F':
            lmulheres.append(dpessoas.copy())
    totp += 1
    [dpessoas.pop(key) for key in ['nome', 'sexo', 'idade']]
    resp = input('Quer continuar?[S/N] -> ').upper()[0]
    while resp not in 'SN':
        resp = input('\033[:31mCaractere inválido\033[m. Quer continuar?[S/N] -> ').upper()[0]
    if resp == 'N':
        break
    print('-='*20)
media = totidade / totp
print('-='*20)
print(f'A) Total de pessoas cadastradas => {totp}')   # PESSOAS CADASTRADAS
print('-='*30)
print(f'B) Média de idade total => {media:5.2f}')  # MEDIA DE IDADE
print('-='*30)
print(f'C) Listagem das mulheres cadastradas:')
for p in lmulheres:  # LISTA DE MULERES
    print(f'{p["nome"]} - idade: {p["idade"]}.')
print('-='*30)
print(f'D) Lista de pessoas acima da média:')  # LISTA DE PESSOAS ACIMA DA MÉDIA
for p in lprincipal:
    if p['idade'] >= media:
        print(' ', end='')
        for k, v in p.items():
            print(f'{k.capitalize()}: {v} | ', end='')
        print()
print('<< ENCERRADO >>')
