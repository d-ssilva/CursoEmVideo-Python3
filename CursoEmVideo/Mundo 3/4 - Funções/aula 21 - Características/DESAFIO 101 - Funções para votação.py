"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
   de uma pessoa, retornando uma valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
   nas eleições."""

def voto(n):
    from datetime import datetime
    while True:
        while n < 1917:
            n = int(input('Erro: ano inválido\nInsira seu ano de Nascimento -> '))
        break
    global situação
    global idade
    idade = datetime.now().year - n


    if idade < 16:
        situação = 'NEGADO'
    elif idade >= 18:
        situação = 'OBRIGATÓRIO'
    else:
        situação = 'OPCIONAL'

    return situação, idade

# PROGRAMA PRINCIPAL
idade = 0
situação = 'n'
voto(int(input('Insira seu ano de Nascimento -> ')))
print(f' - Com {idade} anos, situação de voto: {situação}')
