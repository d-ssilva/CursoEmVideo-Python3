"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
    e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
Aula Anterior
"""
from datetime import date

#inserção de informações
ano_atual = date.today().year
ano_nasc = int(input('Digite o ano de nascimento do(a) atleta: '))

#processamento
idade = ano_atual - ano_nasc

#estrutura condicional
if idade <= 9:
    categoria = ('MIRIM')
elif idade <= 14:
    categoria = ('INFANTIL')
elif idade <= 19:
    categoria = ('JÚNIOR')
elif idade <= 25:
    categoria = ('SÊNIOR')
elif idade > 25:
    categoria = ('MASTER')

print('A idade é {} anos.\nCategoria: {}'.format(idade,categoria))

print("|","="*10,'FIM DE OPREAÇÃO!',"="*10,"|")