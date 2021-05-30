"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""
cont18 = contm = contf = contg = 0
while True:
    print('=-'*11)
    idade = int(input('Digite a idade -> '))
    sexo = str(input('Digite o sexo [M/F] -> ')).upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Erro: caractere inserido em sexo inválido.\nDigite novamente -> ')).upper()[0]
    if idade > 18:  # verificando pessoas maiores de 18 anos
        cont18 += 1
        contg += 1
    if sexo == 'M':  # verificando quantos homens cadastrados
       contm += 1
       contg += 1
    if idade < 20:
        if sexo == 'F':  # quantidade de mulheres que tem menos de 20 anos
            contf += 1
            contg += 1
    resp = input('Quer continuar? [S/N] -> ').upper()[0]
    while resp not in 'SN':
        resp = str(input('Erro: caractere inserido em sexo inválido.\nDigite novamente -> ')).upper()[0]
    if resp == 'N':
        break
print('=-'*11)
print(f'A quantidade de pessoas que tem mais de 18 anos é de: {cont18}')
print(f'A quantidade de homens cadastrados é de: {contm}')
print(f'A quantidade de mulheres que tem menos de 20 anos é de: {contf}')